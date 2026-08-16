---
conversion_metadata:
  converted_at: "2026-07-21T08:24:19Z"
  converter_tool: "markitdown"
  converter_version: "0.1.6"
  source_pdf: "Sabiri et al.pdf"
  source_pdf_sha256: "b1cba4ce70f21dd361b3004e156108d20dc0e7321ced9938f4c0f73e9c0466c6"
  page_count: 66
  markdown_char_count: 417762
---

<!-- PAGE-AWARE EXTRACTION (via pdfminer.six) -->

<!-- PAGE 1 -->

Systematic Review
Hybrid Quality-Based Recommender Systems: A Systematic
Literature Review †

Bihi Sabiri 1,*

, Amal Khtira 2

, Bouchra El Asri 1

and Maryem Rhanoui 3,4

1

2

3

IMS Team, ADMIR Laboratory, Rabat IT Center, ENSIAS, Mohammed V University in Rabat,
Rabat 10130, Morocco
LASTIMI Laboratory, EST Salé, Mohammed V University in Rabat, Salé 11060, Morocco
Laboratory Health Systemic Process (P2S), UR4129, University Claude Bernard Lyon 1, University of Lyon,
69008 Lyon, France

4 Meridian Team, LYRICA Laboratory, School of Information Sciences, Rabat 10100, Morocco
* Correspondence: bihi_sabiri@um5.ac.ma
†

Supported by TekCircle: (https://tekcircle.io).

Abstract: As technology develops, consumer behavior and how people search for what
they want are constantly evolving. Online shopping has fundamentally changed the e-
commerce industry. Although there are more products available than ever before, only a
small portion of them are noticed; as a result, a few items gain disproportionate attention.
Recommender systems can help to increase the visibility of lesser-known products. Major
technology businesses have adopted these technologies as essential offerings, resulting in
better user experiences and more sales. As a result, recommender systems have achieved
considerable economic, social, and global advancements. Companies are improving their
algorithms with hybrid techniques that combine more recommendation methodologies as
these systems are a major research focus. This review provides a thorough examination
of several hybrid models by combining ideas from the current research and emphasizing
their practical uses, strengths, and limits. The review identifies special problems and
opportunities for designing and implementing hybrid recommender systems by focusing
on the unique aspects of big data, notably volume, velocity, and variety. Adhering to the
Cochrane Handbook and the principles developed by Kitchenham and Charters guarantees
that the assessment process is transparent and high in quality. The current aim is to conduct
a systematic review of several recent developments in the area of hybrid recommender
systems. The study covers the state of the art of the relevant research over the last four
years regarding four knowledge bases (ACM, Google Scholar, Scopus, and Springer), as
well as all Web of Science articles regardless of their date of publication. This study employs
ASReview, an open-source application that uses active learning to help academics filter
literature efficiently. This study aims to assess the progress achieved in the field of hybrid
recommender systems to identify frequently used recommender approaches, explore the
technical context, highlight gaps in the existing research, and position our future research
in relation to the current studies.

Keywords: hybrid quality-based recommendations; strategy recommender systems;
systematic review; big data

1. Introduction

Based on extensive datasets, a recommender system is defined as any system that
generates personalized suggestions as an output or has the effect of leading the user to

Academic Editor: Alois Herkommer

Received: 14 October 2024

Revised: 17 November 2024

Accepted: 6 December 2024

Published: 7 January 2025

Citation: Sabiri, B.; Khtira, A.; El Asri,

B.; Rhanoui, M. Hybrid Quality-Based

Recommender Systems: A Systematic

Literature Review. J. Imaging 2025, 11,

12. https://doi.org/10.3390/

jimaging11010012

Copyright: © 2025 by the authors.

Licensee MDPI, Basel, Switzerland.

This article is an open access article

distributed under the terms and

conditions of the Creative Commons

Attribution (CC BY) license

(https://creativecommons.org/

licenses/by/4.0/).

J. Imaging 2025, 11, 12

https://doi.org/10.3390/jimaging11010012

---

<!-- PAGE 2 -->

J. Imaging 2025, 11, 12

2 of 66

interesting or helpful objects in a broad range of alternative options. In the context of big
data, recommender systems are a crucial tool for sharing knowledge and assisting users in
finding pertinent content.

1.1. Current Landscape of E-Commerce

Propelled by significant technology advancements, the e-commerce industry today is
marked by a growing rivalry among platforms competing for user attention [1,2]. A sizable
fraction of the worldwide population currently shops online, and the e-commerce industry
is only expected to expand more. Correspondingly, consumer behavior is shifting toward
web-related activities such as online purchasing and product research. With so much variety,
e-commerce enterprises must develop inventive ways to retain or attract customers. In this
context, robust recommendation systems are critical for identifying diverse forms of data
and understanding consumer preferences. Increasing volumes of data and technological
improvements have turned the focus to data analytics as businesses now value the insights
and helpful patterns that result from the process. In a typical market, a small percentage of
loyal clients account for a considerable portion of the future income. This demonstrates
the necessity of retaining high customer value and advancing potential customers up
the profit chain. Prospective product and service offerings should effectively appeal to
consumer preferences, helping them to progress up the loyalty ladder. Social media play
an important role in e-commerce nowadays, and enormous volumes of data regarding
individual preferences are frequently publicized. The availability of platforms that use
various methodologies indicates how diversified recommendation systems contribute to
significant improvements in modern e-commerce. The issues ahead are mostly related to
information overload and erroneous suggestions across multiple categories. The current
situation requires the use of an effective hybrid recommender system to ensure correct
targeting of potential clients.

1.2. Hybrid Recommendation Systems: Industry Impacts and Applications

Today, major internet businesses such as Amazon, LinkedIn, Google, Facebook, Netflix,
Spotify, Microsoft, eBay, and Airbnb use hybrid recommendation algorithms, which have
had a significant impact on the global economy, social sphere, and digital space [3]. The
following are specific examples of studies and applications that demonstrate how hybrid
recommendation systems are used across several sectors:

•

E-Commerce: Amazon’s recommendation engine has a hybrid approach, combining
collaborative filtering with content-based filtering. For example, the authors of [1]
found that Amazon customizes recommendation systems to reflect customer habits
and interests, resulting in a huge 35% boost in sales volume on their online shopping
platform [4].

• Music Streaming: Spotify: Spotify combines user listening history (collaborative
filtering) with musical elements such as genre, pace, and lyrics (content-based filtering).
Spotify’s “Discover Weekly” playlist has successfully leveraged these strategies to
increase user engagement and satisfaction, resulting in a personalized experience that
retains users. As demonstrated by the authors of [5], after implementing their model,
the rate at which consumers began new audiobooks increased by 46%.

• Online Video Platforms: Netflix’s recommendation algorithm uses collaborative
filtering, content-based approaches, and contextual considerations (such as time of
day and device type). Collaborative filtering detects patterns in user viewing behavior,
whereas content-based filtering suggests shows based on genre and theme. The
authors of [6] discovered that this hybrid strategy improves the user experience and
retention rates by providing timely and relevant recommendations.

---

<!-- PAGE 3 -->

J. Imaging 2025, 11, 12

3 of 66

•

•

•

YouTube: YouTube’s recommendation system is fundamental to the platform, and it
was meticulously engineered to optimize user engagement and time spent watching
videos. The system works by evaluating user interaction data, including watch history,
likes, comments, shares, and the amount of time spent on different types of content.
It learns from these interactions to create a more detailed picture of each viewer’s
preferences. In addition to analyzing user behavior, the program examines content.
This includes evaluating metadata such as video titles, descriptions, tags, and more
complicated aspects such as the topic, style, and tone of the content. By merging these
data, the system detects trends and predicts what viewers are likely to watch and
appreciate. The final objective of YouTube’s recommendation algorithm is to present
each viewer with a personalized feed that will keep them interested for longer times.
By proposing content that closely matches their interests, YouTube is able to boost
viewers’ viewing time, which benefits both advertisers and content providers while
also guaranteeing that consumers continue to find relevant, engaging videos on the site.
This cycle of personalized recommendations not only improves the user experience but
also promotes YouTube’s status as a top content platform by encouraging long-term
and recurring use.
Travel and Hospitality: Airbnb’s recommendation system personalizes listing sug-
gestions based on user interests, demographics, and geography.
Social Media:

•

•

Facebook employs a hybrid algorithm for friend suggestions that incorporates
user interactions, mutual connections, and demographic information. Backstrom
et al. (2011) showed that this method promotes user engagement by fostering
more meaningful connections.
LinkedIn’s job recommendation engine incorporates profile information, user
behavior, and collaborative filtering. LinkedIn tailors job suggestions based
on user data and behaviors from comparable users, increasing the job-seeking
relevance and improving the professional networking experience.

These systems have also made contributions to the issues of information overload,

user experience, user decision-making, and business sales [7].

Regardless of the goals of any recommendation technique, hybrid recommender sys-
tems (HRSs) combine two or more of them to improve the forecast accuracy [8–10]. In this
manner, the drawbacks of each method that would arise from using them separately can
be somewhat mitigated [11,12]. Since advances in technology have made it possible for
individuals and businesses to acquire a vast amount of information on any topic, the field
of human resource systems has been becoming increasingly relevant. This tendency can
be recognized in several areas, including e-learning systems, digital libraries, navigation
services, electronic enterprises, and news and publication suggestions. Hybrid recom-
mender systems integrate several models to reduce the shortcomings of one model with
another, lowering the overall disadvantages of using different models and resulting in
more credible solutions.

The two primary categories of hybrid recommendation systems are collaborative-
filtering-based and content-based. While collaborative-filtering-based systems rely on user
activity, content-based systems create suggestions based on the characteristics of the things
being recommended. Both categories can be used by hybrid recommender systems to
create a more successful recommendation engine [13].

One benefit of hybrid systems is their ability to provide users more individualized
recommendations. They can consider a wider range of criteria when making suggestions
by merging various models, which can produce more accurate and pertinent findings.

---

<!-- PAGE 4 -->

J. Imaging 2025, 11, 12

4 of 66

However, because hybrid systems sometimes combine multiple recommendation systems,
they can be more complex and challenging to analyze.

In technical terms, all recommendation systems generate suggestions using vari-
ous methodologies, such as collaborative filtering (CF), content-based filtering (CBF),
knowledge-based filtering (KBF), demographic filtering (DF), and others. Let us consider
the specifics of these strategies.

1.

2.

Content-Based Filtering: The CBF approach is based on the notion that people who
have previously appreciated products with certain characteristics would continue
to enjoy similar items in the future. It examines item features to match them to
user profiles and provide suggestions. This strategy uses content representation and
comparison techniques from information retrieval, as well as classification algorithms
from machine learning, to represent those items previously rated by the user and
compare them to other items to propose comparable items [3,14–16].
Collaborative Filtering: The CF approach works on the notion that people who
had similar preferences in the past would have similar ones in the future. The most
significant part of collaborative filtering is determining whether the user’s preferences
match those of other users [17]. It entails people working together to help each
other filter information by documenting their emotions regarding the things they
encounter [3]. To find similarities in taste among groups of people, CF uses ratings
or user-generated comments. The commonalities between users are then used to
produce recommendations [2]. However, CF recommenders encounter difficulties
such as the cold-start problem (for new users or goods) and the “gray sheep” problem
(users who do not fall into any single taste cluster) [3,14,18,19].

3. Utility-Based Filtering: UBF is a recommendation approach that provides person-
alized recommendations to users by calculating the utility of each item for the user.
However, a key challenge in this category lies in determining the utility value for each
individual user [20,21].
Contextual Filtering: This system considers contextual information such as time, loca-
tion, and device to deliver recommendations pertinent to the user’s present position.
It can improve the user experience by taking into account the exact environment in
which the recommendations are presented [22,23].

4.

5. Knowledge-Based Filtering: The KBF method suggests things based on clear user
preferences and needs. It considers information supplied by the user, such as specific
interests, desired qualities, or limitations, and recommends things that meet those
requirements. It does not rely primarily on demographic information but instead on
user-specified choices [24,25].

6. Demographic Filtering System: DF determines user categories by employing demo-
graphic data such as gender, educational background, age, and so on. It does not have
the new user issue because it does not use ratings to create suggestions. However, due
to internet privacy concerns, it is difficult to obtain enough demographic information
that is necessary today, limiting the use of DF. It is still used in conjunction with other
recommenders as a quality-enforcing strategy [26].

7. Hybrid Recommender Systems: HRSs integrate various recommendation methods
to create a more accurate and personalized recommendation system. By combining
more than one recommender system approach, hybrid recommender systems leverage
multiple sources of data and algorithms to enhance the quality of recommendations.
The goal is to reinforce the benefits of each strategy while minimizing their downsides
or limitations, resulting in a more effective and comprehensive recommendation
approach [13,15,16,18,21,27–36].

---

<!-- PAGE 5 -->

J. Imaging 2025, 11, 12

5 of 66

The goal of the study was to examine recently released HRS papers that focus on
e-commerce and demonstrate the evolving perspectives of these systems, specifically their
types, approaches, algorithms, and implementations in detail. Our key findings and
contributions might be summarized as follows:

-

-

-

-

-

-

Data scarcity is a major limiting factor in the performance of recommendation systems.
The current approaches to dealing with cold-start concerns for new users and objects
frequently fail to incorporate demographic information into the suggestion process.
According to research, the existence of cold-start users, together with the volume and
quality of the surrounding data points used in the recommendation framework, have
a substantial impact on prediction accuracy.
The contribution provides a synthesis of the existing information and approaches
to hybrid-based quality in recommender systems via a thorough examination of
the literature. This includes exploring, evaluating, and categorizing diverse hybrid
models, assessment criteria, and real-world implementations, as well as identifying
their strengths and drawbacks.
Identifying Challenges and Opportunities: The review recognized and articulated the
distinct problems and opportunities provided by big data in recommender systems.
This involved understanding the unique characteristics of big data, such as volume,
velocity, and diversity, as well as the implications for hybrid recommender system
design and implementation.
Proposing Frameworks and Rules: Drawing on the findings of the literature review,
the contribution provided frameworks, architectures, or rules for designing and eval-
uating hybrid recommender systems in the context of big data. These frameworks
incorporated best practices, addressed frequent hazards, and proposed solutions for
dealing with big data’s distinct characteristics and requirements, such as scalability,
real-time processing, and data integration.
Domain-Driven Insights: The review investigated the use of hybrid recommender
systems in big data situations. It examined successful implementations in e-commerce,
social media, healthcare, IoT, and the less-explored area of talent pool optimization for
recruitment solutions.
Employing an open-source program, ASReview uses active learning to improve the
systematic selection process in research. It efficiently processes vast amounts of text,
reducing the number of documents that must be examined by humans and eliminating
false negatives.

The following portions of the essay are organized as follows. Section 2 provides the
related work and background. The objectives and reasons for conducting a systematic
literature review are presented in Section 3. Section 4 describes the methodology for the
review process, including the information sources, eligibility criteria, and data extraction,
while Section 5 covers the synthesis of the results and discussion. Section 6 brings the paper
to its conclusion.

The selected papers are presented at the end of this paper (see Appendix A).

2. Background and Related Work

The overabundance of irrelevant information frequently results in a significant invest-
ment of time and resources in the search for useful information, or possibly the inability
to locate the necessary knowledge completely. Recommendation systems (RSs) have been
created to address these difficulties. Their goal is to reduce these concerns by making
specific recommendations and solutions.

---

<!-- PAGE 6 -->

J. Imaging 2025, 11, 12

6 of 66

The research in [37] emphasizes the value of alternate evaluation metrics for recom-
mendation systems (RSs) in the classifieds area, in addition to typical accuracy measures.
The key metrics that were discussed include the following:

• Diversity: Assesses the diversity among the recommendations, which is critical for
providing users with a wide range of options and improving engagement. The paper
in [37] uses measures such as test coverage, Shannon entropy, and the Gini index to
assess diversity, with values 0.74, 10.40, and 0.79, respectively. Greater diversity in
recommendations could offer consumers additional choices, potentially increasing
user engagement and satisfaction.

• Novelty: Determines how surprising the recommendations are, which helps to keep

•

users interested by suggesting goods they may not have considered.
User Satisfaction: Assesses the total user experience using feedback and engagement
metrics to customize suggestions to user preferences. By adding these indicators,
HRSs can improve their performance, better correspond with user needs, and increase
overall engagement and satisfaction.

The success of recommender systems is measured using a range of metrics that
go beyond ordinary accuracy measures (accuracy, precision, recall, and F1-score).
In
practical implementations, it is critical to connect these measures with user-centric goals to
ensure that the recommendations not only perform well algorithmically but also boost user
happiness and engagement. In addition to the new metrics provided above (see Section 2),
below is a thorough study of the alternative metrics used to evaluate recommender systems,
especially in real-world applications. The papers in [38,39] covered different criteria for
evaluating the efficacy of the Conformity-Aware Multi-Task (CAM2) model in the context
of system recommendations and scoring hotels in the suggested recommendation system.

1.

3.

Aggregated User Engagement: This indicator measures how engaged users are with
the system’s recommended content. The CAM2 model significantly increased this
measure by 0.50%, demonstrating improved user involvement with the platform [39].
2. Daily Active Users (DAUs): This indicator counts the number of unique users who
interact with the site each day. The CAM2 model led to a 0.21% rise in DAUs,
indicating that more users are returning to the site due to better suggestions [39].
Retention Metrics: Renewal metrics are used to assess the model’s capacity to im-
prove user experience and motivate return visits, particularly among casual users. The
model’s design promotes better engagement and retention among casual users [39].
Reviews and Comments: The system evaluates customer reviews to measure
thoughts and sentiments about hotels, which assists in creating recommendations
according to user preferences [38].
Surrounding Environments: It considers surrounding Points of Interest (POIs) to as-
sess the facilities accessible around the hotels, which can impact a user’s decision [38].
6. Numerical Ratings: The system integrates numerical ratings submitted by users,

5.

4.

serving as a quantifiable assessment of hotel quality.

7. Aggregated Scores: The suggested system aggregates scores from both reviews and

8.

surrounding facilities, enabling a thorough evaluation of each hotel [38].
Polarity Ratings: The system creates polarity ratings from reviews using natural
language processing (NLP) techniques, which helps to comprehend the sentiments
represented in the reviews [38].

The main goal of the research by Sivasankari et al. [40] is to create a hybrid scientific
article recommendation system that uses the COOT optimization algorithm to improve
the accuracy and relevance of article suggestions. The COOT optimization technique is in-
tended to efficiently traverse the citation graph and discover highly important publications.

---

<!-- PAGE 7 -->

J. Imaging 2025, 11, 12

7 of 66

The study addresses key issues in recommendation systems, such as the cold-start problem
and user interest unpredictability, by combining content- and graph-based recommenda-
tion algorithms [40]. The COOT optimization algorithm is used to select articles that closely
match user queries, ensuring that recommendations are highly personalized and matched
to individual needs. The suggested strategy seeks to increase important performance
indicators, such as precision, recall, and mean reciprocal rank (MRR), thus boosting the
overall effectiveness of the recommendation system. Furthermore, the qualitative results
show that providing more relevant and diverse recommendations increases user happiness,
demonstrating the system’s effectiveness in satisfying users’ particular needs.

The article in [41] discusses how different amounts of novelty and variety in recom-
mendation algorithms affect user happiness, algorithm performance, and system accuracy:

•

•

Impact of Diversification on User Satisfaction: According to the study, user satis-
faction is highest when recommendations have a balanced level of relevance and
diversity, especially a diversity score of 0.6. This balance indicates that people respect
moderately diversified content in their suggestions [41].
Relevance–Diversity Trade-Off: One important point raised is the inevitable trade-off
between relevance and diversity; as diversity grows, relevance frequently declines,
potentially affecting user experience. This tension is critical for recommendation
techniques that try to enhance both elements concurrently [41].

• Algorithm Performance: Algorithms that use a greedy, marginal relevance maximiza-
tion (MMR) approach perform better in terms of diversity without compromising
too much relevance. Adaptive algorithms that modify the timing of diversification
outperformed similarity-based techniques [41].
Empirical Comparisons Using Metrics: The article examines algorithms based on
metrics such as ERR-IA and subtopic recall to assess relevance and variety. These
measurements, especially when applied to movie genres, provide a complete picture
of algorithm effectiveness [41].

•

The study on the kernel-mapping-based Group Recommender System (KGR) by Guo
et al. [42] aims to enhance recommender system performance by addressing cold-start
and data sparsity issues. The KGR model leverages user-trust relationships to form user
groups, mitigating these problems. The study introduces kernel mapping techniques to
create group kernels and matrices, enabling multilinear mapping between group–item
interactions and user preferences. A hybrid model is proposed that combines group and
individual user kernels, emphasizing individual preferences within groups. The KGR
model [42] is validated on two trust-based datasets, demonstrating effectiveness through
RMSE metrics. Optimal parameter values are identified to further improve the model’s
performance and reduce RMSE errors. These strategies collectively enhance the accuracy
and effectiveness of group recommendations in the KGR system.

The recommender system is a mechanism that helps users to make decisions in
complex information contexts [3,14]. In the world of e-commerce, it is a tool that helps
consumers to find knowledge that is relevant to their interests and preferences [29]. It also
promotes the social process of relying on recommendations from others when personal
knowledge or experience is insufficient. Recommender systems address the issue of infor-
mation overload by making individualized and specialized recommendations for content
and services. These systems have been designed using a variety of approaches, including
collaborative filtering, content-based filtering, and hybrid filtering [13,30]. Collaborative
filtering is the most widely utilized of these approaches. It recognizes people who share
similar likes and recommends products based on their assessments.

Collaborative filtering has been applied in a variety of sectors, including news-based
architectures, online social information filtering systems, and e-commerce platforms such

---

<!-- PAGE 8 -->

J. Imaging 2025, 11, 12

8 of 66

as Amazon [43], Netflix [44], Spotify, YouTube, Facebook, news articles, and financial
services [27]. On the other hand, content-based filtering associates content resources with
user attributes, relying on human knowledge rather than the opinions of others.

Both collaborative- and content-based approaches provide numerous benefits, such
as business advantages, personalization, efficiency, and discovery. However, they have
some disadvantages, including limited content analysis, privacy concerns, a lack of user
control, overspecialization, data scarcity, cold-start challenges, and scalability limitations.
To address these restrictions, hybrid filtering methods have been proposed [15]. These ap-
proaches incorporate various filtering strategies to improve the accuracy and performance
of recommender systems [29]. Hybrid filtering approaches are classified according to their
operations: weighted hybrid, mixed hybrid, switching hybrid, feature-combination hybrid,
cascade hybrid, feature-augmented hybrid, and meta-level hybrid [24]. Currently, collabo-
rative filtering and content-based filtering methods are widely used, either by combining
their predictions or adding features from one technique into the other [15,18,29,31–33,35].
In the study in [45], the authors investigated the several challenges of developing
an effective hybrid recommendation system for online purchasing. The key issues are
as follows:

Defining Lexical Variables: The fuzzy expert system uses linguistic variables to model

ambiguous notions [45].

Various Approaches: The system includes collaborative filtering, content-based tech-
niques, and a fuzzy expert system. It can be difficult to balance these many approaches and
guarantee that they function together nicely, resulting in inconsistencies in ideas [45].

Evaluating Performance Metrics: Achieving great precision and recall is critical to the
system’s performance. The study aspires for results above 90%, so comprehensive testing
and validation against established methodologies is required to ensure dependability and
effectiveness [45].

User Choice Management: The system must be able to react to changing user prefer-
ences and behaviors. This necessitates a reliable technique for capturing and evaluating
user activity regarding online shopping, which can be challenging given the fast pace of
customer interactions [45].

The primary goal of the study in [46] is to provide a hybrid recommender system de-
signed to improve the selective dissemination of the research resources inside a Technology
Transfer Office (TTO). The precise objectives described in the paper are the following:

Improving Information Discovery: The system is intended to assist TTO personnel
and researchers in quickly locating relevant information, addressing the issues created by
the expanding volume of available research materials [46].

Personalized Suggestions: The goal is to provide tailored suggestions based on user

profiles, boosting the relevancy of the information supplied to users [46].

Facilitating Cooperation: The system is designed to detect possible cooperation oppor-
tunities among researchers, hence encouraging the formation of multidisciplinary teams to
better research outputs.

Using Fuzzy Lexical Modeling: The article discusses the use of fuzzy linguistic
modeling to describe qualitative information, which improves user–system interaction and
the complete efficacy of the recommender system [46].

In the realm of recommendation systems, hybrid-based quality recommender systems
are becoming increasingly significant. Combining several approaches has shown promise
in raising the efficacy and accuracy of recommendations in a range of fields. The increasing
need for customized recommendation services will surely require the research and devel-
opment of hybrid-based recommender systems, which will help to reduce information
overload and provide users insightful suggestions.

---

<!-- PAGE 9 -->

J. Imaging 2025, 11, 12

9 of 66

Hybrid recommendation systems based on quality consider both user preferences and
the quality of the recommended goods at the same time, combining several techniques
to deliver relevant recommendations [18]. With the goal of overcoming the drawbacks
of single-strategy techniques, these quality-aware hybrid recommender systems offer an
exciting evolution in the industry. These systems combine several techniques to provide
more accurate and nuanced recommendations. These tactics include content-based filtering,
which focuses on item attributes, and collaborative filtering, which leverages the behavior
and preferences of other users. These hybrid systems’ capacity to manage the complexity
and diversity of user preferences and item characteristics is one of their main advantages.
For instance, a hybrid approach to movie selection may take into account both the user’s
favorite genres and the films’ critical reception, guaranteeing that only well-received films
are recommended.

3. Goal of the Literature Review

Systematic reviews use rigorous and transparent procedures to provide a full and
impartial appraisal of several relevant studies in a single document. A systematic review’s
goal is to synthesize and summarize the current body of knowledge, with the goal of
uncovering all the relevant data relative to a certain subject.
It is an additional area
of study that aims to locate, evaluate, and interpret all the available information from
primary studies that is relevant to a specific research issue. To guarantee a robust and
systematic literature review (SLR) approach, we followed the standards stated in the
Cochrane Handbook [47] and those proposed by Kitchenham and Charters [48,49]. These
criteria, which are widely accepted in the research community, provide a foundation
for conducting comprehensive and unbiased assessments. We aimed to reduce bias and
ensure the reliability and validity of our systematic review by adhering to these established
principles (see Figure 1).

The overall goal is to assess the progress of hybrid recommender techniques and
propose potential topics for further study. The objectives are to examine the current trends
in difficulties, approaches, datasets, application areas, and assessment measures using a
hybrid approach. A systematic literature review is a time-consuming task that requires the
researcher to design the protocol, adjust the search string, filter the results, sometimes more
than a thousand articles, select those that meet the inclusion criteria, and remove those that
do not meet the exclusion criteria. Following that, the researcher may begin to study the
relevant results one by one.

3.1. Reasons for Conducting Systematic Literature Reviews

A systematic literature review is performed for a variety of reasons [48]:

1.

2.

Summarizing the existing knowledge and information concerning research questions
or technology, such as the empirical evidence on the benefits and limitations of a
specific agile approach. They provide a comprehensive overview of what is known in
the field.
Identifying Knowledge Gaps: Systematic reviews can discover knowledge gaps by
reviewing existing material. These gaps can assist researchers in identifying places
where further study is required.

3. Making Choices Based on Proof: Systematic reviews are an important tool for making
evidence-based decisions. They serve as a foundation for making educated judgments
in a variety of disciplines, including healthcare, education, and policy creation.
4. Minimizing Bias: Systematic reviews locate and choose relevant research in a system-
atic and accessible manner. This decreases the possibility of bias in study selection
and interpretation, making the results more credible.

---

<!-- PAGE 10 -->

J. Imaging 2025, 11, 12

10 of 66

5.

6.

7.

8.

9.

Bringing Conflicting Evidence Together: In some domains, the literature may present
contradictory conclusions. Systematic reviews seek to synthesize and evaluate contra-
dictory material to present a more complete picture of the state of knowledge.
Policy and Practice Insights: Systematic reviews are frequently used to inform policy
decisions and clinical practice guidelines. They provide a solid evidence framework
for making recommendations and judgments with substantial societal implications.
Time and Resource Efficiency: Conducting a systematic review might be more effi-
cient than beginning a new study, especially if the issue has previously been well
investigated. By using the current research, it can save time and resources.
Systematic reviews can aid in the prevention of duplication of research efforts. Re-
searchers may assess what has previously been completed and concentrate their
attention on areas that require fresh investigation.
Establishing a Baseline: A systematic review can serve as a starting point for re-
searchers who are new to a topic, offering a baseline grasp of the present state of
knowledge. Systematic literature reviews, on the other hand, can be used to assess
how much the empirical data supports or contradicts the theoretical assumptions, or
even to aid in the development of new theories.

Figure 1. The basic steps in conducting a systematic literature review.

3.2. The Value of Systematic Literature Reviews

The goal of systematic reviews is to synthesize available knowledge in an equitable and
transparent manner. They adhere to a preset search technique that allows them to analyze

---

<!-- PAGE 11 -->

J. Imaging 2025, 11, 12

11 of 66

the completeness of the search. Researchers performing a systematic review must seek
out and publish findings that both support and contradict their favored study hypothesis.
Systematic reviews improve the integrity and credibility of the research process by adhering
to these standards.

They are critical tools for advancing knowledge, influencing decision-making, and
guaranteeing the use of the best available evidence in a variety of research and practice sectors.

4. Methodology for Review Process

The Preferred Reporting Items for Systematic Reviews and Meta-Analyses (PRISMA)
guidelines comprised the methodology used for this investigation [50]. Several recommen-
dation techniques have been proposed and applied in the field of recommendation systems.
However, implementing these techniques in the context of hybrid recommendation sys-
tems poses several challenges and opportunities while considering quality. The primary
objective of this research is to examine the current and emerging approaches applied to
hybrid recommendation systems in the recent research literature and outline avenues for
future research. To ensure a systematic review process as indicated above, we have adopted
the guidelines from [47,48]. The steps of our review process are illustrated in Figure 1.
It involves eight main steps: research question formulation, establishment of systematic
review protocol, performing an extensive literature search, screening and selecting studies,
examining the bias and quality of the studies, data extraction, analyzing the information
gathered, and sharing the outcomes (see Figure 1).

4.1. Question Formalization

The fundamental purpose of this systematic literature review is to learn what diffi-
culties HRSs could successfully handle, how they are built and evaluated, and how they
could be experimented with in terms of manner or features [24,51,52]. Thus, the following
research questions (see Table 1) were developed:

Table 1. SLR: research questions.

Research Questions

Motivation and Projected Results

RQ1. What are the relevant studies on
hybrid recommenders, and how do hy-
bridization techniques solve specific diffi-
culties such as cold-start, novelty, diversity,
and user satisfaction?
RQ2. What are the various hybridization
strategies that have been employed to in-
crease the performance of quality recom-
mender systems in the context of big data?
RQ3. What types of data sources have
been used to evaluate the techniques in re-
cently published hybrid recommendation
systems?
RQ4. What experimental outcomes are
generated when hybrid recommender tech-
niques are used?
RQ5. What is the suggested methodology
in hybrid recommendation systems?
RQ6. What are the most promising future
research directions?

Identifying challenges connected to recom-
mendation systems (Data Sparsity, Model
Bias, Overfitting, and Dimensionality Re-
duction).

Address the issues that come with develop-
ing effective quality recommender systems
in a setting of massive amounts of data.

To pinpoint contributions closely associ-
ated with using recommendation systems
for proposing housing alternatives.

To increase the overall performance and
efficacy of recommendation systems, espe-
cially in large-scale, complex data contexts.

Identify the proposed methods in hybrid
quality-based recommendation systems.

Determine potential research directions
for improving hybrid quality-based recom-
mendation systems.

---

<!-- PAGE 12 -->

J. Imaging 2025, 11, 12

12 of 66

To address these research questions, we generated a research string utilizing terms

related to our topic.

The primary keywords are hybrid, quality, recommender systems, dissemination,
information, and big data, and then we introduced synonyms to obtain the final list of
keywords, as shown in Table 2.

Table 2. Keywords and synonyms.

Keyword

Synonyms

Hybrid

System

Hybridization, Mixture, Mixed

Systems, Approach, Software, Engine, Technology, Technique, Techniques

Recommender Recommendation

We employed Boolean operators in our systematic literature review search method.
These operators, which include “AND” and “OR”, are used to connect alternative terms.
We can cluster synonymous or related phrases by using the “OR” operator, and we can
merge distinct components inside the search string by using the “AND” operator. We
created a comprehensive and precise search string by skillfully applying these operators,
allowing us to highlight relevant studies and gather valuable insights for our methodical
assessment of the literature. Then, we used the selection strategy, which was based on
some critical factors such as the year of publication, the language of the paper, and the title.
We restricted our research to English papers. In addition, we considered the reputation
and validity of the journals, as well as the recently published papers. Subsequently, we
reviewed each item and selected those that were relevant to the topic. As a result, the
selection procedure consists of three major steps: searching, paper and journal filtering,
and content-based selection.

Consequently, we obtained the study string illustrated in Table 3.

Table 3. Basic query.

* Basic Search String

((hybrid OR hybridization OR mixture OR mixed) AND “Quality Based” AND (recom-
mender OR recommendation) AND (system OR systems OR approach OR software OR
engine OR technology OR technique OR techniques)) OR ((hybrid OR hybridization
OR mixture OR mixed) AND “Quality Based” AND (recommender OR recommenda-
tion) AND (system OR systems OR approach OR software OR engine OR technology
OR technique OR techniques) AND information AND “big data”)

4.2. Database Analysis and Research Methodology

Researchers have studied hybrid recommender systems in many different studies.
We examined this research using the established method of a systematic literature review,
which is based on the state-of-the-art recommendations outlined above.

This protocol’s steps are as follows (see Figure 2):

Identifying research questions.
Previous research findings.
Searching databases for relevant research based on hypotheses.
Selecting data based on predefined inclusion and exclusion criteria.

1.
2.
3.
4.
5. Analyzing the collected data.
6.
7.

Study findings.
Ideas for further research.

---

<!-- PAGE 13 -->

J. Imaging 2025, 11, 12

13 of 66

Figure 2. Literature review process template.

The information sources chosen are most prominent scientific databases that have been
used for other relevant works of indexed journals in Journal Citation Report (JCR) [3,7].
These datasets are as follows:

1.

Scopus: This database may accept the complete query and offers the options to specify
additional particular filters (see Table 4 for question formulation and Figure 3 for
yearly distribution).

2. Web of Science: When conducting a systematic review, employing Web of Science has
benefits like thorough coverage, easy access to high-quality content, citation tracking,
sophisticated search tools, effective bibliographic management, and collaboration
support. Using these elements, systematic reviews can be made more thorough and
rigorous, enabling researchers to efficiently find, assess, and synthesize pertinent
papers (see Figure 4).
Springer Link: To comply with the download limit of 1000 objects imposed by this
database for the csv file, filters must be added to the item list. Because the current
query returned 4068 items at that time, exceeding the allowed threshold, it was
critical to narrow the list. This can be accomplished by implementing filters that
consider criteria such as publication date, discipline, language, and content type. By
incorporating these filters, we could effectively reduce the item list while still adhering
to the download restriction (see Figure 5 for distribution by year).

3.

4. Google Scholar: To overcome the limitation of extracting Google Scholar search
results, we used the open-source tool “Harzing’s Publish or Perish” for exporting the
results in Excel (see Table 5). The search process in this database presented additional
challenges when compared to other databases for three main reasons:

•

•

Incomplete Search String: Google Scholar does not allow you to directly enter a
complete search string. As a result, we had to use the basic search tool to conduct
a search that would return results matching the initial search string.
Difficulty in Search: Google Scholar’s search functionality is more intricate than
that of other databases, making it more difficult to obtain desired results. To
retrieve the relevant information, careful navigation and the use of appropriate
search techniques were required (see Figure 6). In fact, due to the absence of

---

<!-- PAGE 14 -->

J. Imaging 2025, 11, 12

14 of 66

results from the original query, we decided to cancel it in order to address this
issue. In its place, we shall investigate an alternative technique by running the
below query.

• However, using this specific database made it possible to include “gray litera-

ture”, including proceedings from conferences.

5. ACM Digital Library https://dl.acm.org/, access date: 10 December 2023 Because of
the enormous quantity of papers, we narrowed our search to the years 2020 to 2024
and focused on journals (see Figure 7).

Figure 3. Scopus: number of articles published in the study area from 2020 to 2024.

Table 4. Scopus: the search string keywords with filters.

* Scopus: Advanced Search Keywords

((hybrid OR hybridization OR mixture OR mixed) AND “Quality Based” AND (recom-
mender OR recommendation) AND (system OR systems OR approach OR software OR
engine OR technology OR technique OR techniques)) OR ((hybrid OR hybridization OR
mixture OR mixed) AND “Quality Based” AND (recommender OR recommendation)
AND (system OR systems OR approach OR software OR engine OR technology OR
technique OR techniques) AND information AND “big data”) AND PUBYEAR > 2019
AND PUBYEAR < 2025 AND (LIMIT-TO (OA, “all”)) AND (LIMIT-TO (SUBJAREA,
“ENGI”) OR LIMIT-TO (SUBJAREA, “COMP”) OR LIMIT-TO (SUBJAREA, “BUSI”))
AND (LIMIT-TO (LANGUAGE, “English”)) AND (LIMIT-TO (EXACTKEYWORD, “Ma-
chine Learning”)) AND (LIMIT-TO (DOCTYPE, “ar”))

---

<!-- PAGE 15 -->

J. Imaging 2025, 11, 12

15 of 66

Figure 4. Web of Science: number of articles published in the study area.

Figure 5. Springer: number of articles published in the study area from 2020 to 2024 without
preview-only content.

---

<!-- PAGE 16 -->

J. Imaging 2025, 11, 12

16 of 66

Figure 6. Google Scholar: number of articles published in the study area from 2020 to 2024.

Figure 7. ACM Digital Library: number of articles published in the study area.

---

<!-- PAGE 17 -->

J. Imaging 2025, 11, 12

17 of 66

Table 5. Google Scholar: the search string keywords with filters.

* Google Scholar: Advanced Search Keywords

((hybrid OR hybridization OR mixture OR mixed) AND (recommender OR recommen-
dation) AND (system OR systems OR approach OR software OR engine OR technology
OR technique OR techniques)) OR ((hybrid OR hybridization OR mixture OR mixed)
AND (recommender OR recommendation) AND (system OR systems OR approach OR
software OR engine OR technology OR technique OR techniques) AND information)

4.3. Eligibility Criteria

As previously stated, the fundamental goal of a systematic review is to collect relevant
techniques suggested within a certain field. To guarantee that only relevant articles are
kept during the search process, the inclusion and exclusion criteria for a literature review
must be properly defined [48,53].

The specific traits, attributes, or criteria that are utilized to determine whether a given
study or article should be included in the review are referred to as inclusion criteria (IC).
Exclusion criteria (EC), on the other hand, are the specific features, attributes, or
conditions used to determine which studies or papers should be rejected during the review
process. A paper is considered to be eligible if it meets the following requirements:

•

•
•
•
•

•
•
•
•
•

IC1: Papers offering hybrid quality-based recommender systems, algorithms, and
techniques in the context of big data.
IC2: Papers from conferences and journals published between 2020 and 2024.
IC3: The paper incorporates search-relevant keywords within its title or abstract.
IC4: The paper addresses hybrid recommendation systems.
IC5: The paper addresses at least one problem of recommendation or proposes at least
one technique of hybridization.

The exclusion criteria are the following:

EC1: The publication date is earlier than 2020.
EC2: The paper is written in a language other than English.
EC3: The paper is a short article, a standard, a poster, an editorial, or a tutorial.
EC4: The title, abstract, and keywords are not relevant to the research topic.
EC5: The paper does not discuss hybrid recommendation systems.

4.4. Information Sources

In accordance with review process Step 2 (see Figure 2), we ran the search string
through the search engines of some digital libraries, yielding a total of 5857 preliminary
primary studies (see Table 6). This retrieval process was conducted at the start of 2024.
The varying number of publications obtained from digital libraries is due to changing the
primary query (see Figure 8) of the search in certain databases that have a limit on the
number of Boolean operators, using third-party data extraction tools, and differences in
search engine filtering settings. We developed a set of inclusion/exclusion criteria, as shown
in Section 4.3, to help us make rational decisions about which exploratory investigation
to pursue further. These requirements serve as the foundation for focusing on the most
relevant research that aligns with the review’s aims. Duplicate papers were removed, and a
coarse selection phase followed. Given the impracticality of processing all publications, we
decided to include just journal articles, scientific articles, and machine learning articles in
some databases and all article types in others, excluding workshop presentations, review
reports, and gray literature, especially for Scopus and Springer data, due to the number
returned by the basic query (see Figure 8). We started by looking at the title, publishing
type (conference, workshop, journal, etc.), and publication year. We looked at the abstract

---

<!-- PAGE 18 -->

J. Imaging 2025, 11, 12

18 of 66

or other sections of each article in many situations to determine its relevance. Because
the goal of this review study is to focus on quality in a large data setting with hybrid
recommender systems, we chose articles that offered mixed or blended recommendation
systems while avoiding those that addressed single recommendation techniques or did not
discuss recommendation systems at all in the context of big data.

The first selection process, along with the application of date-related inclusion and
exclusion criteria, yielded a list of 3557 articles. Following that, we conducted a more
thorough review and selection of articles, limiting ourselves to specific sorts of articles to
yield 131 articles. Following that, we conducted a more in-depth review and selection of
the papers, selecting only open-access articles, to yield 81 articles. (see Figure 8). The whole
list, as well as publication information, can be found in Appendix A.

As indicated in Figure 8, these statistics provide an overview of the number of articles
discovered in multiple databases and based on various search parameters, such as pub-
lication date, article type (e.g., journal articles, open access, etc.), and specific topic (e.g.,
science, machine learning, and English). These data will be used to refine our search or
analyze the relevancy of the results based on our individual research objectives.

Here is an interpretation of the numbers indicating the articles found in various

databases and using various search criteria:

1.

Preliminary Research Findings (see Figure 8):
• Total articles found in the preliminary research: 5857 articles.

2. ACM:

• Total articles found in the ACM database: 376 articles.
• Articles from 2020 or later in the ACM database: 187 articles.
• Total journal articles found: 33 articles.
• Total open-access articles found: 19 articles.

3. Google Scholar:

• Total articles found on Google Scholar: 55 articles.
• Articles from 2020 or later on Google Scholar: 13 articles.
• Total articles of all types on Google Scholar: 13 articles.
• Open-access articles on Google Scholar: 6 articles.

4.

5.

Scopus:
• Total articles found in Scopus with basic query string: 1348 articles.
• Articles from 2020 or later in Scopus: 838 articles.
• Total articles with restrictions (English, engineering, ML, business, etc.): 28 articles.
• Open-access articles in Scopus: 14 articles.

Springer:
• Total articles found in Springer: 4068 articles.
• Articles from 2020 or later in Springer: 2509 articles.
• Articles related to science in Springer: 32 articles.
• Open-access articles in Springer: 32 articles.

6. Web of Science:

• Total articles found on Web of Science: 10 articles.
• Articles from various dates in Web of Science: 10 articles.
• Total articles of all types in Web of Science: 10 articles.

---

<!-- PAGE 19 -->

J. Imaging 2025, 11, 12

19 of 66

Preliminary research
findings=5857

ACM = 376

Google
Scholar = 55

Scopus
= 1348

Spinger
= 4068

Web of
science = 10

Date ≥ 2020
= 187

Date ≥ 2020
= 13

Date ≥ 2020
= 838

Date ≥ 2020
= 2509

All dates
= 10

Journals
= 33

All Types
= 13

(En, ML,B)
= 43

science
Articles = 32

All Types
= 10

Open Access
or Free= 19

Open Access
or Free= 6

Art, Open Access
or Free= 14

Open Access
or Free= 32

Open Access
or Free = 10

Figure 8. Data selection methods.

Table 6. Dissemination of papers sourced from academic databases.

Retrieval

Preliminary Removal Second-Level Selection

376

55

1348

4068

10

187

13

838

2509

10

19

6

14

32

10

Database
Source

ACM

Google Scholar

Scopus

Springer

Web of Science

Total

4.5. Data Extraction

At this point, every study that was part of the systematic review had been located,
and we need to move on to extracting the data. A template can be used to gather the data
needed to analyze the studies. Standard documents are available for this purpose, such
as the Preferred Reporting Items for Systematic Reviews and Meta-Analyses (PRISMA)
Statement [54] and the Cochrane data collection form for intervention review [55]. These
forms can be utilized in the training and education sciences, and analysts can modify and
test them in accordance with the goals of the systematic review.

During this phase, we designed a customized form with a range of parameters such
as title, author, year, and so on [48]. The form was then filled out with information about
the research topics for all the selected papers. Table 7 contains a list of these attributes. The
purpose of this operation was to collect and synthesize data to answer the defined research
questions. The extracted data were listed in the first column, an explanation for some of
the extracted data that may appear ambiguous is provided in the second column, and the
research question to which the data are connected is provided in the third column (see
Table 7).

---

<!-- PAGE 20 -->

J. Imaging 2025, 11, 12

Table 7. Form for extracting data.

Extracted Data

Explanation

Title

Authors

The name of the article

-

Description

Brief overview of the paper’s content

Publication year

Source

Publisher

Source of digital library access

-

Application domain

Application domain of the study

Approach

Contribution

Methodology employed

Research work’s significance

20 of 66

RQ

RQ1

-

-

RQ1

RQ3

-

-

RQ2, RQ5

-

Evaluation methodology Approach to evaluating the recommender system RQ6

Dataset

Experiment

Future work

Data repository

Explanation of the experiment

Proposed future research areas

RQ4

RQ4

RQ6

5. PRISMA Checklist

The PRISMA Checklist is a tool used mostly in the field of health and research to
assess the quality of studies and reports (see Table 8). The term “PRISMA” refers to the
abbreviation “Preferred Reporting Items for Systematic Reviews and Meta-Analyses”.

Table 8. PRISMA 2020 Checklist.

Section/Topic

#

Item

Page Where
Item Is Reported

the

TITLE

Title

1 This report describes a systematic review conducted in accor-
dance with PRISMA guidelines. The goal of this review was
to summarize the evidence on hybrid recommender systems.

1

ABSTRACT

Abstract

2

1, 8, 19, 36

Systematic reviews use rigorous methodologies to provide
a thorough assessment of relevant studies while combining
existing knowledge on specific issues. Following the stan-
dards in the Cochrane Handbook, Kitchenham, and Charters
ensures transparency and quality. This paper also evaluates
hybrid recommendation systems, emphasizing their expand-
ing importance and potential future research avenues, such as
incorporating contextual information and enhancing scalabil-
ity with sophisticated algorithms. A strong emphasis is placed
on the effectiveness of machine learning in filtering relevant
material on these systems.

---

<!-- PAGE 21 -->

J. Imaging 2025, 11, 12

21 of 66

Page Where
Item Is Reported

the

2, 3, 4, 45–66

3, 4, 45–66

16

Table 8. Cont.

Section/Topic

#

Item

INTRODUCTION

Rationale

Objectives

3 The review of hybrid recommendation systems discusses their
increasing importance in providing individualized user expe-
riences while overcoming the constraints of older methods. It
seeks to identify best practices, emerging trends, and future
research directions that will improve the effectiveness and flex-
ibility of these systems.

4 The paper attempts to consolidate existing knowledge on hy-
brid recommendation systems, identify best practices, and
assess emerging machine learning trends. It also aims to iden-
tify research gaps, present a consistent evaluation system, and
guide practical applications to improve user experiences.

METHODS

Eligibility Criteria

5

IC1: Papers offering hybrid quality-based recommender sys-
tems, algorithms, and techniques in the context of big data.
IC2: Papers from conferences and journals published between
2020 and 2024.
IC3: The paper incorporates search-relevant keywords within
its title or abstract.
IC4: The paper addresses hybrid recommendation systems.
IC5: The paper addresses at least one problem of recommen-
dation or proposes at least one technique of hybridization.
EC1: The publication date is earlier than 2020.
EC2: The paper is written in a language other than English.
EC3: The paper is a short article, a standard, a poster, an
editorial, or a tutorial.
EC4: The title, abstract, and keywords are not relevant to the
research topic.
EC5: The paper does not discuss hybrid recommendation
systems.

Information Sources

6 Using specific search keywords, we searched Scopus, ACM,

17, 18

Search Strategy

7

Web of Science, Springer, and Google Scholar.

Scopus’ search method included employing specific terms such
as “Hybrid Quality Based Recommender Systems”, “Informa-
tion”, and “Big Data”, paired with Boolean operators. The
search was restricted to publications published from 2020 to
early 2024, with emphasis on relevant subject areas and docu-
ment types.

Selection Process

8 Two independent reviewers first choose titles and abstracts,
then analyze the complete text of the selected research. Any
disagreements were handled through consensus on articles
that were not retained by the two authors. An additional
perspective was gained utilizing the ASReview tool to ensure
a comprehensive and impartial selection process.

12, 14, 18

10–20, 28

---

<!-- PAGE 22 -->

J. Imaging 2025, 11, 12

22 of 66

Table 8. Cont.

Section/Topic

#

Item

Data Collection Process

Data Items

Risk of Bias Assessment

9 We ensured validity by conducting a double extraction process
by independent reviewers after going through the entire text
of the included articles to methodically extract and summarize
the data in a standardized table format to make comparisons
easier. Choosing the pertinent data points, constructing and
testing the extraction table, checking the gathered data for mis-
takes, and, if required, updating and pilot testing the approach
are all part of this process.

10 Data extraction was utilized to look for factors such as the
study’s subject, strategy, sample size, demographic charac-
teristics, objectives, data gathering techniques, and outcomes.
These factors enable a comprehensive examination and com-
parison of studies.

11 We evaluated the risk of bias using the Cochrane Risk of Bias
Tool, which included independent reviews by two reviewers
and an open-source application. Discrepancies were resolved
collectively, and the outcomes were thoroughly documented
for analysis.

Page Where
Item Is Reported

the

17–20

45–66

37–38

Effect Measures

12 Commonly Used Principal Summary Measures (Precision, re-

35–36, 41

Synthesis of Results

call, and F1-score).

13 A systematic literature study for hybrid recommender systems
begins with data extraction, which is organized and standard-
ized, followed by method categorization and statistical evalua-
tions of performance measures. Meta-analysis, visualization
tools, and thematic synthesis are used to combine and under-
stand findings from multiple studies.

24–45

Reporting Biases

14 Describe any methods used to assess the risk of bias due to

38, 39

selective reporting.

Certainty Assessment

RESULTS

15 The assessment of evidence certainty, which takes into ac-
count study quality, bias risk, and consistency, guarantees
solid results and conformity to quality and transparency re-
quirements.

18, 19, 32, 35

Study Selection

16 Present the number of studies screened, assessed, and in-

25, 35, 40

cluded, with reasons for exclusions.

Study Characteristics

17

For each included study, present characteristics (e.g., partici-
pants and interventions).

45–66

Risk of Bias in Studies

18 Present risk of bias judgments for each included study.

38, 39

Results of Individual Stud-
ies

19

For all outcomes considered, present the results of each study.

37–38

Synthesis of Results

20 Present results of syntheses (e.g., meta-analyses), including

45–66

confidence intervals.

Reporting Biases

21 Report on the presence of any selective reporting.

Certainty of Evidence

22 Present an assessment of the certainty (e.g., GRADE).

18, 19, 32, 35

DISCUSSION

Summary of Evidence

23

Summarize the main findings, including the strength of evi-
dence.

4, 6, 7, 36, 38

---

<!-- PAGE 23 -->

J. Imaging 2025, 11, 12

23 of 66

Table 8. Cont.

Section/Topic

#

Item

Page Where
Item Is Reported

the

Limitations

Conclusions

FUNDING

Funding

24 Discuss limitations of the evidence and the review process.

15, 18, 19, 38, 39

25

Provide a general interpretation of the results in the context of
other evidence.

10, 12, 37, 38, 42, 44

26 Describe sources of funding and other support for the review. Not Available

5.1. Main Objectives

•

Transparency: Ensure that systematic studies and meta-analyses are presented clearly
and completely.

• Quality: Improve the quality of research reports to facilitate understanding and

•

evaluation.
Standardization: Provide a standardized framework for researchers to follow while
writing their work.

5.2. Components

The PRISMA Checklist often includes a list of important criteria to follow, such as

the following:

1.
2.
3.
4.

The definition of research objectives.
The methodology for selecting studies.
Evaluation of bias.
The synthesis of results.

5.3. Utilization

Researchers use this checklist to ensure that they cover all the necessary aspects while
writing their studies, which contributes to better research valorization and use in the
scientific environment.

6. Results Synthesis and Discussion

In this section, we provide the findings from the selected studies, addressing the
research questions (see Section 4.1) by analyzing categorized challenges, procedures, hy-
bridization classes, and evaluation methodologies. The investigations highlight a variety
of concerns, including information overload, suggestion accuracy, and system scalability,
all of which offer substantial hurdles for e-commerce recommendation systems. These
identified concerns inform our investigation of potential approaches for overcoming them.
To address these issues, the research applies to a variety of recommendation strategies,
including collaborative filtering, content-based algorithms, and deep learning approaches.
Each strategy is designed to address a certain need, such as increasing customization or
lowering computational demands. This diversity emphasizes the necessity of using the
proper strategy for each individual challenge, and examples from the research show their
success in various aspects of e-commerce.

We assessed the numerous papers that we deemed relevant for our evaluation from

various angles.

We used examples from the included research to show the various kinds of problems,

strategies, hybridization classes, assessment methodologies, and so on.

---

<!-- PAGE 24 -->

J. Imaging 2025, 11, 12

24 of 66

6.1. Quantitative Evaluation

This part examined the screened papers in the hybrid recommender systems, con-
centrating solely on three types of metadata: database, year of publication, and informa-
tion sources. To address these issues, the research applies a variety of recommendation
strategies, including collaborative filtering, content-based algorithms, and deep learning
approaches. Each strategy is designed to address a certain need, such as increasing cus-
tomization or lowering computational demands. This diversity emphasizes the necessity
of using the proper strategy for each individual challenge, and examples from the research
show their success in various e-commerce contexts.

6.1.1. Data Origin

The percentage of papers in each database is shown in Figure 9a. We found nineteen
papers in the ACM database (24%), six papers in Google Scholar (7%), fourteen papers
in Scopus (17%), thirty-two papers in Spinger (40%), and ten papers in Web of Science
(12%). With a percentage of 40%, we observe that Springer offers the repository with the
highest quantity of papers. Springer’s extensive collection may be due in large part to the
company’s lengthy history, well-established reputation, and fame in academic publishing.

(a)

(b)

Figure 9. Article counts for the distribution of academic paper databases. (a) Ratio of articles vs.
database. (b) Academic paper database spread.

6.1.2. Year of Publishing

As previously mentioned, the research was carried out for the period 2020 to the
beginning 2024 excluding Web of Science and Scopus, which include data from all dates
(until the beginning of 2024). The diagram presented in Figure 9b shows the number of
papers by year of publication.

Additionally, the pie chart in Figure 9b reveals that the current year has the fewest
articles. This outcome is understandable given that the data were taken at the start of
2024. The timing undoubtedly adds to the lower figure as it does not account for possible
publications that may appear later in the year.

Below is a PRISMA flowchart that illustrates the inclusion and exclusion strategies
used in the study (see Figure 10). This flow chart was chosen for this study, describing
the flow of information through the various phases of a systematic review. It shows the
number of records identified, included and excluded, as well as the reasons for exclusions.
This section focuses on the four inclusion and exclusion stages of the PRISMA table:
identification, selection, eligibility, and inclusion. The search engine results from the five
databases (ACM, Google Scholar, Scopus, Springer, and Web of Science) yielded a total of

---

<!-- PAGE 25 -->

J. Imaging 2025, 11, 12

25 of 66

5857 articles. More than 2300 publications were eliminated because they did not correspond
to the time range set over the past 4 years for databases that return many articles and over
the past 10 years for those that return few. For certain databases, such as Scopus, which
are very consistent, we limited the search to journal, computer science, machine learning,
and business and management articles in order to reduce the scope of this study. We
obtained one-hundred-thirty-one documents. We then eliminated fifty publications due to
a lack of full text, four articles due to redundancy, and twenty-five others because they did
not correspond to the subject’s relevance based on their titles, keywords, or abstracts, or
because they did not meet the eligibility criteria, either because their text was not directly
related to our field of research or because their content lacked detail and precision, resulting
in fifty-two documents at the end.

The interaction of technology improvements and publishing patterns in hybrid rec-
ommender systems demonstrates how fast-changing tools and approaches can influence
research paths. As neural network architectures evolve, transformer models gain popular-
ity, and privacy concerns grow, researchers respond with novel answers and techniques.
These variables not only explain the increase in publication numbers but also indicate a
dynamic area that is evolving to meet the demands of the current technology and societal
needs. The number of articles on recommender systems over time shows a significant
trend (see Figure 11). This graph depicts the values after making various PRISMA analysis
selections, particularly the inclusion and exclusion criteria. Several significant patterns
emerge from the publication trends over time, reflecting the evolution of study interest in
hybrid recommender systems and associated technologies. Starting with modest research
production in the early years, such as 2004, 2008, 2012, and 2018, with only one publication
in each of these years, it is obvious that the topic was in its early stages or garnered little
attention during this time. Evidently, the field was still in its early stages of development,
which could be explained by a lack of funding and interest. However, 2020 was a watershed
moment, with the number of papers jumping to seven, indicating increased interest or
developments in the field. This rising trend continued into 2021, when the count increased
to eight items, then surged again in 2022, reaching fifteen.

In 2023, the total rose slightly to sixteen, indicating a continued rise in research
production. This consistent rise in recent years indicates a growing recognition of the value
and relevance of recommender systems in academic discourse. These rapid increases can
be attributed to the emergence of deep learning techniques, which enabled the integration
of complex data representations into recommendation models, as well as the frequent
adoption of cloud computing and technologies for big data, which made it easier to
manage large-scale, multifaceted data. The focus of the academic community on enhancing
user experience, combined with the industry’s quest for more personalized and adaptive
recommendation engines, are likely to have fueled this development. Using transformer
models could potentially help to hasten this advancement. The introduction of transformer
models was a significant milestone in natural language processing (NLP) as well. The
findings show that scholars are increasingly interested in this area owing to its practical
applications and theoretical significance. As the research in this area progresses, it is critical
to monitor these trends in order to understand the changing environment of recommender
systems. Overall, this tendency implies that a vibrant and dynamic field is gaining traction
within the academic community.

---

<!-- PAGE 26 -->

J. Imaging 2025, 11, 12

26 of 66

Figure 10. The research approach employed: diagram of the PRISMA process for inclusion
and exclusion.

Figure 11 and the pie chart in Figure 9b show that the current year has the fewest
number of articles. This development is expected given that the data were collected at
the beginning of 2024. The time of data collection most certainly influenced the outcome,
resulting in fewer publications being available this year. The early collection period does not
accurately reflect the possibilities for publication throughout the year. This understanding is
critical for appropriately analyzing the data. The figures emphasize the seasonality of article
creation. As a result, the current figures should be considered in light of their chronology.
Overall, the findings point to a transient dip rather than a long-term deterioration. Future
analysis may provide a more complete picture when additional articles are released. Given
the observed patterns in the publication numbers, it is critical to investigate how key
technological advancements influenced the landscape of hybrid recommender system

---

<!-- PAGE 27 -->

J. Imaging 2025, 11, 12

27 of 66

research. Advancements in neural network designs, the adoption of transformer models,
and the increased emphasis on privacy-preserving strategies have all likely had a significant
impact on the publication trends. We will examine each of these elements in depth:

Figure 11. Spread of research based on the publication year of chosen papers.

1. Advances in Neural Network Architectures: Recent years have witnessed tremen-
dous advances in neural network topologies, which have transformed the field of
machine Learning and, by extension, recommender systems.

• Deep Learning Techniques: The development and refinement of deep learn-
ing approaches have enabled academics to develop more sophisticated models
capable of processing complex data inputs. These developments enable better
representation learning, in which models can automatically recognize patterns
and features in raw data, resulting in higher recommendation accuracy.

• Hybrid Approaches: The merging of several neural network architectures, such
as convolutional neural networks (CNNs) for image data and recurrent neural
networks (RNNs) for sequential data, has aided in the creation of hybrid rec-
ommender systems that can use numerous data sources. This flexibility is most
certainly a major contributor to the current increase in publication rates.

2. Adoption of Transformer Models: Transformer models have ushered in a new era of

natural language processing (NLP) and beyond.

•

•

Transformer Architecture: Transformers, introduced through models such
as BERT and GPT, have raised the bar for comprehending and creating hu-
man language. Their capacity to capture long-term dependencies in data
makes them ideal for jobs involving user interactions and preferences in
recommendation systems.
Impact on Recommendations: The potential to more effectively simulate user
behavior and preferences with transformers has prompted study into their use
in recommender systems. This has most likely led to the rise in publications

---

<!-- PAGE 28 -->

J. Imaging 2025, 11, 12

28 of 66

as academics investigate creative ways to integrate transformers into hybrid
models, increasing their effectiveness across many domains.

To obtain a second opinion on this study, we used Active Learning for Systematic
Reviews (ASReview) as a secondary reviewer to identify the relevant articles [56]. This
tool is a machine learning software that implements different machine learning algorithms
that interactively query the researcher (see Figure 12). It enables the systematic review of
articles and analysis of metadata. ASReview could significantly improve the efficiency and
relevance of the systematic literature review process. ASReview allows the user to sort
documents while the active learning algorithm (Naïve Bayes by default) ranks unlabeled
documents in the background, from most relevant to least relevant.

It is sometimes viewed as a tool for selecting titles and abstracts in systematic reviews
or meta-analyses, but it can handle any type of textual data that needs to be selected
systematically.

Using the AI tool “ASReview” required multiple steps [57]. Before screening, the
software required training for its algorithm with multiple prelabelled papers. The AI tool
then offered the article with the greatest chance to be relevant using a researcher-in-the-loop
approach. The reviewer then determined the relevance of each recommended article. This
procedure was repeated until the stopping requirement was met.

The objective is to screen less data than are in our dataset, and simulated research
has shown that we may skip up to 95% of documents [56], although this is extremely
dependent on the dataset and inclusion/exclusion criteria [58]. When we have decided to
finish screening, we may export the findings (i.e., the partially labeled data and the project
file with the technical information to replicate the entire process) and post them on sites
like the Open Science Framework. Finally, in ASReview, mark the project as completed.

ASReview LAB saves time, improves the quality of results, and makes work more
transparent when examining large quantities of textual data to extract the relevant informa-
tion. Active learning will facilitate decision-making in any discipline or industry.

Using the AI tool involved multiple stages, prior to screening, the tool’s algorithm
needed to be trained using several prelabelled articles [57]. Next, using a researcher-in-
the-loop approach, the AI tool recommended the article with the highest likelihood of
relevance. The reviewer then determined the relevance of each article proposed. The
operation was repeated until the halting requirement was met. All papers deemed relevant
by the reviewer were reviewed for full text (see Figure 12).

The following are the essential steps [59]:

1. Data Import: Import the entire set of research documents into the ASReview software

2.

(that is, the metadata containing the text of the titles and abstracts).
Initial Formation: ASReview begins with an initial formation phase. The researcher
classifies a small subset of articles as relevant or irrelevant in order to form the
automatic learning model. In fact, prior knowledge is chosen and used to create
the first model and present the first recording to the researcher. Because this is a
binary classification problem, the evaluator must choose at least one key record to
include (specify label: relevant) and at least one key record to exclude (specify label:
irrelevant) based on prior knowledge. An automatic learning classifier is tasked with
predicting the relevance of the study (labels) based on a representation of the text
containing the recording (characteristic space) and prior knowledge.
After being trained with previous expertise, the AI tool ranks all unlabeled papers
(i.e., articles that had not yet been determined to be eligible) from highest to lowest
probability of relevance [57].

---

<!-- PAGE 29 -->

J. Imaging 2025, 11, 12

29 of 66

To avoid any authority bias in the inclusions, we have purposefully chosen not to
include the name of an author or a representation of a network of citations in the
space for characteristics.
Active Learning: ASReview employs an active learning strategy. The model examines
the labeled articles and selects the most ambiguous or informative ones. These articles
are presented to us in order to manually examine and categorize. Alternatively,
during the active learning cycle, the software displays a new record that the user must
examine and label. The user’s binary etiquette (1 for relevant and 0 for irrelevant) is
then used to create a new model, after which a new record is presented to the user.
This cycle will continue until the user specifies an end point.
Currently, the user has access to a file that contains (1) entries that have been labeled
as relevant or irrelevant and (2) entries that have not been labeled but are likely to be
relevant based on the current model’s predictions [56].
This configuration allows us to search for a large dataset much faster than possible
with a manual process while maintaining decision-making transparency.
Iterative Process: the researcher examines the selected articles and assigns labels
(relevant or not). ASReview incorporates the labeled data into the overall training
and updates the automatic learning model.

3.

4.

5. Model Refinement: The updated model learns from our labeled data and improves

6.

7.

its ability to predict the relevance of unlabeled items.
Iteration: Steps 3–5 are iteratively repeated. The model continues to select new
articles to investigate based on its uncertainty, and the researcher labels them in
order to refine the model. This iterative process reduces the number of articles to be
manually examined while maintaining high precision.
Final Article Selection: When the model reaches a stopping point (for example, a
desired level of examination exhaustion), ASReview returns a list of articles classified
according to their predicted relevance. This list will assist us in focusing our attention
on the articles that are most relevant to our systematic review.

Using ASReview, the researcher can significantly speed up the selection process by
assigning priority to the most relevant articles for the examination while reducing the
number of irrelevant articles that must be evaluated manually.

6.2. Out of Scope

The search mechanisms used in online databases are not perfect, so a substantial
number of papers obtained during the first phase of the appraisal are unrelated to the
searching scope. For this reason, a qualitative analysis founded on the examination and
assessment of content is required (see Figure 10).

6.3. Qualitative Analysis

The selected articles were classified using fundamental recommender system ap-
proaches. Table 9 shows how we classified the relevant studies into different groups.
Regarding relevancy according to inclusion/exclusion criteria, each study’s quality and
completeness were considered (in terms of problem characterization, description of sug-
gested method/technique/algorithm, and evaluation of findings).

---

<!-- PAGE 30 -->

J. Imaging 2025, 11, 12

30 of 66

Figure 12. Machine-learning-based ASReview pipeline. Graphic icons denote actions performed by
human or computer.

The research we examined shows a substantial tendency toward the growth of hybrid
recommender systems (HRSs). According to publication year, over 75 percent of the
studies we reviewed were published within the last three years (see Figure 11). These
statistics definitely suggest an increase in interest and research conducted in the field of
HRS. Researchers and practitioners are noticing the potential benefits and advantages of
integrating multiple filtering algorithms to improve the effectiveness and performance of
recommendation engines. The expanding corpus of recent literature indicates that hybrid
recommendation systems are becoming increasingly important and relevant in addressing
the constraints and limits of classic single-approach recommendation approaches. This

---

<!-- PAGE 31 -->

J. Imaging 2025, 11, 12

31 of 66

Primary

Collaborative

Filtering

Quality

Content-based

Based

Filtering

Hybrid filtering

Other filtering

trend emphasizes the field’s dynamic character and ongoing efforts to develop more
accurate tailored recommendation systems via the combination of various methodologies.

Table 9. Main selection of papers identified by categories, journals, and publishers.

Author

Publisher

Year

Journal

Category

[60]

[30]

[16]

[19]

[15]

[36]

[18]

[29]

[60]

[31]

[30]

[16]

[19]

[14]

[29]

[30]

[35]

[33]

[31]

[18]

[36]

[34]

[13]

[16]

[32]

[15]

[61]
[73]
[85]

Springer Nature

Elsevier BV

Google Scholar

Johannes Kepler

Springer Berlin

Computer Science

Appl. Sci.

ACM

Springer Nature

Springer, Cham

Elsevier BV

Google Scholar

Johannes Kepler

2023

2012

N/A

2021

2023

2013

2020

2022

2023

2020

2012

N/A

2021

Int. Jrnl. of Tech

Elect. Commerce Research

Google Scholar

N/A

Jrnl Cloud Comp.

Comp. Col. Int

Applied Sciences

Jrnl. Edu. D.Mng.

Int. Jrnl. of Tech

Adv.Net. Inf. Systems

Elect. Commerce Research

Google Scholar

N/A

Journal Of King Saud University

2022

Journal Of King Saud University

ACM

Elsevier BV

Elsevier Ltd

AI and Society

Springer, Cham

Appl. Sci.

Computer Science

Springer Int. Publish.

Taylor and Francis

Google Scholar

Springer

Springer

[62–67]
[74–79]
[86–91]

Legend: N/A = Not available.

6.3.1. Evaluation of Quality

2022

2012

2022

2020

2020

2020

2013

2023

2018

N/A

2020

2021

[68]
[80]
[92]

Jrnl. Edu. D.Mng.

Elect. Commerce Research

Inf. Proc. and Mngt

AI and Society

Adv.Net. Inf. Systems

Applied Sciences

Comp. Col. Int

Journal of Big Data

Applied AI

Google Scholar

Int. Jrnl on D.Lib.

Knowledge and Inf. Syst.

[69–72]
[81–84]
[93–96]

A systematic review locates, evaluates, and critically assesses pertinent studies by
applying explicit and systematic methods to a well-defined research question. Additionally,
it gathers and arranges data from the studies to comprise the review. The results of the
included studies are not always analyzed and summarized using statistical techniques
(meta-analysis) [97]. The relationship between the research question, methods, results, and
interpretation is assessed using a technique for evaluating the original quality of research

---

<!-- PAGE 32 -->

J. Imaging 2025, 11, 12

32 of 66

using methodological quality protocols, checklists, and/or scales. As such, the validity and
applicability of synthetic research findings depend heavily on the methodological quality
of the original studies [97].

To estimate the quality of the chosen studies, we also developed the nine questions

that are listed in Table 10.

We use weights of 0.5 for low importance, 1 for medium significance, and 1.5 for high
significance to assign weights to the questions. These coefficients are essential in establishing
how important each question is in relation to the others during the evaluation procedure.

Moreover, rate values are used to evaluate the answers to the questions. A “no” answer
receives a score of 0, a “partly” answer receives a score of 0.5, and a “yes” answer receives
a score of 1. These score values are useful for quantifying responses and evaluating study
quality [3,24].

The following formula is used to explain each paper’s evaluation [3,24]:

Evaluationpaper =

∑N

i=1 qwi ∗ ari
N

(1)

which performs a product operation between the query weight (qwi) (0.5, 1, 1.5) and the
answer rating value (ari) (0, 0.5, 1). N = 9 in our case is the number of quality questions (see
Table 10). Papers must meet the quality threshold of 0.80 in order to be accepted.

Table 10. Questions to evaluate the studies’ quality.

N# Quality Question

Weight

1
2
3
4
5
6
7
8
9

Has the study looked over the relevant research for the issues?
Did the study adequately describe the issue it is trying to solve?
Was an experimental solution clearly developed in the study?
Did the study explain recommender systems or algorithms in detail?
Was metrics evaluation for recommender systems explicitly used in the study?
Was the dataset used in the study described in detail?
Was the application domain introduced in the study clearly?
Was the architecture or were the parts of the suggested system described in the study?
Did the study provide a concise summary of its findings?

1
1
1.5
0.5
1.5
0.5
1
1.5
1

6.3.2. Word Cloud and Frequency

Before creating the word cloud, stemming was used to discover the phrases’ com-

mon origin.

To begin the classification process, the tag cloud presentation was utilized to determine
the major keywords. The clouds of the 30 keywords from the abstracts are provided in
Figures 13 and 14, which provide the 1000 important words from the whole texts of the
articles with their relative relevance and prominence.

Keywords were analyzed using Python, NumPy, Pandas, and Matplotlib to produce a

simple frequency analysis and word cloud graph.

Before constructing the graph, all characters in the text were converted to lower-
case. Pre-processing included deleting digits, punctuation, and stop words often found
in English.

Figure 15 represents the frequencies of the first 30 words extracted from the abstracts
of all publications, while Figure 16 presents the frequencies of relevant words constructed
from 1000 words selected from the content of all sections of the paper, omitting references.

---

<!-- PAGE 33 -->

J. Imaging 2025, 11, 12

33 of 66

Figure 13. Top 1000 abstract words.

Figure 14. Top 1000 words in whole papers.

Figure 15. Word frequency in abstracts (top 30).

---

<!-- PAGE 34 -->

J. Imaging 2025, 11, 12

34 of 66

Figure 16. Word frequency: top 1000 words in whole papers.

6.4. Approach to Inclusion and Exclusion Standards

To make sure the studies chosen for analysis were pertinent, we used precise inclusion
and exclusion criteria. We determined significance during the filtering process in the
following ways:

•

•

•

•

Initial Retrieval: After a retrieval process, 5857 preliminary primary studies were
found using five digital libraries’ search engines. Each library utilized various filtering
parameters, which resulted in differing quantities of papers being returned. Each
library utilized various filtering parameters, which resulted in differing quantities of
papers being returned.
Criteria Definition: In order to concentrate on the most pertinent studies, we es-
tablished a set of inclusion/exclusion criteria. Except for gray literature, workshop
presentations, and articles that reported just abstracts or presentation slides, this in-
volved choosing only journals for the Scopus and Springer databases and all categories
for ACM, Google Scholar, and Web of Sciences. The chosen papers were to highlight
current developments in the discipline and be published between 2020 and 2024.
Selection Based on Peer Review: To ensure a degree of quality and credibility in
the chosen studies, we only included articles that were approved for publication
after a peer review procedure. Articles that were not peer-reviewed or did not fit the
designated research focus were disqualified. Additionally, articles that did not include
recommender hybrid techniques in their abstract or title were not included. This was
essential for maintaining attention on the pertinent subject. To ensure linguistic and
understanding consistency, non-English papers were eliminated.
Coarse Selection Phase: We first examined the publishing type, year of publication,
and title as part of our coarse selection phase. We frequently looked at abstracts or
other sections of the publications to determine their applicability.

---

<!-- PAGE 35 -->

J. Imaging 2025, 11, 12

35 of 66

• Hybrid Recommendation Systems: The review excluded papers that had nothing to
do with recommender systems and instead focused on those that presented hybrid
recommender systems.

• Data Entry and Analysis: To enable a methodical review process, the data were input

into an Excel spreadsheet, including keywords and cited information.

• Quality Assurance: To guarantee high-quality results, a systematic review uses a
weighted score system to quantify study quality, accepting only those that meet a
threshold of 0.80.
Final Selection: Fifty-two primary papers that satisfied the predetermined standards
were ultimately chosen, offering a strong basis for the systematic review. By guaran-
teeing that only pertinent and excellent papers were incorporated into the analysis,
this exacting process raises the review’s academic worth and transparency.

•

6.5. Commonly Used Principal Summary Measures

In a systematic study of hybrid recommender systems, performance metrics are often
employed as primary summary measures rather than standard measures such as risk
ratios or odds ratios. In this scenario, summary measures would be used to assess the
success of hybrid recommender systems. Some common performance indicators include
the following:

Precision: The percentage of recommended items that are relevant.
Recall: The percentage of relevant items that are recommended.
F1-Score: The harmonic mean of precision and recall, which achieves a balance

between the two.

These three metrics presume that the provided data are divided into “relevant” and
“irrelevant” categories and may be organized into confusion tables (see Figure 17). The
precision of a system is calculated by dividing the number of genuine positives by the
total number of positive cases predicted by the system. The precision measure can be
defined as the system’s precision in percentage terms using the generic confusion table. The
recall value determines how well the system captures relevant instances and is calculated
using the recall equation. The F1-score assesses the system’s accuracy and is calculated
as the weighted average of the precision and recall scores. The findings for the hybrid
recommender system are as follows:

Precision (0.80) indicates that 80% of the things recommended by the system are

relevant. A precision of 0.80 is high.

Recall (0.92): A recall of 0.92 indicates that the system can retrieve 92% of the relevant
elements, implying that it is quite effective at avoiding forgetting crucial recommendations.
This high recall indicates that the system effectively covers a wide range of relevant articles.
F1-Score (0.86): The F1-score, which measures precision and recall, is 0.86. This
rating shows great overall performance, implying that the system’s recommendations are
generally accurate (high precision) and comprehensive (high recall).

6.6. Challenges and Setbacks (RQ1)

In response to RQ1, this section explains the different obstacles currently in use that

recommendation systems face and offers different answers to these challenges.

6.6.1. Approaches for Addressing the Cold-Start Problem

Cold-start was the most critical issue discovered. It becomes challenging when the
recommender system is unable to draw any inferences from the little available data. Cold-
start is a circumstance in which the system is unable to create effective recommendations
for cold (or new) consumers who have rated no or only a few items. It typically happens
when a new user enters the system or when new items (or products) are added to the

---

<!-- PAGE 36 -->

J. Imaging 2025, 11, 12

36 of 66

database. Approaches to the cold-start problem usually concentrate more on gathering
extra information such as user registration details or item metadata.

Figure 17. Confusion matrix for the articles selected for the study.

For this issue, the CF-based recommendation with an implicit rating was used in
the study in [30]. Because explicit rating information on items was not available for
online shopping malls, this method was used. The researchers extracted implicit rating
information from transaction data, which served as a proxy for explicit rating information.
The authors of [29] created a hybrid recommendation system for personalized course
recommendations in e-learning settings, which addresses cold-start difficulties and insuffi-
cient information.

Modern hybrid systems effectively incorporate several technologies, such as machine
learning and deep learning, to address the user cold-start problem, outperforming previous
systems that often rely on a single strategy. This integration enhances performance by
combining data-driven and method-driven strategies [98].

Meta-Learning: Modern systems use meta-learning to quickly adapt to new users with
less data, but traditional systems struggle to make recommendations without significant
previous knowledge [98].

Deep Learning Capabilities: Hybrid systems commonly use deep learning techniques
to capture complex interactions between people and things, which is a difficult task for
traditional systems. This enables more tailored recommendations, even when less user
data are available [98].

Multiple-Feature Fusion: Modern systems can combine a variety of features and data
sources, enhancing their recommendation capabilities for new users. Traditional systems
lack this adaptability and rely on simpler models that may not accurately reflect various
user preferences [98].

To solve the cold-start problem in content-based recommender systems, effective user
profiling is required. This can be accomplished by leveraging demographic variables such as
geographic location, age, gender, occupation, and education [7]. One effective technique is
to utilize onboarding questionnaires to collect user preferences at the beginning of program
use [99]. This procedure entails connecting the initial data acquired to subsequent recom-
mendations, thereby incorporating user preferences into the recommendation architecture.

---

<!-- PAGE 37 -->

J. Imaging 2025, 11, 12

37 of 66

Businesses that aggressively seek explicit feedback from new users via onboarding
questionnaires, surveys, or interactive chatbots can acquire significant insights into client
tastes and preferences from the start.

This direct approach not only improves the relevancy of recommendations but also
contributes to the establishment of a personalized experience, thereby alleviating the issues
connected with the cold-start issue [99].

6.6.2. Sparsity

Approaches to the data sparsity problem concentrate more on using existing data to
fill in the gaps. To make accurate recommendations, collaborative filtering (CF) requires
many users who have rated many items. However, this is not always the case, resulting
in sparsity issues. To address this issue, the paper [30] suggests a hybrid approach that
combines CF with sequential pattern analysis (SPA). The limitations of CF in reflecting
changes in user preferences over time can be reduced by integrating SPA, which considers
item associations, with CF, which uses rating information. By providing recommendations
based on both rating information and sequential patterns, this hybrid approach helps to
mitigate the sparsity problem.

The combination of sequential pattern analysis (SPA) and collaborative filtering
(CF) was used in [30] to address the sparsity problem. The study aimed to mitigate the
higher probability of inaccurate and biased recommendations for items that arise from
considering only purchasing information rather than rating information by integrating
CF, which uses evaluating information, with SPA, which returns adjustments to user
choices over time in a sequence of sequential patterns. The techniques of modern
hybrid recommender systems and conventional systems are compiled based on the
general recommendation framework. Reducing the dimensionality of complicated rating
matrices to approximate ones is one useful strategy to mitigate the adverse impact
of data sparsity [7,44,80]. For example, a latent factor model, matrix factorization, or
singular value decomposition can accomplish this. We show that even a basic hybrid
recommender system that simply combines user and item data can produce a better
prediction than conventional systems.

Contrastive learning [100] can assist in addressing the problem of sparsity in recom-
mendation systems. Sparsity is a situation in which there is insufficient user–item inter-
action data, making it difficult for standard models to anticipate accurately. Contrastive
learning is a self-supervised learning method that seeks to acquire usable representations by
differentiating between similar and dissimilar data points. In the context of recommenda-
tion systems, contrastive learning can be used to increase the model’s capacity to generalize
and produce better suggestions by learning robust user and object representations, even
when interaction data are limited.

According to the study in [100], contrastive learning outperforms conventional models
in classification and exhibit enhanced accuracy through hyperparameter optimization
and fine-tuning. The accuracy of a semi-supervised model with only 5% labeled data is
57.72% according to the results, whereas careful tuning in a supervised setting increases
the accuracy to 88.70% [100].

6.6.3. Alluvial Diagram

RAWGraphs is a high-quality open-source platform for developing unique data visu-
alizations [101]. Figure 18 shows a graph generated with this tool to better comprehend
data flow. This graph includes factors like document type, journal, and date of publication.

---

<!-- PAGE 38 -->

J. Imaging 2025, 11, 12

38 of 66

Legend:

Blue: Books

•
• Orange: Journal Articles
• Green: Published in 2020
Purple: Published in 2019
•
Red: Published in 2018
•
Yellow: Published in 2021
•
• Gray: Other years
•

Flow Width: Represents the number of items

Figure 18. Multicategorical article analysis with a complete color-coded legend.

6.6.4. Limitations and Biases

The deployment of hybrid recommender systems at scale confronts constraints such
as high processing needs and latency concerns caused by complicated models. Additional
issues include integrating varied data sources, retraining on a regular basis, and assuring
interpretability. Cold-start issues, data scarcity, and algorithm scalability are all factors that
influence performance. Balancing real-time customization with system response time and
costs remains a challenge.

The biases we confront when reviewing abstracts and titles may impact our perception
of relevance. Subconsciously, factors such as the authors’ reputation, the prestige of the
journal, or even the authors’ names can influence our evaluation despite the precautions
taken to prevent this from happening. However, it is critical to recognize that the topic of
the abstract should not be the only factor influencing how we make choices.

We acknowledge that we were susceptible to biases during the manual screening
process prior to using ASReview. One type of bias that impacts research papers is pub-
lication bias. Top-tier publications in almost all disciplines tend to publish papers with
substantial findings, frequently accompanied by significant effect sizes. Using only the
most prestigious publications may result in an overestimation of the effects in the field
of interest. Lower-tier journals typically report smaller effect sizes in their publications.
This search’s limitations include the authors’ exclusive use of academic databases for this

---

<!-- PAGE 39 -->

J. Imaging 2025, 11, 12

39 of 66

investigation; therefore, they cannot ensure that all the relevant papers were located. A
second method using artificial intelligence algorithms (ASReview) recommended the top
articles based on relevancy to eliminate bias or misclassification. Finally, relevant items may
have been excluded due to a lack of precision in the omission context of certain knowledge
bases. While some articles clearly stated the context in which they were applied, many
others did not. As a result, this study may not have considered other methodologies that
are applicable to hybrid recommender systems.

The other biases can be summarized as follows:
Hybrid recommender systems, which combine two or more recommender techniques
in order to improve the quality and effectiveness of tailored recommendations and applied
methodology, may provide bias-related hazards and difficulties.

-

-

-

-

-

-

-

Data Bias: Hybrid recommenders use data from several sources, each with inherent
biases. For example, collaborative filtering algorithms rely on user–item interaction
data, which can be skewed by popularity or suffer from the cold-start problem. Con-
versely, content-based approaches rely on item qualities, which may be prejudiced
if the item descriptions are inadequate or skewed. Combining various data sources
without considering their respective biases can result in biased suggestions.
Algorithm Selection Bias: In a hybrid system, various algorithms are used to handle
different circumstances or specific jobs. The decision of which algorithm to apply
for a specific user or environment may result in selection bias. If the system prefers
one algorithm over another based on biased criteria, it may result in unfair or erro-
neous suggestions. For example, applying a specific algorithm just to certain user
demographics may result in biased results.
Combination Bias: Hybrid systems usually integrate the outputs of several algorithms,
which might result in bias. Different algorithms may have different biases, and, if the
merging process is not carefully managed, it may exacerbate existing biases or create
new ones.
Feedback Loop Bias: Hybrid recommenders, like other recommendation systems,
are susceptible to feedback loop bias. A self-reinforcing loop can occur when the
system’s recommendations influence user behavior, which is subsequently utilized to
train the system. This bias can grow with time, particularly in hybrid systems with
numerous algorithms contributing to the feedback loop. If the system fails to account
for this prejudice, it may limit the diversity of the recommendations while reinforcing
existing biases.
Over-Specialization Bias: Hybrid systems seek to increase performance by integrating
methodologies; however, this can occasionally result in over-specialization. If the
system is overly reliant on a single algorithm or data source, it may excel in some
cases but underperform in others, resulting in biased suggestions. Balancing the
contributions of various components in a hybrid system is critical for preventing this
type of bias.
Contextual Bias: Hybrid recommenders frequently use contextual characteristics to
generate individualized recommendations. However, biased or inadequate contex-
tual information can result in biased outcomes. For example, using demographic
data without addressing potential biases may result in suggestions that reinforce
preconceptions.
Evaluation Bias: Evaluating the performance of hybrid recommenders can be difficult,
and the selection of evaluation measures and test datasets may create bias. If the
evaluation process favors some parts of the system’s performance, it may overlook or
underestimate biases in other areas.

---

<!-- PAGE 40 -->

J. Imaging 2025, 11, 12

40 of 66

To reduce these dangers, researchers and developers should carefully design and assess
hybrid recommender systems, taking into account fairness, diversity, and the potential
biases of individual components and combinations. Implementing algorithms with fairness
restrictions can help to balance recommendations across different user groups. Regular
monitoring and user feedback can also assist in uncovering and correcting biases in real-
world installations.

6.6.5. Overfitting

The integration of some features in a recommendation system model can cause overfit-
ting due to the absence of valuable and consistent information regarding the nature of the
digital platforms under consideration [19]. Some additional contexts may not improve or
perhaps have a negative impact on the model’s accuracy. However, this type of knowledge
can be generalized and classified into more broad and intelligible categories.

6.7. Hybridization Stratégies (RQ2)

Several hybridization tactics have been investigated by researchers to improve the
quality recommender system performance in the big data setting, where enormous volumes
of user and item information are available. A few of the most important hybridization
techniques used are as follows:

Content–Collaborative Hybridization: Combining collaborative filtering, which
makes use of past preferences and user–item interactions, with content-based filtering,
which makes use of item attributes and user profiles, is known as content–collaborative
hybridization. Combining collaborative- and content-based signals enables this hybrid
technique to deliver suggestions that are more thorough and precise. The research in [71]
offers an ontology-based model that combines multi-level k-means, rough set, and Bayesian
network to beat SVM, DT, and RF with the lowest log error loss and 98% accuracy.

Deep-Learning-Based Hybrid Recommenders: New developments in deep learning
methods, like neural networks and embeddings, have made it possible to create hybrid
recommender systems that efficiently manage complicated large-scale data. Recommen-
dations from deep-learning-based models are more precise and tailored because they are
able to identify complex patterns and linkages in user–item interactions. The study in [70]
solves various research challenges by creating a CNN-based no-reference video quality
assessment for gaming footage that is impacted by compression artifacts.

Hybrid Matrix Factorization: By adding more data, hybrid matrix factorization
approaches build upon the foundation of standard matrix factorization techniques. This
can involve adding hybrid regularization words, user or item traits, or side information.
The method is able to capture more intricate associations and enhance the quality of
recommendations by including hybridization in the factorization process. The study in [31]
introduces a hybrid content-based and neighborhood-based recommender model that uses
a new similarity measure. It achieves accuracy similar to innovative item-oriented and
matrix factorization models while running at least twice as fast.

Demographic–Collaborative Hybridization: Combining collaborative filtering algo-
rithms with user demographic data, such as age, gender, location, or socioeconomic status,
this hybrid paradigm, which combines collaborative patterns with user-specific features,
can improve personalization and tackle the cold-start issue.

The paper [33] presents a hybrid strategy that combines collaborative filtering and
demographic recommendation systems, utilizing data mining, artificial neural networks,
and fuzzy techniques.

---

<!-- PAGE 41 -->

J. Imaging 2025, 11, 12

41 of 66

Knowledge-Based Hybridization: It enhances the recommender system’s comprehen-
sion of user preferences and item linkages by integrating domain-specific knowledge, rules,
or ontologies. With this hybrid method, more context and explanation may be provided.
In the article [19], the author created a Music Information Knowledge Graph (MKG) that
contains user-track interaction pairs, track content attributes, and artist context elements.

6.8. Datasets (RQ3)

In response to RQ3, we followed the available datasets that the writers used to eval-
uate their hybrid recommendation systems (HRSs). These databases enable the scientific
community to reproduce studies and validate or enhance their procedures. Out of the
fifty-two studies, forty-eight used at least one dataset, whereas three did not. Figure 19
depicts the datasets used and their frequencies among the studies.

The findings show a heterogeneous sector of dataset utilization, with a few web and
survey datasets dominating the research landscape while also including less prevalent
datasets. This distribution might provide information pertaining to the research trends and
preferences regarding the topic.

Dataset Distribution: The table depicts the distribution of studies among different
datasets used for evaluation. The most common datasets are “web dataset” and “survey
data”, accounting for 26% of all the research.

Concentration of Studies: The results show that the studies are concentrated on
specific datasets. The top three datasets (“web dataset”, “survey data”, and “social media
data”) account for more than half of all the studies, indicating that the research community
prioritizes these types of datasets.

Diversity of Datasets: While the most prevalent datasets dominate the distribution,
the table also includes less common datasets, such as “Instructional materials”, “Qualitative
Data”, “Synthetic dataset”, and “Clinical Data”, which account for 2–4% of all the studies.
This indicates a degree of diversity in the datasets utilized for study.

Balanced Representation: The distribution appears to be somewhat balanced, with
no single dataset accounting for an overwhelming majority (the largest percentage is 26%
for both “web dataset” and “Survey data”). This shows a healthy diversity of datasets used
in the investigations.

Missing or Unspecified Data: The 6% of research labeled as “NA” (not available)
indicates that a minor amount of data may be missing or undefined in the source material.

6.9. Experimental Outcomes (RQ4)

Hybrid recommender systems frequently seek to use the capabilities of various recom-
mendation methodologies (e.g., content-based, collaborative filtering, and demographic-
based) in order to provide more accurate and personalized recommendations to users.
Combining various algorithms can improve recommendation performance, as assessed by
measures such as precision, recall, F1-score, or normalized discounted cumulative gain.
The study in [31] provides a hybrid recommendation system that blends content-based
and neighborhood-based algorithms to increase accuracy and speed. It employs novel ap-
proaches to improving item-level similarity measures in collaborative filtering algorithms
(see Table A1). The work employs genomic tags and aims to outperform the traditional
collaborative filtering methods in terms of accuracy and speed. The experiment results
indicate that it is more precise and faster than ‘pure’ collaborative filtering techniques.

The study in [61] incorporates both conventional and additional aspects pertaining to
pandemic, environment, digital technology, and information systems; the study offers a
thorough methodology for assessing airline service quality.

---

<!-- PAGE 42 -->

J. Imaging 2025, 11, 12

42 of 66

Ref. [71] utilized an ensemble approach consisting of three techniques: clustering,
rough set, and Bayesian network. The strategy was divided into four phases: clustering,
knowledge discovery, probabilistic network design, and model evaluation. Based on
experimental data, this model outperformed other models like DT, RF, and SVM, with an
accuracy of 98.36% (several further results are included in Table A1 in Appendix A.

Figure 19. Trends in using assessment datasets for recommender system research.

6.10. Methodologies and Recommended Techniques (RQ5)

According to Table A1, Column 2 in Appendix A, the proposed technique for hybrid

recommendation systems typically includes the following important steps:

-

-

Data Collection: Gather data from various sources, including user behavior logs,
questionnaires, interviews, item metadata, and user profiles.
Feature Engineering: Relevant qualities that influenced proposals were identified
and selected. To increase model performance, more features were developed using
existing data. Categorical variables were encoded utilizing techniques like one-hot
encoding and embedding [60,94].

---

<!-- PAGE 43 -->

J. Imaging 2025, 11, 12

43 of 66

-

-

-

-

-

-

-

Employ the Strengths of Different Methods: Hybrid systems combine the benefits of
several recommendation techniques, such as those based on content, collaborative fil-
tering, and demographic information, to take advantage of their respective capabilities
and provide more precise and personalized recommendations.
Experiment and Evaluate Performance: Experiments are carried out to evaluate the
performance of hybrid systems regarding individual recommendation strategies. The
increases in recommendation accuracy are evaluated using metrics like as precision,
recall, F1-score, and normalized discounted cumulative gain.
Address Individual Technique Limits: Hybrid systems are intended to overcome the
limits of individual recommendation approaches, such as the cold-start problem or
the inclination to propose primarily popular goods. The experiments show increased
coverage of long-tail items and more diverse recommendations according to users’
unique interests.
Analyze Efficiency and Scalability: The study compares the computational efficiency,
memory utilization, and scalability of hybrid strategies to individual recommendation
approaches. The experiments evaluate hybrid systems’ processing times, memory
footprints, and applicability for real-world big data applications.
Assess Customer Experience and Satisfaction: Experiments are carried out to assess
the influence of hybrid systems on user experience, engagement, loyalty, and overall
satisfaction. The efficacy of the hybrid techniques is measured by analyzing user input,
engagement metrics, and satisfaction levels.
Appreciate Hybridization: Experiments are intended to highlight any trade-offs con-
nected with hybridization, such as the effect on model transparency, interpretability,
or the complexity of the recommendation process. These findings can help to inform
future system design decisions and the selection of appropriate hybridization strategies.
Identify Optimal hybridized Strategies: Experiments are performed to determine the
best ways to combine several recommendation approaches, such as weighted hybrid,
switching hybrid, feature augmentation, and meta-level hybrid. The study provides
practitioners with guidance for selecting and implementing hybrid approaches de-
pending on the data characteristics and intended recommendation performance.

6.11. Potential Future Research Directions (RQ6)

The last study question concerns the future job prospects and directions. Our results

are reported in Table 11 and briefly discussed below:

For the study in [31], employing a recommendation system as an integrated Movie
Sales Recommendation Engine, future work will focus on enhancing movie representations
and integrating matrix factorization techniques for increased accuracy.

The authors of the study in [33] on a hybrid model in social networks recommendation
system architecture development will evaluate their techniques on more social networks and
investigate the possibility of combining them with genetic algorithms for better outcomes.
The authors of the study in [36] examined courseware and open educational resources
with an emphasis on quality. One of their future objectives is to automate processes
related to the creation of an effective and personalized adaptive recommendation system.
Future plans call for automating several framework operations to enhance flexibility and
recommendations. Developing an excellent adaptive recommender system that is tailored
to users’ learning needs is the ultimate objective.

One of the goals for the future is task automation for the development of a per-
sonalized and effective adaptive recommender system. The plans for the future include
automating some framework activities to enhance recommendations and flexibility. Creat-

---

<!-- PAGE 44 -->

J. Imaging 2025, 11, 12

44 of 66

ing a superior, personalized adaptive recommender system for users’ learning needs is the
ultimate objective.

One of the primary goals of the project management system study [75] is to raise
the general standard of Jakarta’s municipal parks; subsequent studies could concentrate
on raising the administration and management of Jakarta’s parks, as well as raising the
administration of construction projects, especially in the pre-construction stage.

The authors of [81] underline the importance of assessing and monitoring societal
perceptions of enhanced individuals. They contend that understanding these perspectives
is critical for guiding the development and use of future augmentation technologies.

According to the article [78] on financial modeling techniques, future gains can be

achieved by adjusting reimbursement structures and implementing quality-based incentives.

Table 11. Future study proposals.

Potential Future Work

Enhance the offered solution.
Conduct more detailed reviews.
Include contextual information in recommendations.
Investigate applications in various fields.
Use more data or item features.
Test a variety of algorithms.
Experimentation with various hybrid recommendation models.
Other.

Studies

7
6
7
5
5
8
6
8

Building on our previous responses, we conducted in-depth evaluations of each indi-
vidual study to correctly address research questions RQ2 to RQ6. The goal was to document
the technical methods, algorithms, approaches, and findings utilized in developing hy-
brid recommender systems as described in the literature. Table A1 in Appendix A shows
a summary of the employed strategy, the dataset used, the objectives, and the results.
As presented in Appendix A, the hybrid recommendation systems used a variety of ap-
proaches to improve accuracy, coverage, and user experience. The experiments found
that hybrid systems outperformed individual techniques in terms of precision, recall, and
diversity. The hybrid techniques also demonstrated higher efficiency and scalability in
large-scale applications. The evaluations of user feedback and interaction revealed that
personalized, relevant recommendations increased satisfaction. The experiments revealed
trade-offs in hybridization strategies and helped to identify the optimal procedures for
specific applications.

Future Research

Given the findings of this study, we see potential for further research in context-
sensitive systems and hybridization techniques. To efficiently design CARS, the following
tools and approaches could be used:

•

Context-Aware Recommendation Systems (CARSs) enhance traditional recommenda-
tion models by integrating contextual factors, such as location, time, or environmental
conditions, into the recommendation process, developing techniques for gathering
contextual data, such as user behavior analytics or environmental sensors, and design-
ing algorithms that include contextual information in the recommendation process.
Unlike conventional systems that predict ratings based only on user–item interactions
(F : User × Item → Rating), CARSs expand the prediction function to include context
(F : User × Item× Context → Rating), adding a third dimension. This added com-
plexity makes the recommendations more relevant by aligning them with situational

---

<!-- PAGE 45 -->

J. Imaging 2025, 11, 12

45 of 66

user needs, although it also increases the computational demands. A clear under-
standing of “context”, defined as any information shaping the user interactions with
the system, is essential for effectively designing these systems. To efficiently design a
CARS, the following tools and approaches could be used:

1. Machine Learning Frameworks: Use machine learning frameworks such as
TensorFlow or PyTorch to create prediction models based on contextual infor-
mation. These frameworks provide strong libraries for developing and training
machine learning models, enabling the integration of complicated characteristics
such as context in addition to user and object data.

3.

2. Dataset, Model, and Evaluation: Creating a contextual dataset, creating a rein-
forcement learning model, and using performance measures to evaluate adaptation.
Contextual Bandits: Use contextual bandit algorithms to dynamically adjust
recommendations based on real-time circumstances. These algorithms strike
a balance between exploration and exploitation by determining which recom-
mendations function best in various contextual settings, allowing the system to
deliver tailored ideas that adapt as user behaviors and contexts change.

4. User Studies: Conduct user research to determine the effectiveness of context-
aware recommendations. Gathering qualitative input from consumers allows us
to measure how effectively the recommendations suit their needs and preferences
in various scenarios. This approach may include surveys, interviews, or A/B
testing to measure user happiness and engagement with contextual features.

• Hybridization: In machine learning, hybridization is the process of merging multiple
algorithms or models to improve predicted accuracy, resilience, and flexibility by
utilizing their strengths while mitigating individual limitations. Hybridization in
recommendation systems frequently employs ensemble learning techniques such
as stacking and meta-learning to combine collaborative- and content-based filtering
methods. This method enhances recommendation accuracy by modifying model
weights in response to user interactions. Scikit-learn and PyTorch are tools that
help to apply these concepts, making it easier to experiment and enhance hybrid
systems across a wide range of applications, including recommendation engines,
identifying fraud, and natural language processing. To supplement the conversation,
we will provide a more detailed examination regarding how these concerns could
be investigated:

1.

Frameworks for Hybrid Systems: Use libraries that support hybrid recommen-
dation algorithms, such as Surprise or Apache Mahout.

2. A/B Testing: Use A/B testing techniques to compare the performance of hybrid

models to standard approaches.

3. Data Fusion Techniques: Explore data fusion approaches to successfully merge
multiple sources of data, hence improving the quality of recommendations.

The gaps in the literature require more exploration. Addressing these deficiencies is
critical to improving the scalability, accuracy, and ethical issues of hybrid recommender
systems:

Scalability Challenges: To manage enormous datasets efficiently, scalable techniques

are required.

Integration of Advanced AI techniques: Investigating how deep reinforcement learn-

ing and generative models might improve recommendation accuracy.

Data Privacy and Ethical Considerations: Creating techniques for implementing

privacy-preserving procedures while maintaining the quality of suggestions.

---

<!-- PAGE 46 -->

J. Imaging 2025, 11, 12

46 of 66

Experience and Engagement Metrics: Focusing on the importance of increasing user

happiness and trust in the advice provided.

7. Conclusions

This article provided a comprehensive survey and assessment, as well as an extended
organized taxonomy, for the most recent, ever-increasingly efficient hybrid recommenda-
tion system models used in both academia and industry, with successful applications in
fields such as e-commerce, music, and geographic location services. In this work, we em-
ployed an open-source system that uses machine learning to efficiently filter and categorize
large amounts of textual data, which sped up the document selection process. Using this
approach in conjunction with the traditional methods, we discovered 52 key publications
from conference proceedings and journals on hybrid recommender systems. Our goal was
to highlight the most relevant concerns addressed by these studies in order to make more
informed suggestions. We also studied the machine learning and data mining approaches
they employ, the recommendation strategies they merge, the hybridization classes they
adhere to, the application domains and datasets, the evaluation procedure, and potential
future work paths. A significant portion of the research we examined (more than 75%) was
published during the last three years, demonstrating a noticeable and growing interest in
hybrid recommender systems (HRSs). This work emphasizes the need for further research
into context-sensitive systems and hybridization tactics in context-aware recommendation
systems (CARSs). By incorporating contextual aspects, a CARS improves the traditional
models, improving their relevance while increasing the processing demands. Machine
learning frameworks, contextual bandits, and user studies are key tools for assessing effec-
tiveness. Furthermore, hybridization combines algorithms to improve accuracy, with an
emphasis on using frameworks such as Apache Mahout, while also addressing scalability,
ethical concerns, and user engagement metrics in future studies. Furthermore, our out-
comes indicate that using larger datasets and hybrid parallel algorithms may be a viable
way to handle scalability issues and improve recommendation quality in the age of big
data. Another intriguing area for future research is the use of hybrid recommendation
systems to create cross-domain recommenders or lower the computational complexity of
the existing approaches.

Author Contributions: B.S. created the concept and composed the manuscript. A.K. and B.E.A.
monitored and assisted B.S. in developing and structuring the manuscript. M.R. read and commented
on the most recent version. All authors discussed the analyses, interpreted the methodology, and
provided feedback on the text. All authors have read and agreed to the published version of
the manuscript.

Funding: This research received no external funding.

Institutional Review Board Statement: Not applicable.

Informed Consent Statement: Not applicable.

Acknowledgments: This project is supported in part by TekCircle and CNRST. Our experiments were
performed in the CNRST environment with GPU cluster obtained during their valuable collaboration.

Conflicts of Interest: The authors declare no conflicts of interest.

---

<!-- PAGE 47 -->

J. Imaging 2025, 11, 12

47 of 66

Appendix A. Recapitulative Table A1 of the Selected Articles

Table A1. A comprehensive review-based overview of recommender techniques.

Study Issue

Employed Strategy

Dataset

Objectives/Results

[14] A hybrid rec-
ommender system
for patron-driven
library acquisition
and weeding.

A Novel
[31]
Recom-
Hybrid
Sys-
mendation
tem Integrating
Content-Based and
Rating Information

The study uses a hy-
brid recommender sys-
tem that combines col-
laborative filtering and
content-based filtering
to help library admin-
istrators make acquisi-
tion and weeding de-
cisions based on user
feelings.

tag

The work presents
a mixture of recom-
mendations that uses
infor-
genome
mation to
increase
accuracy of prediction
in collaborative filter-
ing. It provides a novel
similarity measure that
includes content-based
information into ex-
isting formulas, with
the goal of improving
the accuracy of item-
oriented collaborative
filtering algorithms.

of

Amzon
dataset:
This dataset con-
sists
278,858
users who pro-
vided
1,149,780
ratings for 271,379
Library
books.
Library
Catalog:
provides
dataset
information
and
statistics for com-
book
paring
availability.

benchmark
The
dataset
is Movie-
Lens 20Min, which
retains just users
and movies with
20 or more ratings.
just movies having
tag genome infor-
mation are kept.
As a result, 10,239
movies
received
19,799,049 ratings
from 138,493 users.

CF, CB, Hybrid

213 courses

[29] A course hy-
brid recommender
system for limited
user
information
scenarios

Objectives:
The study’s goal is to create a hybrid recom-
mender system that helps library administrators
to make educated decisions about acquisitions
and weeding by incorporating user comments
and preferences.
Results:
The hybrid recommender system was success-
fully implemented in a national library, deliv-
ering acquisition and weeding advice based
on user feedback and machine learning ap-
proaches.

Objectives:
The paper presents a hybrid recommenda-
tion system that combines content-based infor-
mation with neighborhood-based algorithms
to improve accuracy and speed. It employs
unique ways to improve item-level similarity
measurements in item-oriented collaborative
filtering algorithms. The study uses genome
tags and seeks to outperform standard collabo-
rative filtering approaches regarding accuracy
and speed.
Results:
The suggested hybrid recommendation sys-
tem, which combines content-based and
neighborhood-based information, provides
comparable accuracy to leading models while
being at least twice as fast. Experiment find-
ings suggest that it is more accurate and faster
than ‘pure’ collaborative filtering methods. Fu-
ture work will include improving movie repre-
sentations and merging the model with matrix
factorization techniques to increase accuracy
even further.

Objectives:
This work addresses the cold-start issue and lim-
ited information circumstances by creating a hy-
brid recommendation system for personalized
course recommendations in e-learning environ-
ments.
Results:
Estimation, validate hypotheses for better rec-
ommendation system performance, investi-
gate application to various recommendation
scenarios, and investigate contextual embed-
dings for multiple languages.
LSA model Precision = 0.17
LDA model Precision = 0.16
Hybrid best result α = 0.9

---

<!-- PAGE 48 -->

J. Imaging 2025, 11, 12

48 of 66

Table A1. Cont.

Study Issue

Employed Strategy

Dataset

Objectives/Results

Neural
interaction
layer, NCTR model
tochastic
Gradient
Descent algorithm

MovieLens
Amazon

and

CF, Sequential Pattern
Analysis (SPA)

and
E-commerce
transaction
data:
Dataset of 16,486
transactions of 247
users on 1911 items

[15] A hybrid
neural network ap-
proach to combine
textual information
and rating infor-
item
mation for
recommendation

[30] A hybrid
online-product
recommendation
system: Combining
rating-
implicit
based collaborative
filtering and se-
quential
pattern
analysis.

[60] A parametric
analysis of AVA to
optimize Netflix
performance Inter-
national Journal of
Information Tech-
nology (Singapore)

[13] A Propound
Hybrid Approach
Personalized
for
Online
Product
Recommendations

CF, CB, Quality Con-
trol

307 Delhi respon-
dents. Netflix dom-
inates, aesthetic an-
notations (63.8%).

Random Forest (RF)
Pearson Correlation
(PC)
Gradient Boosting(GB)

300 visitors and 100
products.

Objectives:
The study aims to overcome limitations of exist-
ing recommendation algorithms by proposing a
hybrid neural network model, novel hybrid neu-
ral network to combine textual information and
rating (NCTR), which incorporates textual infor-
mation and rating data to enhance recommen-
dation accuracy, particularly for sparse data.
Results:
Enhancing techniques for capturing the non-
linearity of feature interactions and enhancing
strategies for feature extraction from textual
data

Objectives:
The study’s goal is to generate implicit ratings
and combine CF with sequential pattern analy-
sis to improve online recommendations.
Results:
In collaborative filtering (CF), implicit ratings
effectively replace explicit ratings for digital
transaction data. A CF-SPA hybrid approach
improves recommendation quality. Four experi-
ments were carried out to compare the proposed
approach to others. Data from a large Korean
online mall, focusing on users who made more
than 30 purchases. In terms of precision, recall,
and F1, the suggested hybrid system exceeded
CF and SPA-based methods. In the hybrid sys-
tem, the value of weight for CF-based recom-
mendation is set to 0.1. The study recognized
that a small dataset size was a limitation.

Objectives:
The study examines the impact of aesthetic vi-
sual analysis (AVA) on Netflix’s thumbnail se-
lection process.
Results:
Among OTT platforms, Netflix was chosen by
63.8% of respondents as their preferred choice.

Objectives:
A hybrid technique for tailored online sug-
gestion of products in e-commerce websites.
The goal is to increase the accuracy of sugges-
tions by utilizing collaborative filtering, im-
plicit data and sequential patterns.
Results:
Integration of CF and PSP approaches outper-
forms individual methods.
No scalability of the proposed approach

---

<!-- PAGE 49 -->

J. Imaging 2025, 11, 12

49 of 66

Table A1. Cont.

Study Issue

Employed Strategy

Dataset

Objectives/Results

[61] A three-level
framework to eval-
uate airline service
quality based on in-
terval valued neu-
trosophic AHP con-
sidering the new di-
mensions.

SERVQUAL
The
ex-
methodology is
panded to evaluate
airline
in
terms of pandemic,
information systems.,
digital technology and
environment.

service

For criteria weight
estimation, the Best
approach
Worst
(BWM)
and the
Modified Delphi
were
approach
used.

[32] An analysis
and
comparison
of keyword rec-
ommendation
methods for scien-
tific data

The study compares
keyword suggestion
approaches for scien-
tific data by combining
analysis, metrics pro-
posals, and tests.

Latent Dirichlet Al-
location (LDA with
300 topics and 1000
iterations)
Stanford
Topic
Modeling Toolbox.

[62] An extended
model for assessing
Ira-
E-Services of
nian Universities
Websites
Using
Mixed
MCDM
method.

Analytical Hierarchy
Process (AHP)
Promethee (Preference
Ranking Organization
Method for Enrich-
ment Evaluations).

21 top-leading Ira-
nian universities.

This study investigates
fuzzy neural networks,
GST, AHP, DBT-SVM,
and DM methods.

Students’
Aca-
demic Performance
(xAPI-
Dataset
(100
Edu-Data)
students).

[63] Artificial intel-
ligence and edge
computing
for
quality
teaching
evaluation based
on
5G-enabled
wireless communi-
cation technology.

Objectives:
The goal of this research is to provide a three-
level framework for evaluating airline service
quality based on the SERVQUAL model while
taking into account new aspects such as pan-
demic, environment, digital technology, and in-
formation systems.
Results:
The study presents a comprehensive method-
ology for evaluating airline service quality by
using the extended SERVQUAL model, which
includes traditional and extra factors related to
pandemic, environment, digital technology, and
information systems.

Objectives:
The purpose of this research is to investigate and
compare keyword recommendation strategies
for scientific data, specifically the indirect and
direct approaches, as well as to assess metadata
quality and propose assessment criteria for con-
trolled vocabularies.
Results:
This publication would most likely give a more
complete evaluation of the study’s limitations,
study’s particular findings are not provided, po-
tential areas for improvement, and ideas for fu-
ture research initiatives.

Objectives:
This study aims to provide a more comprehen-
sive model for evaluating university websites’
e-services’ preparedness. The model seeks to
pinpoint these websites’ advantages and disad-
vantages while offering suggestions for raising
their standard of design.
Results:
The study evaluated the readiness of 21 top
Iranian university websites for providing e-
services, but specific values and rankings were
not provided.

Objectives:
Provide an environment in the classroom with
edge computing that is structured to enhance
social-emotional learning and academic learn-
ing. boost the effectiveness of the teaching-
learning process.
Results:
Possible implications include the usefulness
of the recommended optimization strategy for
teaching college English, the advantages of in-
corporating edge computing and 5G in medical
education, and the general advantages of using
cutting-edge technologies in instruction across
the board for educational purposes.

---

<!-- PAGE 50 -->

J. Imaging 2025, 11, 12

50 of 66

Table A1. Cont.

Study Issue

Employed Strategy

Dataset

Objectives/Results

qualitative data analy-
sis techniques such as
thematic analysis.

17 interviews were
conducted with 3
administrators,
2
staff members, 2
parents 5 teachers.

[64] Beyond Bricks
and Mortar: The
of
efficacy
on-
learning
line
and
community-
building at College
Park Academy dur-
ing the COVID-19
pandemic.

[86] Business pro-
cess modeling lan-
guage selection for
research modelers.

expert interviews, doc-
ument analysis, snow-
balling literature re-
view.

97 criteria, 23 BPM
languages, 25 qual-
ity attributes, and
72 BPM features.

CAQoE:
[92]
A
No-
Novel
Reference Context-
aware
Speech
Quality Prediction
Metric.

CAQoE metric, evalu-
ating its performance
using objective and
subjective
quality
scores.

PTB
ECG
148 subjects,
patients.

diagnostic
database
52

Basic similarity metrics
Algo-
Prefetching
rithms
simulation model.

32 people watch-
ing 360° videos
head
including
movements
from
439 unique view-
ings, totaling 21 h
and 40 mn.

DAC-HPP algorithm.

datasets: LFR-EA-
1000, WEBKB.

Cross-User
[95]
in
Similarities
Viewing Behavior
for 360° Video and
Caching
Implica-
tions.

DAC-HPP:
[91]
attributed
deep
clustering
with
high-order proxim-
ity preserve.

[87] DataPilot: Uti-
lizing Quality and
Usage Information
for Subset Selection
during Visual Data
Preparation.

Semi-structured inter-
views, brainstorming
sessions, and feedback
sessions

1000 records from
open-source
an
digital marketing
dataset with 42
properties.

Objectives:
This study investigates College Park Academy’s
transition to virtual learning during COVID-19,
analyzing its structure, effects on stakeholders,
and making recommendations for technology-
enhanced teaching.
Results:
Transition had readiness challenges: academic
rigor and social-emotional well-being issues.

Objectives:
The goal of this research is to provide a reliable
decision model for the problem of business pro-
cedure modeling language selection in research
projects.
Results:
A selection model for choosing business process
modeling languages (BPMN) with 97 criteria, 23
alternatives, and 25 quality features was devel-
oped.

Objectives:
The research presents context-aware Quality of
Experience (CAQoE), a measure for real-time
voice quality in VoIP applications that incorpo-
rates a context-classifier, Voice Activity Detector
(VAD), and validation with subjective evalua-
tions.
Results:
XGBoost presents the best F-score (0.95%)

Objectives:
investigate the effects of stacking and quality-
adaptive anticipating strategies for 360° video
on content cache performance.
Results:
Perspectives on the circumstances in which over-
lap might be significant and caching useful for
360° video

Objectives:
Suggest a method for deep attributed graph clus-
tering called Deep Attributed Clustering with
High-order Proximity Preserve) (DAC-HPP).
Results:
Constructing a consensus matrix, Compared
to seven cutting-edge methods, DAC-HPP per-
forms superior.

Objectives:
Tackling the problem of identifying meaningful
data subsets from big, unusual datasets while
visual data processing.
Results:
Several hypotheses that were tested during the
user study.

---

<!-- PAGE 51 -->

J. Imaging 2025, 11, 12

51 of 66

Table A1. Cont.

Study Issue

Employed Strategy

Dataset

Objectives/Results

[88] Development
of a Quality-Based
Model for Software
Architecture Opti-
mization: A Case
Study of Monolith
and Microservice
Architectures.

[89] DHR: Dis-
tributed Hybrid
Rendering
for
Metaverse Experi-
ences.

Create a quality-based
mathematical model
for optimizing soft-
ware architecture.

N/A.

Distributed Hybrid
Rendering
(DHR)
approach

N/A.

[74] Empirical anal-
ysis of the tool sup-
port
for software
product lines.

Researchers used sam-
pling and snowballing
to select representative
case studies.

case

20
studies
from 6 different
domains.

Framework with a col-
lection of explanation
techniques.

task notes
46

6800
spread over
days.

CF, CB,
Quality-based recom-
mendation,
Hybrid Approoach.

53 participants
400 Open Educa-
tional Resources.

[94] Evaluating Ex-
plainability Meth-
ods Intended for
Multiple Stakehold-
ers.

Examining
[18]
the
usefulness
of quality scores
generating
for
object
learning
recommendations
in repositories of
open educational
resources (OERs).

Objectives:
The purpose of this research is to examine how
modular and microservice software architec-
tures are implemented in terms of attributes re-
lated to software quality.
Results:
The work develops a mathematical model for
software design optimization based on quality-
based mixed integer goal programming.

Objectives:
This paper introduces and evaluates a dis-
tributed hybrid rendering (DHR) solution for
standalone XR devices, with the goal of com-
bining ray tracing graphics with high fidelity
while maintaining interactive frame speeds in
high-latency network environments.
Results:
The research presents a number of findings
based on an evaluation of the Distributed Hy-
brid Rendering (DHR) technique.

Objectives:
The goal of this study is to conduct an empirical
analysis of tool support for software product
lines (SPL).
Results:
The research looks at tool assistance for software
product lines (SPLs) and underlines the signif-
icance of sophisticated variability modeling in
many fields.

Objectives:
The purpose of this study is to offer an ex-
plainability structure for intelligent systems that
may suit the clarification needs of different user
groups.
Results:
The majority of engineers (65%) were pleased
with the explanation quality.

Objectives:
A study evaluates alternative techniques to rec-
ommending open educational resources, with
the goal of determining if pedagogical quality
scores improve recommender systems.
Results:
The hybrid strategy scored the highest in terms
of relevance (0.64), followed by the traditional
content-based approach (0.60), suggesting its ef-
fectiveness.

---

<!-- PAGE 52 -->

J. Imaging 2025, 11, 12

52 of 66

Table A1. Cont.

Study Issue

Employed Strategy

Dataset

Objectives/Results

[16] Hybrid Ap-
proach to Music
Recommender
Systems.

Analyze quality scores’
impact on OER recom-
mender systems and
engine tools: CF, CB,
DNN, auto-encoder, in-
put vectors BOW.

Million Song Sub-
set: 10,000 songs
1 million users.

[35] Hybrid collab-
filtering
orative
for
model
con-
sumer
dynamic
service recommen-
dation based on
mobile cloud infor-
mation system.

[19] Hybrid Music
Recommendation
Approach
for
Heterogeneous In-
formation Network
using Factorization
Machines.

[93]
Identifying
User Needs for Ad-
vertising Controls
on Facebook

In mobile cloud-based
collaborative filtering,
a hybrid model for cus-
tomer service recom-
mendation integrates
user preferences.

339 users 30 coun-
tries 5825 web ser-
vices 70 countries,
1.97 million access
logs of QoS of web
service.

hybrid recommenda-
tion model utilizing
content-based, context-
based, and CF meth-
ods, with factorization
machines.

Music Information
Knowledge Graph
(MKG):
Users 7510
Tracks 11,184
Artists 30,012

Study employed on-
line survey and remote
usability study for col-
lecting user data on
Facebook’s advertising
controls.

data
collected
through an online
survey

[102] Active Ac-
in the Ex-
tions
traction of Urban
Objects for Infor-
mation Quality and
Knowledge Recom-
mendation with
Machine Learning.

The project uses a De-
sign Science Investi-
gation (DSR) method-
ology to improve in-
formation quality and
knowledge suggestion
using machine learn-
ing techniques.

The study used a
dataset with 49,325
instances and 18
variables to evalu-
ate the effectiveness
of several classifiers
in city object recog-
nition.

Objectives:
A The system suggests songs that are compa-
rable to the user’s preferences and have been
highly rated by other users.
So, hybrid music recommendation system that
combines content-based and collaborative filter-
ing is used.
Results:
cold-start problem: use DNN

Objectives:
Hybrid collaborative filtering methodology for
consumer service recommendation in mobile
cloud to solve data sparsity and boost accuracy.
Results:
The study introduces a hybrid collaborative fil-
tering model for service recommendation in the
mobile cloud, addressing data sparsity and im-
proving prediction accuracy.

Objectives:
The research develops a hybrid recommenda-
tion model for a heterogeneous music infor-
mation network using content-based, context-
based, and collaborative filtering methods.
Results:
FM offers a novel approach to analyzing and
comprehending the relationship between users
and tracks.

Objectives:
The purpose of this study was to better under-
stand user desires and worries about Facebook
advertising restrictions, evaluate the efficiency
of present controls, and identify gaps in service
to improve conformity with user expectations.
Results:
Identifiying user goals as well as concerns with
the discoverability of Facebook ad controls

Objectives:
This work aims to map urban zones in Itajaí,
Brazil, using machine learning approaches to
improve object detection and information qual-
ity for land management and monitoring deci-
sions.
Results:
The study obtained a classification accuracy of
85.20% utilizing the J48 decision tree technique,
with a kappa statistic of 76.11%, demonstrating
good object identification and information ex-
traction from urban data.

---

<!-- PAGE 53 -->

J. Imaging 2025, 11, 12

53 of 66

Table A1. Cont.

Study Issue

Employed Strategy

Dataset

Objectives/Results

[65]
Interpretable
Aesthetic Analysis
Model
for Intelli-
gent Photography
Guidance Systems

hyper-network
The
attribute
combines
scores and a method
of attention to learn
aesthetic evaluations
and recognize visual
features.

Dataset
AADB
(10,000 images) (11
aesthetic attributes)

[66] Learning GUI
Completions with
User-defined Con-
straints.

Varying buttons
Rico (NDN)
Artificial web
Enrico

The study determines
element
insertion
and placement for a
consistent GUI layout
across screens by com-
bining
graph-based
and sequence-based
approaches.

[68] Model-driven
development plat-
form selection: four
industry case stud-
ies

platforms,
MDD
decision-making
ap-
proach, and quality
attribute information.

30 MDD platforms
and 94 MDD fea-
tures

Multiple
[69]
criteria
decision
analytic methods in
management with
T-spherical
fuzzy
information.

Using the T-SF frame-
work,
a new eval-
uation process and
decision-analytic
ap-
proach for ambiguous
multi-criteria evalua-
tion were devised.

Dataset
available
from (Mr Chen,
Ting Yu)

[67] Multi-source
knowledge fusion:
a survey.

Graph models, fuzzy
set
theory, D-S the-
ory, CNN and VAE
Bayesian analysis

DFB,
DBP-YAG,
DBP15k (ZH-EN),
YAGO3

Objectives:
integrating attribute scores and implementing
an attention mechanism to improve the inter-
pretability of aesthetic models of evaluation for
improved user interaction
Results:
Extraction feautures with ResNet with 101 lay-
ers
fully connected neural network + ReLU

Objectives:
creating machine-learning-based layout recom-
mendation techniques to guarantee consistency
in graphical user interfaces (GUIs), with an em-
phasis on implicit layout patterns.
Results:
kNN (95% match scores)
GNN (20–50 valid results)
Transformer model (30–50%)
Enrico (≤30%)

Objectives:
Model-driven development platform selection:
four industry case studies
Results:
The decision support system (DSS) recom-
mended four potential MDD platforms out of
30, and five solutions in another case study. The
decision model considered 75 criterias.

Objectives:
The paper uses T-spherical fuzzy (T-SF) struc-
tures and Minkowski distance indices to pro-
vide a unique architecture and technique for
multiple criterion decision analysis with uncer-
tainty.
Results:
A novel T-SF-based appraisal mechanism and
a decision-analytic method for multiple-criteria
assessment under uncertain conditions.

Objectives:
The goal of this study is to present a survey of
multi-source knowing fusion research and to
analyze its current status and future potential.
Results:
The study presents a classification of research
progress in multi-source knowledge fusion and
discusses

---

<!-- PAGE 54 -->

J. Imaging 2025, 11, 12

54 of 66

Table A1. Cont.

Study Issue

Employed Strategy

Dataset

Objectives/Results

[70]
NDNetGaming—
development of a
no-reference deep
CNN for gaming
video quality pre-
diction.

A study addresses
research
numerous
problems by devel-
oping a CNN-based
video
no-reference
for
quality
gaming footage influ-
enced by compression
artifacts.

rating

GVSET (24 source
sequences
video
from 12 different
games)
KUGVD (6 videos,
se-
videos
90
quences)

[71]
Ontology-
based Soft Comput-
ing and Machine
Learning.

Article
proposes
(multi-level K-mean
clustering) MLK-rBO
model:
clustering,
knowledge discovery,
probabilistic network,
ensemble approach.

[72]
OpExHAN:
opinion extraction
using hierarchical
attention network
from unstructured
reviews.

study uses

The
a
hierarchical attention
network to
extract
opinions from reviews,
with good accuracy,
precision, and recall
on Amazon’s Smart-
phone’s reviews.

[90] Performance
analysis of H2BR:
HTTP/2-based
segment upgrading
to improve the QoE
in HAS.

The study made use
of the HTTP/2-based
H2BR approach, which
involves late transmis-
sions of better video
portions that are pre-
viously stored in the
client buffer in order to
enhance video quality.

The dataset com-
9263
of
prises
respondents’
re-
collected
sponses
years
over
con-
(2018–2022),
centrating on fever
state and related
characteristics.

4

OpExHAN model
applied on Ama-
zon
Smartphone
dataset from ama-
zonin
150,000
reviews scrapped,
56,000 collected.

in

The Multi-codec
DASH dataset was
utilized
this
study to evaluate
performance across
video
multiple
codecs and stream-
ing
situations.
Different segment
durations of 1 s, 2 s,
4 s, and 6 s from
YouTube.

Objectives:
VMAF and innovative approaches are used in
the development of a CNN that predicts game
video quality.
Results:
The study creates a no-reference CNN model
for forecasting game video quality while taking
into account unique gaming characteristics. The
model was trained using VMAF and fine-tuned
with subjective assessments. A new method
of temporal pooling is proposed. High perfor-
mance across a variety of contents and datasets.

Objectives:
The MLK-rBO model combines clustering,
knowledge discovery, and Bayesian network ap-
proaches to ensure reliable knowledge retrieval
in domain ontologies.
Results:
According to the experimental data, the MLK-
rBO model described in the study outperformed
other models such as DT, RF, and SVM with an
accuracy of 98.36%.

Objectives:
This research creates a hierarchical attention net-
work to extract opinions from smartphone re-
views on Amazon, resulting in precise product
classification and feature summaries.
Results:
High accuracy (94.68%), precision 91.67%, and
recall(91.25%) are attained by the OpExHAN
model following hyperparameter testing. 16 is
the ideal batch size for results.

Objectives:
The goal of this research is to assess the per-
formance of the HTTP/2-Based Retransmission
(H2BR) approach in a variety of scenarios and
compare it to previous studies.
Results:
The study presents performance metrics for
H2BR across different configurations, demon-
strating its effectiveness in high-throughput net-
works with varying parameters.

---

<!-- PAGE 55 -->

J. Imaging 2025, 11, 12

55 of 66

Table A1. Cont.

Study Issue

Employed Strategy

Dataset

Objectives/Results

[33] Presenting a
hybrid model in so-
cial networks rec-
ommendation sys-
tem architecture de-
velopment.

A hybrid approach
combining fundamen-
tal collaborative filter-
ing and demographic
recommendation sys-
tems, using artificial
neural networks, data
mining,
and fuzzy
techniques.

Researchers exam-
ined a LinkedIn
from a
dataset
location,
specific
included
which
inter-
1404 users’
ests
in followed
firms across five
industries and five
services, for a total
of 9891 interests.

Not available

Quality-
[36]
Open
driven
educational
re-
source/courseware
case-based
REC-
ommending
Tenet(QORECT)—
Case-Based
a
Framework
for
Quality-based Rec-
ommending Open
and
Courseware
Open Educational
Resources

To recommend ed-
ucational
resources,
a hybrid technique
combines user
that
feedback, case-based
and
recommending,
a quality model
is
employed. Case-Based
Reasoning (CBR)
is
used in the study to
extract solutions from
instances of
earlier
related issues.
The
k-Nearest Neighbors
(kNN)
technique is
used by the system to
identify comparable
situations and adds
new data in order to
continually learn.

Objectives:
The study’s goal is to create a hybrid recom-
mendation system that employs supply-chain
management and organizational communica-
tion principles to suggest organizational mem-
bers in social networks. This system will hope-
fully solve problems with traditional recommen-
dation systems, such as diversity, scalability,
cold-start, and serendipity.
Results:
A hybrid recommendation system that ad-
dressed issues with cold-start, scalability, va-
riety, and serendipity in social network sugges-
tions was presented in the study. It performed
faster and more accurately than existing tech-
niques. Recall, Precision, MAE, RMSE, and
other evaluation measures were utilized to show
how well the hybrid system performed while
recommending users in social networks. In the
future, these techniques will be combined with
genetic algorithms to get better outcomes, and
their testing on more social networks will be in-
vestigated.

Objectives:
The paper presents QORECT, a hybrid archi-
tecture that recommends open-source course-
ware (OCW) as well as open educational re-
sources (OERs) by fusing a quality-driven ap-
proach with user feedback. It seeks to enhance
the suggestion process by case-based recommen-
dations and user involvement, hence improving
the findability of varied educational resources.
The study aims to create a working model sys-
tem for computer science students, assess the
quality of the available resources, and deter-
mine whether the system can be implemented
successfully in various learning environments.
Automating tasks to develop a customized and
efficient adaptive recommender system is one
of the future objectives.
Results:
The QORECT hybrid architecture is suggested by
the study as a method for promoting open educa-
tional resources and courseware. In addition to
creating the prototype system, the researchers are
presently assessing the caliber of resources avail-
able to students studying computer science. One
of the first objectives is to test the prototype on
students in order to evaluate its efficacy. Future
plans call for automating a number of framework
operations to improve suggestion and adaptabil-
ity. The ultimate goal is to develop an excellent
individualized adaptive recommender system for
users’ learning needs.

---

<!-- PAGE 56 -->

J. Imaging 2025, 11, 12

56 of 66

Table A1. Cont.

Study Issue

Employed Strategy

Dataset

Objectives/Results

[75]
Revealing
the Construction
Project Manage-
ment System of
City Park in Jakarta:
Between Hope and
Reality.

the

A
mixed-methods
research study con-
Jakarta
ducted
in
evaluated
city
parks’
construction
project management
system.
In order to
improve park quality,
the
emphasis was
on identifying gaps
pre-construction
in
and
management
stakeholder
interac-
tion. The process of
data analysis included
determining average
ratings for a thorough
assessment.

A questionnaire
dataset was em-
ployed in a Jakartan
study to evaluate
factors pertaining
community
to
involvement,
park quality, and
municipal park de-
velopment project
management. Cal-
culating
average
scores and classi-
fying them into
interval classes for
assessment were
part of
the data
analysis process.

RTiSR:

a
[34]
review-driven time
interval-aware
sequential
recom-
mendation method.

Long
Bi-directional
Short-Term Memory
(BiLSTM) and CNN
are used in the work to
capture variable order
aggregate
sequence
dependencies.

The datasets used
in this study are
from Yelp from
the Yelp Challenge
2019 as well as Mu-
sical
Instruments
(MIs), Automotive
(Auto),
Luxury
Beauty (LB), and
Beer from Amazon.

Objectives:
The purpose of the study is to evaluate Jakarta’s
current urban park building project manage-
ment system, pointing out flaws and making
suggestions for enhancement.
It focuses on
evaluating the municipal parks’ construction
project management system in order to learn
more about the areas that can be improved and
the current state of affairs.
Results:
The pre-construction phase and stakeholder
involvement of Jakarta’s city park manage-
ment system fell short of expectations. The
attainment of the intended park quality was
hampered by inadequate management of con-
struction projects, particularly during the pre-
construction phase and community engagement.
The results of the assessment showed that dif-
ferent city parks had different building project
outcomes, with certain parks receiving higher
scores for quality characteristics. To meet peo-
ple’ expectations for high-quality city parks,
more research is advised to obtain a deeper un-
derstanding of the pre-construction phase and
stakeholder involvement. In order to raise the
general standard of Jakarta’s municipal parks,
future research might focus on improving the
administration of construction projects, particu-
larly during the pre-construction stage and com-
munity engagement.

Objectives:
This work aims to propose and assess the ef-
ficacy of a sequential recommendation model
that integrates user reviews, time intervals,
the review-driven
and sequence patterns:
time interval-aware sequential recommendation
(RTiSR) model.
Results:
The research discovered that on all datasets,
increasing the depth size (h) significantly en-
hanced recommendation performance, with h
= 3 demonstrating the greatest results. Further-
more, suggestion performance improved as the
latent factor’s size increased; the optimal per-
formance was attained at a latent factor size of
50. RTiSR achieved the best performance and
highest F-rank value across all datasets, consis-
tently outperforming most baselines. The exper-
imental results consistently showed that RTiSR
is more effective and superior to numerous state-
of-the-art models in terms of HR and NDCG.

---

<!-- PAGE 57 -->

J. Imaging 2025, 11, 12

57 of 66

Table A1. Cont.

Study Issue

Employed Strategy

Dataset

Objectives/Results

Selecting
[76]
appropriate
the
leading journal in
Hospitality
and
Tourism research:
a guide based on
the topic-journal fit
and the JCR impact
factor.

Because of its flexibil-
ity, speed of process-
ing, and text database
processing tools, R soft-
ware is used in this pa-
per to analyze text data.
Excel and SPSS V. 26
were also utilized in
the data analysis.

18,798
articles
with abstracts ex-
tacted from Scopus
database

[77]
Self-
supervised Learn-
ing for Large-scale
Item Recommenda-
tions.

sizable
Two
were
datasets
employed in the
an AAI
study:
dataset
gathered
from a for-profit
mobile app shop
(5.3 million ques-
tions, 5.3 million
items)
a
Wikipedia dataset
(2.4 million queries,
2.4 million items)
that was centered
on link prediction
between Wikipedia
pages.

and

This paper presents
for
framework
a
large-scale
item
recommendations
using multi-task self-
supervised learning.
integrates a new
It
technique
for data
augmentation based
on feature correlations.
training
Enhancing
data with various data
augmentations and su-
pervised tasks are part
of the self-supervised
learning framework.
These tasks function as
support assignments
for tasks that predict
or reconstruct original
examples.

Objectives:
The paper discusses the importance of selecting
an academic journal that meets the requirements
of the journal and the study topic in order to as-
sist researchers in making the proper choice. It
also offers a guidance that considers the topic–
journal fit and JCR impact factor, as well as a
tool to gauge this fit for journals in the travel
and hospitality industries.
Results:
The study used corrected standardized resid-
uals to determine the degree of fit and statis-
tically measured the fit of research subjects in
each journal, emphasizing the significance of
topic–journal fit in connection to the impact fac-
tor.

Objectives:
This study proposes a multi-task self-supervised
learning (SSL) framework to tackle the label
sparsity issue in large-scale item recommenda-
tions. It aims to enhance item representation
learning, regularize the model for improved gen-
eralization, and leverage feature correlations for
data augmentation. The research explores the
impact of training data size on SSL improve-
ments, examines SSL parameters such as loss
multiplier and dropout rate, and compares the
performance of Random Feature Masking (RFM)
with (Correlated Feature Masking) CFM.
Results:
The study demonstrates that, when it comes to
improving model performance for large-scale
item suggestions, SSL regularization works bet-
ter than conventional methods. This is demon-
strated by the fact that, in live traffic experi-
ments, it outperforms the most advanced tech-
niques and achieves notable gains in business
KPIs. The results further highlight the signifi-
cance of choosing the right parameters by show-
ing that model performance can be negatively
impacted by dropout rates and SSL weights that
are too high.

---

<!-- PAGE 58 -->

J. Imaging 2025, 11, 12

58 of 66

Table A1. Cont.

Study Issue

Employed Strategy

Dataset

Objectives/Results

Short

text
[80]
modeling
topic
approaches in the
context of big data:
taxonomy, survey,
and analysis.

[81] Society’s Atti-
tudes Towards Hu-
man Augmentation
and Performance
Enhancement Tech-
nologies (SHAPE)
Scale.

The dataset used
study is
in this
the Google News
dataset, which con-
tains excerpts and
titles from 11,109
news stories orga-
nized into 152 clus-
ters. Furthermore,
the dataset includes
the Web Snippet
dataset, which con-
tains 12,340 web
search snippets or-
ganized into eight
groups.

The study’s dataset
two
comprised
online
surveys
administered
through Qualtrics
software, with 103
respondents in the
first round and 78
respondents in the
second.

study uses

The
a
complete survey and
classification of brief
text Topic Modeling
(STTM)
algorithms,
together with qualita-
tive and quantitative
assessments, to evalu-
ate their performance
and efficacy in topic
finding from short
texts.

The Society’s Attitudes
Human
Towards
Augmentation
and
Performance Enhance-
Technologies
ment
(SHAPE) were devel-
oped and assessed
in the study using
a
mixed-methods
methodology. These
included
methods
and
confirmatory
exploratory
factor
analysis, online sur-
veys,
expert
and
interviews.

Objectives:
The objective of this study is to provide a com-
prehensive review and taxonomy of short text
topic modeling, aiming to assist researchers in
understanding the key elements of STTM, iden-
tifying limitations of existing techniques, and
guiding future research directions in the field.
Results:
The study compared the performance of short
text topic modeling algorithms on RW-Pand-
Twitter and RW-CB-Twitter datasets with dif-
ferent number of topics (k = 5, 7, 20, 40, 60,
80). Different models were evaluated using mea-
sures like as coherence, perplexity, PMI/NPMI,
NMI, purity, ARI, AMI, entropy, accuracy, recall,
precision, and F-measure to demonstrate their
efficacy in handling brief text input.

Objectives:
The goal of the project was to close a research
gap on the societal effects of human augmenta-
tion technology by creating and validating the
SHAPE Scale, a tool for measuring public atti-
tudes toward augmented humans. Rich quanti-
tative data gathering and cross-study compar-
isons are made possible by the scale, which of-
fers a consistent and valid means of measuring
opinions regarding enhanced people. Research
on views regarding human enhancement tech-
nology is intended to be advanced by its intro-
duction.
Results:
Through expert reviews and exploratory compo-
nent analysis, the study established the thirteen-
item SHAPE Scale and confirmed its validity
and reliability. The scale is a useful tool for re-
searchers and practitioners as it helps to under-
stand how society views human augmentation
technologies. In order to inform the design and
acceptability of future augmentation technolo-
gies, the research emphasizes the importance
of evaluating and monitoring society attitudes
toward enhanced humans.

---

<!-- PAGE 59 -->

J. Imaging 2025, 11, 12

59 of 66

Table A1. Cont.

Study Issue

Employed Strategy

Dataset

Objectives/Results

[82] SpeechQoE: A
Novel Personalized
QoE Assessment
Model
for Voice
Services via Speech
Sensing.

of

voice

study

signals

uses
The
to
speech
individual
estimate
quality
ratings
in
services,
adopting a tailored
quality
experi-
of
ence(QoE)assessment
approach
called
SpeechQoE.

The
in-
dataset
cludes 38 individu-
als (23 males and
15 females) who
completed 200 call-
ing sessions while
assessing
their
perceived quality
of
experience,
making it the first
medium-scale QoE-
labeled
dataset
for conversational
voice services.

Supporting
[83]
Shy
Preschool
Children in Joining
Social Play Flan-
nery.

The study evaluated
the effects of applying
the Mind
Tools of
(ToM)-style
playing
with
and without
technology aids using
analysis
a
content
It high-
technique.
lighted the
critical
role that a voice agent
plays in incorporating
shy preschoolers into
sociodramatic play.

senior

re-
Three
searchers examined
the study’s session
video records using
standard content
They
analysis.
used Lucidchart to
organize 894 sticky
notes into subjects
subtopics
and
across numerous
sessions, based on
shape and color
coding to distin-
guish
between
sessions and age
groups

Objectives:
The paper proposes SpeechQoE, a tailored ap-
proach that uses speech signals to quantify indi-
vidual evaluations of quality in voice services. It
overcomes constraints by using few-shot learn-
ing and efficient data synthesis to rapidly adapt
to new users. The study’s goal is to increase the
precision and effectiveness of QoE evaluation in
voice services by prioritizing user-specific eval-
uation and accounting for perceived variability.
Results:
The SpeechQoE model obtained an outstand-
ing 91.4% accuracy in assessing QoE, exceed-
ing previous solutions.
It achieved constant
high accuracies of 90.9% for college students
and 91.4% for non-college students, demonstrat-
ing its usefulness across a wide range of user
backgrounds. The study underlined the model’s
capacity to capture the effect of ambient noise
on QoE perception, showing its superiority over
typical parametric models.

Objectives:
This study examined the effects of using Sto-
ryCarnival, a voice agent, in Tools of the Mind
(ToM)-style activities to encourage sociodra-
matic play among reticent preschoolers. It fo-
cused on integrating shy kids into play sessions
by comparing the behaviors of kids with and
without StoryCarnival. Another goal of the
study was to find out if the voice agent, in partic-
ular, might improve social interaction and child
engagement in sociodramatic play activities for
children aged three to five.
Results:
The study showed that integrating technology
supports into sociodramatic play sessions, such
as the physical voice agent in StoryCarnival,
was an effective way to include shy preschoolers.
Children’s interactions, linguistic exchanges,
and level of involvement all rose when technol-
ogy supports were present. The results indicate
that StoryCarnival has a promising long-term
influence on the social skills and inclusion of
shy children, with no signs of declining effects
over time.

---

<!-- PAGE 60 -->

J. Imaging 2025, 11, 12

60 of 66

Table A1. Cont.

Study Issue

Employed Strategy

Dataset

Objectives/Results

[78] Task Force Re-
port 6. Report on
Financing the New
Model of Family
Medicine.

Techno-
[84]
distress
and
parental burnout:
The
of
impact
home
facilitating
conditions and the
system quality.

[85] The
Impact
of Expertise in the
Loop for Exploring
Machine Rational-
ity.

The study used a fi-
nancial modeling tech-
nique, in order to eval-
uate the New Model of
Care’s effect on prac-
tice finances and sug-
gest health care finan-
cial policies that will
support primary medi-
cal care in the US.

To gather informa-
the authors
tion,
consulted experts
in practice manage-
healthcare
ment,
health
finance,
economics,
and
health policy in ad-
dition to published
literature
medical
and practice man-
agement databases.

The study used an
anonymous
sur-
(https://www.
vey
questionpro.com/,
access date 28 October
2023) that was deliv-
ered online via the
QuestionPro platform
to gather information
on parental burnout,
techno-distress,
sys-
tem quality, and home
enabling conditions.

The study discovered
that individuals with
higher skills tend to
explore the remedy
considerably
space
more
than novices,
matching a maximiz-
ing decision strategy
in which experts aim
to terminate at satis-
faction,
resulting in
increased discontent
as more weaknesses
in the
system are
discovered.

The study includes
a total of 55 ques-
span
that
tions
many views, such
as
home work-
ing conditions (6
frame-
questions),
work quality (5
questions), techno-
logical
issues (18
questions), parental
(23
exhaustion
questions)
and
3
demographic
questions.

The study’s dataset
comprises
user
interfaces for 3D
model
simplifica-
tion, summarized
and image
text,
color
enhance-
ment tasks. These
also
interfaces
incorporate mecha-
nisms for collecting
participant knowl-
ranking
edge,
variants, and as-
sessing satisfaction.

Objectives:
The goal of this research is to create a financial
model that evaluates how the New Model of
Care affects practice finances and offers health-
care finance recommendations to support pri-
mary care in the US over the ensuing few
decades.
Results:
According to the study, family physicians could
see a 26% increase in pay under the current fee-
for-service system if the New Model of care is
implemented. There is also room for future in-
creases through changes to the reimbursement
structure and the implementation of quality-
based incentive programs.

Objectives:
The goal of this research is to create and validate
a unified theory of techno-distress burnout in
families who assist their children with technol-
ogy for distant classes, in order to better under-
stand the influence of techno-distress on parent
burnout.
Results:
The study outcomes reveal that both home
setting and system quality impact parent’s
techno-distress, which in change greatly impacts
parental burnout. This highlights the impor-
tance of addressing these factors to mitigate the
adverse impacts of utilizing technology in edu-
cational institutions.

Objectives:
This study examines how user skill affects the
quality of results and personal satisfaction in
human-in-the-loop optimization. It focuses on
text, photo, and 3D mesh optimization settings
and intends to provide insights for future HIL
systems design.
Results:
The study found that novices may attain expert-
level achievement in outcome quality, although
experts have more explicit likes, discontent, and
iterations. Novices are more satisfied and termi-
nate sooner.

---

<!-- PAGE 61 -->

J. Imaging 2025, 11, 12

61 of 66

Table A1. Cont.

Study Issue

Employed Strategy

Dataset

Objectives/Results

[73] Two-sided Cali-
bration for Quality-
aware Responsible
Recommendation.

The study uses max-
imum marginal rele-
vance (MMR) rerank-
ing to balance a recom-
mender system’s out-
put for improved rele-
vance and calibration.

[79] Voice in Words:
A Mixed-Method
for
Approach
Decoding Digital
Footprints Using
Online Reviews

study uses

a
The
ap-
mixed-method
combining
proach,
sentiment analysis and
logistic regression, to
investigate the connec-
tion between online
recommendations
made by customers
and their opinions on
the quality of airline
services

[96] Vulnerabilities
of
Unattended
Face Verification
Systems to Facial-
Component-based
Presentation
At-
tacks: An Empirical
Study.

The study employs
five presentation at-
tack detection (PAD)
methods focusing on
texture, quality, and
structure clues, utiliz-
ing linear SVM and
discriminant
linear
analysis for classifica-
tion.

The study makes
use of the Tenrec
dataset, which is
a compilation of
recommendation
from
platforms
Tencent’s feeds.
It
focuses on the QK-
article sample with
annotated quality
information, which
31,413
includes
884,315
articles,
interactions,
and
19,965 users.

The
in-
dataset
cludes 2464 econ-
omy class and 1270
business class pas-
senger data from
three major airlines,
as well as ratings,
recommendations,
and reviews from
other
of
users
https://www.
skytraxratings.
com/, access date
22 September 2023

The dataset com-
prises digital facial
artifacts produced
from 63 Chinese
participants’ frontal
face photos, with
an emphasis on
facial
different
features to evaluate
security flaws in
face
unmanaged
sys-
verification
tems.

Objectives:
The study aims to provide quality-aware and
two-sided calibrated suggestions by comparing
users’ prior interest distributions and ensuring
an overall target exposure distribution of dif-
ferent item categories with the proposed post-
processing method called Personalized Calibra-
tion Targets (PCT).
Results:
As evidenced by the experimental conditions
and outcomes, the suggested PCT technique
beats state-of-the-art baselines in attaining better
user-level calibration and guaranteeing system-
level calibration.

Objectives:
The goal of the study is to determine the critical
factors influencing the major aspects of airline
service quality and to examine the causal rela-
tionship between customer assessments of the
quality of the services received and their online
recommendations.
Results:
This research endeavors to examine the causal
relationship between customer assessments of
airline service quality and their online recom-
mendations, all the while identifying critical fac-
tors that impact critical aspects of airline service
quality. Qatar Airways received the highest rec-
ommendation rate (78%), followed by Singapore
Airlines (77%), and Cathay Pacific (66%).

Objectives:
In addition to suggesting a creative and suc-
cessful face impersonation presentation attack
method, the paper attempts to examine the sus-
ceptibilities of unattended verification of faces
systems to facial-component-based presentation
attacks.
Results:
The study shows that the suggested presenta-
tion attack based on facial components performs
better than current attack techniques, which
presents a serious risk to face verification and
presenting attack detection systems.

---

<!-- PAGE 62 -->

J. Imaging 2025, 11, 12

62 of 66

Table A1. Cont.

Study Issue

Employed Strategy

Dataset

Objectives/Results

[103] A Semi-
Supervised Learn-
ing Approach to
Quality-Based Web
Service Classifica-
tion.

To
improve web
service classification,
the researchers used
semi-supervised
a
self-training
system
that combines several
scoring methodologies
and distance computa-
tions.

The dataset used
in this study pro-
vides data on 2871
genuine online ser-
vices, 364 labeled
services, and 2507
unlabeled
data
points across nine
quality features.

Micro-
[104]
Fine
Locational
Dust
Prediction
Utilizing Machine
Learning and Deep
Learning Models.

study predicts
The
PM10 levels using a
technique
modeling
that
includes Long
Short-Term Memory
(LSTM) networks, Ran-
dom Forest Regression
(RFR), XGBoost (XGB),
and AdaBoost.

in-
dataset
The
cludes around 23
samples
million
from 957
South
Korean air quality
monitoring stations
(2014–2020), with
an emphasis on
pollutants such as
PM10, SO2, CO, O3,
and NO2, and uses
LSTM networks,
Random Forest Re-
gression, XGBoost,
to
and AdaBoost
anticipate
PM10
value.

Objectives:
The goal of this research is to assess the efficacy
of the Semi-Supervised Learning Web Service
Classification (SSL-WSC) algorithm for classify-
ing web services using various base classifier
algorithms, as well as to increase classification
accuracy using semi-supervised learning.
Results:
The study discovered that the SSL-WSC algo-
rithm outperformed the supervised technique
in all classifiers, with average improvements of
11.26% in F1-Score, 9.43% in accuracy, and 9.53%
in precision.

Objectives:
The goal of this research is to increase under-
standing of the elements that influence PM10
levels and prediction accuracy by adding micro-
location measurements and using a time-series
dataset. It aims to reduce regional differences
in surveillance of air quality and contribute to
improving public health by providing accurate
data for responsible choices.
Results:
The study produced the best performance in
PM10 predicting using the LSTM model, with
a Pearson correlation of 0.6176, as well as en-
hanced accuracy by including micro-location
characteristics and addressing data shortage is-
sues.

References

1.

Xu, L.; Sang, X. E-Commerce Online Shopping Platform Recommendation Model Based on Integrated Personalized Recommen-
dation. Sci. Program. 2022, 2022, 4823828. [CrossRef]

2. Hossain, I.; Palash, M.; Sejuty, A.; Tanjim, N.; Nasim, M.; Saif, S.; Suraj, A.; Haque, M.; Karim, N. A Survey of Recommender

System Techniques and the Ecommerce Domain. arXiv 2022, arXiv:2208.07399.

3. Murillo, V.; Avendano, D.; Lopez, F.; Calleros, J. A Systematic Literature Review on the Hybrid Approaches for Recommender

4.

5.

6.

7.

8.

9.

Systems. Comput. Sist. 2022, 26, 357–372. [CrossRef]
Chen, R.; Hua, Q.; Chang, Y.; Wang, B.; Zhang, L.; Kong, X. A survey of collaborative filtering-based recommender systems: From
traditional methods to hybrid methods based on social networks. IEEE Access 2018, 6, 64301–64320. [CrossRef]
De Nadai, M.; Fabbri, F.; Gigioli, P.; Wang, A.; Li, A.; Silvestri, F.; Kim, L.; Lin, S.; Radosavljevic, V.; Ghael, S.; et al. Personalized
Audiobook Recommendations at Spotify Through Graph Neural Networks. In Proceedings of the WWW 2024: The ACM Web
Conference, Singapore, 13–17 May 2024; pp. 403–412.
Sahu, S.; Kumar, R.; Mohdshafi, P.; Shafi, J.; Kim, S.; Ijaz, M. A Hybrid Recommendation System of Upcoming Movies Using
Sentiment Analysis of YouTube Trailer Reviews. Mathematics 2022, 10, 1568. [CrossRef]
Alamdari, P.; Navimipour, N.; Hosseinzadeh, M.; Safaei, A.; Darwesh, A. A Systematic Study on the Recommender Systems in
the E-Commerce. IEEE Access 2020, 8, 115694–115716. [CrossRef]
Raza, S.; Rahman, M.; Kamawal, S.; Toroghi, A.; Raval, A.; Navah, F.; Kazemeini, A. A Comprehensive Review of Recommender
Systems: Transitioning from Theory to Practice. arXiv 2024, arXiv:2407.13699.
Souabi, S.; Retbi, A.; Idrissi, M.; Bennani, S. Recommendation systems on e-learning and social learning: A systematic review.
Electron. J. e-Learn. 2021, 19, 432–451. [CrossRef]

---

<!-- PAGE 63 -->

J. Imaging 2025, 11, 12

63 of 66

10. Pande, C.; Witschel, H.; Martin, A. New Hybrid Techniques for Business Recommender Systems. Appl. Sci. 2022, 12, 4804.

[CrossRef]

11. Da’u, A.; Salim, N. Recommendation system based on deep learning methods: A systematic review and new directions. Artif.

12.

Intell. Rev. 2020, 53, 2709–2748. [CrossRef]
Isinkaye, F.; Folajimi, Y.; Ojokoh, B. Recommendation systems: Principles, methods and evaluation. Egypt. Inform. J. 2015, 16,
261–273. [CrossRef]

13. Dixit, V.; Gupta, S.; Jain, P. A Propound Hybrid Approach for Personalized Online Product Recommendations. Appl. Artif. Intell.

2018, 32, 785–801. [CrossRef]

14. Rhanoui, M.; Mikram, M.; Yousfi, S.; Kasmi, A.; Zoubeidi, N. A hybrid recommender system for patron driven library acquisition

and weeding. J. King Saud Univ.-Comput. Inf. Sci. 2022, 34, 2809–2819. [CrossRef]

15. Liu, D.; Li, J.; Du, B.; Chang, J.; Gao, R.; Wu, Y. A hybrid neural network approach to combine textual information and rating

information for item recommendation. Knowl. Inf. Syst. 2021, 63, 621–646. [CrossRef]

16. Bablani, D.; Gupta, R.; Gokhale, T. Hybrid Approach to Music Recommender Systems. Int. J. Res. Appl. Sci. Eng. Technol. 2022.
17. Paranjape, V.; Nihalani, N.; Mishra, N. Design and Development of an Efficient Demographic-based Movie Recommender System

using Hybrid Machine Learning Techniques. Int. J. Comput. Commun. Control 2024, 19, 5840. [CrossRef]

18. Gordillo, A.; López-Fernández, D.; Verbert, K. Examining the usefulness of quality scores for generating learning object

recommendations in repositories of open educational resources. Appl. Sci. 2020, 10, 4638. [CrossRef]

19. Azzam, M. Hybrid Music Recommendation Approach for Heterogeneous Information Network Using Factorization Machines; Johannes

Kepler Universität Linz: Linz, Austria, 2021.

20. Zheng, Y. Multi-stakeholder Personalized Learning with Preference Corrections. In Proceedings of the 2019 IEEE 19th International

Conference on Advanced Learning Technologies (ICALT), Maceió, Brazil, 15–18 July 2019; pp. 66–70.

21. Kähärä, T.; Haataja, K.; Toivanen, P. Towards more accurate and intelligent recommendation systems. In Proceedings of
the International Conference on Intelligent Systems Design and Applications, ISDA, Okinawa, Japan, 27–29 November 2014;
pp. 165–171.

22. Nithya, B.; Geetha, D.; Kumar, M. Metaheuristic-Assisted Contextual Post-Filtering Method for Event Recommendation System.

Int. J. Image Graph. 2023, 29, 2550043. [CrossRef]

23. Murciego, Á.; Jiménez-Bravo, D.; Román, A.; Santana, J.; Moreno-García, M. Context-aware recommender systems in the music

domain: A systematic literature review. Electronics 2021, 10, 1555. [CrossRef]

24. Çano, E.; Morisio, M. Hybrid recommender systems: A systematic literature review. Intell. Data Anal. 2017, 21, 1487–1524.

[CrossRef]

25. Uta, M.; Felfernig, A.; Le, V.; Tran, T.; Garber, D.; Lubos, S.; Burgstaller, T. Knowledge-based recommender systems: Overview

26.

and research directions. Front. Big Data 2024, 7, 1304439. [CrossRef] [PubMed]
Sofikitis, E.; Makris, C. Development of Recommendation Systems Using Game Theoretic Techniques. Comput. Sci. Inf. Syst. 2022,
19, 1133–1154. [CrossRef]

27. Ramanujam, S.S. A Study on Hybrid Recommender System with Deep Learning and Deployment in Big Data. Available online:

http://www.testmagzine.biz/index.php/testmagzine/article/view/258/229 (accessed on 3 July 2023).

28. Tejeda-Lorente, Á.; Porcel, C.; Peis, E.; Sanz, R.; Herrera-Viedma, E. A quality based recommender system to disseminate

29.

information in a university digital library f. Inf. Sci. 2014, 261, 52–69. [CrossRef]
Sanguino, J.; Mariño, O.; Cardozo, N.; Manrique, R.; Linares-Vásquez, M. A course hybrid recommender system for limited user
information scenarios. J. Educ. Data Min. 2022, 14, 162–188.

30. Choi, K.; Yoo, D.; Kim, G.; Suh, Y. A hybrid online-product recommendation system: Combining implicit rating-based collabora-

tive filtering and sequential pattern analysis. Electron. Commer. Res. Appl. 2012, 11, 309–317. [CrossRef]

31. Duong, T.N.; Than, V.D.; Vuong, T.A.; Tran, T.H. A Novel Hybrid Recommendation System Integrating Content-Based and Rating
Information. In Advances in Networked-Based Information Systems, Proceedings of the 22nd International Conference on Network-Based
Information Systems (NBiS-2019), Oita, Japan, 5–7 September 2019; Springer: Cham, Switzerland, 2020; pp. 325–337.
Ishida, Y.; Shimizu, T.; Yoshikawa, M. An analysis and comparison of keyword recommendation methods for scientific data. Int.
J. Digit. Libr. 2020, 21, 307–327. [CrossRef]

32.

33. Zare, A.; Motadel, M.; Jalali, A. Presenting a hybrid model in social networks recommendation system architecture development.

34.

AI Soc. 2020, 35, 469–483. [CrossRef]
Shi, X.; Liu, Q.; Bai, Y.; Shang, M. RTiSR: A review-driven time interval-aware sequential recommendation method. J. Big Data
2023, 10, 32. [CrossRef]

35. Zhou, Q.; Zhuang, W.; Ren, H.; Chen, Y.; Yu, B.; Lou, J.; Wang, Y. Hybrid collaborative filtering model for consumer dynamic

service recommendation based on mobile cloud information system. Inf. Process. Manag. 2022, 59, 102871. [CrossRef]

---

<!-- PAGE 64 -->

J. Imaging 2025, 11, 12

64 of 66

36. Vladoiu, M.; Constantinescu, Z.; Moise, G. QORECT—A case-based framework for quality-based recommending open course-
ware and open educational resources. In Computational Collective Intelligence. Technologies and Applications; Lecture Notes in
Computer Science (Including Subseries Lecture Notes in Artificial Intelligence and Lecture Notes In Bioinformatics); Springer:
Berlin/Heidelberg, Germany, 2013; Volume 8083 LNAI, pp. 681–690.

37. Kwieci ´nski, R.; Górecki, T.; Filipowska, A.; Dubrov, V. Job Recommendations: Benchmarking of Collaborative Filtering Methods

38.

for Classifieds. Electronics 2024, 13, 3049. [CrossRef]
Forhad, M.; Arefin, M.; Kayes, A.; Ahmed, K.; Chowdhury, M.; Kumara, I. An effective hotel recommendation system through
processing heterogeneous data. Electronics 2021, 10, 1920. [CrossRef]

39. Raul, A.; Porobo Dharwadker, A.; Schumitsch, B. CAM2: Conformity-Aware Multi-Task Ranking Model for Large-Scale
Recommender Systems. In Proceedings of the ACM Web Conference 2023—Companion of the World Wide Web Conference,
WWW 2023, Austin, TX, USA, 30 April–4 May 2023; Volume 1, pp. 513–517.
Sivasankari, R.; Dhilipan, J. Hybrid scientific article recommendation system with COOT optimization. Data Sci. Manag. 2024, 7,
99–107. [CrossRef]

40.

41. Castells, P.; Hurley, N. Vargas & Saul Novelty and Diversity in Recommender Systems. In Recommender Systems Handbook, 2nd

ed.; Springer: New York, NY, USA, 2015; pp. 1–1003.

42. Bukhari, M.; Maqsood, M.; Aadil, F. KGR: A Kernel-Mapping Based Group Recommender System Using Trust Relations. Neural

Process. Lett. 2024, 56, 201. [CrossRef]

43. Lai, C.; Peng, P. A Hybrid Deep Learning Method to Extract Multi-features from Reviews and User–Item Relations for Rating

Prediction. Int. J. Comput. Intell. Syst. 2023, 16, 109. [CrossRef]

44. Gong, J.; Zhang, X.; Li, Q.; Wang, C.; Song, Y.; Zhao, Z.; Wang, S. A top-n movie recommendation framework based on deep

neural network with heterogeneous modeling. Appl. Sci. 2021, 11, 7418 [CrossRef]

45. Walek, B.; Fajmon, P. A hybrid recommender system for an online store using a fuzzy expert system. Expert Syst. Appl. 2023,

212, 118565. [CrossRef]

46. Porcel, C.; Tejeda-Lorente, A.; Martínez, M.; Herrera-Viedma, E. A hybrid recommender system for the selective dissemination of

research resources in a technology transfer office. Inf. Sci. 2012, 184, 1–19. [CrossRef]

47. Higgins, J.; Thomas, J.; Chandler, J.; Cumpston, M.; Li, T.; Page, M.; Welch, V. (Eds.) Cochrane Handbook for Systematic Reviews of
Interventions, Version 6.4; Wiley: Hoboken, NJ, USA, 2023. Available online: www.training.cochrane.org/handbook (accessed on 5
August 2023).

48. Kitchenham, B.; Charters, S. Guidelines for Performing Systematic Literature Reviews in Software Engineering; Technical Report EBSE
2007-001. Keele University and Durham University Joint Report; Software Engineering Group, Department of Computer Science:
Keele, UK, 2007.
Silva, F.; Slodkowski, B.; Silva, K.; Cazella, S. A systematic literature review on educational recommender systems for teaching
and learning: Research trends, limitations and opportunities. Educ. Inf. Technol. 2023, 28, 3289–3328. [CrossRef]

49.

50. Page, M.; McKenzie, J.; Bossuyt, P.; Boutron, I.; Hoffmann, T.; Mulrow, C.; Shamseer, L.; Tetzlaff, J.; Akl, E.; Brennan, S.; et al. The

PRISMA 2020 statement: An updated guideline for reporting systematic reviews. BMJ 2021, 372, 89.

51. Khtira, A.; Benlarabi, A.; El, B. Model Defects in Evolving Software Product Lines: A Review of Literature. Am. Sci. Res. J. Eng.

Technol. Sci. 2018, 45, 20–41.

52. Trabelsi, F.; Khtira, A.; El Asri, B. Hybrid Recommendation Systems: A State of Art. In Proceedings of the International Conference
on Evaluation of Novel Approaches to Software Engineering, ENASE—Proceedings, Online, 26–27 April 2021; pp. 281–288.
53. Roy, D.; Dutta, M. A systematic review and research perspective on recommender systems. J. Big Data 2022, 9, 59. [CrossRef]
54. Moher, D.; Liberati, A.; Tetzlaff, J.; Altman, D. Preferred reporting items for systematic reviews and meta-analyses: The PRISMA

statement. Int. J. Surg. 2010, 8, 336–341. [CrossRef] [PubMed]

55. Higgins, J.; Green, S.; Ben Van Den, A. Cochrane Handbook for Systematic Reviews of Interventions. Int. Coach. Psychol. Rev.

56.

2020, 15, 123–125. [CrossRef]
Schoot, R.; Bruin, J.; Schram, R.; Zahedi, P.; Boer, J.; Weijdema, F.; Kramer, B.; Huijts, M.; Hoogerwerf, M.; Ferdinands, G.; et al. An
open source machine learning framework for efficient and transparent systematic reviews. Nat. Mach. Intell. 2021, 3, 125–133.
[CrossRef]

57. Van Dijk, S.; Brusse-Keizer, M.; Bucsán, C.; Van Der Palen, J.; Doggen, C.; Lenferink, A. Artificial intelligence in systematic

reviews: Promising when appropriately used. BMJ Open 2023, 13, e072254. [CrossRef] [PubMed]

58. Harmsen, W.; De Groot, J.; Harkema, A.; Van Dusseldorp, I.; De Bruin, J.; Van Den Brand, S.; Van De Schoot, R. Artificial Intelligence
Supports Literature Screening in Medical Guideline Development: Towards Up-to-Date Medical Guidelines; Utrecht University: Utrecht,
The Netherlands, 2020.

59. Active Learning for Systematic Reviews? 2023. Available online: https://asreview.readthedocs.io/en/stable/ (accessed on 3

July 2023).

---

<!-- PAGE 65 -->

J. Imaging 2025, 11, 12

65 of 66

60. Rastogi, D.; Parihar, T.; Kumar, H. A parametric analysis of AVA to optimise Netflix performance. Int. J. Inf. Technol. 2023, 15,

2687–2694. [CrossRef] [PubMed]

61. Yalcin Kavus, B.; Gulum Tas, P.; Ayyildiz, E.; Taskin, A. A three-level framework to evaluate airline service quality based on

62.

interval valued neutrosophic AHP considering the new dimensions. J. Air Transp. Manag. 2022, 99, 102179. [CrossRef]
Shayganmehr, M.; Montazer, G. An extended model for assessing E-Services of Iranian Universities Websites Using Mixed
MCDM method. Educ. Inf. Technol. 2020, 25, 3723–3757. [CrossRef]

63. Li, F.; Wang, C. Artificial intelligence and edge computing for teaching quality evaluation based on 5G-enabled wireless

communication technology. J. Cloud Comput. 2023, 12, 45. [CrossRef]

64. Williams, K.; Corwith, A. Beyond Bricks and Mortar: The efficacy of online learning and community-building at College Park

Academy during the COVID-19 pandemic. Educ. Inf. Technol. 2021, 26, 5055–5076. [CrossRef] [PubMed]

65. Wu, X. Interpretable Aesthetic Analysis Model for Intelligent Photography Guidance Systems. In Proceedings of the International

Conference on Intelligent User Interfaces, Proceedings IUI, Helsinki, Finland, 22–25 March 2022; pp. 661–671.

66. Brückner, L.; Leiva, L.; Oulasvirta, A. Learning GUI Completions with User-Defined Constraints. ACM Trans. Interact. Intell. Syst.

2022, 12, 6. [CrossRef]

67. Zhao, X.; Jia, Y.; Li, A.; Jiang, R.; Song, Y. Multi-source knowledge fusion: A survey. World Wide Web 2020, 23, 2567–2592.

68.

[CrossRef]
Farshidi, S.; Jansen, S.; Fortuin, S. Model-driven development platform selection: Four industry case studies. Softw. Syst. Model.
2021, 20, 1525–1551. [CrossRef]

69. Chen, T. Multiple criteria decision analytic methods in management with T-spherical fuzzy information. Artif. Intell. Rev. 2023,

56, 14087–14157. [CrossRef] [PubMed]

70. Utke, M.; Zadtootaghaj, S.; Schmidt, S.; Bosse, S.; Möller, S. NDNetGaming—Development of a no-reference deep CNN for

gaming video quality prediction. Multimed. Tools Appl. 2022, 81, 3181–3203. [CrossRef]

71. Anand, S. Ontology-based Soft Computing and Machine Learning Model for Ecient Retrieval. Knowl. Inf. Syst. 2024, 66, 1371–1402.

[CrossRef]

72. Ratmele, A.; Thakur, R. OpExHAN: Opinion extraction using hierarchical attention network from unstructured reviews. Soc.

Netw. Anal. Min. 2022, 12, 148. [CrossRef] [PubMed]

73. Wang, C.; Liu, Y.; Yu, Y.; Ma, W.; Zhang, M.; Liu, Y.; Zeng, H.; Feng, J.; Deng, C. Two-sided Calibration for Quality-aware
Responsible Recommendation. In Proceedings of the 17th ACM Conference on Recommender Systems, Singapore, 18–22
September 2023.

74. Horcas, J.; Pinto, M.; Fuentes, L. Empirical analysis of the tool support for software product lines. Softw. Syst. Model. 2023, 22,

377–414. [CrossRef]

75. Yuslim, S.; Simanjuntak, M.; Lianto, F. Revealing the Construction Project Management System of City Park in Jakarta: Between

Hope and Reality. Int. J. Adv. Sci. Eng. Inf. Technol. 2022, 12, 2180–2189. [CrossRef]

76. Barrera-Barrera, R. Selecting the appropriate leading journal in Hospitality and Tourism research: A guide based on the topic-

journal fit and the JCR impact factor. Scientometrics 2022, 127, 1801–1823. [CrossRef]

77. Yao, T.; Yi, X.; Cheng, D.; Yu, F.; Chen, T.; Menon, A.; Hong, L.; Chi, E.; Tjoa, S.; Kang, J.; et al. Self-supervised Learning for
Large-scale Item Recommendations. In Proceedings of the International Conference on Information and Knowledge Management,
Online, 1–5 November 2021; pp. 4321–4330.
Spann, S. Task Force Report 6. Report on Financing. In Annals of Family Medicine; Annals of Family Medicine, Inc.: Leawood, KS,
USA, 2004; pp. 1–21.

78.

79. Rasool, G.; Pathania, A. Voice in Words: A Mixed-Method Approach for Decoding Digital Footprints Using Online Reviews. J.

Qual. Assur. Hosp. Tour. 2022, 24, 1014–1045. [CrossRef]

80. Murshed, B.; Mallappa, S.; Abawajy, J.; Saif, M.; Al-ariki, H.; Abdulwahab, H. Short text topic modelling approaches in the context

of big data: Taxonomy, survey, and analysis. Artif. Intell. Rev. 2023, 56, 5133–5260. [CrossRef]

81. Villa, S.; Niess, J.; Schmidt, A.; Welsch, R. Society’s Attitudes Towards Human Augmentation and Performance Enhancement

Technologies (SHAPE) Scale. Proc. ACM Interact. Mob. Wearable Ubiquitous Technol. 2023, 7, 128. [CrossRef]

82. Wang, C.; Zhu, H.; Li, M. SpeechQoE: A Novel Personalized QoE Assessment Model for Voice Services via Speech Sensing.
In Proceedings of the SenSys 2022—20th ACM Conference on Embedded Networked Sensor Systems, Boston, MA, USA, 6–9
November 2022; pp. 305–319.

83. Currin, F.; Diederich, K.; Blasi, K.; Dale Schmidt, A.; David, H.; Peterman, K.; Hourcade, J. Supporting Shy Preschool Children
in Joining Social Play. In Proceedings of the Interaction Design and Children, IDC 2021, Athens, Greece, 24–30 June 2021;
pp. 396–407.

84. Bravo-Adasme, N.; Cataldo, A.; Toledo, E. Techno-distress and parental burnout: The impact of home facilitating conditions and

the system quality. Educ. Inf. Technol. 2023, 28, 13619–13646. [CrossRef]

---

<!-- PAGE 66 -->

J. Imaging 2025, 11, 12

66 of 66

85. Ou, C.; Mayer, S.; Butz, A. The Impact of Expertise in the Loop for Exploring Machine Rationality. In Proceedings of the
International Conference on Intelligent User Interfaces, Proceedings IUI, Sydney, Australia, 27–31 March 2023; pp. 307–321.
Farshidi, S.; Kwantes, I.; Jansen, S. Business process modeling language selection for research modelers. Softw. Syst. Model. 2023,
23, 137–162. [CrossRef]

86.

87. Narechania, A.; Du, F.; Sinha, A.; Rossi, R.; Hoffswell, J.; Guo, S.; Koh, E.; Navathe, S.; Endert, A. DataPilot: Utilizing Quality and
Usage Information for Subset Selection during Visual Data Preparation. In Proceedings of the Conference on Human Factors in
Computing Systems, Hamburg, Germany, 23–28 April 2023.

88. Mili´c, M.; Makaji´c-Nikoli´c, D. Development of a Quality-Based Model for Software Architecture Optimization: A Case Study of

Monolith and Microservice Architectures. Symmetry 2022, 14, 1824. [CrossRef]

89. Tan, Y.; Tan, A.; Nge, N.; Bhojan, A. DHR: Distributed Hybrid Rendering for Metaverse Experiences. In Proceedings of the IXR

2022—The 1st Workshop on Interactive EXtended Reality, Lisbon, Portugal, 10–14 October 2022; pp. 51–59.

90. Nguyen, M.; Amirpour, H.; Tashtarian, F.; Timmerer, C.; Hellwagner, H. Performance analysis of H2BR: HTTP/2-based segment

upgrading to improve the QoE in HAS. Multimed. Tools Appl. 2023, 83, 12561–12595. [CrossRef]

91. Berahmand, K.; Li, Y.; Xu, Y. DAC-HPP: Deep attributed clustering with high-order proximity preserve. Neural Comput. Appl.

92.

2023, 4, 152. [CrossRef]
Jaiswal, R.; Dubey, R. CAQoE: A Novel No-Reference Context-Aware Speech Quality Prediction Metric. ACM Trans. Multimed.
Comput. Commun. Appl. 2023, 19, 35. [CrossRef]

93. Habib, H.; Pearman, S.; Young, E.; Saxena, I.; Zhang, R.; Cranor, L. Identifying User Needs for Advertising Controls on Facebook.

Proc. ACM Hum.-Comput. Interact. 2023, 6, 59. [CrossRef]

94. Martin, K.; Liret, A.; Wiratunga, N.; Owusu, G.; Kern, M. Evaluating Explainability Methods Intended for Multiple Stakeholders.

KI-Kunstl. Intell. 2021, 35, 397–411. [CrossRef]

95. Carlsson, N.; Eager, D. Cross-User Similarities in Viewing Behavior for 360° Video and Caching Implications. ACM Trans.

Multimed. Comput. Commun. Appl. 2022, 19, 1–24. [CrossRef]

96. Qin, L.; Peng, F.; Long, M.; Ramachandra, R.; Busch, C. Vulnerabilities of Unattended Face Verification Systems to Facial

Components-based Presentation Attacks: An Empirical Study. ACM Trans. Priv. Secur. 2022, 25, 4. [CrossRef]

97. Acosta, S.; Garza, T.; Hsu, H.; Goodson, P. Assessing Quality in Systematic Literature Reviews: A Study of Novice Rater Training.

SAGE Open 2020, 10, 2158244020939530. [CrossRef]

98. Yuan, H.; Hernandez, A. User Cold Start Problem in Recommendation Systems: A Systematic Review. IEEE Access 2023, 11,

136958–136977. [CrossRef]

99. Access, O.; Pasrija, V.; Pasrija, S. The Cold-Start Problem in Recommender Systems: Challenges and Mitigation Techniques. Int.

Res. J. Mod. Eng. Technol. Sci. 2024, 6.

100. Sabiri, B.; Khtira, A.; El Asri, B.; Rhanoui, M. Investigating Contrastive Pair Learning’s Frontiers in Supervised, Semisupervised,

and Self-Supervised Learning. J. Imaging 2024, 10, 196. [CrossRef] [PubMed]

101. Mauri, M.; Elli, T.; Caviglia, G.; Uboldi, G.; Azzi, M. RAWGraphs: A Visualisation Platform to Create Open Outputs.

In
Proceedings of the 12th Biannual Conference on Italian SIGCHI Chapter, Cagliari, Italy, 18–20 September 2017. Available online:
https://api.semanticscholar.org/CorpusID:28530715 (accessed on 22 December 2023).

102. Silva, L.; Sales Mendes, A.; Sánchez San Blas, H.; Caetano Bastos, L.; Leopoldo Gonçalves, A.; Fabiano de Moraes, A. Active
Actions in the Extraction of Urban Objects for Information Quality and Knowledge Recommendation with Machine Learning.
Sensors 2023, 23, 138. [CrossRef]

103. Bonab, M.; Tanha, J.; Masdari, M. A Semi-Supervised Learning Approach to Quality-Based Web Service Classification. IEEE

Access 2024, 12, 50489–50503. [CrossRef]

104. Kim, S.; Yu, H.; Yoon, J.; Park, E. Micro-Locational Fine Dust Prediction Utilizing Machine Learning and Deep Learning Models.

Comput. Syst. Sci. Eng. 2024, 48, 413–429. [CrossRef]

Disclaimer/Publisher’s Note: The statements, opinions and data contained in all publications are solely those of the individual
author(s) and contributor(s) and not of MDPI and/or the editor(s). MDPI and/or the editor(s) disclaim responsibility for any injury to
people or property resulting from any ideas, methods, instructions or products referred to in the content.

<!-- MARKITDOWN CONVERSION -->

<!-- Full MarkItDown conversion for formatting fidelity. -->

Journal of
Imaging
SystematicReview
Hybrid Quality-Based Recommender Systems: A Systematic
†
Literature Review
BihiSabiri1,* ,AmalKhtira2 ,BouchraElAsri1 andMaryemRhanoui3,4
1 IMSTeam,ADMIRLaboratory,RabatITCenter,ENSIAS,MohammedVUniversityinRabat,
Rabat10130,Morocco
2 LASTIMILaboratory,ESTSalé,MohammedVUniversityinRabat,Salé11060,Morocco
3 LaboratoryHealthSystemicProcess(P2S),UR4129,UniversityClaudeBernardLyon1,UniversityofLyon,
69008Lyon,France
4 MeridianTeam,LYRICALaboratory,SchoolofInformationSciences,Rabat10100,Morocco
* Correspondence:bihi_sabiri@um5.ac.ma
† SupportedbyTekCircle:(https://tekcircle.io).
Abstract: Astechnologydevelops,consumerbehaviorandhowpeoplesearchforwhat
theywantareconstantlyevolving. Onlineshoppinghasfundamentallychangedthee-
commerceindustry. Althoughtherearemoreproductsavailablethaneverbefore,onlya
smallportionofthemarenoticed;asaresult,afewitemsgaindisproportionateattention.
Recommendersystemscanhelptoincreasethevisibilityoflesser-knownproducts. Major
technologybusinesseshaveadoptedthesetechnologiesasessentialofferings,resultingin
betteruserexperiencesandmoresales. Asaresult,recommendersystemshaveachieved
considerableeconomic,social,andglobaladvancements. Companiesareimprovingtheir
algorithmswithhybridtechniquesthatcombinemorerecommendationmethodologiesas
thesesystemsareamajorresearchfocus. Thisreviewprovidesathoroughexamination
ofseveralhybridmodelsbycombiningideasfromthecurrentresearchandemphasizing
their practical uses, strengths, and limits. The review identifies special problems and
opportunitiesfordesigningandimplementinghybridrecommendersystemsbyfocusing
ontheuniqueaspectsofbigdata,notablyvolume,velocity,andvariety. Adheringtothe
CochraneHandbookandtheprinciplesdevelopedbyKitchenhamandChartersguarantees
thattheassessmentprocessistransparentandhighinquality. Thecurrentaimistoconduct
asystematicreviewofseveralrecentdevelopmentsintheareaofhybridrecommender
AcademicEditor: AloisHerkommer systems. Thestudycoversthestateoftheartoftherelevantresearchoverthelastfour
yearsregardingfourknowledgebases(ACM,GoogleScholar,Scopus,andSpringer),as
Received:14October2024
Revised:17November2024 wellasallWebofSciencearticlesregardlessoftheirdateofpublication.Thisstudyemploys
Accepted:6December2024 ASReview,anopen-sourceapplicationthatusesactivelearningtohelpacademicsfilter
Published:7January2025 literatureefficiently. Thisstudyaimstoassesstheprogressachievedinthefieldofhybrid
Citation: Sabiri,B.;Khtira,A.;ElAsri, recommendersystemstoidentifyfrequentlyusedrecommenderapproaches,explorethe
B.;Rhanoui,M.HybridQuality-Based technicalcontext,highlightgapsintheexistingresearch,andpositionourfutureresearch
RecommenderSystems:ASystematic
inrelationtothecurrentstudies.
LiteratureReview.J.Imaging2025,11,
12. https://doi.org/10.3390/
Keywords: hybrid quality-based recommendations; strategy recommender systems;
jimaging11010012
systematicreview;bigdata
Copyright:©2025bytheauthors.
LicenseeMDPI,Basel,Switzerland.
Thisarticleisanopenaccessarticle
distributedunderthetermsand
1. Introduction
conditionsoftheCreativeCommons
Attribution(CCBY)license Based on extensive datasets, a recommender system is defined as any system that
(https://creativecommons.org/ generatespersonalizedsuggestionsasanoutputorhastheeffectofleadingtheuserto
licenses/by/4.0/).
J.Imaging2025,11,12 https://doi.org/10.3390/jimaging11010012

J.Imaging2025,11,12 2of66
interestingorhelpfulobjectsinabroadrangeofalternativeoptions. Inthecontextofbig
data,recommendersystemsareacrucialtoolforsharingknowledgeandassistingusersin
findingpertinentcontent.
1.1. CurrentLandscapeofE-Commerce
Propelledbysignificanttechnologyadvancements,thee-commerceindustrytodayis
markedbyagrowingrivalryamongplatformscompetingforuserattention[1,2].Asizable
fractionoftheworldwidepopulationcurrentlyshopsonline,andthee-commerceindustry
isonlyexpectedtoexpandmore. Correspondingly,consumerbehaviorisshiftingtoward
web-relatedactivitiessuchasonlinepurchasingandproductresearch.Withsomuchvariety,
e-commerceenterprisesmustdevelopinventivewaystoretainorattractcustomers. Inthis
context,robustrecommendationsystemsarecriticalforidentifyingdiverseformsofdata
andunderstandingconsumerpreferences. Increasingvolumesofdataandtechnological
improvementshaveturnedthefocustodataanalyticsasbusinessesnowvaluetheinsights
andhelpfulpatternsthatresultfromtheprocess. Inatypicalmarket,asmallpercentageof
loyalclientsaccountforaconsiderableportionofthefutureincome. Thisdemonstrates
the necessity of retaining high customer value and advancing potential customers up
theprofitchain. Prospectiveproductandserviceofferingsshouldeffectivelyappealto
consumerpreferences,helpingthemtoprogressuptheloyaltyladder. Socialmediaplay
an important role in e-commerce nowadays, and enormous volumes of data regarding
individualpreferencesarefrequentlypublicized. Theavailabilityofplatformsthatuse
variousmethodologiesindicateshowdiversifiedrecommendationsystemscontributeto
significantimprovementsinmoderne-commerce. Theissuesaheadaremostlyrelatedto
informationoverloadanderroneoussuggestionsacrossmultiplecategories. Thecurrent
situation requires the use of an effective hybrid recommender system to ensure correct
targetingofpotentialclients.
1.2. HybridRecommendationSystems: IndustryImpactsandApplications
Today,majorinternetbusinessessuchasAmazon,LinkedIn,Google,Facebook,Netflix,
Spotify,Microsoft,eBay,andAirbnbusehybridrecommendationalgorithms,whichhave
hadasignificantimpactontheglobaleconomy,socialsphere,anddigitalspace[3]. The
followingarespecificexamplesofstudiesandapplicationsthatdemonstratehowhybrid
recommendationsystemsareusedacrossseveralsectors:
• E-Commerce: Amazon’srecommendationenginehasahybridapproach,combining
collaborativefilteringwithcontent-basedfiltering. Forexample,theauthorsof[1]
foundthatAmazoncustomizesrecommendationsystemstoreflectcustomerhabits
andinterests,resultinginahuge35%boostinsalesvolumeontheironlineshopping
platform[4].
• Music Streaming: Spotify: Spotify combines user listening history (collaborative
filtering)withmusicalelementssuchasgenre,pace,andlyrics(content-basedfiltering).
Spotify’s“DiscoverWeekly”playlisthassuccessfullyleveragedthesestrategiesto
increaseuserengagementandsatisfaction,resultinginapersonalizedexperiencethat
retainsusers. Asdemonstratedbytheauthorsof[5],afterimplementingtheirmodel,
therateatwhichconsumersbegannewaudiobooksincreasedby46%.
• Online Video Platforms: Netflix’s recommendation algorithm uses collaborative
filtering,content-basedapproaches,andcontextualconsiderations(suchastimeof
dayanddevicetype). Collaborativefilteringdetectspatternsinuserviewingbehavior,
whereas content-based filtering suggests shows based on genre and theme. The
authorsof[6]discoveredthatthishybridstrategyimprovestheuserexperienceand
retentionratesbyprovidingtimelyandrelevantrecommendations.

J.Imaging2025,11,12 3of66
• YouTube: YouTube’srecommendationsystemisfundamentaltotheplatform,andit
wasmeticulouslyengineeredtooptimizeuserengagementandtimespentwatching
videos. Thesystemworksbyevaluatinguserinteractiondata,includingwatchhistory,
likes,comments,shares,andtheamountoftimespentondifferenttypesofcontent.
It learns from these interactions to create a more detailed picture of each viewer’s
preferences. Inadditiontoanalyzinguserbehavior,theprogramexaminescontent.
Thisincludesevaluatingmetadatasuchasvideotitles,descriptions,tags,andmore
complicatedaspectssuchasthetopic,style,andtoneofthecontent. Bymergingthese
data, the system detects trends and predicts what viewers are likely to watch and
appreciate. ThefinalobjectiveofYouTube’srecommendationalgorithmistopresent
eachviewerwithapersonalizedfeedthatwillkeeptheminterestedforlongertimes.
Byproposingcontentthatcloselymatchestheirinterests, YouTubeisabletoboost
viewers’viewingtime,whichbenefitsbothadvertisersandcontentproviderswhile
alsoguaranteeingthatconsumerscontinuetofindrelevant,engagingvideosonthesite.
Thiscycleofpersonalizedrecommendationsnotonlyimprovestheuserexperiencebut
alsopromotesYouTube’sstatusasatopcontentplatformbyencouraginglong-term
andrecurringuse.
• TravelandHospitality: Airbnb’srecommendationsystempersonalizeslistingsug-
gestionsbasedonuserinterests,demographics,andgeography.
• SocialMedia:
• Facebookemploysahybridalgorithmforfriendsuggestionsthatincorporates
userinteractions,mutualconnections,anddemographicinformation. Backstrom
etal. (2011)showedthatthismethodpromotesuserengagementbyfostering
moremeaningfulconnections.
• LinkedIn’sjobrecommendationengineincorporatesprofileinformation,user
behavior, and collaborative filtering. LinkedIn tailors job suggestions based
onuserdataandbehaviorsfromcomparableusers,increasingthejob-seeking
relevanceandimprovingtheprofessionalnetworkingexperience.
Thesesystemshavealsomadecontributionstotheissuesofinformationoverload,
userexperience,userdecision-making,andbusinesssales[7].
Regardlessofthegoalsofanyrecommendationtechnique,hybridrecommendersys-
tems(HRSs)combinetwoormoreofthemtoimprovetheforecastaccuracy[8–10]. Inthis
manner,thedrawbacksofeachmethodthatwouldarisefromusingthemseparatelycan
besomewhatmitigated[11,12]. Sinceadvancesintechnologyhavemadeitpossiblefor
individualsandbusinessestoacquireavastamountofinformationonanytopic,thefield
ofhumanresourcesystemshasbeenbecomingincreasinglyrelevant. Thistendencycan
berecognizedinseveralareas,includinge-learningsystems,digitallibraries,navigation
services, electronic enterprises, and news and publication suggestions. Hybrid recom-
mendersystemsintegrateseveralmodelstoreducetheshortcomingsofonemodelwith
another, lowering the overall disadvantages of using different models and resulting in
morecrediblesolutions.
The two primary categories of hybrid recommendation systems are collaborative-
filtering-basedandcontent-based. Whilecollaborative-filtering-basedsystemsrelyonuser
activity,content-basedsystemscreatesuggestionsbasedonthecharacteristicsofthethings
being recommended. Both categories can be used by hybrid recommender systems to
createamoresuccessfulrecommendationengine[13].
Onebenefitofhybridsystemsistheirabilitytoprovideusersmoreindividualized
recommendations. Theycanconsiderawiderrangeofcriteriawhenmakingsuggestions
by merging various models, which can produce more accurate and pertinent findings.

J.Imaging2025,11,12 4of66
However,becausehybridsystemssometimescombinemultiplerecommendationsystems,
theycanbemorecomplexandchallengingtoanalyze.
In technical terms, all recommendation systems generate suggestions using vari-
ous methodologies, such as collaborative filtering (CF), content-based filtering (CBF),
knowledge-basedfiltering(KBF),demographicfiltering(DF),andothers. Letusconsider
thespecificsofthesestrategies.
1. Content-BasedFiltering: TheCBFapproachisbasedonthenotionthatpeoplewho
havepreviouslyappreciatedproductswithcertaincharacteristicswouldcontinue
to enjoy similar items in the future. It examines item features to match them to
userprofilesandprovidesuggestions. Thisstrategyusescontentrepresentationand
comparisontechniquesfrominformationretrieval,aswellasclassificationalgorithms
from machine learning, to represent those items previously rated by the user and
comparethemtootheritemstoproposecomparableitems[3,14–16].
2. Collaborative Filtering: The CF approach works on the notion that people who
hadsimilarpreferencesinthepastwouldhavesimilaronesinthefuture. Themost
significantpartofcollaborativefilteringisdeterminingwhethertheuser’spreferences
match those of other users [17]. It entails people working together to help each
other filter information by documenting their emotions regarding the things they
encounter[3]. Tofindsimilaritiesintasteamonggroupsofpeople,CFusesratings
or user-generated comments. The commonalities between users are then used to
producerecommendations[2]. However,CFrecommendersencounterdifficulties
suchasthecold-startproblem(fornewusersorgoods)andthe“graysheep”problem
(userswhodonotfallintoanysingletastecluster) [3,14,18,19].
3. Utility-BasedFiltering: UBFisarecommendationapproachthatprovidesperson-
alizedrecommendationstousersbycalculatingtheutilityofeachitemfortheuser.
However,akeychallengeinthiscategoryliesindeterminingtheutilityvalueforeach
individualuser[20,21].
4. ContextualFiltering:Thissystemconsiderscontextualinformationsuchastime,loca-
tion,anddevicetodeliverrecommendationspertinenttotheuser’spresentposition.
Itcanimprovetheuserexperiencebytakingintoaccounttheexactenvironmentin
whichtherecommendationsarepresented[22,23].
5. Knowledge-BasedFiltering: TheKBFmethodsuggeststhingsbasedonclearuser
preferencesandneeds. Itconsidersinformationsuppliedbytheuser,suchasspecific
interests,desiredqualities,orlimitations,andrecommendsthingsthatmeetthose
requirements. Itdoesnotrelyprimarilyondemographicinformationbutinsteadon
user-specifiedchoices[24,25].
6. DemographicFilteringSystem: DFdeterminesusercategoriesbyemployingdemo-
graphicdatasuchasgender,educationalbackground,age,andsoon. Itdoesnothave
thenewuserissuebecauseitdoesnotuseratingstocreatesuggestions. However,due
tointernetprivacyconcerns,itisdifficulttoobtainenoughdemographicinformation
thatisnecessarytoday,limitingtheuseofDF.Itisstillusedinconjunctionwithother
recommendersasaquality-enforcingstrategy[26].
7. HybridRecommenderSystems: HRSsintegratevariousrecommendationmethods
tocreateamoreaccurateandpersonalizedrecommendationsystem. Bycombining
morethanonerecommendersystemapproach,hybridrecommendersystemsleverage
multiplesourcesofdataandalgorithmstoenhancethequalityofrecommendations.
Thegoalistoreinforcethebenefitsofeachstrategywhileminimizingtheirdownsides
or limitations, resulting in a more effective and comprehensive recommendation
approach[13,15,16,18,21,27–36].

J.Imaging2025,11,12 5of66
The goal of the study was to examine recently released HRS papers that focus on
e-commerceanddemonstratetheevolvingperspectivesofthesesystems,specificallytheir
types, approaches, algorithms, and implementations in detail. Our key findings and
contributionsmightbesummarizedasfollows:
- Datascarcityisamajorlimitingfactorintheperformanceofrecommendationsystems.
Thecurrentapproachestodealingwithcold-startconcernsfornewusersandobjects
frequentlyfailtoincorporatedemographicinformationintothesuggestionprocess.
Accordingtoresearch,theexistenceofcold-startusers,togetherwiththevolumeand
qualityofthesurroundingdatapointsusedintherecommendationframework,have
asubstantialimpactonpredictionaccuracy.
- The contribution provides a synthesis of the existing information and approaches
to hybrid-based quality in recommender systems via a thorough examination of
theliterature. Thisincludesexploring,evaluating,andcategorizingdiversehybrid
models,assessmentcriteria,andreal-worldimplementations,aswellasidentifying
theirstrengthsanddrawbacks.
- IdentifyingChallengesandOpportunities: Thereviewrecognizedandarticulatedthe
distinctproblemsandopportunitiesprovidedbybigdatainrecommendersystems.
Thisinvolvedunderstandingtheuniquecharacteristicsofbigdata,suchasvolume,
velocity,anddiversity,aswellastheimplicationsforhybridrecommendersystem
designandimplementation.
- ProposingFrameworksandRules: Drawingonthefindingsoftheliteraturereview,
thecontributionprovidedframeworks,architectures,orrulesfordesigningandeval-
uatinghybridrecommendersystemsinthecontextofbigdata. Theseframeworks
incorporatedbestpractices,addressedfrequenthazards,andproposedsolutionsfor
dealingwithbigdata’sdistinctcharacteristicsandrequirements,suchasscalability,
real-timeprocessing,anddataintegration.
- Domain-DrivenInsights: Thereviewinvestigatedtheuseofhybridrecommender
systemsinbigdatasituations. Itexaminedsuccessfulimplementationsine-commerce,
socialmedia,healthcare,IoT,andtheless-exploredareaoftalentpooloptimizationfor
recruitmentsolutions.
- Employinganopen-sourceprogram,ASReviewusesactivelearningtoimprovethe
systematicselectionprocessinresearch. Itefficientlyprocessesvastamountsoftext,
reducingthenumberofdocumentsthatmustbeexaminedbyhumansandeliminating
falsenegatives.
Thefollowingportionsoftheessayareorganizedasfollows. Section2providesthe
related work and background. The objectives and reasons for conducting a systematic
literaturereviewarepresentedinSection3. Section4describesthemethodologyforthe
reviewprocess,includingtheinformationsources,eligibilitycriteria,anddataextraction,
whileSection5coversthesynthesisoftheresultsanddiscussion. Section6bringsthepaper
toitsconclusion.
Theselectedpapersarepresentedattheendofthispaper(seeAppendixA).
2. BackgroundandRelatedWork
Theoverabundanceofirrelevantinformationfrequentlyresultsinasignificantinvest-
mentoftimeandresourcesinthesearchforusefulinformation,orpossiblytheinability
tolocatethenecessaryknowledgecompletely. Recommendationsystems(RSs)havebeen
created to address these difficulties. Their goal is to reduce these concerns by making
specificrecommendationsandsolutions.

J.Imaging2025,11,12 6of66
Theresearchin[37]emphasizesthevalueofalternateevaluationmetricsforrecom-
mendationsystems(RSs)intheclassifiedsarea,inadditiontotypicalaccuracymeasures.
Thekeymetricsthatwerediscussedincludethefollowing:
• Diversity: Assessesthediversityamongtherecommendations,whichiscriticalfor
providinguserswithawiderangeofoptionsandimprovingengagement. Thepaper
in[37]usesmeasuressuchastestcoverage,Shannonentropy,andtheGiniindexto
assessdiversity,withvalues0.74,10.40,and0.79,respectively. Greaterdiversityin
recommendationscouldofferconsumersadditionalchoices,potentiallyincreasing
userengagementandsatisfaction.
• Novelty: Determineshowsurprisingtherecommendationsare,whichhelpstokeep
usersinterestedbysuggestinggoodstheymaynothaveconsidered.
• UserSatisfaction: Assessesthetotaluserexperienceusingfeedbackandengagement
metrics to customize suggestions to user preferences. By adding these indicators,
HRSscanimprovetheirperformance,bettercorrespondwithuserneeds,andincrease
overallengagementandsatisfaction.
The success of recommender systems is measured using a range of metrics that
go beyond ordinary accuracy measures (accuracy, precision, recall, and F1-score). In
practicalimplementations,itiscriticaltoconnectthesemeasureswithuser-centricgoalsto
ensurethattherecommendationsnotonlyperformwellalgorithmicallybutalsoboostuser
happinessandengagement. Inadditiontothenewmetricsprovidedabove(seeSection2),
belowisathoroughstudyofthealternativemetricsusedtoevaluaterecommendersystems,
especiallyinreal-worldapplications. Thepapersin[38,39]covereddifferentcriteriafor
evaluatingtheefficacyoftheConformity-AwareMulti-Task(CAM2)modelinthecontext
ofsystemrecommendationsandscoringhotelsinthesuggestedrecommendationsystem.
1. AggregatedUserEngagement: Thisindicatormeasureshowengagedusersarewith
thesystem’srecommendedcontent. TheCAM2modelsignificantlyincreasedthis
measureby0.50%,demonstratingimproveduserinvolvementwiththeplatform[39].
2. DailyActiveUsers(DAUs): Thisindicatorcountsthenumberofuniqueuserswho
interact with the site each day. The CAM2 model led to a 0.21% rise in DAUs,
indicatingthatmoreusersarereturningtothesiteduetobettersuggestions[39].
3. RetentionMetrics: Renewalmetricsareusedtoassessthemodel’scapacitytoim-
proveuserexperienceandmotivatereturnvisits,particularlyamongcasualusers.The
model’sdesignpromotesbetterengagementandretentionamongcasualusers[39].
4. Reviews and Comments: The system evaluates customer reviews to measure
thoughtsandsentimentsabouthotels, whichassistsincreatingrecommendations
accordingtouserpreferences[38].
5. SurroundingEnvironments: ItconsiderssurroundingPointsofInterest(POIs)toas-
sessthefacilitiesaccessiblearoundthehotels,whichcanimpactauser’sdecision[38].
6. Numerical Ratings: The system integrates numerical ratings submitted by users,
servingasaquantifiableassessmentofhotelquality.
7. AggregatedScores: Thesuggestedsystemaggregatesscoresfrombothreviewsand
surroundingfacilities,enablingathoroughevaluationofeachhotel[38].
8. Polarity Ratings: The system creates polarity ratings from reviews using natural
languageprocessing(NLP)techniques,whichhelpstocomprehendthesentiments
representedinthereviews[38].
ThemaingoaloftheresearchbySivasankarietal.[40]istocreateahybridscientific
articlerecommendationsystemthatusestheCOOToptimizationalgorithmtoimprove
theaccuracyandrelevanceofarticlesuggestions. TheCOOToptimizationtechniqueisin-
tendedtoefficientlytraversethecitationgraphanddiscoverhighlyimportantpublications.

J.Imaging2025,11,12 7of66
Thestudyaddresseskeyissuesinrecommendationsystems,suchasthecold-startproblem
anduserinterestunpredictability,bycombiningcontent-andgraph-basedrecommenda-
tionalgorithms[40]. TheCOOToptimizationalgorithmisusedtoselectarticlesthatclosely
matchuserqueries,ensuringthatrecommendationsarehighlypersonalizedandmatched
to individual needs. The suggested strategy seeks to increase important performance
indicators,suchasprecision,recall,andmeanreciprocalrank(MRR),thusboostingthe
overalleffectivenessoftherecommendationsystem. Furthermore,thequalitativeresults
showthatprovidingmorerelevantanddiverserecommendationsincreasesuserhappiness,
demonstratingthesystem’seffectivenessinsatisfyingusers’particularneeds.
Thearticlein[41]discusseshowdifferentamountsofnoveltyandvarietyinrecom-
mendationalgorithmsaffectuserhappiness,algorithmperformance,andsystemaccuracy:
• ImpactofDiversificationonUserSatisfaction: Accordingtothestudy,usersatis-
faction is highest when recommendations have a balanced level of relevance and
diversity,especiallyadiversityscoreof0.6. Thisbalanceindicatesthatpeoplerespect
moderatelydiversifiedcontentintheirsuggestions[41].
• Relevance–DiversityTrade-Off: Oneimportantpointraisedistheinevitabletrade-off
betweenrelevanceanddiversity;asdiversitygrows,relevancefrequentlydeclines,
potentially affecting user experience. This tension is critical for recommendation
techniquesthattrytoenhancebothelementsconcurrently[41].
• AlgorithmPerformance: Algorithmsthatuseagreedy,marginalrelevancemaximiza-
tion (MMR) approach perform better in terms of diversity without compromising
toomuchrelevance. Adaptivealgorithmsthatmodifythetimingofdiversification
outperformedsimilarity-basedtechniques[41].
• EmpiricalComparisonsUsingMetrics: Thearticleexaminesalgorithmsbasedon
metrics such as ERR-IA and subtopic recall to assess relevance and variety. These
measurements,especiallywhenappliedtomoviegenres,provideacompletepicture
ofalgorithmeffectiveness[41].
Thestudyonthekernel-mapping-basedGroupRecommenderSystem(KGR)byGuo
et al. [42] aims to enhance recommender system performance by addressing cold-start
anddatasparsityissues. TheKGRmodelleveragesuser-trustrelationshipstoformuser
groups,mitigatingtheseproblems. Thestudyintroduceskernelmappingtechniquesto
create group kernels and matrices, enabling multilinear mapping between group–item
interactionsanduserpreferences. Ahybridmodelisproposedthatcombinesgroupand
individual user kernels, emphasizing individual preferences within groups. The KGR
model[42]isvalidatedontwotrust-baseddatasets,demonstratingeffectivenessthrough
RMSEmetrics. Optimalparametervaluesareidentifiedtofurtherimprovethemodel’s
performanceandreduceRMSEerrors. Thesestrategiescollectivelyenhancetheaccuracy
andeffectivenessofgrouprecommendationsintheKGRsystem.
The recommender system is a mechanism that helps users to make decisions in
complexinformationcontexts[3,14]. Intheworldofe-commerce, itisatoolthathelps
consumerstofindknowledgethatisrelevanttotheirinterestsandpreferences[29]. Italso
promotesthesocialprocessofrelyingonrecommendationsfromotherswhenpersonal
knowledgeorexperienceisinsufficient. Recommendersystemsaddresstheissueofinfor-
mationoverloadbymakingindividualizedandspecializedrecommendationsforcontent
andservices. Thesesystemshavebeendesignedusingavarietyofapproaches,including
collaborativefiltering,content-basedfiltering,andhybridfiltering[13,30]. Collaborative
filteringisthemostwidelyutilizedoftheseapproaches. Itrecognizespeoplewhoshare
similarlikesandrecommendsproductsbasedontheirassessments.
Collaborativefilteringhasbeenappliedinavarietyofsectors,includingnews-based
architectures,onlinesocialinformationfilteringsystems,ande-commerceplatformssuch

J.Imaging2025,11,12 8of66
as Amazon [43], Netflix [44], Spotify, YouTube, Facebook, news articles, and financial
services[27]. Ontheotherhand,content-basedfilteringassociatescontentresourceswith
userattributes,relyingonhumanknowledgeratherthantheopinionsofothers.
Bothcollaborative-andcontent-basedapproachesprovidenumerousbenefits,such
asbusinessadvantages,personalization,efficiency,anddiscovery. However,theyhave
somedisadvantages,includinglimitedcontentanalysis,privacyconcerns,alackofuser
control,overspecialization,datascarcity,cold-startchallenges,andscalabilitylimitations.
Toaddresstheserestrictions,hybridfilteringmethodshavebeenproposed[15]. Theseap-
proachesincorporatevariousfilteringstrategiestoimprovetheaccuracyandperformance
ofrecommendersystems[29]. Hybridfilteringapproachesareclassifiedaccordingtotheir
operations: weightedhybrid,mixedhybrid,switchinghybrid,feature-combinationhybrid,
cascadehybrid,feature-augmentedhybrid,andmeta-levelhybrid[24]. Currently,collabo-
rativefilteringandcontent-basedfilteringmethodsarewidelyused,eitherbycombining
theirpredictionsoraddingfeaturesfromonetechniqueintotheother[15,18,29,31–33,35].
In the study in [45], the authors investigated the several challenges of developing
an effective hybrid recommendation system for online purchasing. The key issues are
asfollows:
DefiningLexicalVariables: Thefuzzyexpertsystemuseslinguisticvariablestomodel
ambiguousnotions[45].
VariousApproaches: Thesystemincludescollaborativefiltering,content-basedtech-
niques,andafuzzyexpertsystem. Itcanbedifficulttobalancethesemanyapproachesand
guaranteethattheyfunctiontogethernicely,resultingininconsistenciesinideas[45].
EvaluatingPerformanceMetrics: Achievinggreatprecisionandrecalliscriticaltothe
system’sperformance. Thestudyaspiresforresultsabove90%,socomprehensivetesting
andvalidationagainstestablishedmethodologiesisrequiredtoensuredependabilityand
effectiveness[45].
UserChoiceManagement: Thesystemmustbeabletoreacttochanginguserprefer-
encesandbehaviors. Thisnecessitatesareliabletechniqueforcapturingandevaluating
useractivityregardingonlineshopping,whichcanbechallenginggiventhefastpaceof
customerinteractions[45].
Theprimarygoalofthestudyin[46]istoprovideahybridrecommendersystemde-
signedtoimprovetheselectivedisseminationoftheresearchresourcesinsideaTechnology
TransferOffice(TTO).Thepreciseobjectivesdescribedinthepaperarethefollowing:
ImprovingInformationDiscovery: ThesystemisintendedtoassistTTOpersonnel
andresearchersinquicklylocatingrelevantinformation,addressingtheissuescreatedby
theexpandingvolumeofavailableresearchmaterials[46].
PersonalizedSuggestions: Thegoalistoprovidetailoredsuggestionsbasedonuser
profiles,boostingtherelevancyoftheinformationsuppliedtousers[46].
FacilitatingCooperation: Thesystemisdesignedtodetectpossiblecooperationoppor-
tunitiesamongresearchers,henceencouragingtheformationofmultidisciplinaryteamsto
betterresearchoutputs.
Using Fuzzy Lexical Modeling: The article discusses the use of fuzzy linguistic
modelingtodescribequalitativeinformation,whichimprovesuser–systeminteractionand
thecompleteefficacyoftherecommendersystem[46].
Intherealmofrecommendationsystems,hybrid-basedqualityrecommendersystems
arebecomingincreasinglysignificant. Combiningseveralapproacheshasshownpromise
inraisingtheefficacyandaccuracyofrecommendationsinarangeoffields. Theincreasing
needforcustomizedrecommendationserviceswillsurelyrequiretheresearchanddevel-
opment of hybrid-based recommender systems, which will help to reduce information
overloadandprovideusersinsightfulsuggestions.

J.Imaging2025,11,12 9of66
Hybridrecommendationsystemsbasedonqualityconsiderbothuserpreferencesand
thequalityoftherecommendedgoodsatthesametime, combiningseveraltechniques
to deliver relevant recommendations [18]. With the goal of overcoming the drawbacks
ofsingle-strategytechniques,thesequality-awarehybridrecommendersystemsofferan
excitingevolutionintheindustry. Thesesystemscombineseveraltechniquestoprovide
moreaccurateandnuancedrecommendations.Thesetacticsincludecontent-basedfiltering,
whichfocusesonitemattributes,andcollaborativefiltering,whichleveragesthebehavior
andpreferencesofotherusers. Thesehybridsystems’capacitytomanagethecomplexity
anddiversityofuserpreferencesanditemcharacteristicsisoneoftheirmainadvantages.
Forinstance,ahybridapproachtomovieselectionmaytakeintoaccountboththeuser’s
favoritegenresandthefilms’criticalreception,guaranteeingthatonlywell-receivedfilms
arerecommended.
3. GoaloftheLiteratureReview
Systematic reviews use rigorous and transparent procedures to provide a full and
impartialappraisalofseveralrelevantstudiesinasingledocument. Asystematicreview’s
goal is to synthesize and summarize the current body of knowledge, with the goal of
uncovering all the relevant data relative to a certain subject. It is an additional area
of study that aims to locate, evaluate, and interpret all the available information from
primary studies that is relevant to a specific research issue. To guarantee a robust and
systematic literature review (SLR) approach, we followed the standards stated in the
CochraneHandbook[47]andthoseproposedbyKitchenhamandCharters[48,49]. These
criteria, which are widely accepted in the research community, provide a foundation
forconductingcomprehensiveandunbiasedassessments. Weaimedtoreducebiasand
ensurethereliabilityandvalidityofoursystematicreviewbyadheringtotheseestablished
principles(seeFigure1).
The overall goal is to assess the progress of hybrid recommender techniques and
proposepotentialtopicsforfurtherstudy. Theobjectivesaretoexaminethecurrenttrends
indifficulties,approaches,datasets,applicationareas,andassessmentmeasuresusinga
hybridapproach. Asystematicliteraturereviewisatime-consumingtaskthatrequiresthe
researchertodesigntheprotocol,adjustthesearchstring,filtertheresults,sometimesmore
thanathousandarticles,selectthosethatmeettheinclusioncriteria,andremovethosethat
donotmeettheexclusioncriteria. Followingthat,theresearchermaybegintostudythe
relevantresultsonebyone.
3.1. ReasonsforConductingSystematicLiteratureReviews
Asystematicliteraturereviewisperformedforavarietyofreasons[48]:
1. Summarizingtheexistingknowledgeandinformationconcerningresearchquestions
or technology, such as the empirical evidence on the benefits and limitations of a
specificagileapproach. Theyprovideacomprehensiveoverviewofwhatisknownin
thefield.
2. IdentifyingKnowledgeGaps: Systematicreviewscandiscoverknowledgegapsby
reviewingexistingmaterial. Thesegapscanassistresearchersinidentifyingplaces
wherefurtherstudyisrequired.
3. MakingChoicesBasedonProof: Systematicreviewsareanimportanttoolformaking
evidence-baseddecisions. Theyserveasafoundationformakingeducatedjudgments
inavarietyofdisciplines,includinghealthcare,education,andpolicycreation.
4. MinimizingBias: Systematicreviewslocateandchooserelevantresearchinasystem-
aticandaccessiblemanner. Thisdecreasesthepossibilityofbiasinstudyselection
andinterpretation,makingtheresultsmorecredible.

J.Imaging2025,11,12 10of66
5. BringingConflictingEvidenceTogether: Insomedomains,theliteraturemaypresent
contradictoryconclusions. Systematicreviewsseektosynthesizeandevaluatecontra-
dictorymaterialtopresentamorecompletepictureofthestateofknowledge.
6. PolicyandPracticeInsights: Systematicreviewsarefrequentlyusedtoinformpolicy
decisionsandclinicalpracticeguidelines. Theyprovideasolidevidenceframework
formakingrecommendationsandjudgmentswithsubstantialsocietalimplications.
7. TimeandResourceEfficiency: Conductingasystematicreviewmightbemoreeffi-
cient than beginning a new study, especially if the issue has previously been well
investigated. Byusingthecurrentresearch,itcansavetimeandresources.
8. Systematicreviewscanaidinthepreventionofduplicationofresearchefforts. Re-
searchers may assess what has previously been completed and concentrate their
attentiononareasthatrequirefreshinvestigation.
9. Establishing a Baseline: A systematic review can serve as a starting point for re-
searchers who are new to a topic, offering a baseline grasp of the present state of
knowledge. Systematicliteraturereviews,ontheotherhand,canbeusedtoassess
howmuchtheempiricaldatasupportsorcontradictsthetheoreticalassumptions,or
eventoaidinthedevelopmentofnewtheories.
Figure1.Thebasicstepsinconductingasystematicliteraturereview.
3.2. TheValueofSystematicLiteratureReviews
Thegoalofsystematicreviewsistosynthesizeavailableknowledgeinanequitableand
transparentmanner. Theyadheretoapresetsearchtechniquethatallowsthemtoanalyze

J.Imaging2025,11,12 11of66
thecompletenessofthesearch. Researchersperformingasystematicreviewmustseek
outandpublishfindingsthatbothsupportandcontradicttheirfavoredstudyhypothesis.
Systematicreviewsimprovetheintegrityandcredibilityoftheresearchprocessbyadhering
tothesestandards.
They are critical tools for advancing knowledge, influencing decision-making, and
guaranteeingtheuseofthebestavailableevidenceinavarietyofresearchandpracticesectors.
4. MethodologyforReviewProcess
ThePreferredReportingItemsforSystematicReviewsandMeta-Analyses(PRISMA)
guidelinescomprisedthemethodologyusedforthisinvestigation[50]. Severalrecommen-
dationtechniqueshavebeenproposedandappliedinthefieldofrecommendationsystems.
However,implementingthesetechniquesinthecontextofhybridrecommendationsys-
temsposesseveralchallengesandopportunitieswhileconsideringquality. Theprimary
objectiveofthisresearchistoexaminethecurrentandemergingapproachesappliedto
hybridrecommendationsystemsintherecentresearchliteratureandoutlineavenuesfor
futureresearch. Toensureasystematicreviewprocessasindicatedabove,wehaveadopted
the guidelines from [47,48]. The steps of our review process are illustrated in Figure 1.
Itinvolveseightmainsteps: researchquestionformulation,establishmentofsystematic
reviewprotocol,performinganextensiveliteraturesearch,screeningandselectingstudies,
examiningthebiasandqualityofthestudies,dataextraction,analyzingtheinformation
gathered,andsharingtheoutcomes(seeFigure1).
4.1. QuestionFormalization
Thefundamentalpurposeofthissystematicliteraturereviewistolearnwhatdiffi-
cultiesHRSscouldsuccessfullyhandle,howtheyarebuiltandevaluated,andhowthey
couldbeexperimentedwithintermsofmannerorfeatures[24,51,52]. Thus,thefollowing
researchquestions(seeTable1)weredeveloped:
Table1.SLR:researchquestions.
ResearchQuestions MotivationandProjectedResults
RQ1. What are the relevant studies on Identifyingchallengesconnectedtorecom-
hybrid recommenders, and how do hy- mendationsystems(DataSparsity,Model
bridizationtechniquessolvespecificdiffi- Bias,Overfitting,andDimensionalityRe-
cultiessuchascold-start,novelty,diversity, duction).
andusersatisfaction?
RQ2. Whatarethevarioushybridization Addresstheissuesthatcomewithdevelop-
strategiesthathavebeenemployedtoin- ingeffectivequalityrecommendersystems
crease the performance of quality recom- inasettingofmassiveamountsofdata.
mendersystemsinthecontextofbigdata?
RQ3. What types of data sources have To pinpoint contributions closely associ-
beenusedtoevaluatethetechniquesinre- atedwithusingrecommendationsystems
centlypublishedhybridrecommendation forproposinghousingalternatives.
systems?
RQ4. What experimental outcomes are To increase the overall performance and
generatedwhenhybridrecommendertech- efficacyofrecommendationsystems,espe-
niquesareused? ciallyinlarge-scale,complexdatacontexts.
RQ5. Whatisthesuggestedmethodology Identifytheproposedmethodsinhybrid
inhybridrecommendationsystems? quality-basedrecommendationsystems.
RQ6. Whatarethemostpromisingfuture Determine potential research directions
researchdirections? forimprovinghybridquality-basedrecom-
mendationsystems.

J.Imaging2025,11,12 12of66
Toaddresstheseresearchquestions,wegeneratedaresearchstringutilizingterms
relatedtoourtopic.
The primary keywords are hybrid, quality, recommender systems, dissemination,
information, and big data, and then we introduced synonyms to obtain the final list of
keywords,asshowninTable2.
Table2.Keywordsandsynonyms.
Keyword Synonyms
Hybrid Hybridization,Mixture,Mixed
System Systems,Approach,Software,Engine,Technology,Technique,Techniques
Recommender Recommendation
WeemployedBooleanoperatorsinoursystematicliteraturereviewsearchmethod.
Theseoperators,whichinclude“AND”and“OR”,areusedtoconnectalternativeterms.
Wecanclustersynonymousorrelatedphrasesbyusingthe“OR”operator,andwecan
merge distinct components inside the search string by using the “AND” operator. We
createdacomprehensiveandprecisesearchstringbyskillfullyapplyingtheseoperators,
allowingustohighlightrelevantstudiesandgathervaluableinsightsforourmethodical
assessment of the literature. Then, we used the selection strategy, which was based on
somecriticalfactorssuchastheyearofpublication,thelanguageofthepaper,andthetitle.
WerestrictedourresearchtoEnglishpapers. Inaddition,weconsideredthereputation
andvalidityofthejournals,aswellastherecentlypublishedpapers. Subsequently,we
reviewed each item and selected those that were relevant to the topic. As a result, the
selectionprocedureconsistsofthreemajorsteps: searching,paperandjournalfiltering,
andcontent-basedselection.
Consequently,weobtainedthestudystringillustratedinTable3.
Table3.Basicquery.
* BasicSearchString
((hybridORhybridizationORmixtureORmixed)AND“QualityBased”AND(recom-
menderORrecommendation)AND(systemORsystemsORapproachORsoftwareOR
engineORtechnologyORtechniqueORtechniques))OR((hybridORhybridization
ORmixtureORmixed)AND“QualityBased”AND(recommenderORrecommenda-
tion)AND(systemORsystemsORapproachORsoftwareORengineORtechnology
ORtechniqueORtechniques)ANDinformationAND“bigdata”)
4.2. DatabaseAnalysisandResearchMethodology
Researchers have studied hybrid recommender systems in many different studies.
Weexaminedthisresearchusingtheestablishedmethodofasystematicliteraturereview,
whichisbasedonthestate-of-the-artrecommendationsoutlinedabove.
Thisprotocol’sstepsareasfollows(seeFigure2):
1. Identifyingresearchquestions.
2. Previousresearchfindings.
3. Searchingdatabasesforrelevantresearchbasedonhypotheses.
4. Selectingdatabasedonpredefinedinclusionandexclusioncriteria.
5. Analyzingthecollecteddata.
6. Studyfindings.
7. Ideasforfurtherresearch.

J.Imaging2025,11,12 13of66
Figure2.Literaturereviewprocesstemplate.
Theinformationsourceschosenaremostprominentscientificdatabasesthathavebeen
usedforotherrelevantworksofindexedjournalsinJournalCitationReport(JCR)[3,7].
Thesedatasetsareasfollows:
1. Scopus:Thisdatabasemayacceptthecompletequeryandofferstheoptionstospecify
additional particular filters (see Table 4 for question formulation and Figure 3 for
yearlydistribution).
2. WebofScience: Whenconductingasystematicreview,employingWebofSciencehas
benefitslikethoroughcoverage,easyaccesstohigh-qualitycontent,citationtracking,
sophisticated search tools, effective bibliographic management, and collaboration
support. Usingtheseelements,systematicreviewscanbemademorethoroughand
rigorous, enabling researchers to efficiently find, assess, and synthesize pertinent
papers(seeFigure4).
3. SpringerLink: Tocomplywiththedownloadlimitof1000objectsimposedbythis
databaseforthecsvfile,filtersmustbeaddedtotheitemlist. Becausethecurrent
query returned 4068 items at that time, exceeding the allowed threshold, it was
critical to narrow the list. This can be accomplished by implementing filters that
considercriteriasuchaspublicationdate,discipline,language,andcontenttype. By
incorporatingthesefilters,wecouldeffectivelyreducetheitemlistwhilestilladhering
tothedownloadrestriction(seeFigure5fordistributionbyyear).
4. Google Scholar: To overcome the limitation of extracting Google Scholar search
results,weusedtheopen-sourcetool“Harzing’sPublishorPerish”forexportingthe
resultsinExcel(seeTable5). Thesearchprocessinthisdatabasepresentedadditional
challengeswhencomparedtootherdatabasesforthreemainreasons:
• IncompleteSearchString: GoogleScholardoesnotallowyoutodirectlyentera
completesearchstring. Asaresult,wehadtousethebasicsearchtooltoconduct
asearchthatwouldreturnresultsmatchingtheinitialsearchstring.
• DifficultyinSearch: GoogleScholar’ssearchfunctionalityismoreintricatethan
that of other databases, making it more difficult to obtain desired results. To
retrievetherelevantinformation,carefulnavigationandtheuseofappropriate
search techniques were required (see Figure 6). Infact, dueto the absence of

J.Imaging2025,11,12 14of66
resultsfromtheoriginalquery,wedecidedtocancelitinordertoaddressthis
issue. Initsplace,weshallinvestigateanalternativetechniquebyrunningthe
belowquery.
• However,usingthisspecificdatabasemadeitpossibletoinclude“graylitera-
ture”,includingproceedingsfromconferences.
5. ACMDigitalLibraryhttps://dl.acm.org/,accessdate: 10December2023Becauseof
theenormousquantityofpapers,wenarrowedoursearchtotheyears2020to2024
andfocusedonjournals(seeFigure7).
Figure3.Scopus:numberofarticlespublishedinthestudyareafrom2020to2024.
Table4.Scopus:thesearchstringkeywordswithfilters.
*Scopus: AdvancedSearchKeywords
((hybridORhybridizationORmixtureORmixed)AND“QualityBased”AND(recom-
menderORrecommendation)AND(systemORsystemsORapproachORsoftwareOR
engineORtechnologyORtechniqueORtechniques))OR((hybridORhybridizationOR
mixtureORmixed)AND“QualityBased”AND(recommenderORrecommendation)
AND(systemORsystemsORapproachORsoftwareORengineORtechnologyOR
techniqueORtechniques)ANDinformationAND“bigdata”)ANDPUBYEAR>2019
ANDPUBYEAR<2025AND(LIMIT-TO(OA,“all”))AND(LIMIT-TO(SUBJAREA,
“ENGI”)ORLIMIT-TO(SUBJAREA,“COMP”)ORLIMIT-TO(SUBJAREA,“BUSI”))
AND(LIMIT-TO(LANGUAGE,“English”))AND(LIMIT-TO(EXACTKEYWORD,“Ma-
chineLearning”))AND(LIMIT-TO(DOCTYPE,“ar”))

J.Imaging2025,11,12 15of66
Figure4. WebofScience:numberofarticlespublishedinthestudyarea.
Figure 5. Springer: number of articles published in the study area from 2020 to 2024 without
preview-onlycontent.

J.Imaging2025,11,12 16of66
Figure6.GoogleScholar:numberofarticlespublishedinthestudyareafrom2020to2024.
Figure7.ACMDigitalLibrary:numberofarticlespublishedinthestudyarea.

J.Imaging2025,11,12 17of66
Table5.GoogleScholar:thesearchstringkeywordswithfilters.
*GoogleScholar: AdvancedSearchKeywords
((hybridORhybridizationORmixtureORmixed)AND(recommenderORrecommen-
dation)AND(systemORsystemsORapproachORsoftwareORengineORtechnology
ORtechniqueORtechniques))OR((hybridORhybridizationORmixtureORmixed)
AND(recommenderORrecommendation)AND(systemORsystemsORapproachOR
softwareORengineORtechnologyORtechniqueORtechniques)ANDinformation)
4.3. EligibilityCriteria
Aspreviouslystated,thefundamentalgoalofasystematicreviewistocollectrelevant
techniquessuggestedwithinacertainfield. Toguaranteethatonlyrelevantarticlesare
keptduringthesearchprocess,theinclusionandexclusioncriteriaforaliteraturereview
mustbeproperlydefined[48,53].
Thespecifictraits,attributes,orcriteriathatareutilizedtodeterminewhetheragiven
studyorarticleshouldbeincludedinthereviewarereferredtoasinclusioncriteria(IC).
Exclusion criteria (EC), on the other hand, are the specific features, attributes, or
conditionsusedtodeterminewhichstudiesorpapersshouldberejectedduringthereview
process. Apaperisconsideredtobeeligibleifitmeetsthefollowingrequirements:
• IC1: Papersoffering hybridquality-basedrecommendersystems, algorithms, and
techniquesinthecontextofbigdata.
• IC2: Papersfromconferencesandjournalspublishedbetween2020and2024.
• IC3: Thepaperincorporatessearch-relevantkeywordswithinitstitleorabstract.
• IC4: Thepaperaddresseshybridrecommendationsystems.
• IC5: Thepaperaddressesatleastoneproblemofrecommendationorproposesatleast
onetechniqueofhybridization.
Theexclusioncriteriaarethefollowing:
• EC1: Thepublicationdateisearlierthan2020.
• EC2: ThepaperiswritteninalanguageotherthanEnglish.
• EC3: Thepaperisashortarticle,astandard,aposter,aneditorial,oratutorial.
• EC4: Thetitle,abstract,andkeywordsarenotrelevanttotheresearchtopic.
• EC5: Thepaperdoesnotdiscusshybridrecommendationsystems.
4.4. InformationSources
In accordance with review process Step 2 (see Figure 2), we ran the search string
throughthesearchenginesofsomedigitallibraries,yieldingatotalof5857preliminary
primary studies (see Table 6). This retrieval process was conducted at the start of 2024.
Thevaryingnumberofpublicationsobtainedfromdigitallibrariesisduetochangingthe
primary query (see Figure 8) of the search in certain databases that have a limit on the
numberofBooleanoperators,usingthird-partydataextractiontools,anddifferencesin
searchenginefilteringsettings.Wedevelopedasetofinclusion/exclusioncriteria,asshown
inSection4.3,tohelpusmakerationaldecisionsaboutwhichexploratoryinvestigation
topursuefurther. Theserequirementsserveasthefoundationforfocusingonthemost
relevantresearchthatalignswiththereview’saims. Duplicatepaperswereremoved,anda
coarseselectionphasefollowed. Giventheimpracticalityofprocessingallpublications,we
decidedtoincludejustjournalarticles,scientificarticles,andmachinelearningarticlesin
somedatabasesandallarticletypesinothers,excludingworkshoppresentations,review
reports,andgrayliterature,especiallyforScopusandSpringerdata,duetothenumber
returnedbythebasicquery(seeFigure8). Westartedbylookingatthetitle,publishing
type(conference,workshop,journal,etc.),andpublicationyear. Welookedattheabstract

J.Imaging2025,11,12 18of66
or other sections of each article in many situations to determine its relevance. Because
the goal of this review study is to focus on quality in a large data setting with hybrid
recommendersystems,wechosearticlesthatofferedmixedorblendedrecommendation
systemswhileavoidingthosethataddressedsinglerecommendationtechniquesordidnot
discussrecommendationsystemsatallinthecontextofbigdata.
Thefirstselectionprocess,alongwiththeapplicationofdate-relatedinclusionand
exclusion criteria, yielded a list of 3557 articles. Following that, we conducted a more
thoroughreviewandselectionofarticles,limitingourselvestospecificsortsofarticlesto
yield131articles. Followingthat,weconductedamorein-depthreviewandselectionof
thepapers,selectingonlyopen-accessarticles,toyield81articles. (seeFigure8). Thewhole
list,aswellaspublicationinformation,canbefoundinAppendixA.
AsindicatedinFigure8,thesestatisticsprovideanoverviewofthenumberofarticles
discoveredinmultipledatabasesandbasedonvarioussearchparameters,suchaspub-
licationdate,articletype(e.g.,journalarticles,openaccess,etc.),andspecifictopic(e.g.,
science,machinelearning,andEnglish). Thesedatawillbeusedtorefineoursearchor
analyzetherelevancyoftheresultsbasedonourindividualresearchobjectives.
Here is an interpretation of the numbers indicating the articles found in various
databasesandusingvarioussearchcriteria:
1. PreliminaryResearchFindings(seeFigure8):
•Totalarticlesfoundinthepreliminaryresearch: 5857articles.
2. ACM:
•TotalarticlesfoundintheACMdatabase: 376articles.
•Articlesfrom2020orlaterintheACMdatabase: 187articles.
•Totaljournalarticlesfound: 33articles.
•Totalopen-accessarticlesfound: 19articles.
3. GoogleScholar:
•TotalarticlesfoundonGoogleScholar: 55articles.
•Articlesfrom2020orlateronGoogleScholar: 13articles.
•TotalarticlesofalltypesonGoogleScholar: 13articles.
•Open-accessarticlesonGoogleScholar: 6articles.
4. Scopus:
•TotalarticlesfoundinScopuswithbasicquerystring: 1348articles.
•Articlesfrom2020orlaterinScopus: 838articles.
•Totalarticleswithrestrictions(English,engineering,ML,business,etc.): 28articles.
•Open-accessarticlesinScopus: 14articles.
5. Springer:
•TotalarticlesfoundinSpringer: 4068articles.
•Articlesfrom2020orlaterinSpringer: 2509articles.
•ArticlesrelatedtoscienceinSpringer: 32articles.
•Open-accessarticlesinSpringer: 32articles.
6. WebofScience:
•TotalarticlesfoundonWebofScience: 10articles.
•ArticlesfromvariousdatesinWebofScience: 10articles.
•TotalarticlesofalltypesinWebofScience: 10articles.

J.Imaging2025,11,12
19of66
Preliminaryresearch
findings=5857
|     |     | Google |     | Scopus |     | Spinger |     | Webof |
| --- | --- | ------ | --- | ------ | --- | ------- | --- | ----- |
ACM=376
|            | Scholar=55 |       |     | =1348      |     | =4068 |       | science=10 |
| ---------- | ---------- | ----- | --- | ---------- | --- | ----- | ----- | ---------- |
| Date ≥2020 | Date       | ≥2020 |     | Date ≥2020 |     | Date  | ≥2020 | Alldates   |
| =187       |            | =13   |     | =838       |     | =2509 |       | =10        |
| Journals   | AllTypes   |       |     | (En,ML,B)  |     |       |       | AllTypes   |
science
| =33        |            | =13 |                | =43       |     | Articles=32 |     | =10        |
| ---------- | ---------- | --- | -------------- | --------- | --- | ----------- | --- | ---------- |
| OpenAccess | OpenAccess |     | Art,OpenAccess |           |     | OpenAccess  |     | OpenAccess |
| orFree=19  | orFree=6   |     |                | orFree=14 |     | orFree=32   |     | orFree=10  |
Figure8.Dataselectionmethods.
Table6.Disseminationofpaperssourcedfromacademicdatabases.
Database
|     |     | Retrieval |     | PreliminaryRemoval |     |     | Second-LevelSelection |     |
| --- | --- | --------- | --- | ------------------ | --- | --- | --------------------- | --- |
Source
| ACM           |     | 376  |     |     | 187  |     |     | 19  |
| ------------- | --- | ---- | --- | --- | ---- | --- | --- | --- |
| GoogleScholar |     | 55   |     |     | 13   |     |     | 6   |
| Scopus        |     | 1348 |     |     | 838  |     |     | 14  |
| Springer      |     | 4068 |     |     | 2509 |     |     | 32  |
| WebofScience  |     | 10   |     |     | 10   |     |     | 10  |
Total
4.5. DataExtraction
Atthispoint,everystudythatwaspartofthesystematicreviewhadbeenlocated,
andweneedtomoveontoextractingthedata. Atemplatecanbeusedtogatherthedata
neededtoanalyzethestudies. Standarddocumentsareavailableforthispurpose,such
asthePreferredReportingItemsforSystematicReviewsandMeta-Analyses(PRISMA)
Statement [54]andtheCochranedatacollectionformforinterventionreview[55]. These
formscanbeutilizedinthetrainingandeducationsciences,andanalystscanmodifyand
testtheminaccordancewiththegoalsofthesystematicreview.
Duringthisphase,wedesignedacustomizedformwitharangeofparameterssuch
astitle,author,year,andsoon[48]. Theformwasthenfilledoutwithinformationabout
theresearchtopicsforalltheselectedpapers. Table7containsalistoftheseattributes. The
purposeofthisoperationwastocollectandsynthesizedatatoanswerthedefinedresearch
questions. Theextracteddatawerelistedinthefirstcolumn,anexplanationforsomeof
theextracteddatathatmayappearambiguousisprovidedinthesecondcolumn,andthe
researchquestiontowhichthedataareconnectedisprovidedinthethirdcolumn(see
Table7).

J.Imaging2025,11,12
20of66
Table7.Formforextractingdata.
|     | ExtractedData     |     | Explanation                      |     |     | RQ      |     |
| --- | ----------------- | --- | -------------------------------- | --- | --- | ------- | --- |
|     | Title             |     | Thenameofthearticle              |     |     | RQ1     |     |
|     | Authors           |     | -                                |     |     | -       |     |
|     | Description       |     | Briefoverviewofthepaper’scontent |     |     | -       |     |
|     | Publicationyear   |     |                                  |     |     | RQ1     |     |
|     | Source            |     | Sourceofdigitallibraryaccess     |     |     | RQ3     |     |
|     | Publisher         |     | -                                |     |     | -       |     |
|     | Applicationdomain |     | Applicationdomainofthestudy      |     |     | -       |     |
|     | Approach          |     | Methodologyemployed              |     |     | RQ2,RQ5 |     |
|     | Contribution      |     | Researchwork’ssignificance       |     |     | -       |     |
Evaluationmethodology Approachtoevaluatingtherecommendersystem RQ6
|     | Dataset    |     | Datarepository              |     |     | RQ4 |     |
| --- | ---------- | --- | --------------------------- | --- | --- | --- | --- |
|     | Experiment |     | Explanationoftheexperiment  |     |     | RQ4 |     |
|     | Futurework |     | Proposedfutureresearchareas |     |     | RQ6 |     |
5. PRISMAChecklist
The PRISMA Checklist is a tool used mostly in the field of health and research to
assessthequalityofstudiesandreports(seeTable8). Theterm“PRISMA”referstothe
abbreviation“PreferredReportingItemsforSystematicReviewsandMeta-Analyses”.
Table8.PRISMA2020Checklist.
| Section/Topic | # Item |     |     |     |     | Page Where | the |
| ------------- | ------ | --- | --- | --- | --- | ---------- | --- |
ItemIsReported
TITLE
Title 1 Thisreportdescribesasystematicreviewconductedinaccor- 1
|     | dancewithPRISMAguidelines. |     |     | Thegoalofthisreviewwas |     |     |     |
| --- | -------------------------- | --- | --- | ---------------------- | --- | --- | --- |
tosummarizetheevidenceonhybridrecommendersystems.
ABSTRACT
Abstract 2 Systematic reviews use rigorous methodologies to provide 1,8,19,36
|     | a thorough | assessment | of relevant | studies while     | combining |     |     |
| --- | ---------- | ---------- | ----------- | ----------------- | --------- | --- | --- |
|     | existing   | knowledge  | on specific | issues. Following | the stan- |     |     |
dardsintheCochraneHandbook,Kitchenham,andCharters
|     | ensurestransparencyandquality. |     |     | Thispaperalsoevaluates |     |     |     |
| --- | ------------------------------ | --- | --- | ---------------------- | --- | --- | --- |
hybridrecommendationsystems,emphasizingtheirexpand-
ingimportanceandpotentialfutureresearchavenues,suchas
incorporatingcontextualinformationandenhancingscalabil-
|     | itywithsophisticatedalgorithms. |     |     | Astrongemphasisisplaced |     |     |     |
| --- | ------------------------------- | --- | --- | ----------------------- | --- | --- | --- |
ontheeffectivenessofmachinelearninginfilteringrelevant
materialonthesesystems.

J.Imaging2025,11,12
21of66
Table8.Cont.
| Section/Topic | # Item |     |     |     |     |     |     | Page Where | the |
| ------------- | ------ | --- | --- | --- | --- | --- | --- | ---------- | --- |
ItemIsReported
INTRODUCTION
Rationale 3 Thereviewofhybridrecommendationsystemsdiscussestheir 2,3,4,45–66
increasingimportanceinprovidingindividualizeduserexpe-
|     | rienceswhileovercomingtheconstraintsofoldermethods. |     |     |     |     |     |     | It  |     |
| --- | --------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- |
seekstoidentifybestpractices,emergingtrends,andfuture
researchdirectionsthatwillimprovetheeffectivenessandflex-
ibilityofthesesystems.
Objectives 4 Thepaperattemptstoconsolidateexistingknowledgeonhy- 3,4,45–66
|     | brid recommendation                  |     | systems, | identify | best              | practices, | and |     |     |
| --- | ------------------------------------ | --- | -------- | -------- | ----------------- | ---------- | --- | --- | --- |
|     | assessemergingmachinelearningtrends. |     |          |          | Italsoaimstoiden- |            |     |     |     |
tifyresearchgaps,presentaconsistentevaluationsystem,and
guidepracticalapplicationstoimproveuserexperiences.
METHODS
EligibilityCriteria 5 IC1: Papersofferinghybridquality-basedrecommendersys- 16
tems,algorithms,andtechniquesinthecontextofbigdata.
IC2: Papersfromconferencesandjournalspublishedbetween
2020and2024.
IC3: Thepaperincorporatessearch-relevantkeywordswithin
itstitleorabstract.
IC4: Thepaperaddresseshybridrecommendationsystems.
IC5: Thepaperaddressesatleastoneproblemofrecommen-
dationorproposesatleastonetechniqueofhybridization.
EC1: Thepublicationdateisearlierthan2020.
EC2: ThepaperiswritteninalanguageotherthanEnglish.
|     | EC3: The | paper is | a short | article, a | standard, | a poster, | an  |     |     |
| --- | -------- | -------- | ------- | ---------- | --------- | --------- | --- | --- | --- |
editorial,oratutorial.
EC4: Thetitle,abstract,andkeywordsarenotrelevanttothe
researchtopic.
|     | EC5: The | paper does | not | discuss hybrid | recommendation |     |     |     |     |
| --- | -------- | ---------- | --- | -------------- | -------------- | --- | --- | --- | --- |
systems.
InformationSources 6 Usingspecificsearchkeywords,wesearchedScopus,ACM, 17,18
WebofScience,Springer,andGoogleScholar.
SearchStrategy 7 Scopus’searchmethodincludedemployingspecifictermssuch 12,14,18
as“HybridQualityBasedRecommenderSystems”,“Informa-
|     | tion”, and | “Big Data”, | paired | with Boolean |     | operators. | The |     |     |
| --- | ---------- | ----------- | ------ | ------------ | --- | ---------- | --- | --- | --- |
searchwasrestrictedtopublicationspublishedfrom2020to
early2024,withemphasisonrelevantsubjectareasanddocu-
menttypes.
SelectionProcess 8 Twoindependentreviewersfirstchoosetitlesandabstracts, 10–20,28
|     | thenanalyzethecompletetextoftheselectedresearch. |              |         |                  |           |               | Any      |     |     |
| --- | ------------------------------------------------ | ------------ | ------- | ---------------- | --------- | ------------- | -------- | --- | --- |
|     | disagreements                                    | were         | handled | through          | consensus | on            | articles |     |     |
|     | that were                                        | not retained | by      | the two authors. |           | An additional |          |     |     |
perspectivewasgainedutilizingtheASReviewtooltoensure
acomprehensiveandimpartialselectionprocess.

J.Imaging2025,11,12 22of66
Table8.Cont.
Section/Topic # Item Page Where the
ItemIsReported
DataCollectionProcess 9 Weensuredvaliditybyconductingadoubleextractionprocess 17–20
byindependentreviewersaftergoingthroughtheentiretext
oftheincludedarticlestomethodicallyextractandsummarize
thedatainastandardizedtableformattomakecomparisons
easier. Choosingthepertinentdatapoints,constructingand
testingtheextractiontable,checkingthegathereddataformis-
takes,and,ifrequired,updatingandpilottestingtheapproach
areallpartofthisprocess.
DataItems 10 Data extraction was utilized to look for factors such as the 45–66
study’s subject, strategy, sample size, demographic charac-
teristics,objectives,datagatheringtechniques,andoutcomes.
Thesefactorsenableacomprehensiveexaminationandcom-
parisonofstudies.
RiskofBiasAssessment 11 WeevaluatedtheriskofbiasusingtheCochraneRiskofBias 37–38
Tool,whichincludedindependentreviewsbytworeviewers
andanopen-sourceapplication. Discrepancieswereresolved
collectively,andtheoutcomeswerethoroughlydocumented
foranalysis.
EffectMeasures 12 CommonlyUsedPrincipalSummaryMeasures(Precision,re- 35–36,41
call,andF1-score).
SynthesisofResults 13 Asystematicliteraturestudyforhybridrecommendersystems 24–45
beginswithdataextraction,whichisorganizedandstandard-
ized,followedbymethodcategorizationandstatisticalevalua-
tionsofperformancemeasures. Meta-analysis,visualization
tools,andthematicsynthesisareusedtocombineandunder-
standfindingsfrommultiplestudies.
ReportingBiases 14 Describeanymethodsusedtoassesstheriskofbiasdueto 38,39
selectivereporting.
CertaintyAssessment 15 The assessment of evidence certainty, which takes into ac- 18,19,32,35
count study quality, bias risk, and consistency, guarantees
solidresultsandconformitytoqualityandtransparencyre-
quirements.
RESULTS
StudySelection 16 Present the number of studies screened, assessed, and in- 25,35,40
cluded,withreasonsforexclusions.
StudyCharacteristics 17 Foreachincludedstudy,presentcharacteristics(e.g.,partici- 45–66
pantsandinterventions).
RiskofBiasinStudies 18 Presentriskofbiasjudgmentsforeachincludedstudy. 38,39
ResultsofIndividualStud- 19 Foralloutcomesconsidered,presenttheresultsofeachstudy. 37–38
ies
SynthesisofResults 20 Present results of syntheses (e.g., meta-analyses), including 45–66
confidenceintervals.
ReportingBiases 21 Reportonthepresenceofanyselectivereporting.
CertaintyofEvidence 22 Presentanassessmentofthecertainty(e.g.,GRADE). 18,19,32,35
DISCUSSION
SummaryofEvidence 23 Summarizethemainfindings,includingthestrengthofevi- 4,6,7,36,38
dence.

J.Imaging2025,11,12 23of66
Table8.Cont.
Section/Topic # Item Page Where the
ItemIsReported
Limitations 24 Discusslimitationsoftheevidenceandthereviewprocess. 15,18,19,38,39
Conclusions 25 Provideageneralinterpretationoftheresultsinthecontextof 10,12,37,38,42,44
otherevidence.
FUNDING
Funding 26 Describesourcesoffundingandothersupportforthereview. NotAvailable
5.1. MainObjectives
• Transparency: Ensurethatsystematicstudiesandmeta-analysesarepresentedclearly
andcompletely.
• Quality: Improve the quality of research reports to facilitate understanding and
evaluation.
• Standardization: Provideastandardizedframeworkforresearcherstofollowwhile
writingtheirwork.
5.2. Components
ThePRISMAChecklistoftenincludesalistofimportantcriteriatofollow, suchas
thefollowing:
1. Thedefinitionofresearchobjectives.
2. Themethodologyforselectingstudies.
3. Evaluationofbias.
4. Thesynthesisofresults.
5.3. Utilization
Researchersusethischecklisttoensurethattheycoverallthenecessaryaspectswhile
writing their studies, which contributes to better research valorization and use in the
scientificenvironment.
6. ResultsSynthesisandDiscussion
In this section, we provide the findings from the selected studies, addressing the
researchquestions(seeSection4.1)byanalyzingcategorizedchallenges,procedures,hy-
bridizationclasses,andevaluationmethodologies. Theinvestigationshighlightavariety
ofconcerns,includinginformationoverload,suggestionaccuracy,andsystemscalability,
all of which offer substantial hurdles for e-commerce recommendation systems. These
identifiedconcernsinformourinvestigationofpotentialapproachesforovercomingthem.
Toaddress theseissues, theresearchapplies toavarietyof recommendationstrategies,
includingcollaborativefiltering,content-basedalgorithms,anddeeplearningapproaches.
Eachstrategyisdesignedtoaddressacertainneed,suchasincreasingcustomizationor
loweringcomputationaldemands. Thisdiversityemphasizesthenecessityofusingthe
properstrategyforeachindividualchallenge,andexamplesfromtheresearchshowtheir
successinvariousaspectsofe-commerce.
Weassessedthenumerouspapersthatwedeemedrelevantforourevaluationfrom
variousangles.
Weusedexamplesfromtheincludedresearchtoshowthevariouskindsofproblems,
strategies,hybridizationclasses,assessmentmethodologies,andsoon.

J.Imaging2025,11,12 24of66
6.1. QuantitativeEvaluation
This part examined the screened papers in the hybrid recommender systems, con-
centratingsolelyonthreetypesofmetadata: database,yearofpublication,andinforma-
tionsources. Toaddresstheseissues,theresearchappliesavarietyofrecommendation
strategies,includingcollaborativefiltering,content-basedalgorithms,anddeeplearning
approaches. Eachstrategyisdesignedtoaddressacertainneed,suchasincreasingcus-
tomizationorloweringcomputationaldemands. Thisdiversityemphasizesthenecessity
ofusingtheproperstrategyforeachindividualchallenge,andexamplesfromtheresearch
showtheirsuccessinvariouse-commercecontexts.
6.1.1. DataOrigin
ThepercentageofpapersineachdatabaseisshowninFigure9a. Wefoundnineteen
papersintheACMdatabase(24%), sixpapersinGoogleScholar(7%), fourteenpapers
in Scopus (17%), thirty-two papers in Spinger (40%), and ten papers in Web of Science
(12%). Withapercentageof40%,weobservethatSpringerofferstherepositorywiththe
highestquantityofpapers. Springer’sextensivecollectionmaybedueinlargeparttothe
company’slengthyhistory,well-establishedreputation,andfameinacademicpublishing.
(a) (b)
Figure9. Articlecountsforthedistributionofacademicpaperdatabases. (a)Ratioofarticlesvs.
database.(b)Academicpaperdatabasespread.
6.1.2. YearofPublishing
As previously mentioned, the research was carried out for the period 2020 to the
beginning2024excludingWebofScienceandScopus,whichincludedatafromalldates
(untilthebeginningof2024). ThediagrampresentedinFigure9bshowsthenumberof
papersbyyearofpublication.
Additionally,thepiechartinFigure9brevealsthatthecurrentyearhasthefewest
articles. This outcome is understandable given that the data were taken at the start of
2024. Thetimingundoubtedlyaddstothelowerfigureasitdoesnotaccountforpossible
publicationsthatmayappearlaterintheyear.
BelowisaPRISMAflowchartthatillustratestheinclusionandexclusionstrategies
usedinthestudy(seeFigure10). Thisflowchartwaschosenforthisstudy, describing
theflowofinformationthroughthevariousphasesofasystematicreview. Itshowsthe
numberofrecordsidentified,includedandexcluded,aswellasthereasonsforexclusions.
This section focuses on the four inclusion and exclusion stages of the PRISMA table:
identification,selection,eligibility,andinclusion. Thesearchengineresultsfromthefive
databases(ACM,GoogleScholar,Scopus,Springer,andWebofScience)yieldedatotalof

J.Imaging2025,11,12 25of66
5857articles.Morethan2300publicationswereeliminatedbecausetheydidnotcorrespond
tothetimerangesetoverthepast4yearsfordatabasesthatreturnmanyarticlesandover
thepast10yearsforthosethatreturnfew. Forcertaindatabases,suchasScopus,which
areveryconsistent,welimitedthesearchtojournal,computerscience,machinelearning,
and business and management articles in order to reduce the scope of this study. We
obtainedone-hundred-thirty-onedocuments. Wetheneliminatedfiftypublicationsdueto
alackoffulltext,fourarticlesduetoredundancy,andtwenty-fiveothersbecausetheydid
notcorrespondtothesubject’srelevancebasedontheirtitles,keywords,orabstracts,or
becausetheydidnotmeettheeligibilitycriteria,eitherbecausetheirtextwasnotdirectly
relatedtoourfieldofresearchorbecausetheircontentlackeddetailandprecision,resulting
infifty-twodocumentsattheend.
Theinteractionoftechnologyimprovementsandpublishingpatternsinhybridrec-
ommendersystemsdemonstrateshowfast-changingtoolsandapproachescaninfluence
researchpaths. Asneuralnetworkarchitecturesevolve,transformermodelsgainpopular-
ity,andprivacyconcernsgrow,researchersrespondwithnovelanswersandtechniques.
Thesevariablesnotonlyexplaintheincreaseinpublicationnumbersbutalsoindicatea
dynamicareathatisevolvingtomeetthedemandsofthecurrenttechnologyandsocietal
needs. The number of articles on recommender systems over time shows a significant
trend(seeFigure11). ThisgraphdepictsthevaluesaftermakingvariousPRISMAanalysis
selections, particularlytheinclusionandexclusioncriteria. Severalsignificantpatterns
emergefromthepublicationtrendsovertime,reflectingtheevolutionofstudyinterestin
hybridrecommendersystemsandassociatedtechnologies. Startingwithmodestresearch
productionintheearlyyears,suchas2004,2008,2012,and2018,withonlyonepublication
ineachoftheseyears,itisobviousthatthetopicwasinitsearlystagesorgarneredlittle
attentionduringthistime. Evidently,thefieldwasstillinitsearlystagesofdevelopment,
whichcouldbeexplainedbyalackoffundingandinterest.However,2020wasawatershed
moment, with the number of papers jumping to seven, indicating increased interest or
developmentsinthefield. Thisrisingtrendcontinuedinto2021,whenthecountincreased
toeightitems,thensurgedagainin2022,reachingfifteen.
In 2023, the total rose slightly to sixteen, indicating a continued rise in research
production. Thisconsistentriseinrecentyearsindicatesagrowingrecognitionofthevalue
andrelevanceofrecommendersystemsinacademicdiscourse. Theserapidincreasescan
beattributedtotheemergenceofdeeplearningtechniques,whichenabledtheintegration
of complex data representations into recommendation models, as well as the frequent
adoption of cloud computing and technologies for big data, which made it easier to
managelarge-scale,multifaceteddata. Thefocusoftheacademiccommunityonenhancing
userexperience,combinedwiththeindustry’squestformorepersonalizedandadaptive
recommendationengines,arelikelytohavefueledthisdevelopment. Usingtransformer
modelscouldpotentiallyhelptohastenthisadvancement. Theintroductionoftransformer
models was a significant milestone in natural language processing (NLP) as well. The
findingsshowthatscholarsareincreasinglyinterestedinthisareaowingtoitspractical
applicationsandtheoreticalsignificance. Astheresearchinthisareaprogresses,itiscritical
tomonitorthesetrendsinordertounderstandthechangingenvironmentofrecommender
systems. Overall,thistendencyimpliesthatavibrantanddynamicfieldisgainingtraction
withintheacademiccommunity.

J.Imaging2025,11,12 26of66
Figure 10. The research approach employed: diagram of the PRISMA process for inclusion
andexclusion.
Figure 11 and the pie chart in Figure 9b show that the current year has the fewest
number of articles. This development is expected given that the data were collected at
thebeginningof2024. Thetimeofdatacollectionmostcertainlyinfluencedtheoutcome,
resultinginfewerpublicationsbeingavailablethisyear.Theearlycollectionperioddoesnot
accuratelyreflectthepossibilitiesforpublicationthroughouttheyear.Thisunderstandingis
criticalforappropriatelyanalyzingthedata.Thefiguresemphasizetheseasonalityofarticle
creation. Asaresult,thecurrentfiguresshouldbeconsideredinlightoftheirchronology.
Overall,thefindingspointtoatransientdipratherthanalong-termdeterioration. Future
analysismayprovideamorecompletepicturewhenadditionalarticlesarereleased. Given
the observed patterns in the publication numbers, it is critical to investigate how key
technological advancements influenced the landscape of hybrid recommender system

J.Imaging2025,11,12 27of66
research. Advancementsinneuralnetworkdesigns,theadoptionoftransformermodels,
andtheincreasedemphasisonprivacy-preservingstrategieshavealllikelyhadasignificant
impactonthepublicationtrends. Wewillexamineeachoftheseelementsindepth:
Figure11.Spreadofresearchbasedonthepublicationyearofchosenpapers.
1. AdvancesinNeuralNetworkArchitectures: Recentyearshavewitnessedtremen-
dousadvancesinneuralnetworktopologies, whichhavetransformedthefieldof
machineLearningand,byextension,recommendersystems.
• Deep LearningTechniques: Thedevelopment andrefinementof deeplearn-
ingapproacheshaveenabledacademicstodevelopmoresophisticatedmodels
capableofprocessingcomplexdatainputs. Thesedevelopmentsenablebetter
representationlearning,inwhichmodelscanautomaticallyrecognizepatterns
andfeaturesinrawdata,resultinginhigherrecommendationaccuracy.
• HybridApproaches: Themergingofseveralneuralnetworkarchitectures,such
asconvolutionalneuralnetworks(CNNs)forimagedataandrecurrentneural
networks (RNNs) for sequential data, has aided in the creation of hybrid rec-
ommendersystemsthatcanusenumerousdatasources. Thisflexibilityismost
certainlyamajorcontributortothecurrentincreaseinpublicationrates.
2. AdoptionofTransformerModels: Transformermodelshaveusheredinaneweraof
naturallanguageprocessing(NLP)andbeyond.
• Transformer Architecture: Transformers, introduced through models such
asBERTandGPT,haveraisedthebarforcomprehendingandcreatinghu-
man language. Their capacity to capture long-term dependencies in data
makes them ideal for jobs involving user interactions and preferences in
recommendationsystems.
• ImpactonRecommendations: Thepotentialtomoreeffectivelysimulateuser
behaviorandpreferenceswithtransformershaspromptedstudyintotheiruse
in recommender systems. This has most likely led to the rise in publications

J.Imaging2025,11,12 28of66
as academics investigate creative ways to integrate transformers into hybrid
models,increasingtheireffectivenessacrossmanydomains.
To obtain a second opinion on this study, we used Active Learning for Systematic
Reviews(ASReview)asasecondaryreviewertoidentifytherelevantarticles [56]. This
toolisamachinelearningsoftwarethatimplementsdifferentmachinelearningalgorithms
thatinteractivelyquerytheresearcher(seeFigure12). Itenablesthesystematicreviewof
articlesandanalysisofmetadata. ASReviewcouldsignificantlyimprovetheefficiencyand
relevanceofthesystematicliteraturereviewprocess. ASReviewallowstheusertosort
documentswhiletheactivelearningalgorithm(NaïveBayesbydefault)ranksunlabeled
documentsinthebackground,frommostrelevanttoleastrelevant.
Itissometimesviewedasatoolforselectingtitlesandabstractsinsystematicreviews
or meta-analyses, but it can handle any type of textual data that needs to be selected
systematically.
Using the AI tool “ASReview” required multiple steps [57]. Before screening, the
softwarerequiredtrainingforitsalgorithmwithmultipleprelabelledpapers. TheAItool
thenofferedthearticlewiththegreatestchancetoberelevantusingaresearcher-in-the-loop
approach. Thereviewerthendeterminedtherelevanceofeachrecommendedarticle. This
procedurewasrepeateduntilthestoppingrequirementwasmet.
Theobjectiveistoscreenlessdatathanareinourdataset, andsimulatedresearch
has shown that we may skip up to 95% of documents [56], although this is extremely
dependentonthedatasetandinclusion/exclusioncriteria[58]. Whenwehavedecidedto
finishscreening,wemayexportthefindings(i.e.,thepartiallylabeleddataandtheproject
filewiththetechnicalinformationtoreplicatetheentireprocess)andpostthemonsites
liketheOpenScienceFramework. Finally,inASReview,marktheprojectascompleted.
ASReviewLABsavestime, improvesthequalityofresults, andmakesworkmore
transparentwhenexamininglargequantitiesoftextualdatatoextracttherelevantinforma-
tion. Activelearningwillfacilitatedecision-makinginanydisciplineorindustry.
UsingtheAItoolinvolvedmultiplestages,priortoscreening,thetool’salgorithm
neededtobetrainedusingseveralprelabelledarticles[57]. Next,usingaresearcher-in-
the-loop approach, the AI tool recommended the article with the highest likelihood of
relevance. The reviewer then determined the relevance of each article proposed. The
operationwasrepeateduntilthehaltingrequirementwasmet. Allpapersdeemedrelevant
bythereviewerwerereviewedforfulltext(seeFigure12).
Thefollowingaretheessentialsteps[59]:
1. DataImport: ImporttheentiresetofresearchdocumentsintotheASReviewsoftware
(thatis,themetadatacontainingthetextofthetitlesandabstracts).
2. InitialFormation: ASReviewbeginswithaninitialformationphase. Theresearcher
classifies a small subset of articles as relevant or irrelevant in order to form the
automatic learning model. In fact, prior knowledge is chosen and used to create
the first model and present the first recording to the researcher. Because this is a
binaryclassificationproblem,theevaluatormustchooseatleastonekeyrecordto
include(specifylabel: relevant)andatleastonekeyrecordtoexclude(specifylabel:
irrelevant)basedonpriorknowledge. Anautomaticlearningclassifieristaskedwith
predictingtherelevanceofthestudy(labels)basedonarepresentationofthetext
containingtherecording(characteristicspace)andpriorknowledge.
Afterbeingtrainedwithpreviousexpertise,theAItoolranksallunlabeledpapers
(i.e.,articlesthathadnotyetbeendeterminedtobeeligible)fromhighesttolowest
probabilityofrelevance[57].

J.Imaging2025,11,12 29of66
Toavoidanyauthoritybiasintheinclusions, wehavepurposefullychosennotto
include the name of an author or a representation of a network of citations in the
spaceforcharacteristics.
3. ActiveLearning: ASReviewemploysanactivelearningstrategy. Themodelexamines
thelabeledarticlesandselectsthemostambiguousorinformativeones. Thesearticles
are presented to us in order to manually examine and categorize. Alternatively,
duringtheactivelearningcycle,thesoftwaredisplaysanewrecordthattheusermust
examineandlabel. Theuser’sbinaryetiquette(1forrelevantand0forirrelevant)is
thenusedtocreateanewmodel,afterwhichanewrecordispresentedtotheuser.
Thiscyclewillcontinueuntiltheuserspecifiesanendpoint.
Currently,theuserhasaccesstoafilethatcontains(1)entriesthathavebeenlabeled
asrelevantorirrelevantand(2)entriesthathavenotbeenlabeledbutarelikelytobe
relevantbasedonthecurrentmodel’spredictions[56].
Thisconfigurationallowsustosearchforalargedatasetmuchfasterthanpossible
withamanualprocesswhilemaintainingdecision-makingtransparency.
4. Iterative Process: the researcher examines the selected articles and assigns labels
(relevantornot). ASReviewincorporatesthelabeleddataintotheoveralltraining
andupdatestheautomaticlearningmodel.
5. ModelRefinement: Theupdatedmodellearnsfromourlabeleddataandimproves
itsabilitytopredicttherelevanceofunlabeleditems.
6. Iteration: Steps 3–5 are iteratively repeated. The model continues to select new
articles to investigate based on its uncertainty, and the researcher labels them in
ordertorefinethemodel. Thisiterativeprocessreducesthenumberofarticlestobe
manuallyexaminedwhilemaintaininghighprecision.
7. FinalArticleSelection: Whenthemodelreachesastoppingpoint(forexample,a
desiredlevelofexaminationexhaustion),ASReviewreturnsalistofarticlesclassified
accordingtotheirpredictedrelevance. Thislistwillassistusinfocusingourattention
onthearticlesthataremostrelevanttooursystematicreview.
UsingASReview,theresearchercansignificantlyspeeduptheselectionprocessby
assigning priority to the most relevant articles for the examination while reducing the
numberofirrelevantarticlesthatmustbeevaluatedmanually.
6.2. OutofScope
The search mechanisms used in online databases are not perfect, so a substantial
number of papers obtained during the first phase of the appraisal are unrelated to the
searchingscope. Forthisreason,aqualitativeanalysisfoundedontheexaminationand
assessmentofcontentisrequired(seeFigure10).
6.3. QualitativeAnalysis
The selected articles were classified using fundamental recommender system ap-
proaches. Table 9 shows how we classified the relevant studies into different groups.
Regardingrelevancyaccordingtoinclusion/exclusioncriteria,eachstudy’squalityand
completenesswereconsidered(intermsofproblemcharacterization,descriptionofsug-
gestedmethod/technique/algorithm,andevaluationoffindings).

J.Imaging2025,11,12 30of66
Figure12.Machine-learning-basedASReviewpipeline.Graphiciconsdenoteactionsperformedby
humanorcomputer.
Theresearchweexaminedshowsasubstantialtendencytowardthegrowthofhybrid
recommender systems (HRSs). According to publication year, over 75 percent of the
studies we reviewed were published within the last three years (see Figure 11). These
statisticsdefinitelysuggestanincreaseininterestandresearchconductedinthefieldof
HRS.Researchersandpractitionersarenoticingthepotentialbenefitsandadvantagesof
integratingmultiplefilteringalgorithmstoimprovetheeffectivenessandperformanceof
recommendationengines. Theexpandingcorpusofrecentliteratureindicatesthathybrid
recommendationsystemsarebecomingincreasinglyimportantandrelevantinaddressing
theconstraintsandlimitsofclassicsingle-approachrecommendationapproaches. This

J.Imaging2025,11,12
31of66
trend emphasizes the field’s dynamic character and ongoing efforts to develop more
accuratetailoredrecommendationsystemsviathecombinationofvariousmethodologies.
Table9.Mainselectionofpapersidentifiedbycategories,journals,andpublishers.
|     | Author | Publisher |     | Year | Journal |     |
| --- | ------ | --------- | --- | ---- | ------- | --- |
Primary
Category
|               | [60] | SpringerNature  |     | 2023 | Int. Jrnl.              | ofTech |
| ------------- | ---- | --------------- | --- | ---- | ----------------------- | ------ |
| Collaborative | [30] | ElsevierBV      |     | 2012 | Elect. CommerceResearch |        |
| Filtering     | [16] | GoogleScholar   |     | N/A  | GoogleScholar           |        |
|               | [19] | JohannesKepler  |     | 2021 | N/A                     |        |
|               | [15] | SpringerBerlin  |     | 2023 | JrnlCloudComp.          |        |
|               | [36] | ComputerScience |     | 2013 | Comp. Col.              | Int    |
Quality
|               | [18] | Appl. Sci.     |     | 2020 | AppliedSciences |              |
| ------------- | ---- | -------------- | --- | ---- | --------------- | ------------ |
|               | [29] | ACM            |     | 2022 | Jrnl. Edu.      | D.Mng.       |
|               | [60] | SpringerNature |     | 2023 | Int. Jrnl.      | ofTech       |
| Content-based | [31] | Springer,Cham  |     | 2020 | Adv.Net.        | Inf. Systems |
Based
|           | [30] | ElsevierBV     |     | 2012 | Elect. CommerceResearch |     |
| --------- | ---- | -------------- | --- | ---- | ----------------------- | --- |
| Filtering | [16] | GoogleScholar  |     | N/A  | GoogleScholar           |     |
|           | [19] | JohannesKepler |     | 2021 | N/A                     |     |
[14] JournalOfKingSaudUniversity 2022 JournalOfKingSaudUniversity
|                 | [29] | ACM              |          | 2022 | Jrnl. Edu.              | D.Mng.       |
| --------------- | ---- | ---------------- | -------- | ---- | ----------------------- | ------------ |
|                 | [30] | ElsevierBV       |          | 2012 | Elect. CommerceResearch |              |
|                 | [35] | ElsevierLtd      |          | 2022 | Inf. Proc.              | andMngt      |
|                 | [33] | AIandSociety     |          | 2020 | AIandSociety            |              |
|                 | [31] | Springer,Cham    |          | 2020 | Adv.Net.                | Inf. Systems |
| Hybridfiltering | [18] | Appl. Sci.       |          | 2020 | AppliedSciences         |              |
|                 | [36] | ComputerScience  |          | 2013 | Comp. Col.              | Int          |
|                 | [34] | SpringerInt.     | Publish. | 2023 | JournalofBigData        |              |
|                 | [13] | TaylorandFrancis |          | 2018 | AppliedAI               |              |
|                 | [16] | GoogleScholar    |          | N/A  | GoogleScholar           |              |
|                 | [32] | Springer         |          | 2020 | Int. JrnlonD.Lib.       |              |
|                 | [15] | Springer         |          | 2021 | KnowledgeandInf.        | Syst.        |
|                 | [61] | [62–67]          |          | [68] | [69–72]                 |              |
| Otherfiltering  | [73] | [74–79]          |          | [80] | [81–84]                 |              |
|                 | [85] | [86–91]          |          | [92] | [93–96]                 |              |
Legend: N/A=Notavailable.
6.3.1. EvaluationofQuality
A systematic review locates, evaluates, and critically assesses pertinent studies by
applyingexplicitandsystematicmethodstoawell-definedresearchquestion. Additionally,
itgathersandarrangesdatafromthestudiestocomprisethereview. Theresultsofthe
included studies are not always analyzed and summarized using statistical techniques
(meta-analysis)[97]. Therelationshipbetweentheresearchquestion,methods,results,and
interpretationisassessedusingatechniqueforevaluatingtheoriginalqualityofresearch

J.Imaging2025,11,12 32of66
usingmethodologicalqualityprotocols,checklists,and/orscales. Assuch,thevalidityand
applicabilityofsyntheticresearchfindingsdependheavilyonthemethodologicalquality
oftheoriginalstudies[97].
Toestimatethequalityofthechosenstudies,wealsodevelopedtheninequestions
thatarelistedinTable10.
Weuseweightsof0.5forlowimportance,1formediumsignificance,and1.5forhigh
significancetoassignweightstothequestions.Thesecoefficientsareessentialinestablishing
howimportanteachquestionisinrelationtotheothersduringtheevaluationprocedure.
Moreover,ratevaluesareusedtoevaluatetheanswerstothequestions.A“no”answer
receivesascoreof0,a“partly”answerreceivesascoreof0.5,anda“yes”answerreceives
ascoreof1. Thesescorevaluesareusefulforquantifyingresponsesandevaluatingstudy
quality[3,24].
Thefollowingformulaisusedtoexplaineachpaper’sevaluation[3,24]:
∑N q ∗a
Evaluation = i=1 wi ri (1)
paper
N
whichperformsaproductoperationbetweenthequeryweight(q )(0.5,1,1.5)andthe
wi
answerratingvalue(a )(0,0.5,1). N=9inourcaseisthenumberofqualityquestions(see
ri
Table10). Papersmustmeetthequalitythresholdof0.80inordertobeaccepted.
Table10.Questionstoevaluatethestudies’quality.
N# QualityQuestion Weight
1 Hasthestudylookedovertherelevantresearchfortheissues? 1
2 Didthestudyadequatelydescribetheissueitistryingtosolve? 1
3 Wasanexperimentalsolutionclearlydevelopedinthestudy? 1.5
4 Didthestudyexplainrecommendersystemsoralgorithmsindetail? 0.5
5 Wasmetricsevaluationforrecommendersystemsexplicitlyusedinthestudy? 1.5
6 Wasthedatasetusedinthestudydescribedindetail? 0.5
7 Wastheapplicationdomainintroducedinthestudyclearly? 1
8 Wasthearchitectureorwerethepartsofthesuggestedsystemdescribedinthestudy? 1.5
9 Didthestudyprovideaconcisesummaryofitsfindings? 1
6.3.2. WordCloudandFrequency
Before creating the word cloud, stemming was used to discover the phrases’ com-
monorigin.
Tobegintheclassificationprocess,thetagcloudpresentationwasutilizedtodetermine
themajorkeywords. Thecloudsofthe30keywordsfromtheabstractsareprovidedin
Figures13and14,whichprovidethe1000importantwordsfromthewholetextsofthe
articleswiththeirrelativerelevanceandprominence.
KeywordswereanalyzedusingPython,NumPy,Pandas,andMatplotlibtoproducea
simplefrequencyanalysisandwordcloudgraph.
Before constructing the graph, all characters in the text were converted to lower-
case. Pre-processingincludeddeletingdigits,punctuation,andstopwordsoftenfound
inEnglish.
Figure15representsthefrequenciesofthefirst30wordsextractedfromtheabstracts
ofallpublications,whileFigure16presentsthefrequenciesofrelevantwordsconstructed
from1000wordsselectedfromthecontentofallsectionsofthepaper,omittingreferences.

J.Imaging2025,11,12 33of66
Figure13.Top1000abstractwords.
Figure14.Top1000wordsinwholepapers.
Figure15.Wordfrequencyinabstracts(top30).

J.Imaging2025,11,12 34of66
Figure16.Wordfrequency:top1000wordsinwholepapers.
6.4. ApproachtoInclusionandExclusionStandards
Tomakesurethestudieschosenforanalysiswerepertinent,weusedpreciseinclusion
and exclusion criteria. We determined significance during the filtering process in the
followingways:
• InitialRetrieval: Afteraretrievalprocess, 5857preliminaryprimarystudieswere
foundusingfivedigitallibraries’searchengines. Eachlibraryutilizedvariousfiltering
parameters, which resulted in differing quantities of papers being returned. Each
libraryutilizedvariousfilteringparameters,whichresultedindifferingquantitiesof
papersbeingreturned.
• Criteria Definition: In order to concentrate on the most pertinent studies, we es-
tablishedasetofinclusion/exclusioncriteria. Exceptforgrayliterature,workshop
presentations,andarticlesthatreportedjustabstractsorpresentationslides,thisin-
volvedchoosingonlyjournalsfortheScopusandSpringerdatabasesandallcategories
forACM,GoogleScholar,andWebofSciences. Thechosenpapersweretohighlight
currentdevelopmentsinthedisciplineandbepublishedbetween2020and2024.
• Selection Based on Peer Review: To ensure a degree of quality and credibility in
the chosen studies, we only included articles that were approved for publication
afterapeerreviewprocedure. Articlesthatwerenotpeer-reviewedordidnotfitthe
designatedresearchfocusweredisqualified. Additionally,articlesthatdidnotinclude
recommenderhybridtechniquesintheirabstractortitlewerenotincluded. Thiswas
essentialformaintainingattentiononthepertinentsubject. Toensurelinguisticand
understandingconsistency,non-Englishpaperswereeliminated.
• CoarseSelectionPhase: Wefirstexaminedthepublishingtype,yearofpublication,
andtitleaspartofourcoarseselectionphase. Wefrequentlylookedatabstractsor
othersectionsofthepublicationstodeterminetheirapplicability.

J.Imaging2025,11,12 35of66
• HybridRecommendationSystems: Thereviewexcludedpapersthathadnothingto
dowithrecommendersystemsandinsteadfocusedonthosethatpresentedhybrid
recommendersystems.
• DataEntryandAnalysis: Toenableamethodicalreviewprocess,thedatawereinput
intoanExcelspreadsheet,includingkeywordsandcitedinformation.
• Quality Assurance: To guarantee high-quality results, a systematic review uses a
weighted score system to quantify study quality, accepting only those that meet a
thresholdof0.80.
• FinalSelection: Fifty-twoprimarypapersthatsatisfiedthepredeterminedstandards
wereultimatelychosen,offeringastrongbasisforthesystematicreview. Byguaran-
teeingthatonlypertinentandexcellentpaperswereincorporatedintotheanalysis,
thisexactingprocessraisesthereview’sacademicworthandtransparency.
6.5. CommonlyUsedPrincipalSummaryMeasures
Inasystematicstudyofhybridrecommendersystems,performancemetricsareoften
employed as primary summary measures rather than standard measures such as risk
ratios or odds ratios. In this scenario, summary measures would be used to assess the
successofhybridrecommendersystems. Somecommonperformanceindicatorsinclude
thefollowing:
Precision: Thepercentageofrecommendeditemsthatarerelevant.
Recall: Thepercentageofrelevantitemsthatarerecommended.
F1-Score: The harmonic mean of precision and recall, which achieves a balance
betweenthetwo.
Thesethreemetricspresumethattheprovideddataaredividedinto“relevant”and
“irrelevant”categoriesandmaybeorganizedintoconfusiontables(seeFigure17). The
precision of a system is calculated by dividing the number of genuine positives by the
total number of positive cases predicted by the system. The precision measure can be
definedasthesystem’sprecisioninpercentagetermsusingthegenericconfusiontable.The
recallvaluedetermineshowwellthesystemcapturesrelevantinstancesandiscalculated
usingtherecallequation. TheF1-scoreassessesthesystem’saccuracyandiscalculated
as the weighted average of the precision and recall scores. The findings for the hybrid
recommendersystemareasfollows:
Precision (0.80) indicates that 80% of the things recommended by the system are
relevant. Aprecisionof0.80ishigh.
Recall(0.92): Arecallof0.92indicatesthatthesystemcanretrieve92%oftherelevant
elements,implyingthatitisquiteeffectiveatavoidingforgettingcrucialrecommendations.
Thishighrecallindicatesthatthesystemeffectivelycoversawiderangeofrelevantarticles.
F1-Score (0.86): The F1-score, which measures precision and recall, is 0.86. This
ratingshowsgreatoverallperformance,implyingthatthesystem’srecommendationsare
generallyaccurate(highprecision)andcomprehensive(highrecall).
6.6. ChallengesandSetbacks(RQ1)
InresponsetoRQ1,thissectionexplainsthedifferentobstaclescurrentlyinusethat
recommendationsystemsfaceandoffersdifferentanswerstothesechallenges.
6.6.1. ApproachesforAddressingtheCold-StartProblem
Cold-startwasthemostcriticalissuediscovered. Itbecomeschallengingwhenthe
recommendersystemisunabletodrawanyinferencesfromthelittleavailabledata. Cold-
startisacircumstanceinwhichthesystemisunabletocreateeffectiverecommendations
forcold(ornew)consumerswhohaveratednooronlyafewitems. Ittypicallyhappens
when a new user enters the system or when new items (or products) are added to the

J.Imaging2025,11,12 36of66
database. Approachestothecold-startproblemusuallyconcentratemoreongathering
extrainformationsuchasuserregistrationdetailsoritemmetadata.
Figure17.Confusionmatrixforthearticlesselectedforthestudy.
For this issue, the CF-based recommendation with an implicit rating was used in
the study in [30]. Because explicit rating information on items was not available for
onlineshoppingmalls,thismethodwasused. Theresearchersextractedimplicitrating
informationfromtransactiondata,whichservedasaproxyforexplicitratinginformation.
Theauthorsof[29]createdahybridrecommendationsystemforpersonalizedcourse
recommendationsine-learningsettings,whichaddressescold-startdifficultiesandinsuffi-
cientinformation.
Modernhybridsystemseffectivelyincorporateseveraltechnologies,suchasmachine
learninganddeeplearning,toaddresstheusercold-startproblem,outperformingprevious
systems that often rely on a single strategy. This integration enhances performance by
combiningdata-drivenandmethod-drivenstrategies[98].
Meta-Learning:Modernsystemsusemeta-learningtoquicklyadapttonewuserswith
lessdata,buttraditionalsystemsstruggletomakerecommendationswithoutsignificant
previousknowledge[98].
DeepLearningCapabilities:Hybridsystemscommonlyusedeeplearningtechniques
tocapturecomplexinteractionsbetweenpeopleandthings,whichisadifficulttaskfor
traditionalsystems. Thisenablesmoretailoredrecommendations, evenwhenlessuser
dataareavailable[98].
Multiple-FeatureFusion:Modernsystemscancombineavarietyoffeaturesanddata
sources,enhancingtheirrecommendationcapabilitiesfornewusers. Traditionalsystems
lackthisadaptabilityandrelyonsimplermodelsthatmaynotaccuratelyreflectvarious
userpreferences[98].
Tosolvethecold-startproblemincontent-basedrecommendersystems,effectiveuser
profilingisrequired.Thiscanbeaccomplishedbyleveragingdemographicvariablessuchas
geographiclocation,age,gender,occupation,andeducation[7]. Oneeffectivetechniqueis
toutilizeonboardingquestionnairestocollectuserpreferencesatthebeginningofprogram
use[99]. Thisprocedureentailsconnectingtheinitialdataacquiredtosubsequentrecom-
mendations,therebyincorporatinguserpreferencesintotherecommendationarchitecture.

J.Imaging2025,11,12 37of66
Businessesthataggressivelyseekexplicitfeedbackfromnewusersviaonboarding
questionnaires,surveys,orinteractivechatbotscanacquiresignificantinsightsintoclient
tastesandpreferencesfromthestart.
Thisdirectapproachnotonlyimprovestherelevancyofrecommendationsbutalso
contributestotheestablishmentofapersonalizedexperience,therebyalleviatingtheissues
connectedwiththecold-startissue[99].
6.6.2. Sparsity
Approachestothedatasparsityproblemconcentratemoreonusingexistingdatato
fillinthegaps. Tomakeaccuraterecommendations,collaborativefiltering(CF)requires
manyuserswhohaveratedmanyitems. However,thisisnotalwaysthecase,resulting
insparsityissues. Toaddressthisissue,thepaper[30]suggestsahybridapproachthat
combinesCFwithsequentialpatternanalysis(SPA).ThelimitationsofCFinreflecting
changesinuserpreferencesovertimecanbereducedbyintegratingSPA,whichconsiders
itemassociations,withCF,whichusesratinginformation. Byprovidingrecommendations
basedonbothratinginformationandsequentialpatterns,thishybridapproachhelpsto
mitigatethesparsityproblem.
The combination of sequential pattern analysis (SPA) and collaborative filtering
(CF)wasusedin[30]toaddressthesparsityproblem. Thestudyaimedtomitigatethe
higherprobabilityofinaccurateandbiasedrecommendationsforitemsthatarisefrom
consideringonlypurchasinginformationratherthanratinginformationbyintegrating
CF, which uses evaluating information, with SPA, which returns adjustments to user
choices over time in a sequence of sequential patterns. The techniques of modern
hybrid recommender systems and conventional systems are compiled based on the
generalrecommendationframework. Reducingthedimensionalityofcomplicatedrating
matrices to approximate ones is one useful strategy to mitigate the adverse impact
of data sparsity [7,44,80]. For example, a latent factor model, matrix factorization, or
singularvaluedecompositioncanaccomplishthis. Weshowthatevenabasichybrid
recommender system that simply combines user and item data can produce a better
predictionthanconventionalsystems.
Contrastivelearning[100]canassistinaddressingtheproblemofsparsityinrecom-
mendationsystems. Sparsityisasituationinwhichthereisinsufficientuser–iteminter-
actiondata,makingitdifficultforstandardmodelstoanticipateaccurately. Contrastive
learningisaself-supervisedlearningmethodthatseekstoacquireusablerepresentationsby
differentiatingbetweensimilaranddissimilardatapoints. Inthecontextofrecommenda-
tionsystems,contrastivelearningcanbeusedtoincreasethemodel’scapacitytogeneralize
andproducebettersuggestionsbylearningrobustuserandobjectrepresentations,even
wheninteractiondataarelimited.
Accordingtothestudyin[100],contrastivelearningoutperformsconventionalmodels
in classification and exhibit enhanced accuracy through hyperparameter optimization
andfine-tuning. Theaccuracyofasemi-supervisedmodelwithonly5%labeleddatais
57.72%accordingtotheresults,whereascarefultuninginasupervisedsettingincreases
theaccuracyto88.70%[100].
6.6.3. AlluvialDiagram
RAWGraphsisahigh-qualityopen-sourceplatformfordevelopinguniquedatavisu-
alizations[101]. Figure18showsagraphgeneratedwiththistooltobettercomprehend
dataflow. Thisgraphincludesfactorslikedocumenttype,journal,anddateofpublication.

J.Imaging2025,11,12 38of66
Legend:
• Blue: Books
• Orange: JournalArticles
• Green: Publishedin2020
• Purple: Publishedin2019
• Red: Publishedin2018
• Yellow: Publishedin2021
• Gray: Otheryears
• FlowWidth: Representsthenumberofitems
Figure18.Multicategoricalarticleanalysiswithacompletecolor-codedlegend.
6.6.4. LimitationsandBiases
Thedeploymentofhybridrecommendersystemsatscaleconfrontsconstraintssuch
ashighprocessingneedsandlatencyconcernscausedbycomplicatedmodels. Additional
issuesincludeintegratingvarieddatasources,retrainingonaregularbasis,andassuring
interpretability. Cold-startissues,datascarcity,andalgorithmscalabilityareallfactorsthat
influenceperformance. Balancingreal-timecustomizationwithsystemresponsetimeand
costsremainsachallenge.
Thebiasesweconfrontwhenreviewingabstractsandtitlesmayimpactourperception
ofrelevance. Subconsciously,factorssuchastheauthors’reputation,theprestigeofthe
journal,oreventheauthors’namescaninfluenceourevaluationdespitetheprecautions
takentopreventthisfromhappening. However,itiscriticaltorecognizethatthetopicof
theabstractshouldnotbetheonlyfactorinfluencinghowwemakechoices.
We acknowledge that we were susceptible to biases during the manual screening
processpriortousingASReview. Onetypeofbiasthatimpactsresearchpapersispub-
licationbias. Top-tierpublicationsinalmostalldisciplinestendtopublishpaperswith
substantialfindings, frequentlyaccompaniedbysignificanteffectsizes. Usingonlythe
mostprestigiouspublicationsmayresultinanoverestimationoftheeffectsinthefield
ofinterest. Lower-tierjournalstypicallyreportsmallereffectsizesintheirpublications.
Thissearch’slimitationsincludetheauthors’exclusiveuseofacademicdatabasesforthis

J.Imaging2025,11,12 39of66
investigation;therefore,theycannotensurethatalltherelevantpaperswerelocated. A
secondmethodusingartificialintelligencealgorithms(ASReview)recommendedthetop
articlesbasedonrelevancytoeliminatebiasormisclassification.Finally,relevantitemsmay
havebeenexcludedduetoalackofprecisionintheomissioncontextofcertainknowledge
bases. Whilesomearticlesclearlystatedthecontextinwhichtheywereapplied,many
othersdidnot. Asaresult,thisstudymaynothaveconsideredothermethodologiesthat
areapplicabletohybridrecommendersystems.
Theotherbiasescanbesummarizedasfollows:
Hybridrecommendersystems,whichcombinetwoormorerecommendertechniques
inordertoimprovethequalityandeffectivenessoftailoredrecommendationsandapplied
methodology,mayprovidebias-relatedhazardsanddifficulties.
- DataBias: Hybridrecommendersusedatafromseveralsources,eachwithinherent
biases. Forexample,collaborativefilteringalgorithmsrelyonuser–iteminteraction
data,whichcanbeskewedbypopularityorsufferfromthecold-startproblem. Con-
versely,content-basedapproachesrelyonitemqualities,whichmaybeprejudiced
iftheitemdescriptionsareinadequateorskewed. Combiningvariousdatasources
withoutconsideringtheirrespectivebiasescanresultinbiasedsuggestions.
- AlgorithmSelectionBias: Inahybridsystem,variousalgorithmsareusedtohandle
different circumstances or specific jobs. The decision of which algorithm to apply
foraspecificuserorenvironmentmayresultinselectionbias. Ifthesystemprefers
onealgorithmoveranotherbasedonbiasedcriteria,itmayresultinunfairorerro-
neous suggestions. For example, applying a specific algorithm just to certain user
demographicsmayresultinbiasedresults.
- CombinationBias:Hybridsystemsusuallyintegratetheoutputsofseveralalgorithms,
whichmightresultinbias. Differentalgorithmsmayhavedifferentbiases,and,ifthe
mergingprocessisnotcarefullymanaged,itmayexacerbateexistingbiasesorcreate
newones.
- FeedbackLoop Bias: Hybridrecommenders, likeotherrecommendationsystems,
are susceptible to feedback loop bias. A self-reinforcing loop can occur when the
system’srecommendationsinfluenceuserbehavior,whichissubsequentlyutilizedto
trainthesystem. Thisbiascangrowwithtime,particularlyinhybridsystemswith
numerousalgorithmscontributingtothefeedbackloop. Ifthesystemfailstoaccount
forthisprejudice,itmaylimitthediversityoftherecommendationswhilereinforcing
existingbiases.
- Over-SpecializationBias:Hybridsystemsseektoincreaseperformancebyintegrating
methodologies; however, this can occasionally result in over-specialization. If the
system is overly reliant on a single algorithm or data source, it may excel in some
cases but underperform in others, resulting in biased suggestions. Balancing the
contributionsofvariouscomponentsinahybridsystemiscriticalforpreventingthis
typeofbias.
- ContextualBias: Hybridrecommendersfrequentlyusecontextualcharacteristicsto
generateindividualizedrecommendations. However,biasedorinadequatecontex-
tual information can result in biased outcomes. For example, using demographic
data without addressing potential biases may result in suggestions that reinforce
preconceptions.
- EvaluationBias:Evaluatingtheperformanceofhybridrecommenderscanbedifficult,
and the selection of evaluation measures and test datasets may create bias. If the
evaluationprocessfavorssomepartsofthesystem’sperformance,itmayoverlookor
underestimatebiasesinotherareas.

J.Imaging2025,11,12 40of66
Toreducethesedangers,researchersanddevelopersshouldcarefullydesignandassess
hybridrecommendersystems, takingintoaccountfairness, diversity, andthepotential
biasesofindividualcomponentsandcombinations. Implementingalgorithmswithfairness
restrictionscanhelptobalancerecommendationsacrossdifferentusergroups. Regular
monitoringanduserfeedbackcanalsoassistinuncoveringandcorrectingbiasesinreal-
worldinstallations.
6.6.5. Overfitting
Theintegrationofsomefeaturesinarecommendationsystemmodelcancauseoverfit-
tingduetotheabsenceofvaluableandconsistentinformationregardingthenatureofthe
digitalplatformsunderconsideration[19]. Someadditionalcontextsmaynotimproveor
perhapshaveanegativeimpactonthemodel’saccuracy. However,thistypeofknowledge
canbegeneralizedandclassifiedintomorebroadandintelligiblecategories.
6.7. HybridizationStratégies(RQ2)
Severalhybridizationtacticshavebeeninvestigatedbyresearcherstoimprovethe
qualityrecommendersystemperformanceinthebigdatasetting,whereenormousvolumes
of user and item information are available. A few of the most important hybridization
techniquesusedareasfollows:
Content–Collaborative Hybridization: Combining collaborative filtering, which
makes use of past preferences and user–item interactions, with content-based filtering,
whichmakesuseofitemattributesanduserprofiles,isknownascontent–collaborative
hybridization. Combiningcollaborative-andcontent-basedsignalsenablesthishybrid
techniquetodeliversuggestionsthataremorethoroughandprecise. Theresearchin[71]
offersanontology-basedmodelthatcombinesmulti-levelk-means,roughset,andBayesian
networktobeatSVM,DT,andRFwiththelowestlogerrorlossand98%accuracy.
Deep-Learning-BasedHybridRecommenders: Newdevelopmentsindeeplearning
methods,likeneuralnetworksandembeddings,havemadeitpossibletocreatehybrid
recommendersystemsthatefficientlymanagecomplicatedlarge-scaledata. Recommen-
dationsfromdeep-learning-basedmodelsaremorepreciseandtailoredbecausetheyare
abletoidentifycomplexpatternsandlinkagesinuser–iteminteractions. Thestudyin[70]
solvesvariousresearchchallengesbycreatingaCNN-basedno-referencevideoquality
assessmentforgamingfootagethatisimpactedbycompressionartifacts.
Hybrid Matrix Factorization: By adding more data, hybrid matrix factorization
approachesbuilduponthefoundationofstandardmatrixfactorizationtechniques. This
caninvolveaddinghybridregularizationwords,useroritemtraits,orsideinformation.
The method is able to capture more intricate associations and enhance the quality of
recommendationsbyincludinghybridizationinthefactorizationprocess. Thestudyin[31]
introducesahybridcontent-basedandneighborhood-basedrecommendermodelthatuses
anewsimilaritymeasure. Itachievesaccuracysimilartoinnovativeitem-orientedand
matrixfactorizationmodelswhilerunningatleasttwiceasfast.
Demographic–CollaborativeHybridization: Combiningcollaborativefilteringalgo-
rithmswithuserdemographicdata,suchasage,gender,location,orsocioeconomicstatus,
thishybridparadigm,whichcombinescollaborativepatternswithuser-specificfeatures,
canimprovepersonalizationandtacklethecold-startissue.
Thepaper[33]presentsahybridstrategythatcombinescollaborativefilteringand
demographicrecommendationsystems,utilizingdatamining,artificialneuralnetworks,
andfuzzytechniques.

J.Imaging2025,11,12 41of66
Knowledge-BasedHybridization: Itenhancestherecommendersystem’scomprehen-
sionofuserpreferencesanditemlinkagesbyintegratingdomain-specificknowledge,rules,
orontologies. Withthishybridmethod,morecontextandexplanationmaybeprovided.
Inthearticle[19],theauthorcreatedaMusicInformationKnowledgeGraph(MKG)that
containsuser-trackinteractionpairs,trackcontentattributes,andartistcontextelements.
6.8. Datasets(RQ3)
InresponsetoRQ3,wefollowedtheavailabledatasetsthatthewritersusedtoeval-
uatetheirhybridrecommendationsystems(HRSs). Thesedatabasesenablethescientific
community to reproduce studies and validate or enhance their procedures. Out of the
fifty-twostudies,forty-eightusedatleastonedataset,whereasthreedidnot. Figure19
depictsthedatasetsusedandtheirfrequenciesamongthestudies.
Thefindingsshowaheterogeneoussectorofdatasetutilization,withafewweband
survey datasets dominating the research landscape while also including less prevalent
datasets. Thisdistributionmightprovideinformationpertainingtotheresearchtrendsand
preferencesregardingthetopic.
DatasetDistribution: Thetabledepictsthedistributionofstudiesamongdifferent
datasetsusedforevaluation. Themostcommondatasetsare“webdataset”and“survey
data”,accountingfor26%ofalltheresearch.
Concentration of Studies: The results show that the studies are concentrated on
specificdatasets. Thetopthreedatasets(“webdataset”,“surveydata”,and“socialmedia
data”)accountformorethanhalfofallthestudies,indicatingthattheresearchcommunity
prioritizesthesetypesofdatasets.
DiversityofDatasets: Whilethemostprevalentdatasetsdominatethedistribution,
thetablealsoincludeslesscommondatasets,suchas“Instructionalmaterials”,“Qualitative
Data”,“Syntheticdataset”,and“ClinicalData”,whichaccountfor2–4%ofallthestudies.
Thisindicatesadegreeofdiversityinthedatasetsutilizedforstudy.
BalancedRepresentation: Thedistributionappearstobesomewhatbalanced,with
nosingledatasetaccountingforanoverwhelmingmajority(thelargestpercentageis26%
forboth“webdataset”and“Surveydata”). Thisshowsahealthydiversityofdatasetsused
intheinvestigations.
Missing or Unspecified Data: The 6% of research labeled as “NA” (not available)
indicatesthataminoramountofdatamaybemissingorundefinedinthesourcematerial.
6.9. ExperimentalOutcomes(RQ4)
Hybridrecommendersystemsfrequentlyseektousethecapabilitiesofvariousrecom-
mendationmethodologies(e.g.,content-based,collaborativefiltering,anddemographic-
based) in order to provide more accurate and personalized recommendations to users.
Combiningvariousalgorithmscanimproverecommendationperformance,asassessedby
measuressuchasprecision,recall,F1-score,ornormalizeddiscountedcumulativegain.
Thestudyin[31]providesahybridrecommendationsystemthatblendscontent-based
andneighborhood-basedalgorithmstoincreaseaccuracyandspeed. Itemploysnovelap-
proachestoimprovingitem-levelsimilaritymeasuresincollaborativefilteringalgorithms
(seeTableA1). Theworkemploysgenomictagsandaimstooutperformthetraditional
collaborativefilteringmethodsintermsofaccuracyandspeed. Theexperimentresults
indicatethatitismorepreciseandfasterthan‘pure’collaborativefilteringtechniques.
Thestudyin[61]incorporatesbothconventionalandadditionalaspectspertainingto
pandemic,environment,digitaltechnology,andinformationsystems;thestudyoffersa
thoroughmethodologyforassessingairlineservicequality.

J.Imaging2025,11,12 42of66
Ref. [71] utilized an ensemble approach consisting of three techniques: clustering,
roughset,andBayesiannetwork. Thestrategywasdividedintofourphases: clustering,
knowledge discovery, probabilistic network design, and model evaluation. Based on
experimentaldata,thismodeloutperformedothermodelslikeDT,RF,andSVM,withan
accuracyof98.36%(severalfurtherresultsareincludedinTableA1inAppendixA.
Figure19.Trendsinusingassessmentdatasetsforrecommendersystemresearch.
6.10. MethodologiesandRecommendedTechniques(RQ5)
AccordingtoTableA1,Column2inAppendixA,theproposedtechniqueforhybrid
recommendationsystemstypicallyincludesthefollowingimportantsteps:
- Data Collection: Gather data from various sources, including user behavior logs,
questionnaires,interviews,itemmetadata,anduserprofiles.
- FeatureEngineering: Relevantqualitiesthatinfluencedproposalswereidentified
andselected. Toincreasemodelperformance,morefeaturesweredevelopedusing
existingdata. Categoricalvariableswereencodedutilizingtechniqueslikeone-hot
encodingandembedding[60,94].

J.Imaging2025,11,12 43of66
- EmploytheStrengthsofDifferentMethods: Hybridsystemscombinethebenefitsof
severalrecommendationtechniques,suchasthosebasedoncontent,collaborativefil-
tering,anddemographicinformation,totakeadvantageoftheirrespectivecapabilities
andprovidemorepreciseandpersonalizedrecommendations.
- ExperimentandEvaluatePerformance: Experimentsarecarriedouttoevaluatethe
performanceofhybridsystemsregardingindividualrecommendationstrategies. The
increasesinrecommendationaccuracyareevaluatedusingmetricslikeasprecision,
recall,F1-score,andnormalizeddiscountedcumulativegain.
- AddressIndividualTechniqueLimits: Hybridsystemsareintendedtoovercomethe
limitsofindividualrecommendationapproaches,suchasthecold-startproblemor
theinclinationtoproposeprimarilypopulargoods. Theexperimentsshowincreased
coverageoflong-tailitemsandmorediverserecommendationsaccordingtousers’
uniqueinterests.
- AnalyzeEfficiencyandScalability: Thestudycomparesthecomputationalefficiency,
memoryutilization,andscalabilityofhybridstrategiestoindividualrecommendation
approaches. Theexperimentsevaluatehybridsystems’processingtimes, memory
footprints,andapplicabilityforreal-worldbigdataapplications.
- AssessCustomerExperienceandSatisfaction: Experimentsarecarriedouttoassess
theinfluenceofhybridsystemsonuserexperience,engagement,loyalty,andoverall
satisfaction.Theefficacyofthehybridtechniquesismeasuredbyanalyzinguserinput,
engagementmetrics,andsatisfactionlevels.
- AppreciateHybridization:Experimentsareintendedtohighlightanytrade-offscon-
nectedwithhybridization,suchastheeffectonmodeltransparency,interpretability,
orthecomplexityoftherecommendationprocess. Thesefindingscanhelptoinform
futuresystemdesigndecisionsandtheselectionofappropriatehybridizationstrategies.
- IdentifyOptimalhybridizedStrategies: Experimentsareperformedtodeterminethe
bestwaystocombineseveralrecommendationapproaches,suchasweightedhybrid,
switchinghybrid,featureaugmentation,andmeta-levelhybrid. Thestudyprovides
practitionerswithguidanceforselectingandimplementinghybridapproachesde-
pendingonthedatacharacteristicsandintendedrecommendationperformance.
6.11. PotentialFutureResearchDirections(RQ6)
Thelaststudyquestionconcernsthefuturejobprospectsanddirections. Ourresults
arereportedinTable11andbrieflydiscussedbelow:
Forthestudyin[31],employingarecommendationsystemasanintegratedMovie
SalesRecommendationEngine,futureworkwillfocusonenhancingmovierepresentations
andintegratingmatrixfactorizationtechniquesforincreasedaccuracy.
Theauthorsofthestudyin[33]onahybridmodelinsocialnetworksrecommendation
systemarchitecturedevelopmentwillevaluatetheirtechniquesonmoresocialnetworksand
investigatethepossibilityofcombiningthemwithgeneticalgorithmsforbetteroutcomes.
Theauthorsofthestudyin[36]examinedcoursewareandopeneducationalresources
with an emphasis on quality. One of their future objectives is to automate processes
relatedtothecreationofaneffectiveandpersonalizedadaptiverecommendationsystem.
Futureplanscallforautomatingseveralframeworkoperationstoenhanceflexibilityand
recommendations. Developinganexcellentadaptiverecommendersystemthatistailored
tousers’learningneedsistheultimateobjective.
One of the goals for the future is task automation for the development of a per-
sonalizedandeffectiveadaptiverecommendersystem. Theplansforthefutureinclude
automatingsomeframeworkactivitiestoenhancerecommendationsandflexibility. Creat-

J.Imaging2025,11,12 44of66
ingasuperior,personalizedadaptiverecommendersystemforusers’learningneedsisthe
ultimateobjective.
One of the primary goals of the project management system study [75] is to raise
thegeneralstandardofJakarta’smunicipalparks;subsequentstudiescouldconcentrate
onraisingtheadministrationandmanagementofJakarta’sparks,aswellasraisingthe
administrationofconstructionprojects,especiallyinthepre-constructionstage.
The authors of [81] underline the importance of assessing and monitoring societal
perceptionsofenhancedindividuals. Theycontendthatunderstandingtheseperspectives
iscriticalforguidingthedevelopmentanduseoffutureaugmentationtechnologies.
Accordingtothearticle[78]onfinancialmodelingtechniques, futuregainscanbe
achievedbyadjustingreimbursementstructuresandimplementingquality-basedincentives.
Table11.Futurestudyproposals.
PotentialFutureWork Studies
Enhancetheofferedsolution. 7
Conductmoredetailedreviews. 6
Includecontextualinformationinrecommendations. 7
Investigateapplicationsinvariousfields. 5
Usemoredataoritemfeatures. 5
Testavarietyofalgorithms. 8
Experimentationwithvarioushybridrecommendationmodels. 6
Other. 8
Buildingonourpreviousresponses,weconductedin-depthevaluationsofeachindi-
vidualstudytocorrectlyaddressresearchquestionsRQ2toRQ6.Thegoalwastodocument
thetechnicalmethods, algorithms, approaches, andfindingsutilizedindevelopinghy-
bridrecommendersystemsasdescribedintheliterature. TableA1inAppendixAshows
a summary of the employed strategy, the dataset used, the objectives, and the results.
AspresentedinAppendixA,thehybridrecommendationsystemsusedavarietyofap-
proaches to improve accuracy, coverage, and user experience. The experiments found
thathybridsystemsoutperformedindividualtechniquesintermsofprecision,recall,and
diversity. The hybrid techniquesalso demonstratedhigher efficiencyand scalabilityin
large-scaleapplications. Theevaluationsofuserfeedbackandinteractionrevealedthat
personalized,relevantrecommendationsincreasedsatisfaction. Theexperimentsrevealed
trade-offsinhybridizationstrategiesandhelpedtoidentifytheoptimalproceduresfor
specificapplications.
FutureResearch
Given the findings of this study, we see potential for further research in context-
sensitivesystemsandhybridizationtechniques. ToefficientlydesignCARS,thefollowing
toolsandapproachescouldbeused:
• Context-AwareRecommendationSystems(CARSs)enhancetraditionalrecommenda-
tionmodelsbyintegratingcontextualfactors,suchaslocation,time,orenvironmental
conditions,intotherecommendationprocess,developingtechniquesforgathering
contextualdata,suchasuserbehavioranalyticsorenvironmentalsensors,anddesign-
ingalgorithmsthatincludecontextualinformationintherecommendationprocess.
Unlikeconventionalsystemsthatpredictratingsbasedonlyonuser–iteminteractions
(F :User×Item→Rating),CARSsexpandthepredictionfunctiontoincludecontext
(F : User×Item×Context→ Rating),addingathirddimension. Thisaddedcom-
plexitymakestherecommendationsmorerelevantbyaligningthemwithsituational

J.Imaging2025,11,12 45of66
user needs, although it also increases the computational demands. A clear under-
standingof“context”,definedasanyinformationshapingtheuserinteractionswith
thesystem,isessentialforeffectivelydesigningthesesystems. Toefficientlydesigna
CARS,thefollowingtoolsandapproachescouldbeused:
1. MachineLearningFrameworks: Usemachinelearningframeworkssuchas
TensorFloworPyTorchtocreatepredictionmodelsbasedoncontextualinfor-
mation. Theseframeworksprovidestronglibrariesfordevelopingandtraining
machinelearningmodels,enablingtheintegrationofcomplicatedcharacteristics
suchascontextinadditiontouserandobjectdata.
2. Dataset,Model,andEvaluation:Creatingacontextualdataset,creatingarein-
forcementlearningmodel,andusingperformancemeasurestoevaluateadaptation.
3. Contextual Bandits: Use contextual bandit algorithms to dynamically adjust
recommendations based on real-time circumstances. These algorithms strike
abalancebetweenexplorationandexploitationbydeterminingwhichrecom-
mendationsfunctionbestinvariouscontextualsettings,allowingthesystemto
delivertailoredideasthatadaptasuserbehaviorsandcontextschange.
4. UserStudies: Conductuserresearchtodeterminetheeffectivenessofcontext-
awarerecommendations. Gatheringqualitativeinputfromconsumersallowsus
tomeasurehoweffectivelytherecommendationssuittheirneedsandpreferences
invariousscenarios. Thisapproachmayincludesurveys,interviews,orA/B
testingtomeasureuserhappinessandengagementwithcontextualfeatures.
• Hybridization: Inmachinelearning,hybridizationistheprocessofmergingmultiple
algorithms or models to improve predicted accuracy, resilience, and flexibility by
utilizing their strengths while mitigating individual limitations. Hybridization in
recommendation systems frequently employs ensemble learning techniques such
asstackingandmeta-learningtocombinecollaborative-andcontent-basedfiltering
methods. This method enhances recommendation accuracy by modifying model
weights in response to user interactions. Scikit-learn and PyTorch are tools that
help to apply these concepts, making it easier to experiment and enhance hybrid
systems across a wide range of applications, including recommendation engines,
identifyingfraud,andnaturallanguageprocessing. Tosupplementtheconversation,
wewillprovideamoredetailedexaminationregardinghowtheseconcernscould
beinvestigated:
1. FrameworksforHybridSystems: Uselibrariesthatsupporthybridrecommen-
dationalgorithms,suchasSurpriseorApacheMahout.
2. A/BTesting: UseA/Btestingtechniquestocomparetheperformanceofhybrid
modelstostandardapproaches.
3. DataFusionTechniques: Exploredatafusionapproachestosuccessfullymerge
multiplesourcesofdata,henceimprovingthequalityofrecommendations.
Thegapsintheliteraturerequiremoreexploration. Addressingthesedeficienciesis
criticaltoimprovingthescalability,accuracy,andethicalissuesofhybridrecommender
systems:
ScalabilityChallenges: Tomanageenormousdatasetsefficiently,scalabletechniques
arerequired.
IntegrationofAdvancedAItechniques: Investigatinghowdeepreinforcementlearn-
ingandgenerativemodelsmightimproverecommendationaccuracy.
Data Privacy and Ethical Considerations: Creating techniques for implementing
privacy-preservingprocedureswhilemaintainingthequalityofsuggestions.

J.Imaging2025,11,12 46of66
ExperienceandEngagementMetrics: Focusingontheimportanceofincreasinguser
happinessandtrustintheadviceprovided.
7. Conclusions
Thisarticleprovidedacomprehensivesurveyandassessment,aswellasanextended
organizedtaxonomy,forthemostrecent,ever-increasinglyefficienthybridrecommenda-
tionsystemmodelsusedinbothacademiaandindustry,withsuccessfulapplicationsin
fieldssuchase-commerce,music,andgeographiclocationservices. Inthiswork,weem-
ployedanopen-sourcesystemthatusesmachinelearningtoefficientlyfilterandcategorize
largeamountsoftextualdata,whichspedupthedocumentselectionprocess. Usingthis
approachinconjunctionwiththetraditionalmethods,wediscovered52keypublications
fromconferenceproceedingsandjournalsonhybridrecommendersystems. Ourgoalwas
tohighlightthemostrelevantconcernsaddressedbythesestudiesinordertomakemore
informedsuggestions. Wealsostudiedthemachinelearninganddataminingapproaches
theyemploy,therecommendationstrategiestheymerge,thehybridizationclassesthey
adhereto,theapplicationdomainsanddatasets,theevaluationprocedure,andpotential
futureworkpaths. Asignificantportionoftheresearchweexamined(morethan75%)was
publishedduringthelastthreeyears,demonstratinganoticeableandgrowinginterestin
hybridrecommendersystems(HRSs). Thisworkemphasizestheneedforfurtherresearch
intocontext-sensitivesystemsandhybridizationtacticsincontext-awarerecommendation
systems(CARSs). Byincorporatingcontextualaspects,aCARSimprovesthetraditional
models, improving their relevance while increasing the processing demands. Machine
learningframeworks,contextualbandits,anduserstudiesarekeytoolsforassessingeffec-
tiveness. Furthermore,hybridizationcombinesalgorithmstoimproveaccuracy,withan
emphasisonusingframeworkssuchasApacheMahout,whilealsoaddressingscalability,
ethicalconcerns,anduserengagementmetricsinfuturestudies. Furthermore,ourout-
comesindicatethatusinglargerdatasetsandhybridparallelalgorithmsmaybeaviable
waytohandlescalabilityissuesandimproverecommendationqualityintheageofbig
data. Another intriguing area for future research is the use of hybrid recommendation
systemstocreatecross-domainrecommendersorlowerthecomputationalcomplexityof
theexistingapproaches.
AuthorContributions: B.S.createdtheconceptandcomposedthemanuscript. A.K.andB.E.A.
monitoredandassistedB.S.indevelopingandstructuringthemanuscript.M.R.readandcommented
onthemostrecentversion. Allauthorsdiscussedtheanalyses,interpretedthemethodology,and
provided feedback on the text. All authors have read and agreed to the published version of
themanuscript.
Funding:Thisresearchreceivednoexternalfunding.
InstitutionalReviewBoardStatement:Notapplicable.
InformedConsentStatement:Notapplicable.
Acknowledgments:ThisprojectissupportedinpartbyTekCircleandCNRST.Ourexperimentswere
performedintheCNRSTenvironmentwithGPUclusterobtainedduringtheirvaluablecollaboration.
ConflictsofInterest:Theauthorsdeclarenoconflictsofinterest.

J.Imaging2025,11,12
47of66
AppendixA.RecapitulativeTableA1oftheSelectedArticles
TableA1.Acomprehensivereview-basedoverviewofrecommendertechniques.
| StudyIssue |     | EmployedStrategy |     | Dataset |     | Objectives/Results |     |     |     |     |
| ---------- | --- | ---------------- | --- | ------- | --- | ------------------ | --- | --- | --- | --- |
[14] A hybrid rec- The study uses a hy- Amzon dataset: Objectives:
ommender system bridrecommendersys- This dataset con- The study’s goal is to create a hybrid recom-
for patron-driven temthatcombinescol- sists of 278,858 mendersystemthathelpslibraryadministrators
library acquisition laborativefilteringand users who pro- tomakeeducateddecisionsaboutacquisitions
andweeding. content-basedfiltering vided 1,149,780 andweedingbyincorporatingusercomments
|     |     | to help library       | admin- | ratings | for 271,379 | andpreferences. |     |     |     |     |
| --- | --- | --------------------- | ------ | ------- | ----------- | --------------- | --- | --- | --- | --- |
|     |     | istratorsmakeacquisi- |        | books.  | Library     | Results:        |     |     |     |     |
tion and weeding de- Catalog: Library Thehybridrecommendersystemwassuccess-
cisions based on user dataset provides fully implemented in a national library, deliv-
feelings. information and ering acquisition and weeding advice based
|     |     |     |     | statistics | for com- | on user   | feedback | and | machine learning | ap- |
| --- | --- | --- | --- | ---------- | -------- | --------- | -------- | --- | ---------------- | --- |
|     |     |     |     | paring     | book     | proaches. |          |     |                  |     |
availability.
| [31] A | Novel | The work | presents | The | benchmark | Objectives: |     |     |     |     |
| ------ | ----- | -------- | -------- | --- | --------- | ----------- | --- | --- | --- | --- |
Hybrid Recom- a mixture of recom- dataset is Movie- The paper presents a hybrid recommenda-
mendation Sys- mendations that uses Lens20Min,which tionsystemthatcombinescontent-basedinfor-
tem Integrating genome tag infor- retains just users mationwithneighborhood-basedalgorithms
Content-Basedand mation to increase and movies with to improve accuracy and speed. It employs
RatingInformation accuracyofprediction 20 or more ratings. uniquewaystoimproveitem-levelsimilarity
in collaborative filter- justmovieshaving measurementsinitem-orientedcollaborative
ing.Itprovidesanovel tag genome infor- filtering algorithms. The study uses genome
similaritymeasurethat mation are kept. tagsandseekstooutperformstandardcollabo-
includescontent-based As a result, 10,239 rativefilteringapproachesregardingaccuracy
|     |     | information      | into ex- | movies     | received | andspeed. |     |     |     |     |
| --- | --- | ---------------- | -------- | ---------- | -------- | --------- | --- | --- | --- | --- |
|     |     | isting formulas, | with     | 19,799,049 | ratings  | Results:  |     |     |     |     |
the goal of improving from138,493users. The suggested hybrid recommendation sys-
|     |     | the accuracy | of item- |     |     | tem, | which | combines | content-based | and |
| --- | --- | ------------ | -------- | --- | --- | ---- | ----- | -------- | ------------- | --- |
oriented collaborative neighborhood-based information, provides
|     |     | filteringalgorithms. |     |     |     | comparableaccuracytoleadingmodelswhile |          |          |                  |       |
| --- | --- | -------------------- | --- | --- | --- | -------------------------------------- | -------- | -------- | ---------------- | ----- |
|     |     |                      |     |     |     | being                                  | at least | twice as | fast. Experiment | find- |
ingssuggestthatitismoreaccurateandfaster
|     |     |     |     |     |     | than‘pure’collaborativefilteringmethods. |     |     |     | Fu- |
| --- | --- | --- | --- | --- | --- | ---------------------------------------- | --- | --- | --- | --- |
tureworkwillincludeimprovingmovierepre-
sentationsandmergingthemodelwithmatrix
factorizationtechniquestoincreaseaccuracy
evenfurther.
| [29] A course    | hy- | CF,CB,Hybrid |     | 213courses |     | Objectives:                                |     |     |     |     |
| ---------------- | --- | ------------ | --- | ---------- | --- | ------------------------------------------ | --- | --- | --- | --- |
| brid recommender |     |              |     |            |     | Thisworkaddressesthecold-startissueandlim- |     |     |     |     |
system for limited itedinformationcircumstancesbycreatingahy-
| user information |     |     |     |     |     | bridrecommendationsystemforpersonalized   |     |     |     |     |
| ---------------- | --- | --- | --- | --- | --- | ----------------------------------------- | --- | --- | --- | --- |
| scenarios        |     |     |     |     |     | courserecommendationsine-learningenviron- |     |     |     |     |
ments.
Results:
Estimation,validatehypothesesforbetterrec-
|     |     |     |     |     |     | ommendation |             | system      | performance,   | investi- |
| --- | --- | --- | --- | --- | --- | ----------- | ----------- | ----------- | -------------- | -------- |
|     |     |     |     |     |     | gate        | application | to various  | recommendation |          |
|     |     |     |     |     |     | scenarios,  | and         | investigate | contextual     | embed-   |
dingsformultiplelanguages.
LSAmodelPrecision=0.17
LDAmodelPrecision=0.16
|     |     |     |     |     |     | Hybridbestresultα |     | =0.9 |     |     |
| --- | --- | --- | --- | --- | --- | ----------------- | --- | ---- | --- | --- |

J.Imaging2025,11,12
48of66
TableA1.Cont.
| StudyIssue | EmployedStrategy |             | Dataset   | Objectives/Results |     |     |     |
| ---------- | ---------------- | ----------- | --------- | ------------------ | --- | --- | --- |
| [15] A     | hybrid Neural    | interaction | MovieLens | and Objectives:    |     |     |     |
neuralnetworkap- layer, NCTR model Amazon Thestudyaimstoovercomelimitationsofexist-
proach to combine tochastic Gradient ingrecommendationalgorithmsbyproposinga
textualinformation Descentalgorithm hybridneuralnetworkmodel,novelhybridneu-
| and rating     | infor-   |     |     | ralnetworktocombinetextualinformationand    |     |     |     |
| -------------- | -------- | --- | --- | ------------------------------------------- | --- | --- | --- |
| mation         | for item |     |     | rating(NCTR),whichincorporatestextualinfor- |     |     |     |
| recommendation |          |     |     | mationandratingdatatoenhancerecommen-       |     |     |     |
dationaccuracy,particularlyforsparsedata.
Results:
|     |     |     |     | Enhancing | techniques | for capturing | the non- |
| --- | --- | --- | --- | --------- | ---------- | ------------- | -------- |
linearityoffeatureinteractionsandenhancing
|     |     |     |     | strategies | for feature | extraction | from textual |
| --- | --- | --- | --- | ---------- | ----------- | ---------- | ------------ |
data
[30] A hybrid CF,SequentialPattern E-commerce and Objectives:
online-product Analysis(SPA) transaction data: Thestudy’sgoalistogenerateimplicitratings
recommendation Dataset of 16,486 andcombineCFwithsequentialpatternanaly-
system: Combining transactions of 247 sistoimproveonlinerecommendations.
Results:
| implicit | rating- |     | userson1911items |     |     |     |     |
| -------- | ------- | --- | ---------------- | --- | --- | --- | --- |
basedcollaborative In collaborative filtering (CF), implicit ratings
filtering and se- effectively replace explicit ratings for digital
| quential  | pattern |     |     | transaction                    | data. A | CF-SPA hybrid | approach    |
| --------- | ------- | --- | --- | ------------------------------ | ------- | ------------- | ----------- |
| analysis. |         |     |     | improvesrecommendationquality. |         |               | Fourexperi- |
mentswerecarriedouttocomparetheproposed
|     |     |     |     | approachtoothers. |     | DatafromalargeKorean |     |
| --- | --- | --- | --- | ----------------- | --- | -------------------- | --- |
onlinemall,focusingonuserswhomademore
|     |     |     |     | than30purchases. |     | Intermsofprecision,recall, |     |
| --- | --- | --- | --- | ---------------- | --- | -------------------------- | --- |
andF1,thesuggestedhybridsystemexceeded
|     |     |     |     | CFandSPA-basedmethods. |                 | Inthehybridsys-    |        |
| --- | --- | --- | --- | ---------------------- | --------------- | ------------------ | ------ |
|     |     |     |     | tem, the               | value of weight | for CF-based       | recom- |
|     |     |     |     | mendationissetto0.1.   |                 | Thestudyrecognized |        |
thatasmalldatasetsizewasalimitation.
[60] A parametric CF, CB, Quality Con- 307 Delhi respon- Objectives:
analysis of AVA to trol dents. Netflixdom- Thestudyexaminestheimpactofaestheticvi-
optimize Netflix inates,aesthetican- sualanalysis(AVA)onNetflix’sthumbnailse-
| performance       | Inter-     |     | notations(63.8%). | lectionprocess.                           |     |     |     |
| ----------------- | ---------- | --- | ----------------- | ----------------------------------------- | --- | --- | --- |
| national          | Journal of |     |                   | Results:                                  |     |     |     |
| Information       | Tech-      |     |                   | AmongOTTplatforms,Netflixwaschosenby      |     |     |     |
| nology(Singapore) |            |     |                   | 63.8%ofrespondentsastheirpreferredchoice. |     |     |     |
[13] A Propound RandomForest(RF) 300visitorsand100 Objectives:
Hybrid Approach Pearson Correlation products. A hybrid technique for tailored online sug-
for Personalized (PC) gestion of products in e-commerce websites.
Online Product GradientBoosting(GB) Thegoalistoincreasetheaccuracyofsugges-
Recommendations tions by utilizing collaborative filtering, im-
plicitdataandsequentialpatterns.
Results:
IntegrationofCFandPSPapproachesoutper-
formsindividualmethods.
Noscalabilityoftheproposedapproach

J.Imaging2025,11,12 49of66
TableA1.Cont.
StudyIssue EmployedStrategy Dataset Objectives/Results
[61] A three-level The SERVQUAL For criteria weight Objectives:
frameworktoeval- methodology is ex- estimation,theBest The goal of this research is to provide a three-
uateairlineservice panded to evaluate Worst approach levelframeworkforevaluatingairlineservice
qualitybasedonin- airline service in (BWM) and the qualitybasedontheSERVQUALmodelwhile
terval valued neu- terms of pandemic, Modified Delphi taking into account new aspects such as pan-
trosophicAHPcon- information systems., approach were demic,environment,digitaltechnology,andin-
sideringthenewdi- digitaltechnologyand used. formationsystems.
mensions. environment. Results:
The study presents a comprehensive method-
ology for evaluating airline service quality by
usingtheextendedSERVQUALmodel,which
includestraditionalandextrafactorsrelatedto
pandemic,environment,digitaltechnology,and
informationsystems.
[32] An analysis The study compares LatentDirichletAl- Objectives:
and comparison keyword suggestion location(LDAwith Thepurposeofthisresearchistoinvestigateand
of keyword rec- approaches for scien- 300topicsand1000 comparekeywordrecommendationstrategies
ommendation tificdatabycombining iterations) forscientificdata,specificallytheindirectand
methods for scien- analysis, metrics pro- Stanford Topic directapproaches,aswellastoassessmetadata
tificdata posals,andtests. ModelingToolbox. qualityandproposeassessmentcriteriaforcon-
trolledvocabularies.
Results:
Thispublicationwouldmostlikelygiveamore
completeevaluationofthestudy’slimitations,
study’sparticularfindingsarenotprovided,po-
tentialareasforimprovement,andideasforfu-
tureresearchinitiatives.
[62] An extended Analytical Hierarchy 21 top-leading Ira- Objectives:
modelforassessing Process(AHP) nianuniversities. Thisstudyaimstoprovideamorecomprehen-
E-Services of Ira- Promethee(Preference sivemodelforevaluatinguniversitywebsites’
nian Universities RankingOrganization e-services’ preparedness. The model seeks to
Websites Using Method for Enrich- pinpointthesewebsites’advantagesanddisad-
Mixed MCDM mentEvaluations). vantageswhileofferingsuggestionsforraising
method. theirstandardofdesign.
Results:
The study evaluated the readiness of 21 top
Iranian university websites for providing e-
services,butspecificvaluesandrankingswere
notprovided.
[63] Artificial intel- Thisstudyinvestigates Students’ Aca- Objectives:
ligence and edge fuzzyneuralnetworks, demicPerformance Provideanenvironmentintheclassroomwith
computing for GST, AHP, DBT-SVM, Dataset (xAPI- edge computing that is structured to enhance
teaching quality andDMmethods. Edu-Data) (100 social-emotionallearningandacademiclearn-
evaluation based students). ing. boost the effectiveness of the teaching-
on 5G-enabled learningprocess.
wireless communi- Results:
cationtechnology. Possible implications include the usefulness
oftherecommendedoptimizationstrategyfor
teachingcollegeEnglish,theadvantagesofin-
corporatingedgecomputingand5Ginmedical
education,andthegeneraladvantagesofusing
cutting-edgetechnologiesininstructionacross
theboardforeducationalpurposes.

J.Imaging2025,11,12
50of66
TableA1.Cont.
| StudyIssue | EmployedStrategy | Dataset |     | Objectives/Results |     |     |
| ---------- | ---------------- | ------- | --- | ------------------ | --- | --- |
[64] Beyond Bricks qualitativedataanaly- 17interviewswere Objectives:
and Mortar: The sistechniquessuchas conducted with 3 ThisstudyinvestigatesCollegeParkAcademy’s
efficacy of on- thematicanalysis. administrators, 2 transitiontovirtuallearningduringCOVID-19,
line learning staff members, 2 analyzingitsstructure,effectsonstakeholders,
and community- parents5teachers. andmakingrecommendationsfortechnology-
| buildingatCollege |     |     |     | enhancedteaching.                         |     |          |
| ----------------- | --- | --- | --- | ----------------------------------------- | --- | -------- |
| ParkAcademydur-   |     |     |     | Results:                                  |     |          |
| ing the COVID-19  |     |     |     | Transitionhadreadinesschallenges:         |     | academic |
| pandemic.         |     |     |     | rigorandsocial-emotionalwell-beingissues. |     |          |
[86] Business pro- expertinterviews,doc- 97criteria,23BPM Objectives:
cess modeling lan- umentanalysis,snow- languages,25qual- Thegoalofthisresearchistoprovideareliable
guageselectionfor balling literature re- ity attributes, and decisionmodelfortheproblemofbusinesspro-
researchmodelers. view. 72BPMfeatures. ceduremodelinglanguageselectioninresearch
projects.
Results:
Aselectionmodelforchoosingbusinessprocess
modelinglanguages(BPMN)with97criteria,23
alternatives,and25qualityfeatureswasdevel-
oped.
| [92] | CAQoE: CAQoE metric, | evalu- PTB | diagnostic | Objectives: |     |     |
| ---- | -------------------- | ---------- | ---------- | ----------- | --- | --- |
A Novel No- ating its performance ECG database Theresearchpresentscontext-awareQualityof
Reference Context- using objective and 148 subjects, 52 Experience (CAQoE), a measure for real-time
aware Speech subjective quality patients. voicequalityinVoIPapplicationsthatincorpo-
Quality Prediction scores. ratesacontext-classifier,VoiceActivityDetector
| Metric. |     |     |     | (VAD), and | validation | with subjective evalua- |
| ------- | --- | --- | --- | ---------- | ---------- | ----------------------- |
tions.
Results:
XGBoostpresentsthebestF-score(0.95%)
[95] Cross-User Basicsimilaritymetrics 32 people watch- Objectives:
Similarities in Prefetching Algo- ing 360° videos investigate the effects of stacking and quality-
Viewing Behavior rithms including head adaptiveanticipatingstrategiesfor360°video
for 360° Video and simulationmodel. movements from oncontentcacheperformance.
| Caching | Implica- | 439 | unique view- | Results: |     |     |
| ------- | -------- | --- | ------------ | -------- | --- | --- |
tions. ings, totaling 21 h Perspectivesonthecircumstancesinwhichover-
|     |     | and40mn. |     | lapmightbesignificantandcachingusefulfor |     |     |
| --- | --- | -------- | --- | ---------------------------------------- | --- | --- |
360°video
[91] DAC-HPP: DAC-HPPalgorithm. datasets: LFR-EA- Objectives:
deep attributed 1000,WEBKB. Suggestamethodfordeepattributedgraphclus-
| clustering        | with |     |     | teringcalledDeepAttributedClusteringwith |     |     |
| ----------------- | ---- | --- | --- | ---------------------------------------- | --- | --- |
| high-orderproxim- |      |     |     | High-orderProximityPreserve)(DAC-HPP).   |     |     |
Results:
itypreserve.
|     |     |     |     | Constructing | a consensus | matrix, Compared |
| --- | --- | --- | --- | ------------ | ----------- | ---------------- |
tosevencutting-edgemethods,DAC-HPPper-
formssuperior.
[87] DataPilot: Uti- Semi-structured inter- 1000 records from Objectives:
lizing Quality and views, brainstorming an open-source Tacklingtheproblemofidentifyingmeaningful
Usage Information sessions,andfeedback digital marketing datasubsetsfrombig, unusualdatasetswhile
forSubsetSelection sessions dataset with 42 visualdataprocessing.
| duringVisualData |     | properties. |     | Results:                                 |     |     |
| ---------------- | --- | ----------- | --- | ---------------------------------------- | --- | --- |
| Preparation.     |     |             |     | Severalhypothesesthatweretestedduringthe |     |     |
userstudy.

J.Imaging2025,11,12
51of66
TableA1.Cont.
| StudyIssue       |     | EmployedStrategy     |     | Dataset | Objectives/Results |     |     |     |
| ---------------- | --- | -------------------- | --- | ------- | ------------------ | --- | --- | --- |
| [88] Development |     | Createaquality-based |     | N/A.    | Objectives:        |     |     |     |
of a Quality-Based mathematical model Thepurposeofthisresearchistoexaminehow
ModelforSoftware for optimizing soft- modular and microservice software architec-
Architecture Opti- warearchitecture. turesareimplementedintermsofattributesre-
| mization:        | A Case   |     |     |     | latedtosoftwarequality.                   |            |              |           |
| ---------------- | -------- | --- | --- | --- | ----------------------------------------- | ---------- | ------------ | --------- |
| Study of         | Monolith |     |     |     | Results:                                  |            |              |           |
| and Microservice |          |     |     |     | The work                                  | develops a | mathematical | model for |
| Architectures.   |          |     |     |     | softwaredesignoptimizationbasedonquality- |            |              |           |
basedmixedintegergoalprogramming.
| [89] DHR: | Dis- | Distributed | Hybrid | N/A. | Objectives: |     |     |     |
| --------- | ---- | ----------- | ------ | ---- | ----------- | --- | --- | --- |
tributed Hybrid Rendering (DHR) This paper introduces and evaluates a dis-
Rendering for approach tributed hybrid rendering (DHR) solution for
Metaverse Experi- standalone XR devices, with the goal of com-
| ences. |     |     |     |     | bining | ray tracing graphics | with | high fidelity |
| ------ | --- | --- | --- | --- | ------ | -------------------- | ---- | ------------- |
whilemaintaininginteractiveframespeedsin
high-latencynetworkenvironments.
Results:
|     |     |     |     |     | The research | presents | a number | of findings |
| --- | --- | --- | --- | --- | ------------ | -------- | -------- | ----------- |
basedonanevaluationoftheDistributedHy-
bridRendering(DHR)technique.
[74]Empiricalanal- Researchersusedsam- 20 case studies Objectives:
ysisofthetoolsup- plingandsnowballing from 6 different Thegoalofthisstudyistoconductanempirical
port for software toselectrepresentative domains. analysis of tool support for software product
| productlines. |     | casestudies. |     |     | lines(SPL). |     |     |     |
| ------------- | --- | ------------ | --- | --- | ----------- | --- | --- | --- |
Results:
Theresearchlooksattoolassistanceforsoftware
productlines(SPLs)andunderlinesthesignif-
icanceofsophisticatedvariabilitymodelingin
manyfields.
[94] Evaluating Ex- Frameworkwithacol- 6800 task notes Objectives:
plainability Meth- lection of explanation spread over 46 The purpose of this study is to offer an ex-
ods Intended for techniques. days. plainabilitystructureforintelligentsystemsthat
MultipleStakehold- maysuittheclarificationneedsofdifferentuser
| ers. |     |     |     |     | groups. |     |     |     |
| ---- | --- | --- | --- | --- | ------- | --- | --- | --- |
Results:
|     |     |     |     |     | The majority | of engineers | (65%) | were pleased |
| --- | --- | --- | --- | --- | ------------ | ------------ | ----- | ------------ |
withtheexplanationquality.
| [18] | Examining | CF,CB, |     | 53participants | Objectives: |     |     |     |
| ---- | --------- | ------ | --- | -------------- | ----------- | --- | --- | --- |
the usefulness Quality-based recom- 400 Open Educa- Astudyevaluatesalternativetechniquestorec-
of quality scores mendation, tionalResources. ommendingopeneducationalresources,with
for generating HybridApprooach. thegoalofdeterminingifpedagogicalquality
| learning        | object      |     |     |     | scoresimproverecommendersystems.           |     |     |     |
| --------------- | ----------- | --- | --- | --- | ------------------------------------------ | --- | --- | --- |
| recommendations |             |     |     |     | Results:                                   |     |     |     |
| in repositories | of          |     |     |     | Thehybridstrategyscoredthehighestinterms   |     |     |     |
| open            | educational |     |     |     | ofrelevance(0.64),followedbythetraditional |     |     |     |
resources(OERs). content-basedapproach(0.60),suggestingitsef-
fectiveness.

J.Imaging2025,11,12
52of66
TableA1.Cont.
| StudyIssue | EmployedStrategy | Dataset | Objectives/Results |     |     |     |
| ---------- | ---------------- | ------- | ------------------ | --- | --- | --- |
[16] Hybrid Ap- Analyzequalityscores’ Million Song Sub- Objectives:
proach to Music impactonOERrecom- set: 10,000songs A The system suggests songs that are compa-
Recommender mender systems and 1millionusers. rable to the user’s preferences and have been
| Systems. | engine tools:        | CF, CB, | highlyratedbyotherusers.                     |     |     |     |
| -------- | -------------------- | ------- | -------------------------------------------- | --- | --- | --- |
|          | DNN,auto-encoder,in- |         | So,hybridmusicrecommendationsystemthat       |     |     |     |
|          | putvectorsBOW.       |         | combinescontent-basedandcollaborativefilter- |     |     |     |
ingisused.
Results:
|     |     |     | cold-startproblem: | useDNN |     |     |
| --- | --- | --- | ------------------ | ------ | --- | --- |
[35] Hybrid collab- Inmobilecloud-based 339 users 30 coun- Objectives:
orative filtering collaborative filtering, tries 5825 web ser- Hybridcollaborativefilteringmethodologyfor
model for con- ahybridmodelforcus- vices 70 countries, consumer service recommendation in mobile
sumer dynamic tomer service recom- 1.97 million access cloudtosolvedatasparsityandboostaccuracy.
service recommen- mendation integrates logsofQoSofweb Results:
dation based on userpreferences. service. Thestudyintroducesahybridcollaborativefil-
| mobilecloudinfor- |     |     | teringmodelforservicerecommendationinthe |     |     |     |
| ----------------- | --- | --- | ---------------------------------------- | --- | --- | --- |
| mationsystem.     |     |     | mobilecloud,addressingdatasparsityandim- |     |     |     |
provingpredictionaccuracy.
[19] Hybrid Music hybrid recommenda- Music Information Objectives:
Recommendation tion model utilizing Knowledge Graph The research develops a hybrid recommenda-
Approach for content-based,context- (MKG): tion model for a heterogeneous music infor-
Heterogeneous In- based, and CF meth- Users7510 mation network using content-based, context-
formationNetwork ods,withfactorization Tracks11,184 based,andcollaborativefilteringmethods.
| usingFactorization | machines. | Artists30,012 | Results:  |                  |              |     |
| ------------------ | --------- | ------------- | --------- | ---------------- | ------------ | --- |
| Machines.          |           |               | FM offers | a novel approach | to analyzing | and |
comprehendingtherelationshipbetweenusers
andtracks.
[93] Identifying Study employed on- data collected Objectives:
UserNeedsforAd- linesurveyandremote through an online Thepurposeofthisstudywastobetterunder-
vertising Controls usabilitystudyforcol- survey standuserdesiresandworriesaboutFacebook
onFacebook lecting user data on advertisingrestrictions,evaluatetheefficiency
Facebook’sadvertising ofpresentcontrols,andidentifygapsinservice
|     | controls. |     | toimproveconformitywithuserexpectations. |     |     |     |
| --- | --------- | --- | ---------------------------------------- | --- | --- | --- |
Results:
Identifiyingusergoalsaswellasconcernswith
thediscoverabilityofFacebookadcontrols
[102] Active Ac- The project uses a De- The study used a Objectives:
tions in the Ex- sign Science Investi- datasetwith49,325 This work aims to map urban zones in Itajaí,
traction of Urban gation (DSR) method- instances and 18 Brazil, using machine learning approaches to
Objects for Infor- ology to improve in- variables to evalu- improveobjectdetectionandinformationqual-
mationQualityand formationqualityand atetheeffectiveness ityforlandmanagementandmonitoringdeci-
KnowledgeRecom- knowledgesuggestion ofseveralclassifiers sions.
mendation with using machine learn- incityobjectrecog- Results:
MachineLearning. ingtechniques. nition. Thestudyobtainedaclassificationaccuracyof
85.20%utilizingtheJ48decisiontreetechnique,
withakappastatisticof76.11%,demonstrating
|     |     |     | good object | identification | and information | ex- |
| --- | --- | --- | ----------- | -------------- | --------------- | --- |
tractionfromurbandata.

J.Imaging2025,11,12
53of66
TableA1.Cont.
| StudyIssue | EmployedStrategy |     | Dataset | Objectives/Results |     |     |
| ---------- | ---------------- | --- | ------- | ------------------ | --- | --- |
[65] Interpretable The hyper-network Dataset AADB Objectives:
Aesthetic Analysis combines attribute (10,000images)(11 integratingattributescoresandimplementing
Model for Intelli- scores and a method aestheticattributes) an attention mechanism to improve the inter-
gent Photography of attention to learn pretabilityofaestheticmodelsofevaluationfor
GuidanceSystems aesthetic evaluations improveduserinteraction
|     | and recognize | visual |     | Results:                                 |     |     |
| --- | ------------- | ------ | --- | ---------------------------------------- | --- | --- |
|     | features.     |        |     | ExtractionfeautureswithResNetwith101lay- |     |     |
ers
fullyconnectedneuralnetwork+ReLU
[66] Learning GUI The study determines Varyingbuttons Objectives:
Completions with element insertion Rico(NDN) creatingmachine-learning-basedlayoutrecom-
User-defined Con- and placement for a Artificialweb mendationtechniquestoguaranteeconsistency
straints. consistent GUI layout Enrico ingraphicaluserinterfaces(GUIs),withanem-
|     | acrossscreensbycom- |             |     | phasisonimplicitlayoutpatterns. |     |     |
| --- | ------------------- | ----------- | --- | ------------------------------- | --- | --- |
|     | bining              | graph-based |     | Results:                        |     |     |
|     | and sequence-based  |             |     | kNN(95%matchscores)             |     |     |
|     | approaches.         |             |     | GNN(20–50validresults)          |     |     |
Transformermodel(30–50%)
Enrico(≤30%)
| [68] Model-driven | MDD | platforms, | 30MDDplatforms | Objectives: |     |     |
| ----------------- | --- | ---------- | -------------- | ----------- | --- | --- |
development plat- decision-making ap- and 94 MDD fea- Model-drivendevelopmentplatformselection:
formselection: four proach, and quality tures fourindustrycasestudies
| industry case | stud- attributeinformation. |     |     | Results:     |                |              |
| ------------- | --------------------------- | --- | --- | ------------ | -------------- | ------------ |
| ies           |                             |     |     | The decision | support system | (DSS) recom- |
mendedfourpotentialMDDplatformsoutof
30,andfivesolutionsinanothercasestudy. The
decisionmodelconsidered75criterias.
[69] Multiple Using the T-SF frame- Dataset available Objectives:
criteria decision work, a new eval- from (Mr Chen, The paper uses T-spherical fuzzy (T-SF) struc-
analyticmethodsin uation process and TingYu) tures and Minkowski distance indices to pro-
management with decision-analytic ap- vide a unique architecture and technique for
T-spherical fuzzy proachforambiguous multiplecriteriondecisionanalysiswithuncer-
| information. | multi-criteria   | evalua- |     | tainty.  |     |     |
| ------------ | ---------------- | ------- | --- | -------- | --- | --- |
|              | tionweredevised. |         |     | Results: |     |     |
AnovelT-SF-basedappraisalmechanismand
adecision-analyticmethodformultiple-criteria
assessmentunderuncertainconditions.
[67] Multi-source Graph models, fuzzy DBP-YAG, DFB, Objectives:
knowledge fusion: set theory, D-S the- DBP15k (ZH-EN), Thegoalofthisstudyistopresentasurveyof
asurvey. ory, CNN and VAE YAGO3 multi-source knowing fusion research and to
|     | Bayesiananalysis |     |     | analyzeitscurrentstatusandfuturepotential. |     |     |
| --- | ---------------- | --- | --- | ------------------------------------------ | --- | --- |
Results:
|     |     |     |     | The study | presents a classification | of research |
| --- | --- | --- | --- | --------- | ------------------------- | ----------- |
progressinmulti-sourceknowledgefusionand
discusses

J.Imaging2025,11,12
54of66
TableA1.Cont.
| StudyIssue |     | EmployedStrategy |           | Dataset |            | Objectives/Results |     |     |
| ---------- | --- | ---------------- | --------- | ------- | ---------- | ------------------ | --- | --- |
| [70]       |     | A study          | addresses | GVSET   | (24 source | Objectives:        |     |     |
NDNetGaming— numerous research video sequences VMAFandinnovativeapproachesareusedin
development of a problems by devel- from 12 different thedevelopmentofaCNNthatpredictsgame
| no-reference | deep       | oping        | a CNN-based | games) |            | videoquality. |     |     |
| ------------ | ---------- | ------------ | ----------- | ------ | ---------- | ------------- | --- | --- |
| CNN          | for gaming | no-reference | video       | KUGVD  | (6 videos, | Results:      |     |     |
video quality pre- quality rating for 90 videos se- The study creates a no-reference CNN model
diction. gaming footage influ- quences) forforecastinggamevideoqualitywhiletaking
encedbycompression intoaccountuniquegamingcharacteristics. The
|     |     | artifacts. |     |     |     | modelwastrainedusingVMAFandfine-tuned |              |              |
| --- | --- | ---------- | --- | --- | --- | ------------------------------------- | ------------ | ------------ |
|     |     |            |     |     |     | with subjective                       | assessments. | A new method |
|     |     |            |     |     |     | oftemporalpoolingisproposed.          |              | Highperfor-  |
manceacrossavarietyofcontentsanddatasets.
| [71] | Ontology- | Article | proposes | The | dataset com- | Objectives: |     |     |
| ---- | --------- | ------- | -------- | --- | ------------ | ----------- | --- | --- |
basedSoftComput- (multi-level K-mean prises of 9263 The MLK-rBO model combines clustering,
ing and Machine clustering) MLK-rBO respondents’ re- knowledgediscovery,andBayesiannetworkap-
Learning. model: clustering, sponses collected proachestoensurereliableknowledgeretrieval
|     |     | knowledge | discovery, | over | 4 years | indomainontologies. |     |     |
| --- | --- | --------- | ---------- | ---- | ------- | ------------------- | --- | --- |
Results:
|     |     | probabilistic | network, | (2018–2022), | con- |     |     |     |
| --- | --- | ------------- | -------- | ------------ | ---- | --- | --- | --- |
ensembleapproach. centratingonfever Accordingtotheexperimentaldata,theMLK-
|     |     |     |     | state            | and related | rBOmodeldescribedinthestudyoutperformed |     |     |
| --- | --- | --- | --- | ---------------- | ----------- | --------------------------------------- | --- | --- |
|     |     |     |     | characteristics. |             | othermodelssuchasDT,RF,andSVMwithan     |     |     |
accuracyof98.36%.
| [72] | OpExHAN: | The study | uses | a OpExHAN | model | Objectives: |     |     |
| ---- | -------- | --------- | ---- | --------- | ----- | ----------- | --- | --- |
opinion extraction hierarchical attention applied on Ama- Thisresearchcreatesahierarchicalattentionnet-
using hierarchical network to extract zon Smartphone work to extract opinions from smartphone re-
attention network opinionsfromreviews, dataset from ama- viewsonAmazon,resultinginpreciseproduct
from unstructured with good accuracy, zonin 150,000 classificationandfeaturesummaries.
| reviews. |     | precision, | and recall | reviews | scrapped, | Results: |     |     |
| -------- | --- | ---------- | ---------- | ------- | --------- | -------- | --- | --- |
on Amazon’s Smart- 56,000collected. Highaccuracy(94.68%),precision91.67%,and
|     |     | phone’sreviews. |     |     |     | recall(91.25%) | are attained | by the OpExHAN |
| --- | --- | --------------- | --- | --- | --- | -------------- | ------------ | -------------- |
modelfollowinghyperparametertesting. 16is
theidealbatchsizeforresults.
[90] Performance The study made use The Multi-codec Objectives:
analysis of H2BR: of the HTTP/2-based DASHdatasetwas The goal of this research is to assess the per-
HTTP/2-based H2BRapproach,which utilized in this formanceoftheHTTP/2-BasedRetransmission
segmentupgrading involveslatetransmis- study to evaluate (H2BR)approachinavarietyofscenariosand
toimprovetheQoE sions of better video performanceacross compareittopreviousstudies.
| inHAS. |     | portions | that are pre- | multiple | video | Results: |     |     |
| ------ | --- | -------- | ------------- | -------- | ----- | -------- | --- | --- |
viously stored in the codecsandstream- The study presents performance metrics for
clientbufferinorderto ing situations. H2BR across different configurations, demon-
enhancevideoquality. Different segment stratingitseffectivenessinhigh-throughputnet-
|     |     |     |     | durationsof1s,2s, |              | workswithvaryingparameters. |     |     |
| --- | --- | --- | --- | ----------------- | ------------ | --------------------------- | --- | --- |
|     |     |     |     | 4 s,              | and 6 s from |                             |     |     |
YouTube.

J.Imaging2025,11,12
55of66
TableA1.Cont.
| StudyIssue | EmployedStrategy | Dataset | Objectives/Results |     |     |     |
| ---------- | ---------------- | ------- | ------------------ | --- | --- | --- |
[33] Presenting a A hybrid approach Researchers exam- Objectives:
hybridmodelinso- combiningfundamen- ined a LinkedIn The study’s goal is to create a hybrid recom-
cial networks rec- tal collaborative filter- dataset from a mendationsystemthatemployssupply-chain
ommendation sys- ing and demographic specific location, management and organizational communica-
temarchitecturede- recommendation sys- which included tionprinciplestosuggestorganizationalmem-
velopment. tems, using artificial 1404 users’ inter- bersinsocialnetworks. Thissystemwillhope-
neuralnetworks, data ests in followed fullysolveproblemswithtraditionalrecommen-
mining, and fuzzy firms across five dation systems, such as diversity, scalability,
|     | techniques. | industries and     | five cold-start,andserendipity. |                         |              |          |
| --- | ----------- | ------------------ | ------------------------------- | ----------------------- | ------------ | -------- |
|     |             | services,foratotal | Results:                        |                         |              |          |
|     |             | of9891interests.   | A hybrid                        | recommendation          | system       | that ad- |
|     |             |                    | dressed                         | issues with cold-start, | scalability, | va-      |
riety,andserendipityinsocialnetworksugges-
|     |     |     | tionswaspresentedinthestudy. |                    | Itperformed   |       |
| --- | --- | --- | ---------------------------- | ------------------ | ------------- | ----- |
|     |     |     | faster and                   | more accurately    | than existing | tech- |
|     |     |     | niques.                      | Recall, Precision, | MAE, RMSE,    | and   |
otherevaluationmeasureswereutilizedtoshow
|     |     |     | how well                           | the hybrid system | performed | while |
| --- | --- | --- | ---------------------------------- | ----------------- | --------- | ----- |
|     |     |     | recommendingusersinsocialnetworks. |                   |           | Inthe |
future,thesetechniqueswillbecombinedwith
geneticalgorithmstogetbetteroutcomes,and
theirtestingonmoresocialnetworkswillbein-
vestigated.
| [36] Quality- | To recommend | ed- Notavailable | Objectives: |     |     |     |
| ------------- | ------------ | ---------------- | ----------- | --- | --- | --- |
driven Open ucational resources, The paper presents QORECT, a hybrid archi-
educational re- a hybrid technique tecture that recommends open-source course-
source/courseware that combines user ware (OCW) as well as open educational re-
case-based REC- feedback, case-based sources (OERs) by fusing a quality-driven ap-
ommending recommending, and proachwithuserfeedback. Itseekstoenhance
Tenet(QORECT)— a quality model is thesuggestionprocessbycase-basedrecommen-
a Case-Based employed. Case-Based dationsanduserinvolvement,henceimproving
Framework for Reasoning (CBR) is thefindabilityofvariededucationalresources.
Quality-based Rec- used in the study to Thestudyaimstocreateaworkingmodelsys-
ommending Open extract solutions from tem for computer science students, assess the
Courseware and earlier instances of quality of the available resources, and deter-
Open Educational related issues. The minewhetherthesystemcanbeimplemented
Resources k-Nearest Neighbors successfullyinvariouslearningenvironments.
|     | (kNN) technique | is  | Automatingtaskstodevelopacustomizedand |     |     |     |
| --- | --------------- | --- | -------------------------------------- | --- | --- | --- |
used by the system to efficientadaptiverecommendersystemisone
|     | identify comparable |     | ofthefutureobjectives. |     |     |     |
| --- | ------------------- | --- | ---------------------- | --- | --- | --- |
Results:
|     | situations and | adds |     |     |     |     |
| --- | -------------- | ---- | --- | --- | --- | --- |
new data in order to TheQORECThybridarchitectureissuggestedby
|     | continuallylearn. |     | thestudyasamethodforpromotingopeneduca- |     |              |     |
| --- | ----------------- | --- | --------------------------------------- | --- | ------------ | --- |
|     |                   |     | tionalresourcesandcourseware.           |     | Inadditionto |     |
creatingtheprototypesystem,theresearchersare
presentlyassessingthecaliberofresourcesavail-
abletostudentsstudyingcomputerscience.One
ofthefirstobjectivesistotesttheprototypeon
|     |     |     | studentsinordertoevaluateitsefficacy. |     |     | Future |
| --- | --- | --- | ------------------------------------- | --- | --- | ------ |
planscallforautomatinganumberofframework
operationstoimprovesuggestionandadaptabil-
|     |     |     | ity. Theultimategoalistodevelopanexcellent |     |     |     |
| --- | --- | --- | ------------------------------------------ | --- | --- | --- |
individualizedadaptiverecommendersystemfor
users’learningneeds.

J.Imaging2025,11,12
56of66
TableA1.Cont.
| StudyIssue     | EmployedStrategy |     | Dataset         |     | Objectives/Results |     |     |     |     |
| -------------- | ---------------- | --- | --------------- | --- | ------------------ | --- | --- | --- | --- |
| [75] Revealing | A mixed-methods  |     | A questionnaire |     | Objectives:        |     |     |     |     |
the Construction research study con- dataset was em- ThepurposeofthestudyistoevaluateJakarta’s
Project Manage- ducted in Jakarta ployedinaJakartan current urban park building project manage-
ment System of evaluated the city study to evaluate ment system, pointing out flaws and making
CityParkinJakarta: parks’ construction factors pertaining suggestions for enhancement. It focuses on
BetweenHopeand project management to community evaluating the municipal parks’ construction
Reality. system. In order to involvement, project management system in order to learn
improve park quality, park quality, and moreabouttheareasthatcanbeimprovedand
|     | the emphasis   | was  | municipalparkde- |         | thecurrentstateofaffairs. |     |     |     |     |
| --- | -------------- | ---- | ---------------- | ------- | ------------------------- | --- | --- | --- | --- |
|     | on identifying | gaps | velopment        | project | Results:                  |     |     |     |     |
in pre-construction management. Cal- The pre-construction phase and stakeholder
management and culating average involvement of Jakarta’s city park manage-
stakeholder interac- scores and classi- ment system fell short of expectations. The
tion. The process of fying them into attainment of the intended park quality was
dataanalysisincluded interval classes for hamperedbyinadequatemanagementofcon-
determining average assessment were struction projects, particularly during the pre-
ratingsforathorough part of the data constructionphaseandcommunityengagement.
assessment. analysisprocess. Theresultsoftheassessmentshowedthatdif-
ferentcityparkshaddifferentbuildingproject
outcomes,withcertainparksreceivinghigher
|     |     |     |     |     | scoresforqualitycharacteristics. |     |              | Tomeetpeo- |        |
| --- | --- | --- | --- | --- | -------------------------------- | --- | ------------ | ---------- | ------ |
|     |     |     |     |     | ple’ expectations                | for | high-quality | city       | parks, |
moreresearchisadvisedtoobtainadeeperun-
derstandingofthepre-constructionphaseand
|     |     |     |     |     | stakeholderinvolvement. |     | Inordertoraisethe |     |     |
| --- | --- | --- | --- | --- | ----------------------- | --- | ----------------- | --- | --- |
generalstandardofJakarta’smunicipalparks,
|     |     |     |     |     | future research | might | focus on | improving | the |
| --- | --- | --- | --- | --- | --------------- | ----- | -------- | --------- | --- |
administrationofconstructionprojects,particu-
larlyduringthepre-constructionstageandcom-
munityengagement.
[34] RTiSR: a Bi-directional Long The datasets used Objectives:
review-driventime Short-Term Memory in this study are This work aims to propose and assess the ef-
interval-aware (BiLSTM) and CNN from Yelp from ficacy of a sequential recommendation model
sequential recom- areusedintheworkto theYelpChallenge that integrates user reviews, time intervals,
mendationmethod. capturevariableorder 2019aswellasMu- and sequence patterns: the review-driven
aggregate sequence sical Instruments timeinterval-awaresequentialrecommendation
|     | dependencies. |     | (MIs), Automotive |           | (RTiSR)model. |            |                        |               |     |
| --- | ------------- | --- | ----------------- | --------- | ------------- | ---------- | ---------------------- | ------------- | --- |
|     |               |     | (Auto),           | Luxury    | Results:      |            |                        |               |     |
|     |               |     | Beauty            | (LB), and | The research  | discovered | that on                | all datasets, |     |
|     |               |     | BeerfromAmazon.   |           | increasing    | the depth  | size (h) significantly |               | en- |
hancedrecommendationperformance,withh
|     |     |     |     |     | =3demonstratingthegreatestresults. |     |     |     | Further- |
| --- | --- | --- | --- | --- | ---------------------------------- | --- | --- | --- | -------- |
more,suggestionperformanceimprovedasthe
|     |     |     |     |     | latent factor’s | size increased; | the | optimal | per- |
| --- | --- | --- | --- | --- | --------------- | --------------- | --- | ------- | ---- |
formancewasattainedatalatentfactorsizeof
|     |     |     |     |     | 50. RTiSR | achieved the | best performance |     | and |
| --- | --- | --- | --- | --- | --------- | ------------ | ---------------- | --- | --- |
highestF-rankvalueacrossalldatasets,consis-
|     |     |     |     |     | tentlyoutperformingmostbaselines. |     |     | Theexper- |     |
| --- | --- | --- | --- | --- | --------------------------------- | --- | --- | --------- | --- |
imentalresultsconsistentlyshowedthatRTiSR
ismoreeffectiveandsuperiortonumerousstate-
of-the-artmodelsintermsofHRandNDCG.

J.Imaging2025,11,12
57of66
TableA1.Cont.
| StudyIssue | EmployedStrategy |     | Dataset |     | Objectives/Results |     |     |     |
| ---------- | ---------------- | --- | ------- | --- | ------------------ | --- | --- | --- |
[76] Selecting Because of its flexibil- 18,798 articles Objectives:
the appropriate ity, speed of process- with abstracts ex- Thepaperdiscussestheimportanceofselecting
leading journal in ing,andtextdatabase tactedfromScopus anacademicjournalthatmeetstherequirements
Hospitality and processingtools,Rsoft- database ofthejournalandthestudytopicinordertoas-
Tourism research: wareisusedinthispa- sistresearchersinmakingtheproperchoice. It
a guide based on pertoanalyzetextdata. alsooffersaguidancethatconsidersthetopic–
thetopic-journalfit Excel and SPSS V. 26 journal fit and JCR impact factor, as well as a
andtheJCRimpact were also utilized in tool to gauge this fit for journals in the travel
| factor. | thedataanalysis. |     |     |     | andhospitalityindustries. |     |     |     |
| ------- | ---------------- | --- | --- | --- | ------------------------- | --- | --- | --- |
Results:
|     |     |     |     |     | The study     | used corrected   | standardized         | resid-  |
| --- | --- | --- | --- | --- | ------------- | ---------------- | -------------------- | ------- |
|     |     |     |     |     | uals to       | determine the    | degree of fit and    | statis- |
|     |     |     |     |     | tically       | measured the fit | of research subjects | in      |
|     |     |     |     |     | each journal, | emphasizing      | the significance     | of      |
topic–journalfitinconnectiontotheimpactfac-
tor.
| [77] | Self- This | paper presents | Two | sizable | Objectives: |     |     |     |
| ---- | ---------- | -------------- | --- | ------- | ----------- | --- | --- | --- |
supervised Learn- a framework for datasets were Thisstudyproposesamulti-taskself-supervised
ing for Large-scale large-scale item employed in the learning (SSL) framework to tackle the label
ItemRecommenda- recommendations study: an AAI sparsityissueinlarge-scaleitemrecommenda-
tions. using multi-task self- dataset gathered tions. It aims to enhance item representation
supervised learning. from a for-profit learning,regularizethemodelforimprovedgen-
It integrates a new mobile app shop eralization,andleveragefeaturecorrelationsfor
technique for data (5.3 million ques- dataaugmentation. Theresearchexploresthe
augmentation based tions, 5.3 million impact of training data size on SSL improve-
onfeaturecorrelations. items) and a ments, examines SSL parameters such as loss
Enhancing training Wikipedia dataset multiplieranddropoutrate,andcomparesthe
datawithvariousdata (2.4millionqueries, performanceofRandomFeatureMasking(RFM)
augmentationsandsu- 2.4 million items) with(CorrelatedFeatureMasking)CFM.
|     | pervisedtasksarepart |     | that was | centered | Results: |     |     |     |
| --- | -------------------- | --- | -------- | -------- | -------- | --- | --- | --- |
of the self-supervised on link prediction Thestudydemonstratesthat,whenitcomesto
learning framework. betweenWikipedia improving model performance for large-scale
Thesetasksfunctionas pages. itemsuggestions,SSLregularizationworksbet-
|     | support | assignments |     |     | terthanconventionalmethods. |     | Thisisdemon- |     |
| --- | ------- | ----------- | --- | --- | --------------------------- | --- | ------------ | --- |
for tasks that predict strated by the fact that, in live traffic experi-
orreconstructoriginal ments,itoutperformsthemostadvancedtech-
|     | examples. |     |     |     | niquesandachievesnotablegainsinbusiness |                 |               |          |
| --- | --------- | --- | --- | --- | --------------------------------------- | --------------- | ------------- | -------- |
|     |           |     |     |     | KPIs. The                               | results further | highlight the | signifi- |
canceofchoosingtherightparametersbyshow-
ingthatmodelperformancecanbenegatively
impactedbydropoutratesandSSLweightsthat
aretoohigh.

J.Imaging2025,11,12
58of66
TableA1.Cont.
| StudyIssue | EmployedStrategy |     | Dataset | Objectives/Results |     |     |
| ---------- | ---------------- | --- | ------- | ------------------ | --- | --- |
[80] Short text The study uses a The dataset used Objectives:
topic modeling complete survey and in this study is Theobjectiveofthisstudyistoprovideacom-
approaches in the classification of brief the Google News prehensivereviewandtaxonomyofshorttext
contextofbigdata: text Topic Modeling dataset,whichcon- topicmodeling,aimingtoassistresearchersin
taxonomy, survey, (STTM) algorithms, tains excerpts and understandingthekeyelementsofSTTM,iden-
andanalysis. together with qualita- titles from 11,109 tifying limitations of existing techniques, and
tive and quantitative news stories orga- guidingfutureresearchdirectionsinthefield.
|     | assessments, | to evalu- | nizedinto152clus- | Results: |     |     |
| --- | ------------ | --------- | ----------------- | -------- | --- | --- |
ate their performance ters. Furthermore, Thestudycomparedtheperformanceofshort
and efficacy in topic thedatasetincludes text topic modeling algorithms on RW-Pand-
finding from short the Web Snippet Twitter and RW-CB-Twitter datasets with dif-
texts. dataset,whichcon- ferent number of topics (k = 5, 7, 20, 40, 60,
|     |     |     | tains 12,340 web    | 80).Differentmodelswereevaluatedusingmea-   |     |     |
| --- | --- | --- | ------------------- | ------------------------------------------- | --- | --- |
|     |     |     | search snippets or- | sureslikeascoherence,perplexity,PMI/NPMI,   |     |     |
|     |     |     | ganized into eight  | NMI,purity,ARI,AMI,entropy,accuracy,recall, |     |     |
|     |     |     | groups.             | precision,andF-measuretodemonstratetheir    |     |     |
efficacyinhandlingbrieftextinput.
Objectives:
| [81] Society’s | Atti- TheSociety’sAttitudes |     | Thestudy’sdataset |     |     |     |
| -------------- | --------------------------- | --- | ----------------- | --- | --- | --- |
tudesTowardsHu- Towards Human comprised two Thegoaloftheprojectwastoclosearesearch
manAugmentation Augmentation and online surveys gaponthesocietaleffectsofhumanaugmenta-
and Performance PerformanceEnhance- administered tiontechnologybycreatingandvalidatingthe
EnhancementTech- ment Technologies through Qualtrics SHAPEScale,atoolformeasuringpublicatti-
nologies (SHAPE) (SHAPE) were devel- software, with 103 tudestowardaugmentedhumans. Richquanti-
Scale. oped and assessed respondents in the tativedatagatheringandcross-studycompar-
in the study using first round and 78 isonsaremadepossiblebythescale,whichof-
a mixed-methods respondents in the fersaconsistentandvalidmeansofmeasuring
methodology. These second. opinionsregardingenhancedpeople. Research
|     | methods      | included    |     | onviewsregardinghumanenhancementtech-        |                             |              |
| --- | ------------ | ----------- | --- | -------------------------------------------- | --------------------------- | ------------ |
|     | confirmatory | and         |     | nologyisintendedtobeadvancedbyitsintro-      |                             |              |
|     | exploratory  | factor      |     | duction.                                     |                             |              |
|     | analysis,    | online sur- |     | Results:                                     |                             |              |
|     | veys,        | and expert  |     | Throughexpertreviewsandexploratorycompo-     |                             |              |
|     | interviews.  |             |     | nentanalysis,thestudyestablishedthethirteen- |                             |              |
|     |              |             |     | item SHAPE                                   | Scale and confirmed         | its validity |
|     |              |             |     | andreliability.                              | Thescaleisausefultoolforre- |              |
searchersandpractitionersasithelpstounder-
standhowsocietyviewshumanaugmentation
|     |     |     |     | technologies. | Inordertoinformthedesignand |     |
| --- | --- | --- | --- | ------------- | --------------------------- | --- |
acceptabilityoffutureaugmentationtechnolo-
|     |     |     |     | gies, the | research emphasizes | the importance |
| --- | --- | --- | --- | --------- | ------------------- | -------------- |
ofevaluatingandmonitoringsocietyattitudes
towardenhancedhumans.

J.Imaging2025,11,12
59of66
TableA1.Cont.
| StudyIssue      | EmployedStrategy |       |      | Dataset |         |     | Objectives/Results |     |     |     |     |     |     |
| --------------- | ---------------- | ----- | ---- | ------- | ------- | --- | ------------------ | --- | --- | --- | --- | --- | --- |
| [82] SpeechQoE: | A The            | study | uses | The     | dataset | in- | Objectives:        |     |     |     |     |     |     |
NovelPersonalized speech signals to cludes38individu- ThepaperproposesSpeechQoE,atailoredap-
QoE Assessment estimate individual als (23 males and proachthatusesspeechsignalstoquantifyindi-
Model for Voice ratings of quality 15 females) who vidualevaluationsofqualityinvoiceservices.It
ServicesviaSpeech in voice services, completed200call- overcomesconstraintsbyusingfew-shotlearn-
Sensing. adopting a tailored ing sessions while ingandefficientdatasynthesistorapidlyadapt
quality of experi- assessing their tonewusers. Thestudy’sgoalistoincreasethe
ence(QoE)assessment perceived quality precisionandeffectivenessofQoEevaluationin
approach called of experience, voiceservicesbyprioritizinguser-specificeval-
SpeechQoE. making it the first uationandaccountingforperceivedvariability.
|     |     |     |     | medium-scaleQoE-   |     |         | Results: |            |            |          |             |                  |     |
| --- | --- | --- | --- | ------------------ | --- | ------- | -------- | ---------- | ---------- | -------- | ----------- | ---------------- | --- |
|     |     |     |     | labeled            |     | dataset | The      | SpeechQoE  |            | model    | obtained    | an outstand-     |     |
|     |     |     |     | for conversational |     |         | ing      | 91.4%      | accuracy   | in       | assessing   | QoE, exceed-     |     |
|     |     |     |     | voiceservices.     |     |         | ing      | previous   | solutions. |          | It achieved | constant         |     |
|     |     |     |     |                    |     |         | high     | accuracies |            | of 90.9% | for         | college students |     |
and91.4%fornon-collegestudents,demonstrat-
|     |     |     |     |     |     |     | ing | its usefulness |     | across | a wide | range of | user |
| --- | --- | --- | --- | --- | --- | --- | --- | -------------- | --- | ------ | ------ | -------- | ---- |
backgrounds.Thestudyunderlinedthemodel’s
capacitytocapturetheeffectofambientnoise
onQoEperception,showingitssuperiorityover
typicalparametricmodels.
[83] Supporting The study evaluated Three senior re- Objectives:
Shy Preschool theeffectsofapplying searchersexamined This study examined the effects of using Sto-
ChildreninJoining Tools of the Mind thestudy’ssession ryCarnival,avoiceagent,inToolsoftheMind
Social Play Flan- (ToM)-style playing videorecordsusing (ToM)-style activities to encourage sociodra-
nery. with and without standard content matic play among reticent preschoolers. It fo-
technologyaidsusing analysis. They cusedonintegratingshykidsintoplaysessions
a content analysis usedLucidchartto by comparing the behaviors of kids with and
technique. It high- organize894sticky without StoryCarnival. Another goal of the
lighted the critical notes into subjects studywastofindoutifthevoiceagent,inpartic-
rolethatavoiceagent and subtopics ular,mightimprovesocialinteractionandchild
playsinincorporating across numerous engagementinsociodramaticplayactivitiesfor
|     | shy                | preschoolers | into | sessions, | based   | on      | childrenagedthreetofive.                   |              |               |       |            |                   |     |
| --- | ------------------ | ------------ | ---- | --------- | ------- | ------- | ------------------------------------------ | ------------ | ------------- | ----- | ---------- | ----------------- | --- |
|     | sociodramaticplay. |              |      | shape     | and     | color   | Results:                                   |              |               |       |            |                   |     |
|     |                    |              |      | coding    | to      | distin- | Thestudyshowedthatintegratingtechnology    |              |               |       |            |                   |     |
|     |                    |              |      | guish     | between |         | supportsintosociodramaticplaysessions,such |              |               |       |            |                   |     |
|     |                    |              |      | sessions  | and     | age     | as                                         | the physical |               | voice | agent      | in StoryCarnival, |     |
|     |                    |              |      | groups    |         |         | wasaneffectivewaytoincludeshypreschoolers. |              |               |       |            |                   |     |
|     |                    |              |      |           |         |         | Children’s                                 |              | interactions, |       | linguistic | exchanges,        |     |
andlevelofinvolvementallrosewhentechnol-
|     |     |     |     |     |     |     | ogysupportswerepresent. |               |        |        | Theresultsindicate |               |     |
| --- | --- | --- | --- | --- | --- | --- | ----------------------- | ------------- | ------ | ------ | ------------------ | ------------- | --- |
|     |     |     |     |     |     |     | that                    | StoryCarnival |        | has    | a promising        | long-term     |     |
|     |     |     |     |     |     |     | influence               |               | on the | social | skills             | and inclusion | of  |
shychildren,withnosignsofdecliningeffects
overtime.

J.Imaging2025,11,12
60of66
TableA1.Cont.
| StudyIssue |     | EmployedStrategy |     | Dataset |     |     | Objectives/Results |     |     |
| ---------- | --- | ---------------- | --- | ------- | --- | --- | ------------------ | --- | --- |
[78] Task Force Re- The study used a fi- To gather informa- Objectives:
port 6. Report on nancialmodelingtech- tion, the authors Thegoalofthisresearchistocreateafinancial
FinancingtheNew nique,inordertoeval- consulted experts model that evaluates how the New Model of
Model of Family uatetheNewModelof inpracticemanage- Careaffectspracticefinancesandoffershealth-
Medicine. Care’s effect on prac- ment, healthcare care finance recommendations to support pri-
tice finances and sug- finance, health mary care in the US over the ensuing few
|     |     | gest health   | care | finan- economics,      |     | and | decades. |     |     |
| --- | --- | ------------- | ---- | ---------------------- | --- | --- | -------- | --- | --- |
|     |     | cial policies | that | will healthpolicyinad- |     |     | Results: |     |     |
supportprimarymedi- ditiontopublished Accordingtothestudy,familyphysicianscould
calcareintheUS. medical literature seea26%increaseinpayunderthecurrentfee-
|     |     |     |     | and               | practice | man- | for-servicesystemiftheNewModelofcareis |                             |     |
| --- | --- | --- | --- | ----------------- | -------- | ---- | -------------------------------------- | --------------------------- | --- |
|     |     |     |     | agementdatabases. |          |      | implemented.                           | Thereisalsoroomforfuturein- |     |
creasesthroughchangestothereimbursement
|     |     |     |     |     |     |     | structure and | the implementation | of quality- |
| --- | --- | --- | --- | --- | --- | --- | ------------- | ------------------ | ----------- |
basedincentiveprograms.
| [84] | Techno- | The study | used | an Thestudyincludes |     |     | Objectives: |     |     |
| ---- | ------- | --------- | ---- | ------------------- | --- | --- | ----------- | --- | --- |
distress and anonymous sur- a total of 55 ques- Thegoalofthisresearchistocreateandvalidate
parental burnout: vey (https://www. tions that span a unified theory of techno-distress burnout in
The impact of questionpro.com/, many views, such familieswhoassisttheirchildrenwithtechnol-
home facilitating accessdate28October as home work- ogyfordistantclasses,inordertobetterunder-
conditions and the 2023) that was deliv- ing conditions (6 standtheinfluenceoftechno-distressonparent
systemquality. ered online via the questions), frame- burnout.
|     |     | QuestionPro | platform | work | quality | (5  | Results: |     |     |
| --- | --- | ----------- | -------- | ---- | ------- | --- | -------- | --- | --- |
to gather information questions), techno- The study outcomes reveal that both home
on parental burnout, logical issues (18 setting and system quality impact parent’s
techno-distress, sys- questions),parental techno-distress,whichinchangegreatlyimpacts
temquality,andhome exhaustion (23 parental burnout. This highlights the impor-
enablingconditions. questions) and tanceofaddressingthesefactorstomitigatethe
|     |     |     |     | 3          | demographic |     | adverseimpactsofutilizingtechnologyinedu- |     |     |
| --- | --- | --- | --- | ---------- | ----------- | --- | ----------------------------------------- | --- | --- |
|     |     |     |     | questions. |             |     | cationalinstitutions.                     |     |     |
[85] The Impact The study discovered Thestudy’sdataset Objectives:
of Expertise in the that individuals with comprises user Thisstudyexamineshowuserskillaffectsthe
LoopforExploring higher skills tend to interfaces for 3D quality of results and personal satisfaction in
Machine Rational- explore the remedy model simplifica- human-in-the-loopoptimization. Itfocuseson
ity. space considerably tion, summarized text,photo,and3Dmeshoptimizationsettings
more than novices, text, and image andintendstoprovideinsightsforfutureHIL
|     |     | matching     | a maximiz- | color | enhance- |       | systemsdesign. |     |     |
| --- | --- | ------------ | ---------- | ----- | -------- | ----- | -------------- | --- | --- |
|     |     | ing decision | strategy   | ment  | tasks.   | These | Results:       |     |     |
in which experts aim interfaces also Thestudyfoundthatnovicesmayattainexpert-
to terminate at satis- incorporatemecha- levelachievementinoutcomequality,although
faction, resulting in nismsforcollecting expertshavemoreexplicitlikes,discontent,and
increased discontent participant knowl- iterations. Novicesaremoresatisfiedandtermi-
|     |     | as more     | weaknesses | edge,                |     | ranking | natesooner. |     |     |
| --- | --- | ----------- | ---------- | -------------------- | --- | ------- | ----------- | --- | --- |
|     |     | in the      | system     | are variants,        |     | and as- |             |     |     |
|     |     | discovered. |            | sessingsatisfaction. |     |         |             |     |     |

J.Imaging2025,11,12
61of66
TableA1.Cont.
| StudyIssue | EmployedStrategy |     | Dataset |     | Objectives/Results |     |     |     |
| ---------- | ---------------- | --- | ------- | --- | ------------------ | --- | --- | --- |
[73]Two-sidedCali- The study uses max- The study makes Objectives:
brationforQuality- imum marginal rele- use of the Tenrec The study aims to provide quality-aware and
aware Responsible vance (MMR) rerank- dataset, which is two-sidedcalibratedsuggestionsbycomparing
Recommendation. ingtobalancearecom- a compilation of users’priorinterestdistributionsandensuring
mender system’s out- recommendation an overall target exposure distribution of dif-
putforimprovedrele- platforms from ferentitemcategorieswiththeproposedpost-
vanceandcalibration. Tencent’s feeds. It processingmethodcalledPersonalizedCalibra-
|     |     |     | focuses           | on the QK- | tionTargets(PCT).                               |                     |     |            |
| --- | --- | --- | ----------------- | ---------- | ----------------------------------------------- | ------------------- | --- | ---------- |
|     |     |     | articlesamplewith |            | Results:                                        |                     |     |            |
|     |     |     | annotated         | quality    | As evidenced                                    | by the experimental |     | conditions |
|     |     |     | information,which |            | and outcomes,                                   | the suggested       | PCT | technique  |
|     |     |     | includes          | 31,413     | beatsstate-of-the-artbaselinesinattainingbetter |                     |     |            |
|     |     |     | articles,         | 884,315    | user-levelcalibrationandguaranteeingsystem-     |                     |     |            |
|     |     |     | interactions,     | and        | levelcalibration.                               |                     |     |            |
19,965users.
[79]VoiceinWords: The study uses a The dataset in- Objectives:
A Mixed-Method mixed-method ap- cludes 2464 econ- Thegoalofthestudyistodeterminethecritical
Approach for proach, combining omyclassand1270 factorsinfluencingthemajoraspectsofairline
Decoding Digital sentimentanalysisand business class pas- servicequalityandtoexaminethecausalrela-
Footprints Using logistic regression, to senger data from tionshipbetweencustomerassessmentsofthe
OnlineReviews investigatetheconnec- threemajorairlines, qualityoftheservicesreceivedandtheironline
|     | tion between    | online | as well          | as ratings, | recommendations. |     |     |     |
| --- | --------------- | ------ | ---------------- | ----------- | ---------------- | --- | --- | --- |
|     | recommendations |        | recommendations, |             | Results:         |     |     |     |
made by customers and reviews from Thisresearchendeavorstoexaminethecausal
and their opinions on other users of relationshipbetweencustomerassessmentsof
the quality of airline https://www. airline service quality and their online recom-
services skytraxratings. mendations,allthewhileidentifyingcriticalfac-
|     |     |     | com/, access    | date | torsthatimpactcriticalaspectsofairlineservice |     |     |     |
| --- | --- | --- | --------------- | ---- | --------------------------------------------- | --- | --- | --- |
|     |     |     | 22September2023 |      | quality. QatarAirwaysreceivedthehighestrec-   |     |     |     |
ommendationrate(78%),followedbySingapore
Airlines(77%),andCathayPacific(66%).
[96]Vulnerabilities The study employs The dataset com- Objectives:
of Unattended five presentation at- prisesdigitalfacial In addition to suggesting a creative and suc-
Face Verification tack detection (PAD) artifacts produced cessfulfaceimpersonationpresentationattack
Systems to Facial- methods focusing on from 63 Chinese method,thepaperattemptstoexaminethesus-
Component-based texture, quality, and participants’frontal ceptibilitiesofunattendedverificationoffaces
Presentation At- structure clues, utiliz- face photos, with systemstofacial-component-basedpresentation
| tacks:AnEmpirical | ing linear | SVM and      | an emphasis | on     | attacks. |     |     |     |
| ----------------- | ---------- | ------------ | ----------- | ------ | -------- | --- | --- | --- |
| Study.            | linear     | discriminant | different   | facial | Results: |     |     |     |
analysis for classifica- featurestoevaluate The study shows that the suggested presenta-
tion. security flaws in tionattackbasedonfacialcomponentsperforms
|     |     |     | unmanaged    | face | better than                               | current attack | techniques, | which |
| --- | --- | --- | ------------ | ---- | ----------------------------------------- | -------------- | ----------- | ----- |
|     |     |     | verification | sys- | presentsaseriousrisktofaceverificationand |                |             |       |
|     |     |     | tems.        |      | presentingattackdetectionsystems.         |                |             |       |

J.Imaging2025,11,12
62of66
TableA1.Cont.
| StudyIssue |         | EmployedStrategy |     | Dataset     |      | Objectives/Results |     |     |     |     |
| ---------- | ------- | ---------------- | --- | ----------- | ---- | ------------------ | --- | --- | --- | --- |
| [103]      | A Semi- | To improve       | web | The dataset | used | Objectives:        |     |     |     |     |
Supervised Learn- service classification, in this study pro- Thegoalofthisresearchistoassesstheefficacy
ing Approach to the researchers used vides data on 2871 of the Semi-Supervised Learning Web Service
Quality-BasedWeb a semi-supervised genuineonlineser- Classification(SSL-WSC)algorithmforclassify-
Service Classifica- self-training system vices, 364 labeled ing web services using various base classifier
tion. that combines several services, and 2507 algorithms,aswellastoincreaseclassification
scoringmethodologies unlabeled data accuracyusingsemi-supervisedlearning.
|     |     | anddistancecomputa- |     | points | across nine | Results: |     |     |     |     |
| --- | --- | ------------------- | --- | ------ | ----------- | -------- | --- | --- | --- | --- |
tions. qualityfeatures. The study discovered that the SSL-WSC algo-
rithmoutperformedthesupervisedtechnique
inallclassifiers,withaverageimprovementsof
11.26%inF1-Score,9.43%inaccuracy,and9.53%
inprecision.
| [104] | Micro- | The study | predicts | The dataset | in- | Objectives: |     |     |     |     |
| ----- | ------ | --------- | -------- | ----------- | --- | ----------- | --- | --- | --- | --- |
Locational Fine PM10 levels using a cludes around 23 The goal of this research is to increase under-
Dust Prediction modeling technique million samples standing of the elements that influence PM10
Utilizing Machine that includes Long from 957 South levelsandpredictionaccuracybyaddingmicro-
LearningandDeep Short-Term Memory Korean air quality locationmeasurementsandusingatime-series
LearningModels. (LSTM)networks,Ran- monitoringstations dataset. Itaimstoreduceregionaldifferences
domForestRegression (2014–2020), with insurveillanceofairqualityandcontributeto
(RFR),XGBoost(XGB), an emphasis on improvingpublichealthbyprovidingaccurate
|     |     | andAdaBoost. |     | pollutants      | such as   | dataforresponsiblechoices.                  |             |            |                |        |
| --- | --- | ------------ | --- | --------------- | --------- | ------------------------------------------- | ----------- | ---------- | -------------- | ------ |
|     |     |              |     | PM10,SO2,CO,O3, |           | Results:                                    |             |            |                |        |
|     |     |              |     | andNO2,anduses  |           | The study                                   | produced    | the best   | performance    | in     |
|     |     |              |     | LSTM            | networks, | PM10predictingusingtheLSTMmodel,with        |             |            |                |        |
|     |     |              |     | RandomForestRe- |           | a Pearson                                   | correlation | of 0.6176, | as well        | as en- |
|     |     |              |     | gression,       | XGBoost,  | hanced                                      | accuracy by | including  | micro-location |        |
|     |     |              |     | and AdaBoost    | to        | characteristicsandaddressingdatashortageis- |             |            |                |        |
|     |     |              |     | anticipate      | PM10      | sues.                                       |             |            |                |        |
value.
References
1. Xu,L.;Sang,X.E-CommerceOnlineShoppingPlatformRecommendationModelBasedonIntegratedPersonalizedRecommen-
dation.Sci.Program.2022,2022,4823828.[CrossRef]
2. Hossain,I.;Palash,M.;Sejuty,A.;Tanjim,N.;Nasim,M.;Saif,S.;Suraj,A.;Haque,M.;Karim,N.ASurveyofRecommender
SystemTechniquesandtheEcommerceDomain.arXiv2022,arXiv:2208.07399.
3. Murillo,V.;Avendano,D.;Lopez,F.;Calleros,J.ASystematicLiteratureReviewontheHybridApproachesforRecommender
Systems.Comput.Sist.2022,26,357–372.[CrossRef]
4. Chen,R.;Hua,Q.;Chang,Y.;Wang,B.;Zhang,L.;Kong,X.Asurveyofcollaborativefiltering-basedrecommendersystems:From
traditionalmethodstohybridmethodsbasedonsocialnetworks.IEEEAccess2018,6,64301–64320.[CrossRef]
5. DeNadai,M.;Fabbri,F.;Gigioli,P.;Wang,A.;Li,A.;Silvestri,F.;Kim,L.;Lin,S.;Radosavljevic,V.;Ghael,S.;etal.Personalized
AudiobookRecommendationsatSpotifyThroughGraphNeuralNetworks. InProceedingsoftheWWW2024:TheACMWeb
| Conference,Singapore,13–17May2024; |     |     | pp.403–412. |     |     |     |     |     |     |     |
| ---------------------------------- | --- | --- | ----------- | --- | --- | --- | --- | --- | --- | --- |
6. Sahu,S.;Kumar,R.;Mohdshafi,P.;Shafi,J.;Kim,S.;Ijaz,M.AHybridRecommendationSystemofUpcomingMoviesUsing
SentimentAnalysisofYouTubeTrailerReviews.Mathematics2022,10,1568.[CrossRef]
7. Alamdari,P.;Navimipour,N.;Hosseinzadeh,M.;Safaei,A.;Darwesh,A.ASystematicStudyontheRecommenderSystemsin
theE-Commerce.IEEEAccess2020,8,115694–115716.[CrossRef]
8. Raza,S.;Rahman,M.;Kamawal,S.;Toroghi,A.;Raval,A.;Navah,F.;Kazemeini,A.AComprehensiveReviewofRecommender
Systems:TransitioningfromTheorytoPractice.arXiv2024,arXiv:2407.13699.
9. Souabi,S.;Retbi,A.;Idrissi,M.;Bennani,S.Recommendationsystemsone-learningandsociallearning:Asystematicreview.
Electron.J.e-Learn.2021,19,432–451.[CrossRef]

J.Imaging2025,11,12 63of66
10. Pande,C.; Witschel,H.; Martin,A.NewHybridTechniquesforBusinessRecommenderSystems. Appl. Sci. 2022,12,4804.
[CrossRef]
11. Da’u,A.;Salim,N.Recommendationsystembasedondeeplearningmethods:Asystematicreviewandnewdirections.Artif.
Intell.Rev.2020,53,2709–2748.[CrossRef]
12. Isinkaye,F.;Folajimi,Y.;Ojokoh,B.Recommendationsystems:Principles,methodsandevaluation.Egypt.Inform.J.2015,16,
261–273.[CrossRef]
13. Dixit,V.;Gupta,S.;Jain,P.APropoundHybridApproachforPersonalizedOnlineProductRecommendations.Appl.Artif.Intell.
2018,32,785–801.[CrossRef]
14. Rhanoui,M.;Mikram,M.;Yousfi,S.;Kasmi,A.;Zoubeidi,N.Ahybridrecommendersystemforpatrondrivenlibraryacquisition
andweeding.J.KingSaudUniv.-Comput.Inf.Sci.2022,34,2809–2819.[CrossRef]
15. Liu,D.;Li,J.;Du,B.;Chang,J.;Gao,R.;Wu,Y.Ahybridneuralnetworkapproachtocombinetextualinformationandrating
informationforitemrecommendation.Knowl.Inf.Syst.2021,63,621–646.[CrossRef]
16. Bablani,D.;Gupta,R.;Gokhale,T.HybridApproachtoMusicRecommenderSystems. Int.J.Res.Appl.Sci.Eng.Technol.2022.
17. Paranjape,V.;Nihalani,N.;Mishra,N.DesignandDevelopmentofanEfficientDemographic-basedMovieRecommenderSystem
usingHybridMachineLearningTechniques.Int.J.Comput.Commun.Control2024,19,5840.[CrossRef]
18. Gordillo, A.; López-Fernández, D.; Verbert, K. Examining the usefulness of quality scores for generating learning object
recommendationsinrepositoriesofopeneducationalresources.Appl.Sci.2020,10,4638.[CrossRef]
19. Azzam,M.HybridMusicRecommendationApproachforHeterogeneousInformationNetworkUsingFactorizationMachines;Johannes
KeplerUniversitätLinz:Linz,Austria,2021.
20. Zheng,Y.Multi-stakeholderPersonalizedLearningwithPreferenceCorrections.InProceedingsofthe2019IEEE19thInternational
ConferenceonAdvancedLearningTechnologies(ICALT),Maceió,Brazil,15–18July2019;pp.66–70.
21. Kähärä, T.; Haataja, K.; Toivanen, P. Towards more accurate and intelligent recommendation systems. In Proceedings of
theInternationalConferenceonIntelligentSystemsDesignandApplications,ISDA,Okinawa,Japan,27–29November2014;
pp.165–171.
22. Nithya,B.;Geetha,D.;Kumar,M.Metaheuristic-AssistedContextualPost-FilteringMethodforEventRecommendationSystem.
Int.J.ImageGraph.2023,29,2550043.[CrossRef]
23. Murciego,Á.;Jiménez-Bravo,D.;Román,A.;Santana,J.;Moreno-García,M.Context-awarerecommendersystemsinthemusic
domain:Asystematicliteraturereview.Electronics2021,10,1555.[CrossRef]
24. Çano,E.; Morisio,M.Hybridrecommendersystems: Asystematicliteraturereview. Intell. DataAnal. 2017,21,1487–1524.
[CrossRef]
25. Uta,M.;Felfernig,A.;Le,V.;Tran,T.;Garber,D.;Lubos,S.;Burgstaller,T.Knowledge-basedrecommendersystems:Overview
andresearchdirections.Front.BigData2024,7,1304439.[CrossRef][PubMed]
26. Sofikitis,E.;Makris,C.DevelopmentofRecommendationSystemsUsingGameTheoreticTechniques.Comput.Sci.Inf.Syst.2022,
19,1133–1154.[CrossRef]
27. Ramanujam,S.S.AStudyonHybridRecommenderSystemwithDeepLearningandDeploymentinBigData.Availableonline:
http://www.testmagzine.biz/index.php/testmagzine/article/view/258/229(accessedon3July2023).
28. Tejeda-Lorente, Á.; Porcel, C.; Peis, E.; Sanz, R.; Herrera-Viedma, E. A quality based recommender system to disseminate
informationinauniversitydigitallibraryf.Inf.Sci.2014,261,52–69.[CrossRef]
29. Sanguino,J.;Mariño,O.;Cardozo,N.;Manrique,R.;Linares-Vásquez,M.Acoursehybridrecommendersystemforlimiteduser
informationscenarios.J.Educ.DataMin.2022,14,162–188.
30. Choi,K.;Yoo,D.;Kim,G.;Suh,Y.Ahybridonline-productrecommendationsystem:Combiningimplicitrating-basedcollabora-
tivefilteringandsequentialpatternanalysis.Electron.Commer.Res.Appl.2012,11,309–317.[CrossRef]
31. Duong,T.N.;Than,V.D.;Vuong,T.A.;Tran,T.H.ANovelHybridRecommendationSystemIntegratingContent-BasedandRating
Information.InAdvancesinNetworked-BasedInformationSystems,Proceedingsofthe22ndInternationalConferenceonNetwork-Based
InformationSystems(NBiS-2019),Oita,Japan,5–7September2019;Springer:Cham,Switzerland,2020;pp.325–337.
32. Ishida,Y.;Shimizu,T.;Yoshikawa,M.Ananalysisandcomparisonofkeywordrecommendationmethodsforscientificdata.Int.
J.Digit.Libr.2020,21,307–327.[CrossRef]
33. Zare,A.;Motadel,M.;Jalali,A.Presentingahybridmodelinsocialnetworksrecommendationsystemarchitecturedevelopment.
AISoc.2020,35,469–483.[CrossRef]
34. Shi,X.;Liu,Q.;Bai,Y.;Shang,M.RTiSR:Areview-driventimeinterval-awaresequentialrecommendationmethod.J.BigData
2023,10,32.[CrossRef]
35. Zhou,Q.;Zhuang,W.;Ren,H.;Chen,Y.;Yu,B.;Lou,J.;Wang,Y.Hybridcollaborativefilteringmodelforconsumerdynamic
servicerecommendationbasedonmobilecloudinformationsystem.Inf.Process.Manag.2022,59,102871.[CrossRef]

J.Imaging2025,11,12 64of66
36. Vladoiu,M.;Constantinescu,Z.;Moise,G.QORECT—Acase-basedframeworkforquality-basedrecommendingopencourse-
wareandopeneducationalresources. InComputationalCollectiveIntelligence. TechnologiesandApplications; LectureNotesin
ComputerScience(IncludingSubseriesLectureNotesinArtificialIntelligenceandLectureNotesInBioinformatics);Springer:
Berlin/Heidelberg,Germany,2013;Volume8083LNAI,pp.681–690.
37. Kwiecin´ski,R.;Górecki,T.;Filipowska,A.;Dubrov,V.JobRecommendations:BenchmarkingofCollaborativeFilteringMethods
forClassifieds.Electronics2024,13,3049.[CrossRef]
38. Forhad,M.;Arefin,M.;Kayes,A.;Ahmed,K.;Chowdhury,M.;Kumara,I.Aneffectivehotelrecommendationsystemthrough
processingheterogeneousdata.Electronics2021,10,1920.[CrossRef]
39. Raul, A.; Porobo Dharwadker, A.; Schumitsch, B. CAM2: Conformity-Aware Multi-Task Ranking Model for Large-Scale
RecommenderSystems. InProceedingsoftheACMWebConference2023—CompanionoftheWorldWideWebConference,
WWW2023,Austin,TX,USA,30April–4May2023;Volume1,pp.513–517.
40. Sivasankari,R.;Dhilipan,J.HybridscientificarticlerecommendationsystemwithCOOToptimization.DataSci.Manag.2024,7,
99–107.[CrossRef]
41. Castells,P.;Hurley,N.Vargas&SaulNoveltyandDiversityinRecommenderSystems.InRecommenderSystemsHandbook,2nd
ed.;Springer:NewYork,NY,USA,2015;pp.1–1003.
42. Bukhari,M.;Maqsood,M.;Aadil,F.KGR:AKernel-MappingBasedGroupRecommenderSystemUsingTrustRelations.Neural
Process.Lett.2024,56,201.[CrossRef]
43. Lai,C.;Peng,P.AHybridDeepLearningMethodtoExtractMulti-featuresfromReviewsandUser–ItemRelationsforRating
Prediction.Int.J.Comput.Intell.Syst.2023,16,109.[CrossRef]
44. Gong,J.;Zhang,X.;Li,Q.;Wang,C.;Song,Y.;Zhao,Z.;Wang,S.Atop-nmovierecommendationframeworkbasedondeep
neuralnetworkwithheterogeneousmodeling.Appl.Sci.2021,11,7418[CrossRef]
45. Walek,B.;Fajmon,P.Ahybridrecommendersystemforanonlinestoreusingafuzzyexpertsystem. ExpertSyst. Appl. 2023,
212,118565.[CrossRef]
46. Porcel,C.;Tejeda-Lorente,A.;Martínez,M.;Herrera-Viedma,E.Ahybridrecommendersystemfortheselectivedisseminationof
researchresourcesinatechnologytransferoffice.Inf.Sci.2012,184,1–19.[CrossRef]
47. Higgins,J.;Thomas,J.;Chandler,J.;Cumpston,M.;Li,T.;Page,M.;Welch,V.(Eds.)CochraneHandbookforSystematicReviewsof
Interventions,Version6.4;Wiley:Hoboken,NJ,USA,2023.Availableonline:www.training.cochrane.org/handbook(accessedon5
August2023).
48. Kitchenham,B.;Charters,S.GuidelinesforPerformingSystematicLiteratureReviewsinSoftwareEngineering;TechnicalReportEBSE
2007-001.KeeleUniversityandDurhamUniversityJointReport;SoftwareEngineeringGroup,DepartmentofComputerScience:
Keele,UK,2007.
49. Silva,F.;Slodkowski,B.;Silva,K.;Cazella,S.Asystematicliteraturereviewoneducationalrecommendersystemsforteaching
andlearning:Researchtrends,limitationsandopportunities.Educ.Inf.Technol.2023,28,3289–3328.[CrossRef]
50. Page,M.;McKenzie,J.;Bossuyt,P.;Boutron,I.;Hoffmann,T.;Mulrow,C.;Shamseer,L.;Tetzlaff,J.;Akl,E.;Brennan,S.;etal.The
PRISMA2020statement:Anupdatedguidelineforreportingsystematicreviews.BMJ2021,372,89.
51. Khtira,A.;Benlarabi,A.;El,B.ModelDefectsinEvolvingSoftwareProductLines:AReviewofLiterature.Am.Sci.Res.J.Eng.
Technol.Sci.2018,45,20–41.
52. Trabelsi,F.;Khtira,A.;ElAsri,B.HybridRecommendationSystems:AStateofArt.InProceedingsoftheInternationalConference
onEvaluationofNovelApproachestoSoftwareEngineering,ENASE—Proceedings,Online,26–27April2021;pp.281–288.
53. Roy,D.;Dutta,M.Asystematicreviewandresearchperspectiveonrecommendersystems.J.BigData2022,9,59.[CrossRef]
54. Moher,D.;Liberati,A.;Tetzlaff,J.;Altman,D.Preferredreportingitemsforsystematicreviewsandmeta-analyses:ThePRISMA
statement.Int.J.Surg.2010,8,336–341.[CrossRef][PubMed]
55. Higgins,J.;Green,S.;BenVanDen,A.CochraneHandbookforSystematicReviewsofInterventions.Int.Coach.Psychol.Rev.
2020,15,123–125.[CrossRef]
56. Schoot,R.;Bruin,J.;Schram,R.;Zahedi,P.;Boer,J.;Weijdema,F.;Kramer,B.;Huijts,M.;Hoogerwerf,M.;Ferdinands,G.;etal.An
opensourcemachinelearningframeworkforefficientandtransparentsystematicreviews.Nat.Mach.Intell.2021,3,125–133.
[CrossRef]
57. VanDijk,S.; Brusse-Keizer,M.; Bucsán,C.; VanDerPalen,J.; Doggen,C.; Lenferink,A.Artificialintelligenceinsystematic
reviews:Promisingwhenappropriatelyused.BMJOpen2023,13,e072254.[CrossRef][PubMed]
58. Harmsen,W.;DeGroot,J.;Harkema,A.;VanDusseldorp,I.;DeBruin,J.;VanDenBrand,S.;VanDeSchoot,R.ArtificialIntelligence
SupportsLiteratureScreeninginMedicalGuidelineDevelopment:TowardsUp-to-DateMedicalGuidelines;UtrechtUniversity:Utrecht,
TheNetherlands,2020.
59. ActiveLearningforSystematicReviews?2023.Availableonline:https://asreview.readthedocs.io/en/stable/(accessedon3
July2023).

J.Imaging2025,11,12 65of66
60. Rastogi,D.;Parihar,T.;Kumar,H.AparametricanalysisofAVAtooptimiseNetflixperformance.Int.J.Inf.Technol.2023,15,
2687–2694.[CrossRef][PubMed]
61. YalcinKavus,B.;GulumTas,P.;Ayyildiz,E.;Taskin,A.Athree-levelframeworktoevaluateairlineservicequalitybasedon
intervalvaluedneutrosophicAHPconsideringthenewdimensions.J.AirTransp.Manag.2022,99,102179.[CrossRef]
62. Shayganmehr,M.; Montazer,G.AnextendedmodelforassessingE-ServicesofIranianUniversitiesWebsitesUsingMixed
MCDMmethod.Educ.Inf.Technol.2020,25,3723–3757.[CrossRef]
63. Li, F.; Wang, C. Artificial intelligence and edge computing for teaching quality evaluation based on 5G-enabled wireless
communicationtechnology.J.CloudComput.2023,12,45.[CrossRef]
64. Williams,K.;Corwith,A.BeyondBricksandMortar:Theefficacyofonlinelearningandcommunity-buildingatCollegePark
AcademyduringtheCOVID-19pandemic.Educ.Inf.Technol.2021,26,5055–5076.[CrossRef][PubMed]
65. Wu,X.InterpretableAestheticAnalysisModelforIntelligentPhotographyGuidanceSystems. InProceedingsoftheInternational
ConferenceonIntelligentUserInterfaces,ProceedingsIUI,Helsinki,Finland,22–25March2022;pp.661–671.
66. Brückner,L.;Leiva,L.;Oulasvirta,A.LearningGUICompletionswithUser-DefinedConstraints.ACMTrans.Interact.Intell.Syst.
2022,12,6.[CrossRef]
67. Zhao, X.; Jia, Y.; Li, A.; Jiang, R.; Song, Y. Multi-source knowledge fusion: A survey. World Wide Web 2020, 23, 2567–2592.
[CrossRef]
68. Farshidi,S.;Jansen,S.;Fortuin,S.Model-drivendevelopmentplatformselection:Fourindustrycasestudies.Softw.Syst.Model.
2021,20,1525–1551.[CrossRef]
69. Chen,T.MultiplecriteriadecisionanalyticmethodsinmanagementwithT-sphericalfuzzyinformation.Artif.Intell.Rev.2023,
56,14087–14157.[CrossRef][PubMed]
70. Utke,M.;Zadtootaghaj,S.;Schmidt,S.;Bosse,S.;Möller,S.NDNetGaming—Developmentofano-referencedeepCNNfor
gamingvideoqualityprediction.Multimed.ToolsAppl.2022,81,3181–3203.[CrossRef]
71. Anand,S.Ontology-basedSoftComputingandMachineLearningModelforEcientRetrieval.Knowl.Inf.Syst.2024,66,1371–1402.
[CrossRef]
72. Ratmele,A.;Thakur,R.OpExHAN:Opinionextractionusinghierarchicalattentionnetworkfromunstructuredreviews. Soc.
Netw.Anal.Min.2022,12,148.[CrossRef][PubMed]
73. Wang, C.; Liu, Y.; Yu, Y.; Ma, W.; Zhang, M.; Liu, Y.; Zeng, H.; Feng, J.; Deng, C.Two-sidedCalibrationforQuality-aware
Responsible Recommendation. In Proceedings of the 17th ACM Conference on Recommender Systems, Singapore, 18–22
September2023.
74. Horcas,J.;Pinto,M.;Fuentes,L.Empiricalanalysisofthetoolsupportforsoftwareproductlines.Softw.Syst.Model.2023,22,
377–414.[CrossRef]
75. Yuslim,S.;Simanjuntak,M.;Lianto,F.RevealingtheConstructionProjectManagementSystemofCityParkinJakarta:Between
HopeandReality.Int.J.Adv.Sci.Eng.Inf.Technol.2022,12,2180–2189.[CrossRef]
76. Barrera-Barrera,R.SelectingtheappropriateleadingjournalinHospitalityandTourismresearch:Aguidebasedonthetopic-
journalfitandtheJCRimpactfactor.Scientometrics2022,127,1801–1823.[CrossRef]
77. Yao,T.;Yi,X.;Cheng,D.;Yu,F.;Chen,T.;Menon,A.;Hong,L.;Chi,E.;Tjoa,S.;Kang,J.;etal. Self-supervisedLearningfor
Large-scaleItemRecommendations.InProceedingsoftheInternationalConferenceonInformationandKnowledgeManagement,
Online,1–5November2021;pp.4321–4330.
78. Spann,S.TaskForceReport6.ReportonFinancing.InAnnalsofFamilyMedicine;AnnalsofFamilyMedicine,Inc.:Leawood,KS,
USA,2004;pp.1–21.
79. Rasool,G.;Pathania,A.VoiceinWords:AMixed-MethodApproachforDecodingDigitalFootprintsUsingOnlineReviews.J.
Qual.Assur.Hosp.Tour.2022,24,1014–1045.[CrossRef]
80. Murshed,B.;Mallappa,S.;Abawajy,J.;Saif,M.;Al-ariki,H.;Abdulwahab,H.Shorttexttopicmodellingapproachesinthecontext
ofbigdata:Taxonomy,survey,andanalysis.Artif.Intell.Rev.2023,56,5133–5260.[CrossRef]
81. Villa,S.;Niess,J.;Schmidt,A.;Welsch,R.Society’sAttitudesTowardsHumanAugmentationandPerformanceEnhancement
Technologies(SHAPE)Scale.Proc.ACMInteract.Mob.WearableUbiquitousTechnol.2023,7,128.[CrossRef]
82. Wang,C.;Zhu,H.;Li,M.SpeechQoE:ANovelPersonalizedQoEAssessmentModelforVoiceServicesviaSpeechSensing.
InProceedingsoftheSenSys2022—20thACMConferenceonEmbeddedNetworkedSensorSystems,Boston,MA,USA,6–9
November2022;pp.305–319.
83. Currin,F.;Diederich,K.;Blasi,K.;DaleSchmidt,A.;David,H.;Peterman,K.;Hourcade,J.SupportingShyPreschoolChildren
in Joining Social Play. In Proceedings of the Interaction Design and Children, IDC 2021, Athens, Greece, 24–30 June 2021;
pp.396–407.
84. Bravo-Adasme,N.;Cataldo,A.;Toledo,E.Techno-distressandparentalburnout:Theimpactofhomefacilitatingconditionsand
thesystemquality.Educ.Inf.Technol.2023,28,13619–13646.[CrossRef]

J.Imaging2025,11,12 66of66
85. Ou, C.; Mayer, S.; Butz, A. The Impact of Expertise in the Loop for Exploring Machine Rationality. In Proceedings of the
InternationalConferenceonIntelligentUserInterfaces,ProceedingsIUI,Sydney,Australia,27–31March2023;pp.307–321.
86. Farshidi,S.;Kwantes,I.;Jansen,S.Businessprocessmodelinglanguageselectionforresearchmodelers.Softw.Syst.Model.2023,
23,137–162.[CrossRef]
87. Narechania,A.;Du,F.;Sinha,A.;Rossi,R.;Hoffswell,J.;Guo,S.;Koh,E.;Navathe,S.;Endert,A.DataPilot:UtilizingQualityand
UsageInformationforSubsetSelectionduringVisualDataPreparation.InProceedingsoftheConferenceonHumanFactorsin
ComputingSystems,Hamburg,Germany,23–28April2023.
88. Milic´,M.;Makajic´-Nikolic´,D.DevelopmentofaQuality-BasedModelforSoftwareArchitectureOptimization:ACaseStudyof
MonolithandMicroserviceArchitectures.Symmetry2022,14,1824.[CrossRef]
89. Tan,Y.;Tan,A.;Nge,N.;Bhojan,A.DHR:DistributedHybridRenderingforMetaverseExperiences. InProceedingsoftheIXR
2022—The1stWorkshoponInteractiveEXtendedReality,Lisbon,Portugal,10–14October2022;pp.51–59.
90. Nguyen,M.;Amirpour,H.;Tashtarian,F.;Timmerer,C.;Hellwagner,H.PerformanceanalysisofH2BR:HTTP/2-basedsegment
upgradingtoimprovetheQoEinHAS.Multimed.ToolsAppl.2023,83,12561–12595.[CrossRef]
91. Berahmand,K.;Li,Y.;Xu,Y.DAC-HPP:Deepattributedclusteringwithhigh-orderproximitypreserve.NeuralComput.Appl.
2023,4,152.[CrossRef]
92. Jaiswal,R.;Dubey,R.CAQoE:ANovelNo-ReferenceContext-AwareSpeechQualityPredictionMetric.ACMTrans.Multimed.
Comput.Commun.Appl.2023,19,35.[CrossRef]
93. Habib,H.;Pearman,S.;Young,E.;Saxena,I.;Zhang,R.;Cranor,L.IdentifyingUserNeedsforAdvertisingControlsonFacebook.
Proc.ACMHum.-Comput.Interact.2023,6,59.[CrossRef]
94. Martin,K.;Liret,A.;Wiratunga,N.;Owusu,G.;Kern,M.EvaluatingExplainabilityMethodsIntendedforMultipleStakeholders.
KI-Kunstl.Intell.2021,35,397–411.[CrossRef]
95. Carlsson, N.; Eager, D. Cross-User Similarities in Viewing Behavior for 360° Video and Caching Implications. ACM Trans.
Multimed.Comput.Commun.Appl.2022,19,1–24.[CrossRef]
96. Qin, L.; Peng, F.; Long, M.; Ramachandra, R.; Busch, C. Vulnerabilities of Unattended Face Verification Systems to Facial
Components-basedPresentationAttacks:AnEmpiricalStudy.ACMTrans.Priv.Secur.2022,25,4.[CrossRef]
97. Acosta,S.;Garza,T.;Hsu,H.;Goodson,P.AssessingQualityinSystematicLiteratureReviews:AStudyofNoviceRaterTraining.
SAGEOpen2020,10,2158244020939530.[CrossRef]
98. Yuan,H.;Hernandez,A.UserColdStartProbleminRecommendationSystems: ASystematicReview. IEEEAccess2023,11,
136958–136977.[CrossRef]
99. Access,O.;Pasrija,V.;Pasrija,S.TheCold-StartProbleminRecommenderSystems:ChallengesandMitigationTechniques.Int.
Res.J.Mod.Eng.Technol.Sci.2024,6.
100. Sabiri,B.;Khtira,A.;ElAsri,B.;Rhanoui,M.InvestigatingContrastivePairLearning’sFrontiersinSupervised,Semisupervised,
andSelf-SupervisedLearning.J.Imaging2024,10,196.[CrossRef][PubMed]
101. Mauri, M.; Elli, T.; Caviglia, G.; Uboldi, G.; Azzi, M.RAWGraphs: AVisualisationPlatformtoCreateOpenOutputs. In
Proceedingsofthe12thBiannualConferenceonItalianSIGCHIChapter,Cagliari,Italy,18–20September2017.Availableonline:
https://api.semanticscholar.org/CorpusID:28530715(accessedon22December2023).
102. Silva,L.;SalesMendes,A.;SánchezSanBlas,H.;CaetanoBastos,L.;LeopoldoGonçalves,A.;FabianodeMoraes,A.Active
ActionsintheExtractionofUrbanObjectsforInformationQualityandKnowledgeRecommendationwithMachineLearning.
Sensors2023,23,138.[CrossRef]
103. Bonab,M.;Tanha,J.;Masdari,M.ASemi-SupervisedLearningApproachtoQuality-BasedWebServiceClassification. IEEE
Access2024,12,50489–50503.[CrossRef]
104. Kim,S.;Yu,H.;Yoon,J.;Park,E.Micro-LocationalFineDustPredictionUtilizingMachineLearningandDeepLearningModels.
Comput.Syst.Sci.Eng.2024,48,413–429.[CrossRef]
Disclaimer/Publisher’sNote: Thestatements, opinionsanddatacontainedinallpublicationsaresolelythoseoftheindividual
author(s)andcontributor(s)andnotofMDPIand/ortheeditor(s).MDPIand/ortheeditor(s)disclaimresponsibilityforanyinjuryto
peopleorpropertyresultingfromanyideas,methods,instructionsorproductsreferredtointhecontent.