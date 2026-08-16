---
conversion_metadata:
  converted_at: "2026-07-21T09:28:05Z"
  converter_tool: "markitdown"
  converter_version: "0.1.6"
  source_pdf: "Yang & Lee.pdf"
  source_pdf_sha256: "c3be82effb4ea0923baa24decf520a2bc5ecafd02b93a0875cb074c9b608d121"
  page_count: 25
  markdown_char_count: 194994
---

<!-- PAGE-AWARE EXTRACTION (via pdfminer.six) -->

<!-- PAGE 1 -->

Article
Enhancing Financial Advisory Services with GenAI: Consumer
Perceptions and Attitudes Through Service-Dominant Logic and
Artificial Intelligence Device Use Acceptance Perspectives

Qin Yang and Young-Chan Lee *

Department of Information Management, College of Global Social Management, Dongguk University,
Gyeongju 38066, Republic of Korea; yangqin05@yeah.net
* Correspondence: chanlee@dongguk.ac.kr

Abstract: Financial institutions are currently undergoing a significant shift from traditional robo-
advisors to more advanced generative artificial intelligence (GenAI) technologies. This transformation
has motivated us to investigate the factors influencing consumer responses to GenAI-driven financial
advice. Despite extensive research on the adoption of robo-advisors, there is a gap in our understand-
ing of the specific contributors to, and differences in, consumer attitudes and reactions to GenAI-based
financial guidance. This study aims to address this gap by analyzing the impact of personalized
investment suggestions, human-like empathy, and the continuous improvement of GenAI-provided
financial advice on its authenticity as perceived by consumers, their utilitarian attitude toward the
use of GenAI for financial advice, and their reactions to GenAI-generated financial suggestions. A
comprehensive research model was developed based on service-dominant logic (SDL) and Artificial
Intelligence Device Use Acceptance (AIDUA) frameworks. The model was subsequently employed
in a structural equation modeling (SEM) analysis of survey data from 822 mobile banking users. The
findings indicate that personalized investment suggestions, human-like empathy, and the continuous
improvement of GenAI’s recommendations positively influence consumers’ perception of its authen-
ticity. Moreover, we discovered a positive correlation between utilitarian attitudes and perceived
authenticity, which ultimately influences consumers’ responses to GenAI’s financial advisory solu-
tions. This is manifested as either a willingness to engage or resistance to communication. This study
contributes to the research on GenAI-powered financial services and underscores the significance of
integrating GenAI financial guidance into the routine operations of financial institutions. Our work
builds upon previous research on robo-advisors, offering practical insights for financial institutions
seeking to leverage GenAI-driven technologies to enhance their services and customer experiences.

Keywords: GenAI financial advice; consumer perceptions; service-dominant logic (SDL); Artificial
Intelligence Device Use Acceptance (AIDUA); perceived authenticity

1. Introduction

The financial sector is undergoing a profound transformation with the advent of
sophisticated technologies such as robo-advisors and generative artificial intelligence
(GenAI) platforms like ChatGPT. This technological revolution has fundamentally altered
how individuals manage their finances and receive financial advice. While robo-advisors
provide algorithm-based asset management services with minimal human intervention
(Sironi 2016), GenAI technologies have significantly advanced these services by offering
personalized, conversational financial advice, which represents a new frontier in digital
financial services (Dewasiri et al. 2024).

Previous research has thoroughly examined the impact of robo-advisors, focusing
on key factors such as behavioral biases, trust, perceived risk, and user attitudes in the
adoption and effectiveness of automated financial advisory systems (Brenner and Meyll

Citation: Yang, Qin, and Young-Chan

Lee. 2024. Enhancing Financial

Advisory Services with GenAI:

Consumer Perceptions and Attitudes

Through Service-Dominant Logic and

Artificial Intelligence Device Use

Acceptance Perspectives. Journal of

Risk and Financial Management 17: 470.

https://doi.org/10.3390/jrfm17100470

Academic Editors: Jong-Min Kim and

Thanasis Stengos

Received: 29 August 2024

Revised: 11 October 2024

Accepted: 15 October 2024

Published: 17 October 2024

Copyright: © 2024 by the authors.

Licensee MDPI, Basel, Switzerland.

This article is an open access article

distributed under the terms and

conditions of the Creative Commons

Attribution (CC BY) license (https://

creativecommons.org/licenses/by/

4.0/).

J. Risk Financial Manag. 2024, 17, 470. https://doi.org/10.3390/jrfm17100470

https://www.mdpi.com/journal/jrfm

---

<!-- PAGE 2 -->

J. Risk Financial Manag. 2024, 17, 470

2 of 25

2020; Bhatia et al. 2022; Xia et al. 2023). However, these studies have largely overlooked
the specific influence of GenAI technologies, particularly in terms of how their distinct
attributes reshape user experiences in financial contexts. The gap identified by prior
research (Fui-Hoon Nah et al. 2023) suggests a need for future studies to explore how
GenAI technologies, with their conversational nature and capacity for continuous learning,
influence consumer perceptions of financial advice services. Addressing this gap, our study
builds on the suggestions of previous research to advance our understanding of how GenAI
platforms affect consumer attitudes and behaviors.

To address this research gap, this study focuses on the unique attributes of GenAI,
such as its personalized investment suggestions, human-like empathy, and ability to con-
tinuously learn and improve. These features have the potential to significantly influence
consumers’ perceptions of the authenticity and reliability of financial advice (Pelau et al.
2021). Building on the gaps identified in earlier studies, we integrate service-dominant
logic (SDL) and AI Device Use Acceptance (AIDUA) frameworks to explore the role these
attributes play in shaping consumer trust in and acceptance of GenAI-based financial advi-
sory services (Vargo and Lusch 2004; Gursoy et al. 2019). We employ structural equation
modeling to analyze data from 822 mobile banking users, providing a comprehensive exam-
ination of the factors that drive the adoption and effectiveness of GenAI in financial advice.

Our research aims to address four principal questions:
How do GenAI’s attributes influence consumers’ perceptions of authenticity in using

GenAI for financial advice?

What is the relationship between perceived authenticity and utilitarian attitudes

towards GenAI financial advice?

How do utilitarian attitudes affect consumers’ responses to GenAI financial advice?
How does AI literacy moderate the impact of GenAI’s attributes on perceived authen-

ticity?

This study contributes to both theory and practice by addressing the research gaps
identified in prior studies. It offers a deeper understanding of how consumers perceive
the authenticity of GenAI financial advice and provides practical insights for designing,
implementing, and educating users about GenAI-powered financial services. By investigat-
ing the impact of GenAI attributes on perceived authenticity and subsequent consumer
attitudes and behaviors, this research not only fills a significant gap in the literature but also
offers practical guidance for developing effective GenAI-based financial advisory services.
This paper is organized as follows: Section 2 presents a literature review and the
theoretical framework, focusing on the evolution of financial advisory services and the
unique attributes of GenAI. Section 3 develops the research hypotheses and model, inte-
grating service-dominant logic (SDL) and AI Device Use Acceptance (AIDUA) frameworks.
Section 4 outlines the research methodology, including the data collection and the de-
velopment of the measurement. Section 5 discusses the data analysis and the results of
the structural model. Finally, Section 6 provides the conclusion, academic and practical
implications, and suggestions for future research directions.

2. Literature Review and Theoretical Framework
2.1. Evolution of Financial Advisory Services: From Robo-Advisors to GenAI

The landscape of financial advisory services has dramatically transformed over the
past decade, with the emergence of robo-advisors representing a crucial turning point. Robo-
advisors emerged as a response to the demand for cost-effective and accessible financial
planning tools, disrupting the traditional finance industry by providing standardized
investment solutions to a wider audience (Huang and Rust 2018). These platforms use
algorithms to build portfolios, reducing the need for human financial planners and lowering
the overall cost of investment advice (Brenner and Meyll 2020; Roh et al. 2023; Chou et al.
2023). However, as technology rapidly advances, the limitations of robo-advisors are
becoming more evident. These limitations include a lack of customization, an inability to

---

<!-- PAGE 3 -->

J. Risk Financial Manag. 2024, 17, 470

3 of 25

empathize with consumers, and a limited capacity to learn from past data. As a result,
there is a growing need for a shift toward more sophisticated tools (Ullah et al. 2024).

The transition from robo-advisors to GenAI represents the next stage in the evolution
of financial advisory services. GenAI platforms represent a significant technological leap,
delivering interactive and personalized financial advice through advanced natural language
processing (NLP) and machine learning (ML) capabilities (Roumeliotis and Tselikas 2023).
In contrast to their robo-advisor predecessors, GenAI tools are capable of engaging in
dynamic human–machine interactions, simulating human-like conversations, and offering
tailored investment suggestions that adapt to changes in users’ financial situations and the
market conditions (Javaid et al. 2023; Oehler and Horn 2024).

The development of GenAI has been significantly advanced by substantial progress
in NLP, which has enabled these systems to understand, interpret, and generate human
language with increasing accuracy. These advancements not only increase the effectiveness
of AI advisors but also enable them to engage in empathetic conversations, thereby im-
proving the consumer experience (Aldunate et al. 2022). The capacity of GenAI to process
complex inquiries and execute transactions through seamless conversations represents a
paradigm shift in how consumers manage their investments, offering a more engaging and
personalized advisory experience (Ko and Lee 2024).

As we continue to examine the capabilities and consequences of GenAI in finance,
it becomes evident that these advancements not only indicate progress within financial
institutions but also foreshadow profound changes in the nature of financial advisory
services. The implications for customer engagement, service delivery, and the role of AI
advisors are significant. GenAI holds immense potential to redefine the financial services
industry (B. Chen et al. 2023). It is imperative that both financial institutions and consumers
comprehend this evolutionary trajectory if they are to effectively leverage these technologies
and navigate the new landscape of investment advice.

2.2. GenAI’s Attributes: Personalized Investment Suggestion, Human-like Empathy, and
Continuous Improvement

A notable feature of GenAI in financial services is its ability to provide personalized
recommendations. Personalization is a key factor in consumer satisfaction and the contin-
ued use of technology-based services (Srinivasan et al. 2002; Tam and Ho 2005). Unlike
robo-advisors, which typically deliver standardized recommendations using limited al-
gorithms, GenAI tools can analyze extensive consumer input and specific data, including
financial goals, risk tolerance, investment preferences, and even emotional cues, to tai-
lor their recommendations to individual needs (Ali and Aysan 2023). This high level of
personalization in GenAI-driven services enhances the relevance and effectiveness of the
investment advice, potentially leading to better financial outcomes for consumers (Ko and
Lee 2024).

In addition to personalization, the continuous improvement of GenAI is another criti-
cal attribute, enabled by the machine learning algorithms embedded into GenAI systems.
These systems can learn and adapt through interactions with consumers, thereby enhancing
their ability to provide accurate and contextual investment advice over time (Ashta and
Herrmann 2021). This self-learning and improvement function is of paramount importance
in a dynamic financial market where consumer needs and the market conditions are in a
constant state of flux. Empirical studies have shown that AI systems capable of continuous
learning and adaptation are more likely to gain user trust and be perceived as authentic
(Vo et al. 2024).

Finally, while the analytical capabilities of GenAI have been widely recognized, the
role of its human-like empathy has also garnered increasing attention (Nazir and Wang
2023). The incorporation of emotional intelligence into GenAI enables it to recognize and
respond to consumers’ emotional cues, thereby elevating its interactions beyond mere
mechanical responses and providing support that aligns with consumers’ emotional states.
The integration of AI tools with human-like empathy can enhance consumer engagement

---

<!-- PAGE 4 -->

J. Risk Financial Manag. 2024, 17, 470

4 of 25

and trust, as emotional connection is an important component of successful consulting
relationships (Pelau et al. 2021).

The combination of personalized investment suggestions, human-like empathy, and
continuous improvement in GenAI represents a compelling value proposition for con-
sumers. These attributes are combined to create a user experience that mirrors interaction
with a human advisor while harnessing the effectiveness and efficiency of GenAI technol-
ogy. GenAI’s approach is notably different from the “one size fits all” model of traditional
robo-advisors. GenAI offers a high degree of participation, adaptability, and emotional
intelligence that aligns with the complex and diverse needs of consumers.

2.3. Perceived Authenticity of GenAI

The perceived authenticity of GenAI-powered financial advice is a pivotal factor in
establishing trust and encouraging user engagement. Users assess the authenticity of
platforms like GenAI based on their perception of the truthfulness, dependability, and
impartiality of the investment recommendations provided. Research has shown that
authenticity is crucial in determining users’ willingness to accept and engage with AI
advisors, forming the foundation for trust (Alboqami 2023; Glikson and Asscher 2023).
When GenAI is perceived as authentic, it not only gains users’ confidence more effectively
but also fosters a stronger connection, which is vital in the context of financial information
and assets given the sensitivity of such matters.

The essence of GenAI’s authenticity in financial advice lies not only in the accuracy of
its information but also in its ability to offer recommendations that align with users’ ethical
principles and financial goals (Esmark Jones et al. 2022). Moreover, it is crucial to ensure
transparency in how GenAI handles user data and arrives at its recommendations in order
to enhance its perceived authenticity. This transparency, in conjunction with a commitment
to ethical AI practices, underscores the significance of clear communication and ethical
design principles in the development of GenAI systems (Stahl and Eke 2024).

2.4. Utilitarian Attitudes towards GenAI and Consumer Responses

In evaluating consumer responses to GenAI, particularly in financial contexts, the
utilitarian perspective offers a compelling lens through which to view this phenomenon.
Utility is a key factor in technology adoption and a strong predictor of consumer willingness
to engage with AI. If consumers believe that GenAI will enhance the efficiency of their asset
management and improve the accuracy of their decisions, their willingness to interact with
the technology will increase (Ma and Huo 2023).

The efficacy of GenAI, including the accuracy and relevance of its investment sugges-
tions, is of paramount importance in determining consumer willingness to engage with
it (Niu and Mvondo 2024). The capacity of GenAI to furnish consistent, personalized,
and valuable counsel exerts a profound influence on the attitude of its users, which, in
turn, affects their engagement, whether positive or negative. Individuals who have had
positive experiences with GenAI are more likely to develop a favorable attitude toward it
and engage with it again in the future (Paul et al. 2023).

However, it is important to acknowledge that not all consumers are willing to adopt
GenAI’s financial advice, despite its potential benefits. Consumer resistance can be at-
tributed to various factors, including a lack of trust, perceived loss of control, privacy
concerns, and discomfort with technology (Chang and Hsiao 2024). Additionally, perceived
complexity and a less anthropomorphic interface may contribute to consumer resistance
(Baek and Kim 2023). Some consumers may perceive GenAI as a threat to their personal au-
tonomy or the security of their assets, which may lead to resistance to communicating with
it. This resistance may be further compounded by a lack of understanding of how GenAI
functions or a belief that it is incapable of replicating the intricate human comprehension
essential for financial decision-making.

To comprehend the reasons behind the differing attitudes toward the utilization of
GenAI, it is essential to investigate the utilitarian attitudes of consumers towards these

---

<!-- PAGE 5 -->

J. Risk Financial Manag. 2024, 17, 470

5 of 25

platforms. A nuanced understanding of these attitudes and their underlying determinants
can assist in the development of GenAI applications that align with consumer needs better,
thereby reducing consumer resistance.

2.5. AI Literacy

The integration of GenAI into financial services is not solely a matter of technological
development; it also involves user adaptation, in which AI literacy plays a crucial role.
AI literacy refers to the skills and competencies individuals need to effectively use AI
technologies and applications (Ng et al. 2021). This includes understanding AI’s capabilities,
context, and implementation. The integration of GenAI into financial services underscores
the crucial role of AI literacy in influencing the adoption and usage of AI technologies
(Perchik et al. 2023).

The previous literature suggests that high AI literacy can alleviate users’ doubts and
help them fully harness AI’s potential in financial decision-making, thereby enhancing the
use of AI technology (Cardon et al. 2023). Individuals with higher levels of AI literacy are
more likely to trust and rely on AI-driven financial advice (Shin et al. 2022). Furthermore,
AI literacy affects the user experience as a whole. Individuals with a deeper understanding
of AI are able to navigate its interface better with greater efficiency and efficacy, pose
specific inquiries to AI, and interpret the recommendations provided by AI with greater
accuracy, thereby leading to a more satisfactory experience (Wang et al. 2023).

Moreover, AI literacy can mitigate users’ resistance to new technologies by elucidating
the nature of AI and rendering its processes more transparent (Markus et al. 2024). Once
users comprehend how GenAI generates financial advice, their skepticism may dissipate,
reducing their resistance to utilizing such systems and fostering openness to them. The
discrepancy in the levels of knowledge about AI among different user groups results in
a knowledge gap. It is therefore imperative to provide education on the functioning of
AI in order to bridge this gap and facilitate more effective adoption of AI among diverse
user groups.

2.6. Service-Dominant Logic (SDL) and Artificially Intelligent Device Use Acceptance (AIDUA)

Service-dominant logic (SDL) has emerged as a key framework for understanding
value co-creation across industries, including financial services. In accordance with SDL,
value is generated through interactions between providers and consumers, rather than
being inherent in the output itself (Vargo and Lusch 2004; Vargo et al. 2008). In the context
of GenAI, SDL offers a perspective on how GenAI can facilitate value co-creation processes.
SDL shifts the focus from traditional goods-dominant logic, which views value as
created by companies and distributed to consumers, to a service-centered perspective,
where value is co-created by multiple parties, including consumers (Grönroos 2008). This
shift is critically important for understanding the relational and interactive nature of the
financial services provided by GenAI technology (Riikkinen et al. 2018).

The operation of GenAI financial services depends on the interaction of multiple
stakeholders, including financial institutions, technology companies, and consumers. SDL
posits that the efficacy of the ecosystem in jointly creating value is pivotal to the success of
the service. Consequently, SDL represents a strategic instrument for understanding and
enhancing the value co-creation process in GenAI-driven financial services. The importance
of interaction, personalization, and resource integration in shaping the user experience and
the overall service efficiency is emphasized (Zhu et al. 2024).

In addition to SDL, the development of a new theoretical framework is necessary for
understanding consumer acceptance and usage behavior when integrating AI systems into
consumer devices. The Artificial Intelligence Device Use Acceptance (AIDUA) model is a
comprehensive framework that reveals the multifaceted nature of consumer interactions
with AI technologies such as GenAI.

The AIDUA model delineates several stages for the acceptance of AI devices, including
primary appraisal, secondary appraisal, and the outcome stage (Gursoy et al. 2019). Each

---

<!-- PAGE 6 -->

J. Risk Financial Manag. 2024, 17, 470

6 of 25

of these stages is crucial in the evaluation of GenAI by consumers. In light of studies that
have applied the AIDUA model, it can be postulated that personalized suggestions, human-
like empathy, and continuous improvement serve as the primary drivers in measuring
consumers’ assessment of GenAI-powered financial advice. In the secondary appraisal
stage, consumers primarily evaluate their decision options and potential outcomes based
on their attitudes. When deciding whether to accept or resist GenAI-driven financial advice,
they assess the costs and benefits of using AI devices in service delivery, considering
their perceived authenticity of these devices. Following this intricate appraisal process,
consumers develop a utilitarian attitude towards GenAI-based financial advice, which
subsequently determines their willingness to communicate with GenAI or their resistance
to utilizing GenAI for financial guidance.

Empirical studies have demonstrated the efficacy of the AIDUA model in explaining
and predicting consumer behavior toward AI devices. These studies have also validated
this model’s utility as a diagnostic and prescriptive tool for businesses (Ma and Huo
2023; Lin et al. 2020; Kelly et al. 2023). For practitioners, the AIDUA model suggests that
marketing and design strategies for AI devices should address consumers’ concerns about
trust, perceived risk, and ease of use in order to increase their acceptance.

As artificial intelligence (AI) technology evolves and becomes more prevalent in
financial institutions, frameworks like AIDUA will become increasingly essential for under-
standing and predicting consumer interactions with AI tools. This comprehensive approach
allows for the design and implementation of AI technologies that align with consumer
expectations and promote acceptance.

2.7. Integrating SDL and AIDUA to Understand Consumer–AI Interactions

The seamless integration of service-dominant logic (SDL) and the AI Device Use Accep-
tance (AIDUA) model provides a comprehensive theoretical foundation for understanding
and explaining consumer interactions with generative AI (GenAI) in the service industry,
particularly within financial services. By combining SDL’s value co-creation perspective
with AIDUA’s focus on consumers’ appraisal stages of AI usage, we create a powerful
framework for investigating the nuances of consumer interactions with GenAI.

SDL emphasizes value co-creation through interaction and resource integration be-
tween service providers and consumers, aligning closely with the AIDUA model, which
highlights consumer acceptance and resistance toward AI technologies. The two frame-
works converge in the context of value-driven usage of AI, where consumers are not passive
recipients but active participants in the co-creation of value (Vargo et al. 2008; Grönroos
2008). Previous studies have shown that AI technologies, when effectively integrated into
service systems, enhance the consumer’s role in co-creating personalized value, resulting
in higher engagement and satisfaction (Riikkinen et al. 2018).

This framework posits that when services are designed to facilitate an active role
of consumers in co-creating personalized value (a fundamental concept of SDL), their
experiences with AI-driven systems, like GenAI, can be significantly enhanced. AIDUA
complements this by focusing on the stages of consumers’ interactions with AI, from initial
awareness to full acceptance, which includes their evaluation of perceived authenticity,
personalization, and continuous improvement—factors central to AI–human collaboration
(Bag et al. 2022; Vesanen 2007). Furthermore, evidence suggests that consumers’ willing-
ness to embrace AI in service settings increases when AI systems exhibit characteristics
such as empathy and anthropomorphism, which can foster more authentic and engaging
interactions (Pelau et al. 2021; Ameen et al. 2021).

The decision to integrate SDL and AIDUA is also supported by recent research in both
the literature on services and AI. For example, studies have highlighted the effectiveness of
combining consumer technology adoption frameworks with service logic to explain the
adoption of AI-driven services, particularly in high-involvement contexts like financial
services (Gursoy et al. 2019; Vesanen 2007). By integrating these models, we offer a more

---

<!-- PAGE 7 -->

J. Risk Financial Manag. 2024, 17, 470

7 of 25

holistic understanding of how consumers perceive and engage with AI-based financial
advisory services.

3. Hypothesis Development and the Research Model
3.1. Personalized Investment Suggestions, Human-like Empathy, and Continuous Improvement

Personalization is increasingly acknowledged as a vital component of enhancing user
experience and fostering authenticity in digital interactions (Vesanen 2007). In financial
advice, personalized recommendations are particularly impactful, as they demonstrate an
understanding of the user’s specific needs and preferences (Musto et al. 2015). The delivery
of personalized financial advice through GenAI can enhance the perceived authenticity
of it, as the advice appears more relevant and trustworthy. Consumer behavior studies
indicate that services are often perceived as more authentic when they are closely aligned
with a user’s unique circumstances (Napoli et al. 2014; Morhart et al. 2015).

Moreover, empathy, especially in the form of human-like emotional intelligence, is
crucial to user interactions. When users feel that AI tools can understand and respond
to their emotional states, they are more likely to trust and use this technology (Chi and
Hoang Vu 2023). The capacity for human-like empathy in GenAI enables it to comprehend
consumers’ financial concerns and objectives at an emotional level, which is crucial for
enhancing the perceived authenticity of its advice (Chuah and Yu 2021). Empathetic
interactions can elevate financial advice beyond being purely transactional, thereby creating
a sense of care and personal connection.

Furthermore, the ability of artificial intelligence systems to continuously learn and
improve over time is essential for maintaining their relevance and ensuring the delivery of
high-quality services. The ongoing enhancement of GenAI’s financial counsel could result
in more precise and contemporary recommendations, which might enhance the credibility
of its advice. The principle of continuous improvement aligns with the dynamic nature of
financial markets and consumer expectations (Huang and Rust 2021). As GenAI adapts and
evolves, its advice may be perceived as more authentic, reflecting up-to-date knowledge
and a deeper understanding of the financial landscape. Based on these insights, we propose
the following hypotheses:

H1: Personalized investment suggestions by GenAI are positively associated with its authenticity
as perceived by consumers.

H2: The human-like empathy of GenAI is positively associated with its authenticity as perceived by
consumers.

H3: Continuous improvement of GenAI is positively associated with its authenticity as perceived
by consumers.

3.2. Perceived Authenticity

Following the initial evaluation of the specific characteristics of GenAI tools, perceived
authenticity plays a crucial role in how consumers assess and adopt these services (Li et al.
2023). When consumers perceive a service as authentic and advice as genuine, they are
more likely to find this service useful and practical. This belief fosters a utilitarian attitude
towards the service, as consumers prioritize its functionality and the ability to effectively
achieve their goals (Alimamy and Al-Imamy 2022).

In the realm of AI-driven financial guidance, like the services offered by GenAI, the
perceived authenticity of the advice is essential in shaping users’ perceptions of a service’s
utility. When recommendations are perceived as truthful, users are more likely to view
them as reliable, precise, and tailored to their specific requirements. Consequently, this
enhances the perceived usefulness of GenAI’s offerings. The concept of perceived authen-
ticity encompasses the effectiveness, efficiency, and overall usefulness of the suggestions
provided by GenAI. The perceived authenticity of GenAI’s financial advice exerts a direct

---

<!-- PAGE 8 -->

J. Risk Financial Manag. 2024, 17, 470

8 of 25

influence on users’ utilitarian attitudes towards a service, which, in turn, determines its
perceived value and adoption (Kwon et al. 2024). Based on the interrelationship between
perceived authenticity, trust, and utility, the following hypothesis is proposed:

H4: Consumers’ perceived authenticity is positively associated with their utilitarian attitude
towards GenAI.

3.3. Utilitarian Attitudes

Utilitarianism in technology usage refers to the extent to which users perceive a
technology as efficient and effective in achieving their objectives (Zamil et al. 2023; Fu
2024). When consumers view a technology through a utilitarian lens, they evaluate its
value based on its ability to help them achieve specific goals and simplify their decision-
making. Essentially, the stronger the belief in a technology’s utilitarian value, the higher
the likelihood of its acceptance and integration into users’ daily lives. This is because
users recognize its practical benefits and its ability to streamline tasks and decision-making
processes (H. Kim et al. 2007).

In considering the role of GenAI in offering financial guidance, a utilitarian perspective
suggests that users value a platform’s capacity to deliver efficient, precise, and timely
information that can support their financial decision-making process. This mindset is
expected to enhance consumers’ readiness to engage with GenAI, as they anticipate that
the interaction will assist them in attaining their financial objectives (Dinh and Park 2023).
In other words, when users perceive GenAI as a tool that can effectively streamline their
financial planning and provide valuable insights, they are more likely to embrace and
utilize the platform. This is driven by the belief that it will contribute to their overall
financial well-being and success.

In addition to the adoption of new technology, resistance to its use is often shaped
by various factors, including a lack of practicality, increased complexity, or perceived
risks to personal information, established social norms, and personal habits (Hsieh 2016;
Ghosh 2024). However, when consumers view a technology through a utilitarian lens,
they recognize its potential to streamline tasks and boost productivity. This perception
reduces the probability of consumer resistance, as the technology aligns with their values
and objectives, and the advantages of its use outweigh the associated efforts, risks, and
costs. In essence, a utilitarian attitude towards technology fosters a sense of value and
purpose, making users more likely to embrace and incorporate it into their daily lives.
They recognize the technology’s practical benefits and its ability to enhance their overall
efficiency and effectiveness (Attié and Meyer-Waarden 2022).

In the context of GenAI, the identification of utilitarian advantages such as time
savings, cost-effectiveness, and enhanced financial results will result in a decrease in users’
resistance to utilizing these AI-driven platforms for financial guidance. The perception
of GenAI as a beneficial tool that aligns with their objectives will make users less likely
to oppose its adoption and integration (Jan et al. 2023). Consequently, they will be more
inclined to accept this innovation, recognizing its potential to positively impact their
financial decision-making process and overall outcomes (Priya and Sharma 2023). In
other words, the more users perceive GenAI as a practical and advantageous tool for
managing their finances, the less likely they will be to resist its adoption and use. As a
result, there will be a greater likelihood of adopting this AI-powered technology in their
financial decision-making process. Based on this understanding, the following hypotheses
are proposed:

H5: Consumers’ utilitarian attitudes towards GenAI are positively associated with their willingness
to communicate with GenAI.

H6: Consumers’ utilitarian attitudes towards GenAI are negatively associated with their resistance
to communicate with GenAI.

---

<!-- PAGE 9 -->

J. Risk Financial Manag. 2024, 17, 470

9 of 25

3.4. AI Literacy

In addition to the inherent features of AI-driven financial tools, the levels of AI literacy
among users play a critical role in the communication process. AI literacy encompasses
users’ comprehension of AI technology, which is crucial for regulating their interactions
with AI tools (Carolus et al. 2023). As AI literacy increases, users are better equipped to
understand complex AI functions, such as personalized recommendations. In the context
of GenAI, higher AI literacy enables consumers to grasp how the platform tailors its
recommendations based on user data better, which, in turn, enhances their perceptions of
its authenticity. Consequently, AI literacy can strengthen the positive relationship between
GenAI’s personalized advice and perceived authenticity. In other words, as users become
more knowledgeable about AI technology, they are more likely to appreciate and trust the
personalized financial guidance provided by GenAI, recognizing its genuine value and
relevance to their specific needs and circumstances.

Moreover, the continuous improvement of GenAI represents another advanced AI
feature. As users’ AI literacy increases, they are better positioned to comprehend and
appreciate this aspect of the platform. They are aware that the AI system will consistently
refine and enhance its recommendations based on ongoing interactions, thereby enhancing
the perceived authenticity of the advice provided. In this context, AI literacy can act as
a moderating factor, enhancing the relationship between continuous improvement and
perceived authenticity. Specifically, more knowledgeable users are more likely to place
higher value on the evolution of AI in delivering precise financial guidance (Tirado-Morueta
et al. 2018). In essence, as consumers become more well versed in AI technology, they are
more predisposed to acknowledge and trust the ongoing advancements in GenAI’s financial
advice. They recognize the genuine benefits of its adaptive nature in providing tailored
and relevant recommendations that align with their evolving needs and circumstances.

Finally, the human-like empathy exhibited by GenAI is the result of sophisticated
programming that enables empathetic interactions. Individuals with a higher level of AI
literacy are better equipped to understand and value these empathetic responses, resulting
in an increased perception of its authenticity. Conversely, individuals with limited AI
literacy may encounter difficulty in comprehending the nuances of empathetic AI, leading
to a diminished perception of its authenticity. As a result, the development of AI literacy
is expected to strengthen the correlation between human-like empathy and perceived
authenticity. As users gain a deeper understanding of AI technology, they are more likely
to recognize and value the genuine nature of GenAI’s empathetic interactions (Baabdullah
et al. 2022; Sperling et al. 2024), thereby increasing their confidence in these platforms’
financial advice. Based on these insights, we propose the following hypotheses:

H7: Consumers’ AI literacy positively moderates the relationship between GenAI’s personalized
investment suggestions and its authenticity as perceived by customers.

H8: Consumers’ AI literacy positively moderates the relationship between GenAI’s continuous
improvement and its authenticity as perceived by customers.

H9: Consumers’ AI literacy positively moderates the relationship between GenAI’s human-like
empathy and its authenticity as perceived by customers.

In essence, as users become more knowledgeable about AI technology, the impact of its
personalized investment suggestions, human-like empathy, and continuous improvement
on their perceptions of the authenticity of GenAI’s financial advice will be amplified,
ultimately leading to a higher level of trust and acceptance among consumers. The research
model based on the research hypotheses so far is shown in Figure 1.

---

<!-- PAGE 10 -->

J. Risk Financial Manag. 2024, 17, 470

10 of 25

Figure 1. Research model.

4. Research Methodology
4.1. Measurement Development

We commenced our investigation by developing a comprehensive questionnaire de-
signed to capture the relevant data necessary for our analysis. In light of the significance of
expert input, we solicited evaluations from esteemed professors in the Finance, Information
Technology, and Management Science departments. Their invaluable feedback prompted
revisions to the questionnaire, allowing us to refine and clarify our questions for greater
precision and relevance.

A rigorous methodology was employed to ensure that the questionnaire accurately
assessed eight key dimensions. These included the extent to which the investment advice
was personalized, GenAI’s capacity for continuous improvement, its ability to demonstrate
human-like empathy, the authenticity of its responses as perceived by consumers, the
utilitarian attitude of consumers towards GenAI, consumers’ willingness and resistance to
engage with GenAI for financial guidance, and their overall AI literacy.

The introductory section of the questionnaire clearly outlined the purpose of the
study, ensuring participants’ confidentiality and anonymity. Additionally, survey instruc-
tions were provided. The initial part of the questionnaire included questions on basic
demographic information, such as age, gender, income level, and education, to establish a
foundational understanding of the respondents’ backgrounds. The second part consisted
of items carefully designed to assess the eight constructs under investigation.

The measurement items for personalized investment suggestions assessed the respon-
dents’ perceptions of GenAI’s ability to comprehend their individual financial needs and
deliver customized recommendations. The evaluation of continuous improvement assessed
the respondents’ views on GenAI’s ability to learn from interactions and improve its sug-
gestions over time (Q. Chen et al. 2022). Human-like empathy was measured through
items (Pelau et al. 2021; Fu et al. 2023; Seitz 2024) that gauged the extent to which GenAI
understood and considered the respondents’ emotional and financial concerns. The per-
ceived authenticity of GenAI’s financial advice was examined by asking the respondents
to rate the genuineness and reliability of its advice (Vo et al. 2024; Meng et al. 2023). The
usefulness, efficiency, and practicality of GenAI’s recommendations were evaluated to
assess the respondents’ utilitarian attitudes (Priya and Sharma 2023). The respondents’

---

<!-- PAGE 11 -->

J. Risk Financial Manag. 2024, 17, 470

11 of 25

willingness to communicate with GenAI was gauged through items (Ma and Huo 2023;
Kim and Hur 2023) that determined the likelihood of future engagement with the AI for
financial advice. Resistance to communicate with GenAI was evaluated by assessing the
respondents’ hesitation in using or reluctance to use GenAI for financial guidance (Ma and
Huo 2023; Yang et al. 2023). Finally, an AI literacy scale was used to assess the respondents’
knowledge and understanding of AI technologies, particularly their application to financial
advice (Almatrafi et al. 2024; Kong et al. 2024). Detailed breakdowns can be found in
Appendix A.

4.2. Data Collection

This study used a comprehensive approach to data collection to gather insights from
mobile banking service users who had engaged with GenAI for financial guidance. The
survey was designed to gather detailed information on the participants’ interactions with
GenAI, their evaluations of AI’s authenticity, their AI literacy, and their attitudes towards
using AI for financial advice.

This study targeted adult mobile banking users aged 18 and above who had interacted
with GenAI financial advice features. Purposive sampling was employed to select respon-
dents who met this criterion, ensuring that the sample was relevant for understanding the
target user group. In total, 1200 participants were initially invited to take part in the survey,
of which 950 respondents completed it. After data cleaning and quality control checks, a
final sample of 822 respondents was retained for analysis. These participants were balanced
across gender, age, and income levels, ensuring a representative cross-section of the mobile
banking population. Table 1 presents their demographic characteristics, showing that the
participants included individuals aged 18 to over 65 years old, with 7 participants being
over 65, reflecting the inclusivity of older users in mobile banking services.

Table 1. Demographic characteristics.

Demographics

Frequency

Percentage (%)

Gender

Age

Education
Background

Monthly
income

Frequency of
using GenAI

Male
Female

18–24
25–34
35–44
45–54
55–64
Above 65

High school or below
Three years of college
Bachelor’s
Master’s or above

3000 CNY or below
3001–5000 CNY
5001–7000 CNY
7001–9000 CNY
9000 CNY and above

Several times per day
Once a day
Several times per week
Once a week
Several times per month
Once a month

412
410

139
322
233
86
35
7

164
252
363
43

141
423
140
61
57

29
78
106
364
208
37

50.1
49.9

16.9
39.2
28.3
10.5
4.3
0.9

20
30.7
44.2
5.2

17.2
51.5
17
7.4
6.9

3.5
9.5
12.9
44.3
25.3
4.5

The data collection took place over a three-month period, from January to March
2024, and was facilitated by collaboration with a professional survey firm. The survey
was distributed using multiple platforms: (1) email campaigns targeting mobile banking

---

<!-- PAGE 12 -->

J. Risk Financial Manag. 2024, 17, 470

12 of 25

users from partner banks, (2) in-app notifications within mobile banking applications
encouraging participation, and (3) financial forums and social media platforms, on which
the survey link was shared.

Before launching the formal survey, a pilot test was conducted with a subset of 50 par-
ticipants to identify and address any potential issues with its clarity, the comprehensibility
of the questions, and the overall structure of the questionnaire. The pilot survey helped re-
fine variables such as AI literacy, perceived authenticity, and human-like empathy following
the recommendations of Ref. (Van Teijlingen and Hundley 2002).

Strict filtering techniques were used during the survey collection process to maintain
the data quality, ensuring that only responses from eligible participants were included.
Anonymity and confidentiality were strictly maintained in compliance with ethical research
standards. Table 1 provides a summary of the respondents’ demographic characteristics.

5. Data Analysis and Results
5.1. The Measurement Model

Ref. (Podsakoff and Organ 1986) suggested that single-source data may be prone to
common method variance (CMV). To determine the presence of common method bias
(CMB) in our collected data, we conducted Harman’s single-factor test. This test involves
loading all the measurement items into a principal component analysis without rotation. It
is widely accepted that CMB is a concern if a single factor accounts for more than 50% of
the total variance. In this study, the first factor accounted for 31.95% of the variance, which
is below the 50% threshold. Therefore, we can conclude that the data in this study were not
affected by common method bias.

The measurement model was assessed by examining the factor loading values, com-
posite reliability (CR), and average variance extracted (AVE). As shown in Table 2, all the
factor loadings exceed the recommended threshold of 0.6. Additionally, Cronbach’s α,
which measures internal consistency reliability, ranged from 0.845 to 0.949, surpassing
the suggested threshold of 0.7 (Hair et al. 2014). These results provide strong evidence
supporting the scale’s reliability.

Table 2. Reliability, CR, and AVE.

Constructs

Items

Item Loadings

Cronbach’s
Alpha

CR

AVE

Personalized Investment
Suggestions

Human-Like Empathy

PIS1
PIS2
PIS3
PIS4
PIS5
PIS6
PIS7
PIS8

HLE1
HLE2
HLE3
HLE4
HLE5
HLE6
HLE7
HLE8
HLE9
HLE10
HLE11

0.924
0.778
0.769
0.741
0.747
0.744
0.783
0.791

0.898
0.793
0.778
0.780
0.754
0.788
0.768
0.768
0.798
0.814
0.814

0.926

0.928

0.619

0.949

0.95

0.635

---

<!-- PAGE 13 -->

J. Risk Financial Manag. 2024, 17, 470

13 of 25

Table 2. Cont.

Constructs

Items

Item Loadings

Cronbach’s
Alpha

CR

AVE

Continuous Improvement

Perceived
Authenticity

Utilitarian Attitudes

Willingness to
Communicate with GenAI

Resistance to
Communicating with
GenAI

AI Literacy

CI1
CI2
CI3
CI4
CI5
CI6
CI7

PA1
PA2
PA3

UA1
UA2
UA3
UA4
UA5

WCG1
WCG2
WCG3
WCG4
WCG5
WCG6

RCG1
RCG2
RCG3
RCG4
RCG5
RCG6

AIL1
AIL2
AIL3
AIL4
AIL5
AIL6

0.870
0.778
0.718
0.750
0.788
0.771
0.796

0.886
0.764
0.781

0.887
0.733
0.685
0.740
0.771

0.888
0.721
0.738
0.726
0.765
0.78

0.863
0.80
0.672
0.686
0.762
0.728

0.768
0.757
0.844
0.818
0.760
0.808

0.915

0.917

0.613

0.845

0.853

0.660

0.865

0.876

0.587

0.894

0.898

0.596

0.885

0.887

0.570

0.910

0.910

0.629

Composite reliability (CR) was used to evaluate the internal consistency of the scale,
with higher values indicating greater reliability. Ref. (Raza et al. 2021) states that CR
values between 0.6 and 0.7 are acceptable, while values between 0.7 and 0.9 are considered
satisfactory to good. As shown in Table 3, all the CR values exceeded 0.8, confirming the
scale’s satisfactory composite reliability.

Table 3. Discriminant validity.

PIS

HLE

CI

PA

UA

WCG

RCG

AIL

PIS
HLE
CI
AIL
PA
UA
WCG
RCG

0.787
0.442 **
0.423 **
0.150 **
0.541 **
0.451 **
0.348 **
−0.315 **

0.797
0.446 **
0.160 **
0.551 **
0.493 **
0.332 **
−0.336 **

0.783
0.174 **
0.500 **
0.480 **
0.324 **
−0.371 **

0.793
0.317 **
0.195 **
0.143 **
−0.198 **

0.812
0.614 **
0.413 **
−0.473 **

0.766
0.669 **
−0.677 **

0.772
−0.435 **

0.755

Note: **, p < 0.01. Values in bold represent the square root of the AVE.

---

<!-- PAGE 14 -->

J. Risk Financial Manag. 2024, 17, 470

14 of 25

Additionally, the average variance extracted (AVE) values for all variables exceeded
0.5, meeting the criteria for convergent validity (Fornell and Larcker 1981). These results
collectively indicate that the measurement model demonstrates strong reliability and
convergent validity.

To assess discriminant validity, we used the method from Ref. (Fornell and Larcker
1981), which requires the square root of the AVE to be greater than the correlations among
the constructs. Table 3 shows the square root of the AVE values along the diagonal (in bold)
and the correlations among the constructs in the off-diagonal cells. These results reveal
that the square root of the AVE for each construct was higher than the corresponding off-
diagonal correlation values. This indicates that the measurement model has a satisfactory
discriminant validity, as each construct is more strongly related to its own measures than
to those of the other constructs.

Before conducting the structural equation modeling (SEM) analysis, a confirmatory
factor analysis (CFA) was performed to evaluate the measurement model. The model’s
goodness of fit was assessed using various indices and their corresponding thresholds, as
recommended by Ref. (Hu and Bentler 1999).

The CFA results indicated that the measurement model fit the data well. Specifically,
the chi-square-to-degrees-of-freedom ratio (χ2/df) was 1.173, which is within the acceptable
range. The Goodness of Fit Index (GFI) and the Adjusted Goodness of Fit Index (AGFI)
values were 0.938 and 0.932, respectively, with both exceeding the recommended thresholds.
Additionally, the Comparative Fit Index (CFI) and the Normed Fit Index (NFI) values were
0.992 and 0.95, respectively, indicating a strong fit. The Incremental Fit Index (IFI) value of
0.992 also met the criteria. Finally, the Standardized Root Mean Square Residual (SRMR)
and the Root Mean Square Error of Approximation (RMSEA) values were 0.026 and 0.015,
respectively, with both falling below the recommended thresholds, further supporting the
model’s acceptable fit.

As shown in Table 4, all the fitting indices of the measurement model met the rec-
ommended criteria, confirming that the model adequately represented the data and was
suitable for the subsequent SEM analysis.

Table 4. Measurement model fit.

Fit Indices

Recommended Criteria
Scores

χ2/df

<3
1.173

GFI

>0.9
0.938

AGFI

>0.8
0.932

NFI

>0.9
0.95

CFI

>0.9
0.992

IFI

>0.9
0.992

SRMR

RMSEA

<0.08
0.026

<0.08
0.015

5.2. The Structural Model

The structural model was evaluated to examine the relationships between the con-
structs proposed in the research model. The analysis revealed that all paths were positive
and significant at the 0.05 level. Table 5 presents the standardized path coefficients between
the constructs, the significance levels, and the explanatory power (R2) for each construct.
According to the rule of thumb, R2 values of 25%, 50%, and 75% indicate weak, average,
and substantial explanatory power, respectively.

In this study, the R2 values for perceived authenticity, utilitarian attitudes, willingness
to communicate with GenAI, and resistance to communicating with GenAI were 56.9%,
50.5%, 50.3%, and 54.6%, respectively, indicating a satisfactory level of explanation.

The results in Table 5 show a positive association between personalized investment
suggestions and perceived authenticity (β = 0.318, p < 0.001), supporting Hypothesis 1.
Similarly, there was a positive association between human-like empathy and perceived
authenticity (β = 0.338, p < 0.001), confirming Hypothesis 2. Additionally, continuous
improvement positively influences perceived authenticity (β = 0.287, p < 0.001), supporting
Hypothesis 3. Together, personalized investment suggestions, human-like empathy, and
continuous improvement account for 56.9% of the variance in perceived authenticity.

---

<!-- PAGE 15 -->

J. Risk Financial Manag. 2024, 17, 470

15 of 25

Table 5. Hypothesis test results.

Hypothesis

H1
H2
H3
H4
H5
H6

PIS
HLE
CI
PA
UA
UA

Moderating Effect

H7
H8
H9

PIS × AIL
HLE × AIL
CI × AIL

Path

→
→
→
→
→
→

Path

→
→
→

Note: ***, p < 0.001.

PA
PA
PA
UA
WCG
RCG

PA
PA
PA

β

0.318
0.338
0.287
0.71
0.709
−0.739

β

0.101
0.097
0.108

p-Value

***
***
***
***
***
***

R2

0.569

0.505
0.503
0.546

p-Value

***
***
***

Remarks

Supported
Supported
Supported
Supported
Supported
Supported

Remarks

Supported
Supported
Supported

Furthermore, perceived authenticity positively impacts utilitarian attitudes (β = 0.71,
p < 0.001), accounting for 50.5% of their variance, thereby supporting Hypothesis 4. In turn,
utilitarian attitudes positively influence willingness to communicate with GenAI (β = 0.709,
p < 0.001), supporting Hypothesis 5, and negatively affect resistance to communicating
with GenAI (β = −0.739, p < 0.001), supporting Hypothesis 6. Utilitarian attitudes explain
50.3% of the variance in willingness to communicate with GenAI and 54.6% of the variance
in resistance to communicating with GenAI.

After verifying the hypotheses, a structural model test was conducted. The results
indicated that the model demonstrated an acceptable fit to the data according to the criteria
recommended by Ref. (Hu and Bentler 1999). The chi-square-to-degrees-of-freedom ratio
(χ2/df) was 1.225, which is within the acceptable range. The Goodness of Fit Index (GFI)
and the Adjusted Goodness of Fit Index (AGFI) values were 0.941 and 0.935, respectively,
with both exceeding the recommended thresholds. Additionally, the Comparative Fit Index
(CFI), Normed Fit Index (NFI), and Incremental Fit Index (IFI) values were 0.990, 0.953, and
0.990, respectively, indicating a strong fit between the model and the data. The Standardized
Root Mean Squared Residual (SRMR) value of 0.038 and the Root Mean Square Error of
Approximation (RMSEA) value of 0.018 were both below the recommended cutoff points,
further supporting the model’s acceptable fit. These fit indices, as presented in Table 6,
collectively indicate that the structural model adequately represents the relationships
among the constructs and provide a satisfactory explanation of the data.

Table 6. Structural model fit.

Fit Indices

Recommended Criteria
Scores

χ2/df

<3
1.173

GFI

>0.9
0.938

AGFI

>0.8
0.932

NFI

>0.9
0.95

CFI

>0.9
0.992

IFI

>0.9
0.992

SRMR

RMSEA

<0.08
0.026

<0.08
0.015

In addition to the primary hypotheses, this study proposed that AI literacy moderates
the relationships between GenAI’s characteristics (personalized investment suggestions,
human-like empathy, and continuous improvement) and perceived authenticity. The results
presented in Table 5 demonstrate that as AI literacy increases or decreases, the positive
associations between GenAI’s characteristics and its authenticity as perceived by consumers
remain consistent.

The interaction term between personalized investment suggestions and AI literacy is
positively associated with perceived authenticity (β = 0.101, p < 0.001), indicating that the
relationship between personalized investment suggestions and perceived authenticity is
strengthened by higher levels of AI literacy. Similarly, the interaction term between human-
like empathy and AI literacy is positively associated with perceived authenticity (β = 0.097,
p < 0.001), suggesting that the relationship between human-like empathy and perceived

---

<!-- PAGE 16 -->

J. Risk Financial Manag. 2024, 17, 470

16 of 25

authenticity is enhanced by higher levels of AI literacy. Finally, the interaction term
between continuous improvement and AI literacy is positively associated with perceived
authenticity (β = 0.108, p < 0.001), indicating that the relationship between continuous
improvement and perceived authenticity is reinforced by higher levels of AI literacy.

Figure 2 presents a visual representation of the standardized path coefficients and the
significance levels for each hypothesis, including the moderating effects of AI literacy on
the relationships between GenAI’s characteristics and perceived authenticity.

Figure 2. Path coefficients of the research model. Note: ***, p < 0.001.

6. Conclusions

The objective of this study was to explore the dynamics of consumer responses to
GenAI-powered financial advice, addressing a critical gap in the literature on the adoption
of GenAI technologies in financial services. Through a rigorous empirical analysis, it was
shown that personalized investment suggestions, human-like empathy, and the continuous
improvement of GenAI significantly enhance consumers’ perceptions of its authenticity.
These perceptions, in turn, foster a utilitarian attitude towards using GenAI for financial
advice, influencing consumers’ willingness to engage with and resistance to communication
with GenAI. Notably, this study highlights the role of AI literacy in amplifying the positive
effects of GenAI’s features on perceived authenticity.

Our findings delineate a clear pathway through which GenAI’s features influence con-
sumer behaviors. The provision of personalized investment advice, the demonstration of
human-like empathy, and commitment to continuous improvement enhance the perceived
authenticity of GenAI’s financial counsel. These insights align with Refs. (Pelau et al. 2021;
J. Kim et al. 2022), which emphasized the importance of perceived human-likeness in user
interactions with AI systems. Additionally, the work of Refs. (Q. Chen et al. 2022; Pitardi
2023) highlighted the role of personalization and continuous improvement in enhancing
consumer trust in AI services.

We also found that perceived authenticity is crucial to developing a utilitarian attitude
towards GenAI, which, in turn, increases willingness to interact with AI and reduces
resistance. These findings extend previous research on the importance of authentic design
of GenAI platforms (Lee and Kim 2024; Pandey and Rai 2024).

---

<!-- PAGE 17 -->

J. Risk Financial Manag. 2024, 17, 470

17 of 25

Furthermore, the significant moderating influence of AI literacy underscores the im-
portance of consumers’ understanding and familiarity with AI technologies in enhancing
the effectiveness of GenAI’s features. These findings support past studies on AI liter-
acy (Ng et al. 2021; Kong et al. 2024) and demonstrate its value in the field of financial
advisory services.

6.1. Academic Implications

This research significantly enhances our understanding of how generative AI (GenAI)
influences consumer behavior in the realm of financial advice. This study’s findings con-
tribute to the theoretical landscape by extending the application of service-dominant logic
(SDL), integrating the AI Device Use Acceptance (AIDUA) framework, and highlighting
the complex interplay between AI’s attributes and consumer perceptions.

These findings emphasize the importance of personalized investment suggestions,
human-like empathy, and continuous improvement to GenAI’s recommendations within
the context of consumer value co-creation, as highlighted by SDL theory. By tailoring its
services to individual consumer needs and preferences, GenAI facilitates a more interactive
and collaborative experience between service providers and consumers, thus enabling
value co-creation. As demonstrated by previous studies (Wen et al. 2022), personalization
is crucial to enabling value co-creation, allowing for a more interactive and collaborative
experience between service providers and consumers. This study’s findings align with
SDL principles and extend the theory by showing how digital technologies enhance per-
sonalized value co-creation, surpassing the limitations of traditional human-to-human
service frameworks.

Moreover, GenAI’s ability to exhibit human-like empathy significantly influences
consumers’ perceived authenticity by demonstrating genuine care and concern. This
finding contributes to the growing body of literature on the importance of designing
AI technologies that are not only competent but also genuine and transparent in their
interactions (Markovitch et al. 2024). Additionally, GenAI’s capacity for continuous learning
enables it to adapt to evolving user needs and preferences, thereby enhancing its perceived
authenticity over time (Baidoo-Anu and Ansah 2023; Raj et al. 2023).

These findings underscore the importance of integrating personalized investment
suggestions, human-like empathy, and continuous improvement into GenAI-driven fi-
nancial advice. This integration reflects the processes of SDL and AIDUA by co-creating
value through tailored, empathetic, and adaptive financial guidance, ultimately enhancing
consumer engagement, trust, and participation in GenAI-powered financial services.

This study also highlights the role of perceived authenticity in human–bot interactions,
especially within the field of artificial intelligence (Seitz 2024; Meng et al. 2023). The
positive correlation between GenAI’s features and its perceived authenticity aligns with the
authenticity principle in AI research (Esmark Jones et al. 2022; Rese et al. 2020; Kuhail et al.
2022). This emphasizes the necessity for GenAI and similar technologies to demonstrate
authenticity to effectively engage and support users.

Additionally, this study identifies a strong correlation between perceived authenticity,
utilitarian attitudes, and consumers’ willingness to communicate or resistance to commu-
nicating with GenAI for financial advice. It expands our understanding of technology
adoption theories by demonstrating that perceived authenticity enhances utilitarian atti-
tudes towards GenAI, which, in turn, affect willingness to use or resistance to using GenAI
for financial advice. This suggests that the value consumers place on authenticity can signif-
icantly influence their practical assessment of a technology’s benefits (Alimamy and Kuhail
2023). These findings advocate for a broader interpretation of perceived usefulness in AI
technology acceptance, highlighting the importance of authenticity in shaping utilitarian
evaluations of AI technology.

Lastly, this study’s focus on AI literacy adds to the theoretical landscape by suggesting
that a higher level of AI literacy can enhance the effectiveness of AI features by improving
their perceived authenticity and, consequently, utilitarian attitudes towards them (Du et al.

---

<!-- PAGE 18 -->

J. Risk Financial Manag. 2024, 17, 470

18 of 25

2024). This implies that individuals’ interactions with AI technologies are significantly
influenced by their understanding of these technologies, leading to increased acceptance
and willingness to communicate with GenAI. Conversely, lower levels of AI literacy may
lead to resistance to communicating with GenAI, highlighting the importance of addressing
this factor to facilitate the effective integration of AI-driven services into the consumer
value co-creation process.

In conclusion, this study offers a comprehensive integration of key concepts, including
personalized investment suggestions, human-like empathy, continuous improvement,
perceived authenticity, utilitarian attitudes, and consumers’ willingness to communicate or
resistance to communicating with GenAI, within the frameworks of SDL and AIDUA. Its
findings show that GenAI’s personalized and empathetic approach, along with its ability to
continuously improve, enhances its perceived authenticity and utilitarian attitudes towards
it among consumers, facilitating value co-creation as proposed by SDL. Additionally, this
study extends the AIDUA model by incorporating continuous improvement as a factor
influencing perceived authenticity, a key determinant of AI tool usage. This research also
underscores the role of AI literacy in shaping consumers’ willingness to engage or resistance
to engaging with GenAI, highlighting the importance of addressing this factor to ensure the
effective integration of AI-driven services into the value co-creation process. Overall, this
study contributes to the growing body of literature on AI-driven services and their impact
on consumer behavior, providing valuable insights for both researchers and practitioners
in the field.

6.2. Practical Implications

The practical implications of this study are substantial, providing valuable insights
for a wide range of stakeholders, including financial institutions, technology developers,
and policymakers. For financial service providers, this study emphasizes the importance
of developing GenAI technologies with enhanced human-like characteristics, such as the
ability to offer personalized advice and exhibit empathy. This suggests that financial
institutions should invest in AI systems that go beyond basic natural language processing
and incorporate the ability to understand and adapt to individual emotional states and
preferences. This research indicates that GenAI-driven chatbots capable of recognizing and
responding to users’ emotions can significantly enhance user satisfaction and engagement.
This underscores the necessity of financial institutions employing GenAI technologies that
can tailor their services to individual needs and preferences.

Furthermore, this study highlights the importance of continuous learning in main-
taining and enhancing consumer trust and engagement with GenAI systems. Financial
institutions should prioritize designing AI systems that can continuously update their
knowledge bases and refine their algorithms based on user interactions. This approach
aligns with the continuous improvement aspect of AI development and ensures that AI
systems remain relevant and effective in meeting evolving consumer needs and preferences.
AI systems capable of continuous learning and improvement are better equipped to build
and maintain user trust over time by demonstrating an ongoing commitment to providing
accurate and up-to-date information.

This study’s findings also emphasize the importance of AI literacy in enhancing the
positive impact of GenAI’s attributes on its perceived authenticity. This suggests that
financial institutions should develop educational programs and resources to improve
consumers’ understanding of AI. By investing in initiatives that demystify AI technologies,
financial institutions can reduce resistance and increase engagement among consumers.
This aligns with the broader goal of enhancing AI literacy and ensuring that consumers
have the necessary knowledge and skills to interact effectively with AI-driven services.
Consumers with higher levels of AI literacy are more likely to appreciate the benefits of
AI-driven services and engage with them more effectively. Therefore, businesses should
invest in educational initiatives to promote consumer understanding and acceptance of
these technologies.

---

<!-- PAGE 19 -->

J. Risk Financial Manag. 2024, 17, 470

19 of 25

In conclusion, this study’s implications highlight the importance of policymakers
considering the impact of GenAI-driven financial advice on personalized investment sug-
gestions, human-like empathy, and continuous improvement in consumer financial services.
As GenAI becomes increasingly integrated into the sector, policymakers must ensure that
consumers receive tailored advice that aligns with their unique financial circumstances,
fostering trust and engagement. Additionally, they should prioritize consumer privacy
protection while promoting equitable access to AI-driven benefits, addressing the digital
divide. This may involve establishing standards for transparency in AI algorithms, ensur-
ing data privacy, and implementing digital literacy programs. By proactively addressing
these issues with a focus on personalization, empathy, and continuous improvement, pol-
icymakers can create a regulatory landscape that supports responsible innovation. This
approach will ultimately encourage the development and deployment of AI technologies
within the financial sector that prioritize individual needs, build meaningful connections,
and continuously evolve to serve consumers better.

6.3. Limitations and Future Directions

Although this study provides valuable insights into the factors influencing consumer
perceptions and attitudes towards GenAI in the context of financial advice, it is important
to recognize its limitations. One limitation is its focus on mobile banking users as the
sample population, which may limit the generalizability of these findings to other con-
sumer segments. Future research could address this by exploring similar questions across
different demographics. Additionally, utilizing qualitative methodologies, such as in-depth
interviews or focus groups, could provide a more nuanced understanding of consumer
perceptions of and attitudes towards GenAI-driven financial advice.

Another avenue for future research is to examine the influence of cultural differences
on consumer reactions to GenAI-powered financial advisors. Given the variability in
cultural values, norms, and expectations across societies, it is plausible that the factors
influencing perceived authenticity and utilitarian attitudes towards GenAI-driven financial
advice may vary. Comparative studies across different cultural contexts could offer valuable
insights into designing and deploying GenAI-driven financial advisors to meet the unique
needs and preferences of diverse consumer groups.

Finally, ethical considerations and privacy concerns surrounding GenAI-driven finan-
cial advice are critical areas for future research. As GenAI systems become more integrated
into financial services, ensuring they are designed and deployed to respect consumer pri-
vacy, avoid bias, and promote fairness is paramount. Research on the ethical implications of
GenAI-driven financial advice could inform the development of guidelines and regulations
to ensure these technologies are used responsibly and in the best interests of consumers.

Author Contributions: Conceptualization, Q.Y. and Y.-C.L.; methodology, Q.Y. and Y.-C.L.; software,
Q.Y.; validation, Q.Y. and Y.-C.L.; formal analysis, Q.Y. and Y.-C.L.; investigation, Q.Y.; data curation,
Q.Y. and Y.-C.L.; writing—original draft preparation, Q.Y.; writing—review and editing, Y.-C.L.;
visualization, Q.Y. and Y.-C.L.; supervision, Y.-C.L. All authors have read and agreed to the published
version of the manuscript.

Funding: This research received no external funding.

Data Availability Statement: The data that support the findings of this study are available from the
authors upon reasonable request.

Conflicts of Interest: The authors declare no conflicts of interest.

---

<!-- PAGE 20 -->

J. Risk Financial Manag. 2024, 17, 470

20 of 25

Appendix A

Table A1. Operational definitions and measurement items.

Constructs

Measurements

Source(s)

Personalized
Investment
Suggestions
(PISs)

Human-Like
Empathy
(HLE)

Continuous Improvement (CI)

Perceived Authenticity (PA)

1. I feel that the investment suggestion by the GenAI is in line
with my preferences.
2. I feel that the investment suggestion by the GenAI is in line
with my taste.
3. The investment suggestion by the GenAI is what I am
interested in.
4. The investment suggestion by the GenAI is better than the
suggestions I get from other places.
5. I feel that the quality of investment suggestion by the GenAI
is what I want.
6. My overall evaluation of the GenAI investment suggestion is
very high.
7. I think the the GenAI investment suggestions are valuable.
8. The investment suggestions of the GenAI is flexible and
changeable according to my question.

1. The GenAI makes me feel warm.
2. The GenAI makes me feel that it cares about my needs.
3. The GenAI makes me feel concerned.
4. I feel that the GenAI serves me attentively.
5. I feel that the GenAI puts my interests first.
6. The GenAI gives me personalized attention.
7. The GenAI has expressed being able to empathize with the
customer’s feelings.
8. The GenAI has indicated it could put itself well in the
customer’s shoes.
9. The GenAI is able to accurately understand the
customer’s concerns.
10. The GenAI can adopt my perspective and recommending
the desired financial products.
11. The GenAI is preoccupied with offering me the best
financial products.

1. The GenAI can learn from past experience.
2. The GenAI’s ability is enhanced through learning.
3. After a period of use, the GenAI’s performance is getting
better and better.
4. I can feel the GenAI is constantly upgrading.
5. The GenAI fixes previous errors.
6. I feel that the GenAI is getting more and more advanced.
7. The function of the GenAI has been enhanced.

1. When I think of the GenAI, I see a unique set
of characteristics.
2. I would think of the GenAI as a unique individual.
3. Using the GenAI provided me with genuine experiences.

Utilitarian Attitude
(UA)

1. The GenaI is useful.
2. The GenAI is productive.
3. The GenaI is necessary.
4. The GenAI is practical.
5. The GenAI is functional.

(Q. Chen et al. 2022)

(Pelau et al. 2021; Fu et al.
2023; Hu and Bentler 1999)

(Q. Chen et al. 2022)

(Vo et al. 2024; Meng et al.
2023)

(Priya and Sharma 2023)

---

<!-- PAGE 21 -->

J. Risk Financial Manag. 2024, 17, 470

21 of 25

Table A1. Cont.

Constructs

Measurements

Source(s)

Willingness to Communicate
with GenAI
(WCG)

Resistance to Communicating
with GenAI
(RCG)

AI Literacy (AIL)

1. I am willing to receive financial advisory services from
GenAI.
2. I will feel happy to interact with GenAI.
3. I am likely to interact with GenAI.
4. I would like to utilize the GenAI-powered financial service if
there is an opportunity.
5. I intend to utilize the GenAI financial advisory
service continuously.
6. I recommend the GenAI financial advisory service to
my friends.

1. The financial advisory service provided by the GenAI is
processed in a less humanized manner.
2. I prefer human contact when looking for
investment suggestions.
3. People need emotional exchange during service transactions.
4. Interaction with the GenAI lacks social contact.
5. The existing problems with GenAI make me take a
wait-and-see approach to it.
6. I do not plan to continue using GenAI.

1. I can use AI to solve problems involving text and words.
2. I know how to decide which data to collect and how to
process them for training AI models to solve problems.
3. I know how to interpret results obtained from AI to
solve problems.
4. I know how to select AI algorithms to solve problems.
5. I know how to improve my ability to use AI for
problem-solving.
6. I can use AI to solve problems involving images and videos.

(Ma and Huo 2023; Kim and
Hur 2023)

(Ma and Huo 2023; Yang et al.
2023)

(Almatrafi et al. 2024; Kong
et al. 2024)

References

Alboqami, Hassan. 2023. Trust Me, I’m an Influencer!-Causal Recipes for Customer Trust in Artificial Intelligence Influencers in the

Retail Industry. Journal of Retailing and Consumer Services 72: 103242. [CrossRef]

Aldunate, Ángeles, Sebastián Maldonado, Carla Vairetti, and Guillermo Armelini. 2022. Understanding Customer Satisfaction via

Deep Learning and Natural Language Processing. Expert Systems with Applications 209: 118309. [CrossRef]

Ali, Hassnian, and Ahmet Faruk Aysan. 2023. What Will ChatGPT Revolutionize in Financial Industry? Available online: https:

//papers.ssrn.com/sol3/papers.cfm?abstract_id=4403372 (accessed on 18 August 2024).

Alimamy, Saifeddin, and Mohammad Amin Kuhail. 2023. I Will Be with You Alexa! The Impact of Intelligent Virtual Assistant’s

Authenticity and Personalization on User Reusage Intentions. Computers in Human Behavior 143: 107711. [CrossRef]

Alimamy, Saifeddin, and Samer Al-Imamy. 2022. Customer Perceived Value through Quality Augmented Reality Experiences in Retail:

The Mediating Effect of Customer Attitudes. Journal of Marketing Communications 28: 428–47. [CrossRef]

Almatrafi, Omaima, Aditya Johri, and Hyuna Lee. 2024. A Systematic Review of AI Literacy Conceptualization, Constructs, and

Implementation and Assessment Efforts (2019–2023). Computers and Education Open 6: 100173. [CrossRef]

Ameen, Nisreen, Ali Tarhini, Alexander Reppel, and Amitabh Anand. 2021. Customer Experiences in the Age of Artificial Intelligence.

Computers in Human Behavior 114: 106548. [CrossRef]

Ashta, Arvind, and Heinz Herrmann. 2021. Artificial Intelligence and Fintech: An Overview of Opportunities and Risks for Banking,

Investments, and Microfinance. Strategic Change 30: 211–22. [CrossRef]

Attié, Elodie, and Lars Meyer-Waarden. 2022. The Acceptance and Usage of Smart Connected Objects According to Adoption Stages:
An Enhanced Technology Acceptance Model Integrating the Diffusion of Innovation, Uses and Gratification and Privacy Calculus
Theories. Technological Forecasting and Social Change 176: 121485. [CrossRef]

Baabdullah, Abdullah M., Ali Abdallah Alalwan, Raed Salah Algharabat, Bhimaraya Metri, and Nripendra P. Rana. 2022. Virtual
Agents and Flow Experience: An Empirical Examination of AI-Powered Chatbots. Technological Forecasting and Social Change 181:
121772. [CrossRef]

Baek, Tae Hyun, and Minseong Kim. 2023. Is ChatGPT Scary Good? How User Motivations Affect Creepiness and Trust in Generative

Artificial Intelligence. Telematics and Informatics 83: 102030. [CrossRef]

---

<!-- PAGE 22 -->

J. Risk Financial Manag. 2024, 17, 470

22 of 25

Bag, Surajit, Gautam Srivastava, Md Mamoon Al Bashir, Sushma Kumari, Mihalis Giannakis, and Abdul Chowdhury. 2022. Journey of
Customers in this Digital Era: Understanding the Role of Artificial Intelligence Technologies in User Engagement and Conversion.
Benchmarking 29: 2074–98. [CrossRef]

Baidoo-Anu, David, and Leticia Owusu Ansah. 2023. Education in the Era of Generative Artificial Intelligence (AI): Understanding the

Potential Benefits of ChatGPT in Promoting Teaching and Learning. Journal of AI 7: 52–62. [CrossRef]

Bhatia, Ankita, Arti Chandani, Rajiv Divekar, Mita Mehta, and Neeraja Vijay. 2022. Digital Innovation in Wealth Management
Landscape: The Moderating Role of Robo Advisors in Behavioural Biases and Investment Decision-Making. International Journal
of Innovation Science 14: 693–712. [CrossRef]

Brenner, Lukas, and Tobias Meyll. 2020. Robo-Advisors: A Substitute for Human Financial Advice? Journal of Behavioral and Experimental

Finance 25: 100275. [CrossRef]

Cardon, Peter, Carolin Fleischmann, Jolanta Aritz, Minna Logemann, and Jeanette Heidewald. 2023. The Challenges and Opportunities
of AI-Assisted Writing: Developing AI Literacy for the AI Age. Business and Professional Communication Quarterly 86: 257–95.
[CrossRef]

Carolus, Astrid, Martin Jakosus Koch, Samantha Straka, Marc Erich Latoschik, and Carolin Wienrich. 2023. MAILS—Meta AI Literacy
Scale: Development and Testing of an AI Literacy Questionnaire Based on Well-Founded Competency Models and Psychological
Change- and Meta-Competencies. Computers in Human Behavior 1: 100014. [CrossRef]

Chang, Tsung-Sheng, and Wei-Hung Hsiao. 2024. Understand Resist Use Online Customer Service Chatbot: An Integrated Innovation

Resist Theory and Negative Emotion Perspective. Aslib Journal. [CrossRef]

Chen, Boyang, Zongxiao Wu, and Ruoran Zhao. 2023. From Fiction to Fact: The Growing Role of Generative AI in Business and

Finance. Journal of Chinese Economic and Business Studies 21: 471–96. [CrossRef]

Chen, Qian, Yeming Gong, Yaobin Lu, and Jing Tang. 2022. Classifying and Measuring the Service Quality of AI Chatbot in Frontline

Service. Journal of Business Research 145: 552–68. [CrossRef]

Chi, Nguyen Thi Khanh, and Nam Hoang Vu. 2023.

Investigating the Customer Trust in Artificial Intelligence: The Role of

Anthropomorphism, Empathy Response, and Interaction. CAAI Transactions on Intelligence Technology 8: 260–73. [CrossRef]
Chou, Szu-Yu, Chih-Wei Lin, Yi-Chun Chen, and Jyh-Shen Chiou. 2023. The Complementary Effects of Bank Intangible Value Binding

in Customer Robo-Advisory Adoption. International Journal of Bank Marketing 41: 971–88. [CrossRef]

Chuah, Stephanie Hui-Wen, and Joanne Yu. 2021. The Future of Service: The Power of Emotion in Human-Robot Interaction. Journal of

Retailing and Consumer Services 61: 102551. [CrossRef]

Dewasiri, Narayanage Jayantha, Karunarathnage Sajith Senaka Nuwansiri Karunarathna, Mananage Shanika Hansini Rathnasiri,
Dunusinghe Dharmarathne, and Kiran Sood. 2024. Unleashing the Challenges of Chatbots and ChatGPT in the Banking Industry:
Evidence from an Emerging Economy. In The Framework for Resilient Industry: A Holistic Approach for Developing Economies. London:
Routledge, pp. 23–37.

Dinh, Cong-Minh, and Sungjun Park. 2023. How to Increase Consumer Intention to Use Chatbots? An Empirical Analysis of Hedonic
and Utilitarian Motivations on Social Presence and the Moderating Effects of Fear across Generations. Electronic Commerce Research
6: 1–41. [CrossRef]

Du, Hua, Yanchao Sun, Haozhe Jiang, A. Y. M. Atiquil Islam, and Xiaoqing Gu. 2024. Exploring the Effects of AI Literacy in Teacher

Learning: An Empirical Study. Humanities and Social Sciences Communications 11: 559. [CrossRef]

Esmark Jones, Carol L., Tyler Hancock, Brett Kazandjian, and Clay M. Voorhees. 2022. Engaging the Avatar: The Effects of Authenticity

Signals during Chat-Based Service Recoveries. Journal of Business Research 144: 703–16. [CrossRef]

Fornell, Claes, and David F. Larcker. 1981. Structural Equation Models with Unobservable Variables and Measurement Error: Algebra

and Statistics. Journal of Marketing Research 18: 39–50. [CrossRef]

Fu, Jindi, Samar Mouakket, and Yuan Sun. 2023. The Role of Chatbots’ Human-Like Characteristics in Online Shopping. Electronic

Commerce Research and Applications 61: 101304. [CrossRef]

Fu, Xuemei. 2024. Understanding the Adoption Intention for Electric Vehicles: The Role of Hedonic-Utilitarian Values. Energy 301:

131703. [CrossRef]

Fui-Hoon Nah, Fiona, Ruilin Zheng, Jingyuan Cai, Keng Siau, and Langtao Chen. 2023. Generative AI and ChatGPT: Applications,
Challenges, and AI-Human Collaboration. Journal of Information Technology Case and Application Research 25: 277–304. [CrossRef]
Ghosh, Manimay. 2024. Empirical Study on Consumers’ Reluctance to Mobile Payments in a Developing Economy. Journal of Science

and Technology Policy Management 15: 67–92. [CrossRef]

Glikson, Ella, and Omri Asscher. 2023. AI-Mediated Apology in a Multilingual Work Context: Implications for Perceived Authenticity

and Willingness to Forgive. Computers in Human Behavior 140: 107592. [CrossRef]

Grönroos, Christian. 2008. Service Logic Revisited: Who Creates Value? And Who Co-Creates? European Business Review 20: 298–314.

[CrossRef]

Gursoy, Dogan, Oscar Hengxuan Chi, Lu Lu, and Robin Nunkoo. 2019. Consumers’ Acceptance of Artificially Intelligent (AI) Device

Use in Service Delivery. International Journal of Information Management 49: 157–69. [CrossRef]

Hair, Joseph Franklin, Marcelo Luiz Dias da Silva Gabriel, and Vijay K. Patel. 2014. AMOS Covariance-Based Structural Equation
Modeling (CB-SEM): Guidelines on its Application as a Marketing Research Tool. Brazil Journal of Marketing 13: 1–15. [CrossRef]
Hsieh, Pi-Jung. 2016. An Empirical Investigation of Patients’ Acceptance and Resistance Toward the Health Cloud: The Dual Factor

Perspective. Computers in Human Behavior 63: 959–69. [CrossRef]

---

<!-- PAGE 23 -->

J. Risk Financial Manag. 2024, 17, 470

23 of 25

Hu, Li-Tze, and Peter M. Bentler. 1999. Cutoff Criteria for Fit Indexes in Covariance Structure Analysis: Conventional Criteria Versus

New Alternatives. Structural Equation Modeling 6: 1–55. [CrossRef]

Huang, Ming-Hui, and Roland T. Rust. 2018. Artificial Intelligence in Service. Journal of Service Research 21: 155–72. [CrossRef]
Huang, Ming-Hui, and Roland T. Rust. 2021. Engaged to a Robot? The Role of AI in Service. Journal of Service Research 24: 30–41.

[CrossRef]

Jan, Ihsan Ullah, Seonggoo Ji, and Changju Kim. 2023. What (De) Motivates Customers to Use AI-Powered Conversational Agents for

Shopping? The Extended Behavioral Reasoning Perspective. Journal of Retailing and Consumer Services 75: 103440. [CrossRef]
Javaid, Mohd, Abid Haleem, and Ravi Pratap Singh. 2023. A Study on ChatGPT for Industry 4.0: Background, Potentials, Challenges,

and Eventualities. Journal of Economy and Technology 1: 127–43. [CrossRef]

Kelly, Sage, Sherrie-Anne Kaye, and Oscar Oviedo-Trespalacios. 2023. What Factors Contribute to the Acceptance of Artificial

Intelligence? A Systematic Review. Telematics and Informatics 77: 101925. [CrossRef]

Kim, Hee Woong, Hock Chuan Chan, and Sumeet Gupta. 2007. Value-Based Adoption of Mobile Internet: An Empirical Investigation.

Decision Support Systems 43: 111–26. [CrossRef]

Kim, Juran, Seungmook Kang, and Joonheui Bae. 2022. Human Likeness and Attachment Effect on the Perceived Interactivity of AI

Speakers. Journal of Business Research 144: 797–804. [CrossRef]

Kim, Woo Bin, and Hee Jin Hur. 2023. What Makes People Feel Empathy for AI Chatbots? Assessing the Role of Competence and

Warmth. International Journal of Human–Computer Interaction 40: 4674–87. [CrossRef]

Ko, Hyungjin, and Jaewook Lee. 2024. Can ChatGPT Improve Investment Decisions? From a Portfolio Management Perspective.

Finance Research Letters 64: 105433. [CrossRef]

Kong, Siu-Cheung, William Man-Yin Cheung, and Olson Tsang. 2024. Developing an Artificial Intelligence Literacy Framework:
Evaluation of a Literacy Course for Senior Secondary Students Using a Project-Based Learning Approach. Computers & Education:
Artificial Intelligence 6: 100214. [CrossRef]

Kuhail, Mohammad Amin, Justin Thomas, Salwa Alramlawi, Syed Jawad Hussain Shah, and Erik Thornquist. 2022. Interacting with a
Chatbot-Based Advising System: Understanding the Effect of Chatbot Personality and User Gender on Behavior. Informatics 9: 81.
[CrossRef]

Kwon, Jookyung, Eklou Amendah, and Jiseon Ahn. 2024. Mediating Role of Perceived Authenticity in the Relationship between

Luxury Service Experience and Life Satisfaction. Journal of Strategic Marketing 32: 137–51. [CrossRef]

Lee, Garim, and Hye-Young Kim. 2024. Human vs. AI: The Battle for Authenticity in Fashion Design and Consumer Response. Journal

of Retailing and Consumer Services 77: 103690. [CrossRef]

Li, Jian, Jinsong Huang, and Yaqi Li. 2023. Examining the Effects of Authenticity Fit and Association Fit: A Digital Human Avatar

Endorsement Model. Journal of Retailing and Consumer Services 71: 103230. [CrossRef]

Lin, Hongxia, Oscar Hengxuan Chi, and Dogan Gursoy. 2020. Antecedents of Customers’ Acceptance of Artificially Intelligent Robotic

Device Use in Hospitality Services. Journal of Hospitality Marketing and Management 29: 530–49. [CrossRef]

Ma, Xiaoyue, and Yudi Huo. 2023. Are Users Willing to Embrace ChatGPT? Exploring the Factors on the Acceptance of Chatbots from

the Perspective of AIDUA Framework. Technology in Society 75: 102362. [CrossRef]

Markovitch, Dmitri G., Rusty A. Stough, and Dongling Huang. 2024. Consumer Reactions to Chatbot Versus Human Service: An
Investigation in the Role of Outcome Valence and Perceived Empathy. Journal of Retailing and Consumer Services 79: 103847.
[CrossRef]

Markus, André, Jan Pfister, Astrid Carolus, Andreas Hotho, and Carolin Wienrich. 2024. Effects of AI Understanding-Training on AI
Literacy, Usage, Self-Determined Interactions, and Anthropomorphization with Voice Assistants. Computers & Education Open 6:
100176. [CrossRef]

Meng, Lu, Tongmao Li, Xiaolin Shi, and Xin Huang. 2023. Double-Sided Messages Improve the Acceptance of Chatbots. Annals of

Tourism Research 102: 103644. [CrossRef]

Morhart, Felicitas, Lucia Malär, Amélie Guèvremont, Florent Girardin, and Bianca Grohmann. 2015. Brand Authenticity: An Integrative

Framework and Measurement Scale. Journal of Consumer Psychology 25: 200–18. [CrossRef]

Musto, Cataldo, Giovanni Semeraro, Pasquale Lops, Marco de Gemmis, and Georgios Lekkas. 2015. Personalized Finance Advisory
through Case-Based Recommender Systems and Diversification Strategies. Decision Support System 77: 100–11. [CrossRef]
Napoli, Julie, Sonia J. Dickinson, Michael B. Beverland, and Francis Farrelly. 2014. Measuring Consumer-Based Brand Authenticity.

Journal of Business Research 67: 1090–98. [CrossRef]

Nazir, Anam, and Ze Wang. 2023. A Comprehensive Survey of ChatGPT: Advancements, Prospects Applications, and Challenges.

Meta-Radiology 1: 100022. [CrossRef]

Ng, Davy Tsz Kit, Jac Ka Lok Leung, Samuel Kai Wah Chu, and Maggie Shen Qiao. 2021. Conceptualizing AI Literacy: An Exploratory

Review. Computers & Education: Artificial Intelligence 2: 100041. [CrossRef]

Niu, Ben, and Gustave Florentin Nkoulou Mvondo. 2024. I Am ChatGPT, the Ultimate AI Chatbot! Investigating the Determinants of
Users’ Loyalty and Ethical Usage Concerns of ChatGPT. Journal of Retailing and Consumer Services 76: 103562. [CrossRef]

Oehler, Andreas, and Matthias Horn. 2024. Does ChatGPT Provide Better Advice than Robo-Advisors? Finance Research Letters 60:

104898. [CrossRef]

Pandey, Palima, and Alok Kumar Rai. 2024. Analytical Modeling of Perceived Authenticity in AI Assistants: Application of PLS-Predict

Algorithm and Importance-Performance Map Analysis. South Asian Journal of Business Studies. [CrossRef]

---

<!-- PAGE 24 -->

J. Risk Financial Manag. 2024, 17, 470

24 of 25

Paul, Justin, Akiko Ueno, and Charles Dennis. 2023. ChatGPT and Consumers: Benefits, Pitfalls and Future Research Agenda.

International Journal of Consumer Studies 47: 1213–25. [CrossRef]

Pelau, Corina, Dan-Cristian Dabija, and Irina Ene. 2021. What makes an AI device human-like? The role of interaction quality, empathy
and perceived psychological anthropomorphic characteristics in the acceptance of artificial intelligence in the service industry.
Computers in Human Behavior 122: 106855. [CrossRef]

Perchik, Jordan D., A. D. Smith, A. A. Elkassem, J. M. Park, S. A. Rothenberg, M. Tanwar, and H. Sotoudeh. 2023. Artificial Intelligence

Literacy: Developing a Multi-Institutional Infrastructure for AI Education. Academic Radiology 30: 1472–80. [CrossRef]

Pitardi, Valentina. 2023. Personalized and Contextual Artificial Intelligence-Based Services Experience. In Artificial Intelligence in

Customer Service: The Next Frontier for Personalized Engagement. Cham: Springer, pp. 101–22. [CrossRef]

Podsakoff, Philip M., and Dennis W. Organ. 1986. Self-Reports in Organizational Research: Problems and Prospects. Journal of

Management 12: 531–44. [CrossRef]

Priya, Bhanu, and Vivek Sharma. 2023. Exploring Users’ Adoption Intentions of Intelligent Virtual Assistants in Financial Services: An
Anthropomorphic Perspectives and Socio-Psychological Perspectives. Computers in Human Behavior 148: 107912. [CrossRef]
Raj, Rohit, Arpit Singh, Vimal Kumar, and Pratima Verma. 2023. Analyzing the Potential Benefits and Use Cases of ChatGPT as a Tool
for Improving the Efficiency and Effectiveness of Business Operations. BenchCouncil Transactions on Benchmarks, Standards and
Evaluations 3: 100140. [CrossRef]

Raza, Syed A., Wasim Qazi, Komai Akram Khan, and Javeria Salam. 2021. Social Isolation and Acceptance of the Learning Management
System (LMS) in the Time of COVID-19 Pandemic: An Expansion of the UTAUT Model. Journal of Educational Computing Research
59: 183–208. [CrossRef]

Rese, Alexandra, Lena Ganster, and Daniel Baier. 2020. Chatbots in Retailers’ Customer Communication: How to Measure Their

Acceptance? Journal of Retailing and Consumer Services 56: 102176. [CrossRef]

Riikkinen, Mikko, Hannu Saarijärvi, Peter Sarlin, and Ilkka Lähteenmäki. 2018. Using Artificial Intelligence to Create Value in

Insurance. International Journal of Bank Marketing 36: 1145–68. [CrossRef]

Roh, Taewoo, Byung Il Park, and Shufeng Xiao. 2023. Adoption of AI-Enabled Robo-Advisors in Fintech: Simultaneous Employment
of UTAUT and the Theory of Reasoned Action. Journal of Electronic Commerce Research 24: 29–47. Available online: https:
//api.semanticscholar.org/CorpusID:258835831 (accessed on 11 October 2024).

Roumeliotis, Konstantinos I., and Nikolaos D. Tselikas. 2023. ChatGPT and Open-AI Models: A Preliminary Review. Future Internet 15:

192. [CrossRef]

Seitz, Lennart. 2024. Artificial Empathy in Healthcare Chatbots: Does it Feel Authentic? Computers in Human Behavior: Artificial Humans

2: 100067. [CrossRef]

Shin, Donghee, Azmat Rasul, and Anestis Fotiadis. 2022. Why Am I Seeing This? Deconstructing Algorithm Literacy through the Lens

of Users. Internet Research 32: 1214–34. [CrossRef]

Sironi, Paolo. 2016. FinTech Innovation: From Robo-Advisors to Goal Based Investing and Gamification. Hoboken: John Wiley & Sons.
Sperling, Katarina, Carl-Johan Stenberg, Cormac McGrath, Anna Åkerfeldt, Fredrik Heintz, and Linnea Stenliden. 2024. In Search of
Artificial Intelligence (AI) Literacy in Teacher Education: A Scoping Review. Computers and Education Open 6: 100169. [CrossRef]
Srinivasan, Srini S., Rolph Anderson, and Kishore Ponnavolu. 2002. Customer Loyalty in E-Commerce: An Exploration of its

Antecedents and Consequences. Journal of Retailing 78: 41–50. [CrossRef]

Stahl, Bernd Carsten, and Damian Eke. 2024. The Ethics of ChatGPT–Exploring the Ethical Issues of an Emerging Technology.

International Journal of Information Management 74: 102700. [CrossRef]

Tam, Kar Yan, and Shuk Ying Ho. 2005. Web Personalization as a Persuasion Strategy: An Elaboration Likelihood Model Perspective.

Information Systems Research 16: 271–91. [CrossRef]

Tirado-Morueta, Ramón, José Ignacio Aguaded-Gómez, and Ángel Hernando-Gómez. 2018. The Socio-Demographic Divide in Internet

Usage Moderated by Digital Literacy Support. Technology in Society 55: 47–55. [CrossRef]

Ullah, Rafid, Hishamuddin Bin Ismail, Mohammad Tariqul Islam Khan, and Ali Zeb. 2024. Nexus between ChatGPT Usage Dimensions
and Investment Decisions Making in Pakistan: Moderating Role of Financial Literacy. Technology in Society 76: 102454. [CrossRef]
Van Teijlingen, Edwin R., and Vanora Hundley. 2002. The importance of pilot studies. Social Research Update 35: 1–4. Available online:

http://sru.soc.surrey.ac.uk/SRU35.html (accessed on 11 October 2024). [CrossRef]

Vargo, Stephen L., and Robert F. Lusch. 2004. Evolving to a New Dominant Logic for Marketing. Journal of Marketing 68: 1–17.

[CrossRef]

Vargo, Stephen L., Paul P. Maglio, and Melissa Archpru Akaka. 2008. On Value and Value Co-Creation: A Service Systems and Service

Logic Perspective. European Management Journal 26: 145–52. [CrossRef]

Vesanen, Jari. 2007. What is Personalization? A Conceptual Framework. European Journal of Marketing 41: 409–18. [CrossRef]
Vo, Diem-Trang, Long T. V. Nguyen, Duy Dang-Pham, and Ai-Phuong Hoang. 2024. When Young Customers Co-Create Value of

AI-Powered Branded App: The Mediating Role of Perceived Authenticity. Young Consumers 25: 557–78. [CrossRef]

Wang, Bingcheng, Pei-Luen Rau, and Tianyi Yuan. 2023. Measuring User Competence in Using Artificial Intelligence: Validity and

Reliability of Artificial Intelligence Literacy Scale. Behaviour & Information Technology 42: 1324–37. [CrossRef]

Wen, Haitao, Lulu Zhang, Ao Sheng, Mingda Li, and Bingfeng Guo. 2022. From “Human-to-Human” to “Human-to-Non-Human”–
Influence Factors of Artificial Intelligence-Enabled Consumer Value Co-Creation Behavior. Frontiers in Psychology 13: 863313.
[CrossRef]

---

<!-- PAGE 25 -->

J. Risk Financial Manag. 2024, 17, 470

25 of 25

Xia, Huosong, Qian Zhang, Justin Zuopeng Zhang, and Leven J. Zheng. 2023. Exploring Investors’ Willingness to Use Robo-Advisors:

Mediating Role of Emotional Response. Industrial Management & Data Systems 123: 2857–81. [CrossRef]

Yang, Bo, Yongqiang Sun, and Xiao-Liang Shen. 2023. Understanding AI-Based Customer Service Resistance: A Perspective of

Defective AI Features and Tri-Dimensional Distrusting Beliefs. Information Processing and Management 60: 103257. [CrossRef]

Zamil, Ahmad M. A., Saqib Ali, Minhas Akbar, Vaclav Zubr, and Farhan Rasool. 2023. The Consumer Purchase Intention toward
Hybrid Electric Car: A Utilitarian-Hedonic Attitude Approach. Frontiers in Environmental Science 11: 1101258. [CrossRef]
Zhu, Hui, Olli Vigren, and Inga-Lill Söderberg. 2024. Implementing Artificial Intelligence Empowered Financial Advisory Services: A

Literature Review and Critical Research Agenda. Journal of Business Research 174: 114494. [CrossRef]

Disclaimer/Publisher’s Note: The statements, opinions and data contained in all publications are solely those of the individual
author(s) and contributor(s) and not of MDPI and/or the editor(s). MDPI and/or the editor(s) disclaim responsibility for any injury to
people or property resulting from any ideas, methods, instructions or products referred to in the content.

<!-- MARKITDOWN CONVERSION -->

<!-- Full MarkItDown conversion for formatting fidelity. -->

Journal of
Risk and Financial
Management
Article
Enhancing Financial Advisory Services with GenAI: Consumer
Perceptions and Attitudes Through Service-Dominant Logic and
Artificial Intelligence Device Use Acceptance Perspectives
QinYangandYoung-ChanLee*
DepartmentofInformationManagement,CollegeofGlobalSocialManagement,DonggukUniversity,
Gyeongju38066,RepublicofKorea;yangqin05@yeah.net
* Correspondence:chanlee@dongguk.ac.kr
Abstract: Financialinstitutionsarecurrentlyundergoingasignificantshiftfromtraditionalrobo-
advisorstomoreadvancedgenerativeartificialintelligence(GenAI)technologies.Thistransformation
hasmotivatedustoinvestigatethefactorsinfluencingconsumerresponsestoGenAI-drivenfinancial
advice.Despiteextensiveresearchontheadoptionofrobo-advisors,thereisagapinourunderstand-
ingofthespecificcontributorsto,anddifferencesin,consumerattitudesandreactionstoGenAI-based
financialguidance. Thisstudyaimstoaddressthisgapbyanalyzingtheimpactofpersonalized
investmentsuggestions,human-likeempathy,andthecontinuousimprovementofGenAI-provided
financialadviceonitsauthenticityasperceivedbyconsumers,theirutilitarianattitudetowardthe
useofGenAIforfinancialadvice,andtheirreactionstoGenAI-generatedfinancialsuggestions.A
comprehensiveresearchmodelwasdevelopedbasedonservice-dominantlogic(SDL)andArtificial
IntelligenceDeviceUseAcceptance(AIDUA)frameworks.Themodelwassubsequentlyemployed
inastructuralequationmodeling(SEM)analysisofsurveydatafrom822mobilebankingusers.The
findingsindicatethatpersonalizedinvestmentsuggestions,human-likeempathy,andthecontinuous
improvementofGenAI’srecommendationspositivelyinfluenceconsumers’perceptionofitsauthen-
ticity. Moreover,wediscoveredapositivecorrelationbetweenutilitarianattitudesandperceived
Citation:Yang,Qin,andYoung-Chan
authenticity,whichultimatelyinfluencesconsumers’responsestoGenAI’sfinancialadvisorysolu-
Lee.2024.EnhancingFinancial
tions.Thisismanifestedaseitherawillingnesstoengageorresistancetocommunication.Thisstudy
AdvisoryServiceswithGenAI:
contributestotheresearchonGenAI-poweredfinancialservicesandunderscoresthesignificanceof
ConsumerPerceptionsandAttitudes
integratingGenAIfinancialguidanceintotheroutineoperationsoffinancialinstitutions.Ourwork
ThroughService-DominantLogicand
ArtificialIntelligenceDeviceUse buildsuponpreviousresearchonrobo-advisors,offeringpracticalinsightsforfinancialinstitutions
AcceptancePerspectives.Journalof seekingtoleverageGenAI-driventechnologiestoenhancetheirservicesandcustomerexperiences.
RiskandFinancialManagement17: 470.
https://doi.org/10.3390/jrfm17100470 Keywords:GenAIfinancialadvice;consumerperceptions;service-dominantlogic(SDL);Artificial
IntelligenceDeviceUseAcceptance(AIDUA);perceivedauthenticity
AcademicEditors:Jong-MinKimand
ThanasisStengos
Received:29August2024
Revised:11October2024 1. Introduction
Accepted:15October2024
The financial sector is undergoing a profound transformation with the advent of
Published:17October2024
sophisticated technologies such as robo-advisors and generative artificial intelligence
(GenAI)platformslikeChatGPT.Thistechnologicalrevolutionhasfundamentallyaltered
howindividualsmanagetheirfinancesandreceivefinancialadvice. Whilerobo-advisors
Copyright: © 2024 by the authors. providealgorithm-basedassetmanagementserviceswithminimalhumanintervention
Licensee MDPI, Basel, Switzerland. (Sironi2016),GenAItechnologieshavesignificantlyadvancedtheseservicesbyoffering
Thisarticleisanopenaccessarticle personalized,conversationalfinancialadvice,whichrepresentsanewfrontierindigital
distributed under the terms and financialservices(Dewasirietal.2024).
conditionsoftheCreativeCommons Previous research has thoroughly examined the impact of robo-advisors, focusing
Attribution(CCBY)license (https:// onkeyfactorssuchasbehavioralbiases, trust, perceivedrisk, anduserattitudesinthe
creativecommons.org/licenses/by/ adoptionandeffectivenessofautomatedfinancialadvisorysystems(BrennerandMeyll
4.0/).
J.RiskFinancialManag.2024,17,470.https://doi.org/10.3390/jrfm17100470 https://www.mdpi.com/journal/jrfm

J.RiskFinancialManag.2024,17,470 2of25
2020;Bhatiaetal.2022;Xiaetal.2023). However,thesestudieshavelargelyoverlooked
thespecificinfluenceofGenAItechnologies, particularlyintermsofhowtheirdistinct
attributes reshape user experiences in financial contexts. The gap identified by prior
research (Fui-Hoon Nah et al. 2023) suggests a need for future studies to explore how
GenAItechnologies,withtheirconversationalnatureandcapacityforcontinuouslearning,
influenceconsumerperceptionsoffinancialadviceservices. Addressingthisgap,ourstudy
buildsonthesuggestionsofpreviousresearchtoadvanceourunderstandingofhowGenAI
platformsaffectconsumerattitudesandbehaviors.
Toaddressthisresearchgap,thisstudyfocusesontheuniqueattributesofGenAI,
suchasitspersonalizedinvestmentsuggestions,human-likeempathy,andabilitytocon-
tinuouslylearnandimprove. Thesefeatureshavethepotentialtosignificantlyinfluence
consumers’perceptionsoftheauthenticityandreliabilityoffinancialadvice(Pelauetal.
2021). Buildingonthegapsidentifiedinearlierstudies,weintegrateservice-dominant
logic(SDL)andAIDeviceUseAcceptance(AIDUA)frameworkstoexploretherolethese
attributesplayinshapingconsumertrustinandacceptanceofGenAI-basedfinancialadvi-
soryservices(VargoandLusch2004;Gursoyetal.2019). Weemploystructuralequation
modelingtoanalyzedatafrom822mobilebankingusers,providingacomprehensiveexam-
inationofthefactorsthatdrivetheadoptionandeffectivenessofGenAIinfinancialadvice.
Ourresearchaimstoaddressfourprincipalquestions:
HowdoGenAI’sattributesinfluenceconsumers’perceptionsofauthenticityinusing
GenAIforfinancialadvice?
What is the relationship between perceived authenticity and utilitarian attitudes
towardsGenAIfinancialadvice?
Howdoutilitarianattitudesaffectconsumers’responsestoGenAIfinancialadvice?
HowdoesAIliteracymoderatetheimpactofGenAI’sattributesonperceivedauthen-
ticity?
Thisstudycontributestoboththeoryandpracticebyaddressingtheresearchgaps
identifiedinpriorstudies. Itoffersadeeperunderstandingofhowconsumersperceive
theauthenticityofGenAIfinancialadviceandprovidespracticalinsightsfordesigning,
implementing,andeducatingusersaboutGenAI-poweredfinancialservices. Byinvestigat-
ingtheimpactofGenAIattributesonperceivedauthenticityandsubsequentconsumer
attitudesandbehaviors,thisresearchnotonlyfillsasignificantgapintheliteraturebutalso
offerspracticalguidancefordevelopingeffectiveGenAI-basedfinancialadvisoryservices.
This paper is organized as follows: Section 2 presents a literature review and the
theoreticalframework, focusingontheevolutionoffinancialadvisoryservicesandthe
uniqueattributesofGenAI.Section3developstheresearchhypothesesandmodel,inte-
gratingservice-dominantlogic(SDL)andAIDeviceUseAcceptance(AIDUA)frameworks.
Section4 outlines the research methodology, including the data collection and the de-
velopmentofthemeasurement. Section5discussesthedataanalysisandtheresultsof
thestructuralmodel. Finally,Section6providestheconclusion,academicandpractical
implications,andsuggestionsforfutureresearchdirections.
2. LiteratureReviewandTheoreticalFramework
2.1. EvolutionofFinancialAdvisoryServices: FromRobo-AdvisorstoGenAI
Thelandscapeoffinancialadvisoryserviceshasdramaticallytransformedoverthe
pastdecade,withtheemergenceofrobo-advisorsrepresentingacrucialturningpoint.Robo-
advisorsemergedasaresponsetothedemandforcost-effectiveandaccessiblefinancial
planning tools, disrupting the traditional finance industry by providing standardized
investmentsolutionstoawideraudience(HuangandRust2018). Theseplatformsuse
algorithmstobuildportfolios,reducingtheneedforhumanfinancialplannersandlowering
theoverallcostofinvestmentadvice(BrennerandMeyll2020;Rohetal.2023;Chouetal.
2023). However, as technology rapidly advances, the limitations of robo-advisors are
becomingmoreevident. Theselimitationsincludealackofcustomization,aninabilityto

J.RiskFinancialManag.2024,17,470 3of25
empathizewithconsumers, anda limitedcapacitytolearn frompast data. Asa result,
thereisagrowingneedforashifttowardmoresophisticatedtools(Ullahetal.2024).
Thetransitionfromrobo-advisorstoGenAIrepresentsthenextstageintheevolution
offinancialadvisoryservices. GenAIplatformsrepresentasignificanttechnologicalleap,
deliveringinteractiveandpersonalizedfinancialadvicethroughadvancednaturallanguage
processing(NLP)andmachinelearning(ML)capabilities(RoumeliotisandTselikas2023).
In contrast to their robo-advisor predecessors, GenAI tools are capable of engaging in
dynamichuman–machineinteractions,simulatinghuman-likeconversations,andoffering
tailoredinvestmentsuggestionsthatadapttochangesinusers’financialsituationsandthe
marketconditions(Javaidetal.2023;OehlerandHorn2024).
ThedevelopmentofGenAIhasbeensignificantlyadvancedbysubstantialprogress
inNLP,whichhasenabledthesesystemstounderstand,interpret,andgeneratehuman
languagewithincreasingaccuracy. Theseadvancementsnotonlyincreasetheeffectiveness
ofAIadvisorsbutalsoenablethemtoengageinempatheticconversations,therebyim-
provingtheconsumerexperience(Aldunateetal.2022). ThecapacityofGenAItoprocess
complexinquiriesandexecutetransactionsthroughseamlessconversationsrepresentsa
paradigmshiftinhowconsumersmanagetheirinvestments,offeringamoreengagingand
personalizedadvisoryexperience(KoandLee2024).
AswecontinuetoexaminethecapabilitiesandconsequencesofGenAIinfinance,
itbecomesevidentthattheseadvancementsnotonlyindicateprogresswithinfinancial
institutions but also foreshadow profound changes in the nature of financial advisory
services. Theimplicationsforcustomerengagement,servicedelivery,andtheroleofAI
advisorsaresignificant. GenAIholdsimmensepotentialtoredefinethefinancialservices
industry(B.Chenetal.2023).Itisimperativethatbothfinancialinstitutionsandconsumers
comprehendthisevolutionarytrajectoryiftheyaretoeffectivelyleveragethesetechnologies
andnavigatethenewlandscapeofinvestmentadvice.
2.2. GenAI’sAttributes: PersonalizedInvestmentSuggestion,Human-likeEmpathy,and
ContinuousImprovement
AnotablefeatureofGenAIinfinancialservicesisitsabilitytoprovidepersonalized
recommendations. Personalizationisakeyfactorinconsumersatisfactionandthecontin-
ueduseoftechnology-basedservices(Srinivasanetal.2002;TamandHo2005). Unlike
robo-advisors,whichtypicallydeliverstandardizedrecommendationsusinglimitedal-
gorithms,GenAItoolscananalyzeextensiveconsumerinputandspecificdata,including
financial goals, risk tolerance, investment preferences, and even emotional cues, to tai-
lortheirrecommendationstoindividualneeds(AliandAysan2023). Thishighlevelof
personalizationinGenAI-drivenservicesenhancestherelevanceandeffectivenessofthe
investmentadvice,potentiallyleadingtobetterfinancialoutcomesforconsumers(Koand
Lee2024).
Inadditiontopersonalization,thecontinuousimprovementofGenAIisanothercriti-
calattribute,enabledbythemachinelearningalgorithmsembeddedintoGenAIsystems.
Thesesystemscanlearnandadaptthroughinteractionswithconsumers,therebyenhancing
theirabilitytoprovideaccurateandcontextualinvestmentadviceovertime(Ashtaand
Herrmann2021). Thisself-learningandimprovementfunctionisofparamountimportance
inadynamicfinancialmarketwhereconsumerneedsandthemarketconditionsareina
constantstateofflux. EmpiricalstudieshaveshownthatAIsystemscapableofcontinuous
learningandadaptationaremorelikelytogainusertrustandbeperceivedasauthentic
(Voetal.2024).
Finally,whiletheanalyticalcapabilitiesofGenAIhavebeenwidelyrecognized,the
roleofitshuman-likeempathyhasalsogarneredincreasingattention(NazirandWang
2023). TheincorporationofemotionalintelligenceintoGenAIenablesittorecognizeand
respond to consumers’ emotional cues, thereby elevating its interactions beyond mere
mechanicalresponsesandprovidingsupportthatalignswithconsumers’emotionalstates.
TheintegrationofAItoolswithhuman-likeempathycanenhanceconsumerengagement

J.RiskFinancialManag.2024,17,470 4of25
andtrust, asemotionalconnectionisanimportantcomponentofsuccessfulconsulting
relationships(Pelauetal.2021).
Thecombinationofpersonalizedinvestmentsuggestions,human-likeempathy,and
continuous improvement in GenAI represents a compelling value proposition for con-
sumers. Theseattributesarecombinedtocreateauserexperiencethatmirrorsinteraction
withahumanadvisorwhileharnessingtheeffectivenessandefficiencyofGenAItechnol-
ogy. GenAI’sapproachisnotablydifferentfromthe“onesizefitsall”modeloftraditional
robo-advisors. GenAIoffersahighdegreeofparticipation,adaptability,andemotional
intelligencethatalignswiththecomplexanddiverseneedsofconsumers.
2.3. PerceivedAuthenticityofGenAI
TheperceivedauthenticityofGenAI-poweredfinancialadviceisapivotalfactorin
establishing trust and encouraging user engagement. Users assess the authenticity of
platforms like GenAI based on their perception of the truthfulness, dependability, and
impartiality of the investment recommendations provided. Research has shown that
authenticity is crucial in determining users’ willingness to accept and engage with AI
advisors, forming the foundation for trust (Alboqami 2023; Glikson and Asscher 2023).
WhenGenAIisperceivedasauthentic,itnotonlygainsusers’confidencemoreeffectively
butalsofostersastrongerconnection,whichisvitalinthecontextoffinancialinformation
andassetsgiventhesensitivityofsuchmatters.
TheessenceofGenAI’sauthenticityinfinancialadviceliesnotonlyintheaccuracyof
itsinformationbutalsoinitsabilitytoofferrecommendationsthatalignwithusers’ethical
principlesandfinancialgoals(EsmarkJonesetal.2022). Moreover,itiscrucialtoensure
transparencyinhowGenAIhandlesuserdataandarrivesatitsrecommendationsinorder
toenhanceitsperceivedauthenticity. Thistransparency,inconjunctionwithacommitment
toethicalAIpractices,underscoresthesignificanceofclearcommunicationandethical
designprinciplesinthedevelopmentofGenAIsystems(StahlandEke2024).
2.4. UtilitarianAttitudestowardsGenAIandConsumerResponses
In evaluating consumer responses to GenAI, particularly in financial contexts, the
utilitarianperspectiveoffersacompellinglensthroughwhichtoviewthisphenomenon.
Utilityisakeyfactorintechnologyadoptionandastrongpredictorofconsumerwillingness
toengagewithAI.IfconsumersbelievethatGenAIwillenhancetheefficiencyoftheirasset
managementandimprovetheaccuracyoftheirdecisions,theirwillingnesstointeractwith
thetechnologywillincrease(MaandHuo2023).
TheefficacyofGenAI,includingtheaccuracyandrelevanceofitsinvestmentsugges-
tions,isofparamountimportanceindeterminingconsumerwillingnesstoengagewith
it (Niu and Mvondo 2024). The capacity of GenAI to furnish consistent, personalized,
andvaluablecounselexertsaprofoundinfluenceontheattitudeofitsusers, which, in
turn,affectstheirengagement,whetherpositiveornegative. Individualswhohavehad
positiveexperienceswithGenAIaremorelikelytodevelopafavorableattitudetowardit
andengagewithitagaininthefuture(Pauletal.2023).
However,itisimportanttoacknowledgethatnotallconsumersarewillingtoadopt
GenAI’s financial advice, despite its potential benefits. Consumer resistance can be at-
tributed to various factors, including a lack of trust, perceived loss of control, privacy
concerns,anddiscomfortwithtechnology(ChangandHsiao2024). Additionally,perceived
complexityandalessanthropomorphicinterfacemaycontributetoconsumerresistance
(BaekandKim2023). SomeconsumersmayperceiveGenAIasathreattotheirpersonalau-
tonomyorthesecurityoftheirassets,whichmayleadtoresistancetocommunicatingwith
it. ThisresistancemaybefurthercompoundedbyalackofunderstandingofhowGenAI
functionsorabeliefthatitisincapableofreplicatingtheintricatehumancomprehension
essentialforfinancialdecision-making.
Tocomprehendthereasonsbehindthedifferingattitudestowardtheutilizationof
GenAI,itisessentialtoinvestigatetheutilitarianattitudesofconsumerstowardsthese

J.RiskFinancialManag.2024,17,470 5of25
platforms. Anuancedunderstandingoftheseattitudesandtheirunderlyingdeterminants
canassistinthedevelopmentofGenAIapplicationsthatalignwithconsumerneedsbetter,
therebyreducingconsumerresistance.
2.5. AILiteracy
TheintegrationofGenAIintofinancialservicesisnotsolelyamatteroftechnological
development; it also involves user adaptation, in which AI literacy plays a crucial role.
AI literacy refers to the skills and competencies individuals need to effectively use AI
technologiesandapplications(Ngetal.2021).ThisincludesunderstandingAI’scapabilities,
context,andimplementation. TheintegrationofGenAIintofinancialservicesunderscores
the crucial role of AI literacy in influencing the adoption and usage of AI technologies
(Perchiketal.2023).
ThepreviousliteraturesuggeststhathighAIliteracycanalleviateusers’doubtsand
helpthemfullyharnessAI’spotentialinfinancialdecision-making,therebyenhancingthe
useofAItechnology(Cardonetal.2023). IndividualswithhigherlevelsofAIliteracyare
morelikelytotrustandrelyonAI-drivenfinancialadvice(Shinetal.2022). Furthermore,
AIliteracyaffectstheuserexperienceasawhole. Individualswithadeeperunderstanding
of AI are able to navigate its interface better with greater efficiency and efficacy, pose
specificinquiriestoAI,andinterprettherecommendationsprovidedbyAIwithgreater
accuracy,therebyleadingtoamoresatisfactoryexperience(Wangetal.2023).
Moreover,AIliteracycanmitigateusers’resistancetonewtechnologiesbyelucidating
thenatureofAIandrenderingitsprocessesmoretransparent(Markusetal.2024). Once
userscomprehendhowGenAIgeneratesfinancialadvice,theirskepticismmaydissipate,
reducingtheirresistancetoutilizingsuchsystemsandfosteringopennesstothem. The
discrepancyinthelevelsofknowledgeaboutAIamongdifferentusergroupsresultsin
aknowledgegap. Itisthereforeimperativetoprovideeducationonthefunctioningof
AIinordertobridgethisgapandfacilitatemoreeffectiveadoptionofAIamongdiverse
usergroups.
2.6. Service-DominantLogic(SDL)andArtificiallyIntelligentDeviceUseAcceptance(AIDUA)
Service-dominantlogic(SDL)hasemergedasakeyframeworkforunderstanding
valueco-creationacrossindustries,includingfinancialservices. InaccordancewithSDL,
valueisgeneratedthroughinteractionsbetweenprovidersandconsumers, ratherthan
beinginherentintheoutputitself(VargoandLusch2004;Vargoetal.2008). Inthecontext
ofGenAI,SDLoffersaperspectiveonhowGenAIcanfacilitatevalueco-creationprocesses.
SDL shifts the focus from traditional goods-dominant logic, which views value as
created by companies and distributed to consumers, to a service-centered perspective,
wherevalueisco-createdbymultipleparties,includingconsumers(Grönroos2008). This
shiftiscriticallyimportantforunderstandingtherelationalandinteractivenatureofthe
financialservicesprovidedbyGenAItechnology(Riikkinenetal.2018).
The operation of GenAI financial services depends on the interaction of multiple
stakeholders,includingfinancialinstitutions,technologycompanies,andconsumers. SDL
positsthattheefficacyoftheecosysteminjointlycreatingvalueispivotaltothesuccessof
theservice. Consequently,SDLrepresentsastrategicinstrumentforunderstandingand
enhancingthevalueco-creationprocessinGenAI-drivenfinancialservices.Theimportance
ofinteraction,personalization,andresourceintegrationinshapingtheuserexperienceand
theoverallserviceefficiencyisemphasized(Zhuetal.2024).
InadditiontoSDL,thedevelopmentofanewtheoreticalframeworkisnecessaryfor
understandingconsumeracceptanceandusagebehaviorwhenintegratingAIsystemsinto
consumerdevices. TheArtificialIntelligenceDeviceUseAcceptance(AIDUA)modelisa
comprehensiveframeworkthatrevealsthemultifacetednatureofconsumerinteractions
withAItechnologiessuchasGenAI.
TheAIDUAmodeldelineatesseveralstagesfortheacceptanceofAIdevices,including
primaryappraisal,secondaryappraisal,andtheoutcomestage(Gursoyetal.2019). Each

J.RiskFinancialManag.2024,17,470 6of25
ofthesestagesiscrucialintheevaluationofGenAIbyconsumers. Inlightofstudiesthat
haveappliedtheAIDUAmodel,itcanbepostulatedthatpersonalizedsuggestions,human-
like empathy, and continuous improvement serve as the primary drivers in measuring
consumers’assessmentofGenAI-poweredfinancialadvice. Inthesecondaryappraisal
stage,consumersprimarilyevaluatetheirdecisionoptionsandpotentialoutcomesbased
ontheirattitudes.WhendecidingwhethertoacceptorresistGenAI-drivenfinancialadvice,
they assess the costs and benefits of using AI devices in service delivery, considering
theirperceivedauthenticityofthesedevices. Followingthisintricateappraisalprocess,
consumers develop a utilitarian attitude towards GenAI-based financial advice, which
subsequentlydeterminestheirwillingnesstocommunicatewithGenAIortheirresistance
toutilizingGenAIforfinancialguidance.
EmpiricalstudieshavedemonstratedtheefficacyoftheAIDUAmodelinexplaining
andpredictingconsumerbehaviortowardAIdevices. Thesestudieshavealsovalidated
this model’s utility as a diagnostic and prescriptive tool for businesses (Ma and Huo
2023;Linetal.2020;Kellyetal.2023). Forpractitioners,theAIDUAmodelsuggeststhat
marketinganddesignstrategiesforAIdevicesshouldaddressconsumers’concernsabout
trust,perceivedrisk,andeaseofuseinordertoincreasetheiracceptance.
As artificial intelligence (AI) technology evolves and becomes more prevalent in
financialinstitutions,frameworkslikeAIDUAwillbecomeincreasinglyessentialforunder-
standingandpredictingconsumerinteractionswithAItools.Thiscomprehensiveapproach
allows for the design and implementation of AI technologies that align with consumer
expectationsandpromoteacceptance.
2.7. IntegratingSDLandAIDUAtoUnderstandConsumer–AIInteractions
Theseamlessintegrationofservice-dominantlogic(SDL)andtheAIDeviceUseAccep-
tance(AIDUA)modelprovidesacomprehensivetheoreticalfoundationforunderstanding
andexplainingconsumerinteractionswithgenerativeAI(GenAI)intheserviceindustry,
particularlywithinfinancialservices. BycombiningSDL’svalueco-creationperspective
with AIDUA’s focus on consumers’ appraisal stages of AI usage, we create a powerful
frameworkforinvestigatingthenuancesofconsumerinteractionswithGenAI.
SDLemphasizesvalueco-creationthroughinteractionandresourceintegrationbe-
tweenserviceprovidersandconsumers,aligningcloselywiththeAIDUAmodel,which
highlightsconsumeracceptanceandresistancetowardAItechnologies. Thetwoframe-
worksconvergeinthecontextofvalue-drivenusageofAI,whereconsumersarenotpassive
recipientsbutactiveparticipantsintheco-creationofvalue(Vargoetal.2008;Grönroos
2008). PreviousstudieshaveshownthatAItechnologies,wheneffectivelyintegratedinto
servicesystems,enhancetheconsumer’sroleinco-creatingpersonalizedvalue,resulting
inhigherengagementandsatisfaction(Riikkinenetal.2018).
This framework posits that when services are designed to facilitate an active role
of consumers in co-creating personalized value (a fundamental concept of SDL), their
experienceswithAI-drivensystems,likeGenAI,canbesignificantlyenhanced. AIDUA
complementsthisbyfocusingonthestagesofconsumers’interactionswithAI,frominitial
awarenesstofullacceptance, whichincludestheirevaluationofperceivedauthenticity,
personalization,andcontinuousimprovement—factorscentraltoAI–humancollaboration
(Bagetal.2022;Vesanen2007). Furthermore,evidencesuggeststhatconsumers’willing-
nesstoembraceAIinservicesettingsincreaseswhenAIsystemsexhibitcharacteristics
suchasempathyandanthropomorphism,whichcanfostermoreauthenticandengaging
interactions(Pelauetal.2021;Ameenetal.2021).
ThedecisiontointegrateSDLandAIDUAisalsosupportedbyrecentresearchinboth
theliteratureonservicesandAI.Forexample,studieshavehighlightedtheeffectivenessof
combiningconsumertechnologyadoptionframeworkswithservicelogictoexplainthe
adoptionofAI-drivenservices, particularlyinhigh-involvementcontextslikefinancial
services(Gursoyetal.2019;Vesanen2007). Byintegratingthesemodels,weofferamore

J.RiskFinancialManag.2024,17,470 7of25
holisticunderstandingofhowconsumersperceiveandengagewithAI-basedfinancial
advisoryservices.
3. HypothesisDevelopmentandtheResearchModel
3.1. PersonalizedInvestmentSuggestions,Human-likeEmpathy,andContinuousImprovement
Personalizationisincreasinglyacknowledgedasavitalcomponentofenhancinguser
experienceandfosteringauthenticityindigitalinteractions(Vesanen2007). Infinancial
advice,personalizedrecommendationsareparticularlyimpactful,astheydemonstratean
understandingoftheuser’sspecificneedsandpreferences(Mustoetal.2015). Thedelivery
ofpersonalizedfinancialadvicethroughGenAIcanenhancetheperceivedauthenticity
ofit,astheadviceappearsmorerelevantandtrustworthy. Consumerbehaviorstudies
indicatethatservicesareoftenperceivedasmoreauthenticwhentheyarecloselyaligned
withauser’suniquecircumstances(Napolietal.2014;Morhartetal.2015).
Moreover,empathy,especiallyintheformofhuman-likeemotionalintelligence,is
crucial to user interactions. When users feel that AI tools can understand and respond
totheiremotionalstates,theyaremorelikelytotrustandusethistechnology(Chiand
HoangVu2023). Thecapacityforhuman-likeempathyinGenAIenablesittocomprehend
consumers’financialconcernsandobjectivesatanemotionallevel, whichiscrucialfor
enhancing the perceived authenticity of its advice (Chuah and Yu 2021). Empathetic
interactionscanelevatefinancialadvicebeyondbeingpurelytransactional,therebycreating
asenseofcareandpersonalconnection.
Furthermore,theabilityofartificialintelligencesystemstocontinuouslylearnand
improveovertimeisessentialformaintainingtheirrelevanceandensuringthedeliveryof
high-qualityservices. TheongoingenhancementofGenAI’sfinancialcounselcouldresult
inmorepreciseandcontemporaryrecommendations,whichmightenhancethecredibility
ofitsadvice. Theprincipleofcontinuousimprovementalignswiththedynamicnatureof
financialmarketsandconsumerexpectations(HuangandRust2021).AsGenAIadaptsand
evolves,itsadvicemaybeperceivedasmoreauthentic,reflectingup-to-dateknowledge
andadeeperunderstandingofthefinanciallandscape. Basedontheseinsights,wepropose
thefollowinghypotheses:
H1: PersonalizedinvestmentsuggestionsbyGenAIarepositivelyassociatedwithitsauthenticity
asperceivedbyconsumers.
H2: Thehuman-likeempathyofGenAIispositivelyassociatedwithitsauthenticityasperceivedby
consumers.
H3: ContinuousimprovementofGenAIispositivelyassociatedwithitsauthenticityasperceived
byconsumers.
3.2. PerceivedAuthenticity
FollowingtheinitialevaluationofthespecificcharacteristicsofGenAItools,perceived
authenticityplaysacrucialroleinhowconsumersassessandadopttheseservices(Lietal.
2023). Whenconsumersperceiveaserviceasauthenticandadviceasgenuine,theyare
morelikelytofindthisserviceusefulandpractical. Thisbelieffostersautilitarianattitude
towardstheservice,asconsumersprioritizeitsfunctionalityandtheabilitytoeffectively
achievetheirgoals(AlimamyandAl-Imamy2022).
IntherealmofAI-drivenfinancialguidance,liketheservicesofferedbyGenAI,the
perceivedauthenticityoftheadviceisessentialinshapingusers’perceptionsofaservice’s
utility. Whenrecommendationsareperceivedastruthful,usersaremorelikelytoview
themasreliable,precise,andtailoredtotheirspecificrequirements. Consequently,this
enhancestheperceivedusefulnessofGenAI’sofferings. Theconceptofperceivedauthen-
ticityencompassestheeffectiveness,efficiency,andoverallusefulnessofthesuggestions
providedbyGenAI.TheperceivedauthenticityofGenAI’sfinancialadviceexertsadirect

J.RiskFinancialManag.2024,17,470 8of25
influenceonusers’utilitarianattitudestowardsaservice,which,inturn,determinesits
perceivedvalueandadoption(Kwonetal.2024). Basedontheinterrelationshipbetween
perceivedauthenticity,trust,andutility,thefollowinghypothesisisproposed:
H4: Consumers’ perceived authenticity is positively associated with their utilitarian attitude
towardsGenAI.
3.3. UtilitarianAttitudes
Utilitarianism in technology usage refers to the extent to which users perceive a
technology as efficient and effective in achieving their objectives (Zamil et al. 2023; Fu
2024). When consumers view a technology through a utilitarian lens, they evaluate its
valuebasedonitsabilitytohelpthemachievespecificgoalsandsimplifytheirdecision-
making. Essentially,thestrongerthebeliefinatechnology’sutilitarianvalue,thehigher
the likelihood of its acceptance and integration into users’ daily lives. This is because
usersrecognizeitspracticalbenefitsanditsabilitytostreamlinetasksanddecision-making
processes(H.Kimetal.2007).
InconsideringtheroleofGenAIinofferingfinancialguidance,autilitarianperspective
suggests that users value a platform’s capacity to deliver efficient, precise, and timely
information that can support their financial decision-making process. This mindset is
expectedtoenhanceconsumers’readinesstoengagewithGenAI,astheyanticipatethat
theinteractionwillassisttheminattainingtheirfinancialobjectives(DinhandPark2023).
Inotherwords,whenusersperceiveGenAIasatoolthatcaneffectivelystreamlinetheir
financial planning and provide valuable insights, they are more likely to embrace and
utilize the platform. This is driven by the belief that it will contribute to their overall
financialwell-beingandsuccess.
Inadditiontotheadoptionofnewtechnology,resistancetoitsuseisoftenshaped
by various factors, including a lack of practicality, increased complexity, or perceived
riskstopersonalinformation,establishedsocialnorms,andpersonalhabits(Hsieh2016;
Ghosh 2024). However, when consumers view a technology through a utilitarian lens,
theyrecognizeitspotentialtostreamlinetasksandboostproductivity. Thisperception
reducestheprobabilityofconsumerresistance,asthetechnologyalignswiththeirvalues
andobjectives,andtheadvantagesofitsuseoutweightheassociatedefforts,risks,and
costs. In essence, a utilitarian attitude towards technology fosters a sense of value and
purpose, making users more likely to embrace and incorporate it into their daily lives.
Theyrecognizethetechnology’spracticalbenefitsanditsabilitytoenhancetheiroverall
efficiencyandeffectiveness(AttiéandMeyer-Waarden2022).
In the context of GenAI, the identification of utilitarian advantages such as time
savings,cost-effectiveness,andenhancedfinancialresultswillresultinadecreaseinusers’
resistancetoutilizingtheseAI-drivenplatformsforfinancialguidance. Theperception
ofGenAIasabeneficialtoolthatalignswiththeirobjectiveswillmakeuserslesslikely
toopposeitsadoptionandintegration(Janetal.2023). Consequently,theywillbemore
inclined to accept this innovation, recognizing its potential to positively impact their
financial decision-making process and overall outcomes (Priya and Sharma 2023). In
other words, the more users perceive GenAI as a practical and advantageous tool for
managingtheirfinances, thelesslikelytheywillbetoresistitsadoptionanduse. Asa
result,therewillbeagreaterlikelihoodofadoptingthisAI-poweredtechnologyintheir
financialdecision-makingprocess. Basedonthisunderstanding,thefollowinghypotheses
areproposed:
H5: Consumers’utilitarianattitudestowardsGenAIarepositivelyassociatedwiththeirwillingness
tocommunicatewithGenAI.
H6: Consumers’utilitarianattitudestowardsGenAIarenegativelyassociatedwiththeirresistance
tocommunicatewithGenAI.

J.RiskFinancialManag.2024,17,470 9of25
3.4. AILiteracy
InadditiontotheinherentfeaturesofAI-drivenfinancialtools,thelevelsofAIliteracy
amongusersplayacriticalroleinthecommunicationprocess. AIliteracyencompasses
users’comprehensionofAItechnology,whichiscrucialforregulatingtheirinteractions
withAItools(Carolusetal.2023). AsAIliteracyincreases,usersarebetterequippedto
understandcomplexAIfunctions,suchaspersonalizedrecommendations. Inthecontext
of GenAI, higher AI literacy enables consumers to grasp how the platform tailors its
recommendationsbasedonuserdatabetter,which,inturn,enhancestheirperceptionsof
itsauthenticity. Consequently,AIliteracycanstrengthenthepositiverelationshipbetween
GenAI’spersonalizedadviceandperceivedauthenticity. Inotherwords,asusersbecome
moreknowledgeableaboutAItechnology,theyaremorelikelytoappreciateandtrustthe
personalizedfinancialguidanceprovidedbyGenAI,recognizingitsgenuinevalueand
relevancetotheirspecificneedsandcircumstances.
Moreover,thecontinuousimprovementofGenAIrepresentsanotheradvancedAI
feature. As users’ AI literacy increases, they are better positioned to comprehend and
appreciatethisaspectoftheplatform. TheyareawarethattheAIsystemwillconsistently
refineandenhanceitsrecommendationsbasedonongoinginteractions,therebyenhancing
theperceivedauthenticityoftheadviceprovided. Inthiscontext,AIliteracycanactas
amoderatingfactor, enhancingtherelationshipbetweencontinuousimprovementand
perceivedauthenticity. Specifically, moreknowledgeableusersaremorelikelytoplace
highervalueontheevolutionofAIindeliveringprecisefinancialguidance(Tirado-Morueta
etal.2018). Inessence,asconsumersbecomemorewellversedinAItechnology,theyare
morepredisposedtoacknowledgeandtrusttheongoingadvancementsinGenAI’sfinancial
advice. Theyrecognizethegenuinebenefitsofitsadaptivenatureinprovidingtailored
andrelevantrecommendationsthatalignwiththeirevolvingneedsandcircumstances.
Finally, the human-like empathy exhibited by GenAI is the result of sophisticated
programmingthatenablesempatheticinteractions. IndividualswithahigherlevelofAI
literacyarebetterequippedtounderstandandvaluetheseempatheticresponses,resulting
in an increased perception of its authenticity. Conversely, individuals with limited AI
literacymayencounterdifficultyincomprehendingthenuancesofempatheticAI,leading
toadiminishedperceptionofitsauthenticity. Asaresult,thedevelopmentofAIliteracy
is expected to strengthen the correlation between human-like empathy and perceived
authenticity. AsusersgainadeeperunderstandingofAItechnology,theyaremorelikely
torecognizeandvaluethegenuinenatureofGenAI’sempatheticinteractions(Baabdullah
et al. 2022; Sperling et al. 2024), thereby increasing their confidence in these platforms’
financialadvice. Basedontheseinsights,weproposethefollowinghypotheses:
H7: Consumers’AIliteracypositivelymoderatestherelationshipbetweenGenAI’spersonalized
investmentsuggestionsanditsauthenticityasperceivedbycustomers.
H8: Consumers’AIliteracypositivelymoderatestherelationshipbetweenGenAI’scontinuous
improvementanditsauthenticityasperceivedbycustomers.
H9: Consumers’AIliteracypositivelymoderatestherelationshipbetweenGenAI’shuman-like
empathyanditsauthenticityasperceivedbycustomers.
Inessence,asusersbecomemoreknowledgeableaboutAItechnology,theimpactofits
personalizedinvestmentsuggestions,human-likeempathy,andcontinuousimprovement
on their perceptions of the authenticity of GenAI’s financial advice will be amplified,
ultimatelyleadingtoahigherleveloftrustandacceptanceamongconsumers. Theresearch
modelbasedontheresearchhypothesessofarisshowninFigure1.

J. Risk Financial Manag. 2024, 17, x FOR PEER REVIEW 10 of 25
H9: Consumers’ AI literacy positively moderates the relationship between GenAI’s human-like em-
pathy and its authenticity as perceived by customers.
In essence, as users become more knowledgeable about AI technology, the impact of
its personalized investment suggestions, human-like empathy, and continuous improve-
ment on their perceptions of the authenticity of GenAI’s financial advice will be amplified,
J.RiskFinancialManag.2024,17,470 ultimately leading to a higher level of trust and acceptance among consumers. Th1e0 orfe2-5
search model based on the research hypotheses so far is shown in Figure 1.
FFigiguurree 11. .RReesseeaarrcchh mmooddeel.l .
4. ResearchMethodology
4. Research Methodology
4.1. MeasurementDevelopment
4.1. Measurement Development
Wecommencedourinvestigationbydevelopingacomprehensivequestionnairede-
We commenced our investigation by developing a comprehensive questionnaire de-
signedtocapturetherelevantdatanecessaryforouranalysis. Inlightofthesignificanceof
signed to capture the relevant data necessary for our analysis. In light of the significance
expertinput,wesolicitedevaluationsfromesteemedprofessorsintheFinance,Information
of expert input, we solicited evaluations from esteemed professors in the Finance, Infor-
Technology,andManagementSciencedepartments. Theirinvaluablefeedbackprompted
mation Technology, and Management Science departments. Their invaluable feedback
revisionstothequestionnaire,allowingustorefineandclarifyourquestionsforgreater
prompted revisions to the questionnaire, allowing us to refine and clarify our questions
precisionandrelevance.
for grAeatreigr oprroeucissimonet ahnodd orelolegvyawncaes. employedtoensurethatthequestionnaireaccurately
asseAss erdigeoirgohutsk meyetdhiomdeonlsoigoyn sw. aTsh eesmepinlocyluedde tdo tehneseuxrtee tnhtatto twheh iqcuhetshtieoinnnvaeisrtem aecncutaradtveilcye
awssaesspseedrs eoingahlti zkeedy, GdiemnAenI’ssiocnasp.a Tcihteysfeo irnccoluntdinedu otuhes iemxtpernotv teom wehnitc,hit sthaeb iilnitvyetsotmdeenmto andsvtriacete
whausm paenr-sloiknealeizmedp,a tGheyn,AthIe’s acuatphaecnittyic iftoyr ocfointtsinreusopuosn ismespraosvpeemrceenitv, eidts baybicliotyn stuom deerms,otnh-e
sutrtailtieta hriuamnaantt-iltiukde eeomfpcaotnhsyu,m theers atuotwheanrdtisciGtye noAf Iit,sc orensspuomnesress’ awsi lplienrgcenievsesda nbdy rceosnisstuamnceerst,o
tehneg uagtielitwaritihanG aettnAituIdfoer ofifn acnoncisaulmgueirds atnocwe,aardnds tGheenirAoIv, ecroanllsAumIleitresr’a wcyi.llingness and re-
sistanTceh etoi nentrgoadguec wtoirtyh GseecntiAonI foorf fithneanqcuiaels tgiounidnaanircee,c alenadr ltyheoiru otlvineeradllt AheI lpituerrpacoys.e of the
studTy,heen isnutrriondgupcatorrtiyc ipseacntitos’nc oonf fithdee nqtiuaelisttyioannndaiarne ocnleyamrliyty .oAutdlidnietido nthalel yp,suurrpvoesye ionfs ttrhuec -
sttiuodnys, wenesruerpinrgo vpiadretidc.ipTahnets’i ncoitniafildpeanrttiaolfityth aenqdu aensotinoynmnaitiyre. Aindcdliutidoendalqlyu,e ssutirovnesy ionnstbruasci-c
tdioenms owgerraep phircovinidfoerdm. aTthioen i,nsituiachl paasrat goef, tgheen qdueer,sitniocnonmaeirlee vinecl,luadnedde qduuecsattiioonns, toone bstaasbicli sdhe-a
mfoougnradpahtiiocn ianlfuornmdeartsiotann, dsuincgh oafst ahgeer,e gspenodnedre,n itnsc’obmacek lgervoeul,n adnsd. T ehdeusceactoionnd, ptoa retsctaobnlsisisht ead
foofuintedmatsiocnaarel fuunlldyedrsetsaingdniendgt oofa tshsee srsesthpeonedigehnttsc’o bnasctrkugcrtosuunnddse. rTihnev essetciognadti opna.rt consisted
of itemThs ecamreefauslulyre dmeesnigtniteedm tso faosrspesesr stohnea eliizgehdt cinovnesstrtmucetns tusnudgegre isntivoensstiagsasteiossne.d therespon-
dentTsh’pe emrceeapstuiornemsoefnGt eitneAmIs’ sfaobr ilpiteyrstooncaolimzepdre ihnevnedsttmheeinrt insudgivgiedsutiaolnfisn aasnsceisaslende etdhes arne-d
sdpeolnivdeernctus’s tpoemrcizepedtiorencso omf mGeenndAaIt’iso anbs.ilTithye toev caolmuaptiroenheonfdco tnhteiinru ionudsivimidpuraol vfienmaennctiaals nseesesdesd
therespondents’viewsonGenAI’sabilitytolearnfrominteractionsandimproveitssug-
gestions over time (Q. Chen et al. 2022). Human-like empathy was measured through
items(Pelauetal.2021;Fuetal.2023;Seitz2024)thatgaugedtheextenttowhichGenAI
understoodandconsideredtherespondents’emotionalandfinancialconcerns. Theper-
ceivedauthenticityofGenAI’sfinancialadvicewasexaminedbyaskingtherespondents
toratethegenuinenessandreliabilityofitsadvice(Voetal.2024;Mengetal.2023). The
usefulness, efficiency, and practicality of GenAI’s recommendations were evaluated to
assesstherespondents’utilitarianattitudes(PriyaandSharma2023). Therespondents’

J.RiskFinancialManag.2024,17,470
11of25
willingnesstocommunicatewithGenAIwasgaugedthroughitems(MaandHuo2023;
KimandHur2023)thatdeterminedthelikelihoodoffutureengagementwiththeAIfor
financialadvice. ResistancetocommunicatewithGenAIwasevaluatedbyassessingthe
respondents’hesitationinusingorreluctancetouseGenAIforfinancialguidance(Maand
Huo2023;Yangetal.2023). Finally,anAIliteracyscalewasusedtoassesstherespondents’
knowledgeandunderstandingofAItechnologies,particularlytheirapplicationtofinancial
advice (Almatrafi et al. 2024; Kong et al. 2024). Detailed breakdowns can be found in
AppendixA.
4.2. DataCollection
Thisstudyusedacomprehensiveapproachtodatacollectiontogatherinsightsfrom
mobilebankingserviceuserswhohadengagedwithGenAIforfinancialguidance. The
surveywasdesignedtogatherdetailedinformationontheparticipants’interactionswith
GenAI,theirevaluationsofAI’sauthenticity,theirAIliteracy,andtheirattitudestowards
usingAIforfinancialadvice.
Thisstudytargetedadultmobilebankingusersaged18andabovewhohadinteracted
withGenAIfinancialadvicefeatures. Purposivesamplingwasemployedtoselectrespon-
dentswhometthiscriterion,ensuringthatthesamplewasrelevantforunderstandingthe
targetusergroup. Intotal,1200participantswereinitiallyinvitedtotakepartinthesurvey,
ofwhich950respondentscompletedit. Afterdatacleaningandqualitycontrolchecks,a
finalsampleof822respondentswasretainedforanalysis.Theseparticipantswerebalanced
acrossgender,age,andincomelevels,ensuringarepresentativecross-sectionofthemobile
bankingpopulation. Table1presentstheirdemographiccharacteristics,showingthatthe
participantsincludedindividualsaged18toover65yearsold,with7participantsbeing
over65,reflectingtheinclusivityofolderusersinmobilebankingservices.
Table1.Demographiccharacteristics.
|     | Demographics |      | Frequency | Percentage(%) |
| --- | ------------ | ---- | --------- | ------------- |
|     |              | Male | 412       | 50.1          |
Gender
|     |     | Female | 410 | 49.9 |
| --- | --- | ------ | --- | ---- |
|     |     | 18–24  | 139 | 16.9 |
|     |     | 25–34  | 322 | 39.2 |
|     |     | 35–44  | 233 | 28.3 |
Age
|            |     | 45–54               | 86  | 10.5 |
| ---------- | --- | ------------------- | --- | ---- |
|            |     | 55–64               | 35  | 4.3  |
|            |     | Above65             | 7   | 0.9  |
|            |     | Highschoolorbelow   | 164 | 20   |
| Education  |     | Threeyearsofcollege | 252 | 30.7 |
| Background |     | Bachelor’s          | 363 | 44.2 |
|            |     | Master’sorabove     | 43  | 5.2  |
|            |     | 3000CNYorbelow      | 141 | 17.2 |
|            |     | 3001–5000CNY        | 423 | 51.5 |
Monthly
|     |     | 5001–7000CNY | 140 | 17  |
| --- | --- | ------------ | --- | --- |
income
|             |                      | 7001–9000CNY       | 61  | 7.4  |
| ----------- | -------------------- | ------------------ | --- | ---- |
|             |                      | 9000CNYandabove    | 57  | 6.9  |
|             |                      | Severaltimesperday | 29  | 3.5  |
|             |                      | Onceaday           | 78  | 9.5  |
| Frequencyof | Severaltimesperweek  |                    | 106 | 12.9 |
| usingGenAI  |                      | Onceaweek          | 364 | 44.3 |
|             | Severaltimespermonth |                    | 208 | 25.3 |
|             |                      | Onceamonth         | 37  | 4.5  |
The data collection took place over a three-month period, from January to March
2024, and was facilitated by collaboration with a professional survey firm. The survey
wasdistributedusingmultipleplatforms: (1)emailcampaignstargetingmobilebanking

J.RiskFinancialManag.2024,17,470
12of25
users from partner banks, (2) in-app notifications within mobile banking applications
encouragingparticipation,and(3)financialforumsandsocialmediaplatforms,onwhich
thesurveylinkwasshared.
Beforelaunchingtheformalsurvey,apilottestwasconductedwithasubsetof50par-
ticipantstoidentifyandaddressanypotentialissueswithitsclarity,thecomprehensibility
ofthequestions,andtheoverallstructureofthequestionnaire. Thepilotsurveyhelpedre-
finevariablessuchasAIliteracy,perceivedauthenticity,andhuman-likeempathyfollowing
| therecommendationsofRef. | (VanTeijlingenandHundley2002). |     |     |     |
| ------------------------ | ------------------------------ | --- | --- | --- |
Strictfilteringtechniqueswereusedduringthesurveycollectionprocesstomaintain
the data quality, ensuring that only responses from eligible participants were included.
Anonymityandconfidentialitywerestrictlymaintainedincompliancewithethicalresearch
standards. Table1providesasummaryoftherespondents’demographiccharacteristics.
5. DataAnalysisandResults
5.1. TheMeasurementModel
Ref. (PodsakoffandOrgan1986)suggestedthatsingle-sourcedatamaybeproneto
common method variance (CMV). To determine the presence of common method bias
(CMB)inourcollecteddata,weconductedHarman’ssingle-factortest. Thistestinvolves
loadingallthemeasurementitemsintoaprincipalcomponentanalysiswithoutrotation. It
iswidelyacceptedthatCMBisaconcernifasinglefactoraccountsformorethan50%of
thetotalvariance. Inthisstudy,thefirstfactoraccountedfor31.95%ofthevariance,which
isbelowthe50%threshold. Therefore,wecanconcludethatthedatainthisstudywerenot
affectedbycommonmethodbias.
Themeasurementmodelwasassessedbyexaminingthefactorloadingvalues,com-
positereliability(CR),andaveragevarianceextracted(AVE).AsshowninTable2,allthe
factor loadings exceed the recommended threshold of 0.6. Additionally, Cronbach’s α,
which measures internal consistency reliability, ranged from 0.845 to 0.949, surpassing
thesuggestedthresholdof0.7(Hairetal.2014). Theseresultsprovidestrongevidence
supportingthescale’sreliability.
Table2.Reliability,CR,andAVE.
Cronbach’s
| Constructs | Items | ItemLoadings |     | CR AVE |
| ---------- | ----- | ------------ | --- | ------ |
Alpha
|                        | PIS1  | 0.924 |       |             |
| ---------------------- | ----- | ----- | ----- | ----------- |
|                        | PIS2  | 0.778 |       |             |
|                        | PIS3  | 0.769 |       |             |
| PersonalizedInvestment | PIS4  | 0.741 |       |             |
|                        |       |       | 0.926 | 0.928 0.619 |
| Suggestions            | PIS5  | 0.747 |       |             |
|                        | PIS6  | 0.744 |       |             |
|                        | PIS7  | 0.783 |       |             |
|                        | PIS8  | 0.791 |       |             |
|                        | HLE1  | 0.898 |       |             |
|                        | HLE2  | 0.793 |       |             |
|                        | HLE3  | 0.778 |       |             |
|                        | HLE4  | 0.780 |       |             |
|                        | HLE5  | 0.754 |       |             |
| Human-LikeEmpathy      | HLE6  | 0.788 | 0.949 | 0.95 0.635  |
|                        | HLE7  | 0.768 |       |             |
|                        | HLE8  | 0.768 |       |             |
|                        | HLE9  | 0.798 |       |             |
|                        | HLE10 | 0.814 |       |             |
|                        | HLE11 | 0.814 |       |             |

J.RiskFinancialManag.2024,17,470
13of25
Table2.Cont.
Cronbach’s
|     |     |     | Constructs | Items | ItemLoadings |     |     | CR AVE |
| --- | --- | --- | ---------- | ----- | ------------ | --- | --- | ------ |
Alpha
|     |     |                       |     | CI1 | 0.870 |     |       |             |
| --- | --- | --------------------- | --- | --- | ----- | --- | ----- | ----------- |
|     |     |                       |     | CI2 | 0.778 |     |       |             |
|     |     |                       |     | CI3 | 0.718 |     |       |             |
|     |     | ContinuousImprovement |     | CI4 | 0.750 |     | 0.915 | 0.917 0.613 |
|     |     |                       |     | CI5 | 0.788 |     |       |             |
|     |     |                       |     | CI6 | 0.771 |     |       |             |
|     |     |                       |     | CI7 | 0.796 |     |       |             |
|     |     |                       |     | PA1 | 0.886 |     |       |             |
Perceived
|     |     |     |     | PA2 | 0.764 |     | 0.845 | 0.853 0.660 |
| --- | --- | --- | --- | --- | ----- | --- | ----- | ----------- |
Authenticity
|     |     |                      |                      | PA3  | 0.781 |     |       |             |
| --- | --- | -------------------- | -------------------- | ---- | ----- | --- | ----- | ----------- |
|     |     |                      |                      | UA1  | 0.887 |     |       |             |
|     |     |                      |                      | UA2  | 0.733 |     |       |             |
|     |     |                      | UtilitarianAttitudes | UA3  | 0.685 |     | 0.865 | 0.876 0.587 |
|     |     |                      |                      | UA4  | 0.740 |     |       |             |
|     |     |                      |                      | UA5  | 0.771 |     |       |             |
|     |     |                      |                      | WCG1 | 0.888 |     |       |             |
|     |     |                      |                      | WCG2 | 0.721 |     |       |             |
|     |     |                      | Willingnessto        | WCG3 | 0.738 |     |       |             |
|     |     |                      |                      |      |       |     | 0.894 | 0.898 0.596 |
|     |     | CommunicatewithGenAI |                      | WCG4 | 0.726 |     |       |             |
|     |     |                      |                      | WCG5 | 0.765 |     |       |             |
|     |     |                      |                      | WCG6 | 0.78  |     |       |             |
|     |     |                      |                      | RCG1 | 0.863 |     |       |             |
|     |     |                      |                      | RCG2 | 0.80  |     |       |             |
Resistanceto
|     |     |                   |     | RCG3 | 0.672 |     |       |             |
| --- | --- | ----------------- | --- | ---- | ----- | --- | ----- | ----------- |
|     |     | Communicatingwith |     |      |       |     | 0.885 | 0.887 0.570 |
|     |     |                   |     | RCG4 | 0.686 |     |       |             |
GenAI
|     |     |     |            | RCG5 | 0.762 |     |       |             |
| --- | --- | --- | ---------- | ---- | ----- | --- | ----- | ----------- |
|     |     |     |            | RCG6 | 0.728 |     |       |             |
|     |     |     |            | AIL1 | 0.768 |     |       |             |
|     |     |     |            | AIL2 | 0.757 |     |       |             |
|     |     |     |            | AIL3 | 0.844 |     |       |             |
|     |     |     | AILiteracy |      |       |     | 0.910 | 0.910 0.629 |
|     |     |     |            | AIL4 | 0.818 |     |       |             |
|     |     |     |            | AIL5 | 0.760 |     |       |             |
|     |     |     |            | AIL6 | 0.808 |     |       |             |
Compositereliability(CR)wasusedtoevaluatetheinternalconsistencyofthescale,
with higher values indicating greater reliability. Ref. (Raza et al. 2021) states that CR
valuesbetween0.6and0.7areacceptable,whilevaluesbetween0.7and0.9areconsidered
satisfactorytogood. AsshowninTable3,alltheCRvaluesexceeded0.8,confirmingthe
scale’ssatisfactorycompositereliability.
Table3.Discriminantvalidity.
|     | PIS     | HLE     | CI      | PA      | UA      | WCG     | RCG   | AIL |
| --- | ------- | ------- | ------- | ------- | ------- | ------- | ----- | --- |
| PIS | 0.787   |         |         |         |         |         |       |     |
| HLE | 0.442** | 0.797   |         |         |         |         |       |     |
| CI  | 0.423** | 0.446** | 0.783   |         |         |         |       |     |
| AIL | 0.150** | 0.160** | 0.174** | 0.793   |         |         |       |     |
| PA  | 0.541** | 0.551** | 0.500** | 0.317** | 0.812   |         |       |     |
| UA  | 0.451** | 0.493** | 0.480** | 0.195** | 0.614** | 0.766   |       |     |
| WCG | 0.348** | 0.332** | 0.324** | 0.143** | 0.413** | 0.669** | 0.772 |     |
−0.315** −0.336** −0.371** −0.198** −0.473** −0.677** −0.435**
| RCG |     |     |     |     |     |     |     | 0.755 |
| --- | --- | --- | --- | --- | --- | --- | --- | ----- |
Note:**,p<0.01.ValuesinboldrepresentthesquarerootoftheAVE.

J.RiskFinancialManag.2024,17,470 14of25
Additionally,theaveragevarianceextracted(AVE)valuesforallvariablesexceeded
0.5,meetingthecriteriaforconvergentvalidity(FornellandLarcker1981). Theseresults
collectively indicate that the measurement model demonstrates strong reliability and
convergentvalidity.
Toassessdiscriminantvalidity,weusedthemethodfromRef. (FornellandLarcker
1981),whichrequiresthesquarerootoftheAVEtobegreaterthanthecorrelationsamong
theconstructs. Table3showsthesquarerootoftheAVEvaluesalongthediagonal(inbold)
andthecorrelationsamongtheconstructsintheoff-diagonalcells. Theseresultsreveal
thatthesquarerootoftheAVEforeachconstructwashigherthanthecorrespondingoff-
diagonalcorrelationvalues. Thisindicatesthatthemeasurementmodelhasasatisfactory
discriminantvalidity,aseachconstructismorestronglyrelatedtoitsownmeasuresthan
tothoseoftheotherconstructs.
Beforeconductingthestructuralequationmodeling(SEM)analysis,aconfirmatory
factoranalysis(CFA)wasperformedtoevaluatethemeasurementmodel. Themodel’s
goodnessoffitwasassessedusingvariousindicesandtheircorrespondingthresholds,as
recommendedbyRef. (HuandBentler1999).
TheCFAresultsindicatedthatthemeasurementmodelfitthedatawell. Specifically,
thechi-square-to-degrees-of-freedomratio(χ2/df)was1.173,whichiswithintheacceptable
range. TheGoodnessofFitIndex(GFI)andtheAdjustedGoodnessofFitIndex(AGFI)
valueswere0.938and0.932,respectively,withbothexceedingtherecommendedthresholds.
Additionally,theComparativeFitIndex(CFI)andtheNormedFitIndex(NFI)valueswere
0.992and0.95,respectively,indicatingastrongfit. TheIncrementalFitIndex(IFI)valueof
0.992alsometthecriteria. Finally,theStandardizedRootMeanSquareResidual(SRMR)
andtheRootMeanSquareErrorofApproximation(RMSEA)valueswere0.026and0.015,
respectively,withbothfallingbelowtherecommendedthresholds,furthersupportingthe
model’sacceptablefit.
As shown in Table 4, all the fitting indices of the measurement model met the rec-
ommendedcriteria,confirmingthatthemodeladequatelyrepresentedthedataandwas
suitableforthesubsequentSEManalysis.
Table4.Measurementmodelfit.
FitIndices χ2/df GFI AGFI NFI CFI IFI SRMR RMSEA
RecommendedCriteria <3 >0.9 >0.8 >0.9 >0.9 >0.9 <0.08 <0.08
Scores 1.173 0.938 0.932 0.95 0.992 0.992 0.026 0.015
5.2. TheStructuralModel
Thestructuralmodelwasevaluatedtoexaminetherelationshipsbetweenthecon-
structsproposedintheresearchmodel. Theanalysisrevealedthatallpathswerepositive
andsignificantatthe0.05level. Table5presentsthestandardizedpathcoefficientsbetween
theconstructs,thesignificancelevels,andtheexplanatorypower(R2)foreachconstruct.
Accordingtotheruleofthumb,R2valuesof25%,50%,and75%indicateweak,average,
andsubstantialexplanatorypower,respectively.
Inthisstudy,theR2valuesforperceivedauthenticity,utilitarianattitudes,willingness
tocommunicatewithGenAI,andresistancetocommunicatingwithGenAIwere56.9%,
50.5%,50.3%,and54.6%,respectively,indicatingasatisfactorylevelofexplanation.
TheresultsinTable5showapositiveassociationbetweenpersonalizedinvestment
suggestionsandperceivedauthenticity(β=0.318, p<0.001), supportingHypothesis1.
Similarly,therewasapositiveassociationbetweenhuman-likeempathyandperceived
authenticity (β = 0.338, p < 0.001), confirming Hypothesis 2. Additionally, continuous
improvementpositivelyinfluencesperceivedauthenticity(β=0.287,p<0.001),supporting
Hypothesis3. Together,personalizedinvestmentsuggestions,human-likeempathy,and
continuousimprovementaccountfor56.9%ofthevarianceinperceivedauthenticity.

J.RiskFinancialManag.2024,17,470
15of25
Table5.Hypothesistestresults.
|     | Hypothesis |     |     | Path |     | β   |     | p-Value |     | R2  | Remarks |
| --- | ---------- | --- | --- | ---- | --- | --- | --- | ------- | --- | --- | ------- |
→
|                  | H1  | PIS     |     |      | PA  | 0.318  |     | *** |         |       | Supported |
| ---------------- | --- | ------- | --- | ---- | --- | ------ | --- | --- | ------- | ----- | --------- |
|                  | H2  | HLE     |     | →    | PA  | 0.338  |     | *** |         | 0.569 | Supported |
|                  | H3  | CI      |     | →    | PA  | 0.287  |     | *** |         |       | Supported |
|                  | H4  | PA      |     | →    | UA  | 0.71   |     | *** |         | 0.505 | Supported |
|                  | H5  | UA      |     | →    | WCG | 0.709  |     | *** |         | 0.503 | Supported |
|                  |     |         |     | →    |     | −0.739 |     |     |         |       |           |
|                  | H6  | UA      |     |      | RCG |        |     | *** |         | 0.546 | Supported |
| ModeratingEffect |     |         |     | Path |     | β      |     |     | p-Value |       | Remarks   |
|                  | H7  | PIS×AIL |     | →    | PA  | 0.101  |     |     | ***     |       | Supported |
|                  | H8  | HLE×AIL |     | →    | PA  | 0.097  |     |     | ***     |       | Supported |
|                  | H9  | CI×AIL  |     | →    | PA  | 0.108  |     |     | ***     |       | Supported |
Note:***,p<0.001.
Furthermore,perceivedauthenticitypositivelyimpactsutilitarianattitudes(β=0.71,
p<0.001),accountingfor50.5%oftheirvariance,therebysupportingHypothesis4. Inturn,
utilitarianattitudespositivelyinfluencewillingnesstocommunicatewithGenAI(β=0.709,
p<0.001),supportingHypothesis5,andnegativelyaffectresistancetocommunicating
withGenAI(β=−0.739,p<0.001),supportingHypothesis6. Utilitarianattitudesexplain
50.3%ofthevarianceinwillingnesstocommunicatewithGenAIand54.6%ofthevariance
inresistancetocommunicatingwithGenAI.
Afterverifyingthehypotheses,astructuralmodeltestwasconducted. Theresults
indicatedthatthemodeldemonstratedanacceptablefittothedataaccordingtothecriteria
recommendedbyRef. (HuandBentler1999). Thechi-square-to-degrees-of-freedomratio
(χ2/df)was1.225,whichiswithintheacceptablerange.
TheGoodnessofFitIndex(GFI)
andtheAdjustedGoodnessofFitIndex(AGFI)valueswere0.941and0.935,respectively,
withbothexceedingtherecommendedthresholds. Additionally,theComparativeFitIndex
(CFI),NormedFitIndex(NFI),andIncrementalFitIndex(IFI)valueswere0.990,0.953,and
0.990,respectively,indicatingastrongfitbetweenthemodelandthedata.TheStandardized
RootMeanSquaredResidual(SRMR)valueof0.038andtheRootMeanSquareErrorof
Approximation(RMSEA)valueof0.018werebothbelowtherecommendedcutoffpoints,
furthersupportingthemodel’sacceptablefit. Thesefitindices, aspresentedinTable6,
collectively indicate that the structural model adequately represents the relationships
amongtheconstructsandprovideasatisfactoryexplanationofthedata.
Table6.Structuralmodelfit.
χ2/df
|                     | FitIndices |     |       | GFI   | AGFI  | NFI  | CFI   |     | IFI   | SRMR  | RMSEA |
| ------------------- | ---------- | --- | ----- | ----- | ----- | ---- | ----- | --- | ----- | ----- | ----- |
| RecommendedCriteria |            |     | <3    | >0.9  | >0.8  | >0.9 | >0.9  |     | >0.9  | <0.08 | <0.08 |
|                     | Scores     |     | 1.173 | 0.938 | 0.932 | 0.95 | 0.992 |     | 0.992 | 0.026 | 0.015 |
Inadditiontotheprimaryhypotheses,thisstudyproposedthatAIliteracymoderates
therelationshipsbetweenGenAI’scharacteristics(personalizedinvestmentsuggestions,
human-likeempathy,andcontinuousimprovement)andperceivedauthenticity.Theresults
presentedinTable5demonstratethatasAIliteracyincreasesordecreases,thepositive
associationsbetweenGenAI’scharacteristicsanditsauthenticityasperceivedbyconsumers
remainconsistent.
TheinteractiontermbetweenpersonalizedinvestmentsuggestionsandAIliteracyis
positivelyassociatedwithperceivedauthenticity(β=0.101,p<0.001),indicatingthatthe
relationshipbetweenpersonalizedinvestmentsuggestionsandperceivedauthenticityis
strengthenedbyhigherlevelsofAIliteracy. Similarly,theinteractiontermbetweenhuman-
likeempathyandAIliteracyispositivelyassociatedwithperceivedauthenticity(β=0.097,
p<0.001),suggestingthattherelationshipbetweenhuman-likeempathyandperceived

J. Risk Financial Manag. 2024, 17, x FOR PEER REVIEW 16 of 25
Table 6. Structural model fit.
Fit Indices χ2/df GFI AGFI NFI CFI IFI SRMR RMSEA
Recommended Criteria <3 >0.9 >0.8 >0.9 >0.9 >0.9 <0.08 <0.08
Scores 1.173 0.938 0.932 0.95 0.992 0.992 0.026 0.015
In addition to the primary hypotheses, this study proposed that AI literacy moderates
the relationships between GenAI’s characteristics (personalized investment suggestions,
human-like empathy, and continuous improvement) and perceived authenticity. The re-
sults presented in Table 5 demonstrate that as AI literacy increases or decreases, the posi-
tive associations between GenAI’s characteristics and its authenticity as perceived by con-
sumers remain consistent.
The interaction term between personalized investment suggestions and AI literacy is
positively associated with perceived authenticity (β = 0.101, p < 0.001), indicating that the
relationship between personalized investment suggestions and perceived authenticity is
J.RiskFinancialManag.2024,17,470strengthened by higher levels of AI literacy. Similarly, the interaction term betwee1n6 hofu2-5
man-like empathy and AI literacy is positively associated with perceived authenticity (β
= 0.097, p < 0.001), suggesting that the relationship between human-like empathy and per-
caeuivtheden atuictihteynitsiceitnyh ias necnehdanbcyedh bigyh heirghleevre llesveolfs AofI AliIt leirtaercayc.y.F Fininaalllyly,,t thhee iinntteerraaccttiioonn tteerrmm
bbeettwweeeenn ccoonnttiinnuuoouuss iimmpprroovveemmeenntt aanndd AAII lliitteerraaccyy iiss ppoossiittiivveelyly aassssoocciiaatteedd wwiitthh ppeerrcceeiivveedd
aauutthheenntticicitiyty (β(β = =0.100.180, 8p, <p 0<.000.10)0, 1in),diincdatiicnagti nthgatt hthate trheelartieolantsihoinps hbeiptwbeeetnw ceoennticnounotiunsu iomu-s
pimropvreomveenmt eanntda npderpceeirvceediv aeudtahuenthteicnittyic iitsy reisinrefoinrcfoedrc ebdy bhyighhiegrh leervleelvs eolfs AofI AlitIelriatecrya. cy.
Figure2presentsavisualrepresentationofthestandardizedpathcoefficientsandthe
Figure 2 presents a visual representation of the standardized path coefficients and
significancelevelsforeachhypothesis,includingthemoderatingeffectsofAIliteracyon
the significance levels for each hypothesis, including the moderating effects of AI literacy
therelationshipsbetweenGenAI’scharacteristicsandperceivedauthenticity.
on the relationships between GenAI’s characteristics and perceived authenticity.
FFiigguurree 22. .PPaathth ccooeeffifficcieienntsts oof fththee rreesseeaarrcchh mmooddeell. .NNoottee: :******, ,pp << 00.0.00011. .
6. Conclusions
6. Conclusions
The objective of this study was to explore the dynamics of consumer responses to
The objective of this study was to explore the dynamics of consumer responses to
GenAI-poweredfinancialadvice,addressingacriticalgapintheliteratureontheadoption
GenAI-powered financial advice, addressing a critical gap in the literature on the adoption
ofGenAItechnologiesinfinancialservices. Througharigorousempiricalanalysis,itwas
of GenAI technologies in financial services. Through a rigorous empirical analysis, it was
shownthatpersonalizedinvestmentsuggestions,human-likeempathy,andthecontinuous
shown that personalized investment suggestions, human-like empathy, and the
improvementofGenAIsignificantlyenhanceconsumers’perceptionsofitsauthenticity.
Theseperceptions,inturn,fosterautilitarianattitudetowardsusingGenAIforfinancial
advice,influencingconsumers’willingnesstoengagewithandresistancetocommunication
withGenAI.Notably,thisstudyhighlightstheroleofAIliteracyinamplifyingthepositive
effectsofGenAI’sfeaturesonperceivedauthenticity.
OurfindingsdelineateaclearpathwaythroughwhichGenAI’sfeaturesinfluencecon-
sumerbehaviors. Theprovisionofpersonalizedinvestmentadvice,thedemonstrationof
human-likeempathy,andcommitmenttocontinuousimprovementenhancetheperceived
authenticityofGenAI’sfinancialcounsel. TheseinsightsalignwithRefs. (Pelauetal.2021;
J.Kimetal.2022),whichemphasizedtheimportanceofperceivedhuman-likenessinuser
interactionswithAIsystems. Additionally,theworkofRefs. (Q.Chenetal.2022;Pitardi
2023)highlightedtheroleofpersonalizationandcontinuousimprovementinenhancing
consumertrustinAIservices.
Wealsofoundthatperceivedauthenticityiscrucialtodevelopingautilitarianattitude
towards GenAI, which, in turn, increases willingness to interact with AI and reduces
resistance. Thesefindingsextendpreviousresearchontheimportanceofauthenticdesign
ofGenAIplatforms(LeeandKim2024;PandeyandRai2024).

J.RiskFinancialManag.2024,17,470 17of25
Furthermore,thesignificantmoderatinginfluenceofAIliteracyunderscorestheim-
portanceofconsumers’understandingandfamiliaritywithAItechnologiesinenhancing
the effectiveness of GenAI’s features. These findings support past studies on AI liter-
acy (Ng et al. 2021; Kong et al. 2024) and demonstrate its value in the field of financial
advisoryservices.
6.1. AcademicImplications
ThisresearchsignificantlyenhancesourunderstandingofhowgenerativeAI(GenAI)
influencesconsumerbehaviorintherealmoffinancialadvice. Thisstudy’sfindingscon-
tributetothetheoreticallandscapebyextendingtheapplicationofservice-dominantlogic
(SDL),integratingtheAIDeviceUseAcceptance(AIDUA)framework,andhighlighting
thecomplexinterplaybetweenAI’sattributesandconsumerperceptions.
Thesefindingsemphasizetheimportanceofpersonalizedinvestmentsuggestions,
human-likeempathy,andcontinuousimprovementtoGenAI’srecommendationswithin
thecontextofconsumervalueco-creation,ashighlightedbySDLtheory. Bytailoringits
servicestoindividualconsumerneedsandpreferences,GenAIfacilitatesamoreinteractive
and collaborative experience between service providers and consumers, thus enabling
valueco-creation. Asdemonstratedbypreviousstudies(Wenetal.2022),personalization
iscrucialtoenablingvalueco-creation,allowingforamoreinteractiveandcollaborative
experiencebetweenserviceprovidersandconsumers. Thisstudy’sfindingsalignwith
SDLprinciplesandextendthetheorybyshowinghowdigitaltechnologiesenhanceper-
sonalized value co-creation, surpassing the limitations of traditional human-to-human
serviceframeworks.
Moreover, GenAI’s ability to exhibit human-like empathy significantly influences
consumers’ perceived authenticity by demonstrating genuine care and concern. This
finding contributes to the growing body of literature on the importance of designing
AI technologies that are not only competent but also genuine and transparent in their
interactions(Markovitchetal.2024).Additionally,GenAI’scapacityforcontinuouslearning
enablesittoadapttoevolvinguserneedsandpreferences,therebyenhancingitsperceived
authenticityovertime(Baidoo-AnuandAnsah2023;Rajetal.2023).
These findings underscore the importance of integrating personalized investment
suggestions, human-like empathy, and continuous improvement into GenAI-driven fi-
nancialadvice. ThisintegrationreflectstheprocessesofSDLandAIDUAbyco-creating
valuethroughtailored,empathetic,andadaptivefinancialguidance,ultimatelyenhancing
consumerengagement,trust,andparticipationinGenAI-poweredfinancialservices.
Thisstudyalsohighlightstheroleofperceivedauthenticityinhuman–botinteractions,
especially within the field of artificial intelligence (Seitz 2024; Meng et al. 2023). The
positivecorrelationbetweenGenAI’sfeaturesanditsperceivedauthenticityalignswiththe
authenticityprincipleinAIresearch(EsmarkJonesetal.2022;Reseetal.2020;Kuhailetal.
2022). ThisemphasizesthenecessityforGenAIandsimilartechnologiestodemonstrate
authenticitytoeffectivelyengageandsupportusers.
Additionally,thisstudyidentifiesastrongcorrelationbetweenperceivedauthenticity,
utilitarianattitudes,andconsumers’willingnesstocommunicateorresistancetocommu-
nicating with GenAI for financial advice. It expands our understanding of technology
adoptiontheoriesbydemonstratingthatperceivedauthenticityenhancesutilitarianatti-
tudestowardsGenAI,which,inturn,affectwillingnesstouseorresistancetousingGenAI
forfinancialadvice. Thissuggeststhatthevalueconsumersplaceonauthenticitycansignif-
icantlyinfluencetheirpracticalassessmentofatechnology’sbenefits(AlimamyandKuhail
2023). ThesefindingsadvocateforabroaderinterpretationofperceivedusefulnessinAI
technologyacceptance,highlightingtheimportanceofauthenticityinshapingutilitarian
evaluationsofAItechnology.
Lastly,thisstudy’sfocusonAIliteracyaddstothetheoreticallandscapebysuggesting
thatahigherlevelofAIliteracycanenhancetheeffectivenessofAIfeaturesbyimproving
theirperceivedauthenticityand,consequently,utilitarianattitudestowardsthem(Duetal.

J.RiskFinancialManag.2024,17,470 18of25
2024). This implies that individuals’ interactions with AI technologies are significantly
influencedbytheirunderstandingofthesetechnologies,leadingtoincreasedacceptance
andwillingnesstocommunicatewithGenAI.Conversely,lowerlevelsofAIliteracymay
leadtoresistancetocommunicatingwithGenAI,highlightingtheimportanceofaddressing
this factor to facilitate the effective integration of AI-driven services into the consumer
valueco-creationprocess.
Inconclusion,thisstudyoffersacomprehensiveintegrationofkeyconcepts,including
personalized investment suggestions, human-like empathy, continuous improvement,
perceivedauthenticity,utilitarianattitudes,andconsumers’willingnesstocommunicateor
resistancetocommunicatingwithGenAI,withintheframeworksofSDLandAIDUA.Its
findingsshowthatGenAI’spersonalizedandempatheticapproach,alongwithitsabilityto
continuouslyimprove,enhancesitsperceivedauthenticityandutilitarianattitudestowards
itamongconsumers,facilitatingvalueco-creationasproposedbySDL.Additionally,this
studyextendstheAIDUAmodelbyincorporatingcontinuousimprovementasafactor
influencingperceivedauthenticity,akeydeterminantofAItoolusage. Thisresearchalso
underscorestheroleofAIliteracyinshapingconsumers’willingnesstoengageorresistance
toengagingwithGenAI,highlightingtheimportanceofaddressingthisfactortoensurethe
effectiveintegrationofAI-drivenservicesintothevalueco-creationprocess. Overall,this
studycontributestothegrowingbodyofliteratureonAI-drivenservicesandtheirimpact
onconsumerbehavior,providingvaluableinsightsforbothresearchersandpractitioners
inthefield.
6.2. PracticalImplications
Thepracticalimplicationsofthisstudyaresubstantial,providingvaluableinsights
forawiderangeofstakeholders,includingfinancialinstitutions,technologydevelopers,
andpolicymakers. Forfinancialserviceproviders,thisstudyemphasizestheimportance
ofdevelopingGenAItechnologieswithenhancedhuman-likecharacteristics,suchasthe
ability to offer personalized advice and exhibit empathy. This suggests that financial
institutionsshouldinvestinAIsystemsthatgobeyondbasicnaturallanguageprocessing
andincorporatetheabilitytounderstandandadapttoindividualemotionalstatesand
preferences. ThisresearchindicatesthatGenAI-drivenchatbotscapableofrecognizingand
respondingtousers’emotionscansignificantlyenhanceusersatisfactionandengagement.
ThisunderscoresthenecessityoffinancialinstitutionsemployingGenAItechnologiesthat
cantailortheirservicestoindividualneedsandpreferences.
Furthermore,thisstudyhighlightstheimportanceofcontinuouslearninginmain-
tainingandenhancingconsumertrustandengagementwithGenAIsystems. Financial
institutions should prioritize designing AI systems that can continuously update their
knowledgebasesandrefinetheiralgorithmsbasedonuserinteractions. Thisapproach
alignswiththecontinuousimprovementaspectofAIdevelopmentandensuresthatAI
systemsremainrelevantandeffectiveinmeetingevolvingconsumerneedsandpreferences.
AIsystemscapableofcontinuouslearningandimprovementarebetterequippedtobuild
andmaintainusertrustovertimebydemonstratinganongoingcommitmenttoproviding
accurateandup-to-dateinformation.
Thisstudy’sfindingsalsoemphasizetheimportanceofAIliteracyinenhancingthe
positive impact of GenAI’s attributes on its perceived authenticity. This suggests that
financial institutions should develop educational programs and resources to improve
consumers’understandingofAI.ByinvestingininitiativesthatdemystifyAItechnologies,
financialinstitutionscanreduceresistanceandincreaseengagementamongconsumers.
ThisalignswiththebroadergoalofenhancingAIliteracyandensuringthatconsumers
havethenecessaryknowledgeandskillstointeracteffectivelywithAI-drivenservices.
ConsumerswithhigherlevelsofAIliteracyaremorelikelytoappreciatethebenefitsof
AI-drivenservicesandengagewiththemmoreeffectively. Therefore,businessesshould
investineducationalinitiativestopromoteconsumerunderstandingandacceptanceof
thesetechnologies.

J.RiskFinancialManag.2024,17,470 19of25
In conclusion, this study’s implications highlight the importance of policymakers
consideringtheimpactofGenAI-drivenfinancialadviceonpersonalizedinvestmentsug-
gestions,human-likeempathy,andcontinuousimprovementinconsumerfinancialservices.
AsGenAIbecomesincreasinglyintegratedintothesector,policymakersmustensurethat
consumersreceivetailoredadvicethatalignswiththeiruniquefinancialcircumstances,
fosteringtrustandengagement. Additionally,theyshouldprioritizeconsumerprivacy
protectionwhilepromotingequitableaccesstoAI-drivenbenefits,addressingthedigital
divide. ThismayinvolveestablishingstandardsfortransparencyinAIalgorithms,ensur-
ingdataprivacy,andimplementingdigitalliteracyprograms. Byproactivelyaddressing
theseissueswithafocusonpersonalization,empathy,andcontinuousimprovement,pol-
icymakerscancreatearegulatorylandscapethatsupportsresponsibleinnovation. This
approachwillultimatelyencouragethedevelopmentanddeploymentofAItechnologies
withinthefinancialsectorthatprioritizeindividualneeds,buildmeaningfulconnections,
andcontinuouslyevolvetoserveconsumersbetter.
6.3. LimitationsandFutureDirections
Althoughthisstudyprovidesvaluableinsightsintothefactorsinfluencingconsumer
perceptionsandattitudestowardsGenAIinthecontextoffinancialadvice,itisimportant
to recognize its limitations. One limitation is its focus on mobile banking users as the
sample population, which may limit the generalizability of thesefindings to other con-
sumersegments. Futureresearchcouldaddressthisbyexploringsimilarquestionsacross
differentdemographics. Additionally,utilizingqualitativemethodologies,suchasin-depth
interviewsorfocusgroups,couldprovideamorenuancedunderstandingofconsumer
perceptionsofandattitudestowardsGenAI-drivenfinancialadvice.
Anotheravenueforfutureresearchistoexaminetheinfluenceofculturaldifferences
on consumer reactions to GenAI-powered financial advisors. Given the variability in
cultural values, norms, and expectations across societies, it is plausible that the factors
influencingperceivedauthenticityandutilitarianattitudestowardsGenAI-drivenfinancial
advicemayvary.Comparativestudiesacrossdifferentculturalcontextscouldoffervaluable
insightsintodesigninganddeployingGenAI-drivenfinancialadvisorstomeettheunique
needsandpreferencesofdiverseconsumergroups.
Finally,ethicalconsiderationsandprivacyconcernssurroundingGenAI-drivenfinan-
cialadvicearecriticalareasforfutureresearch. AsGenAIsystemsbecomemoreintegrated
intofinancialservices,ensuringtheyaredesignedanddeployedtorespectconsumerpri-
vacy,avoidbias,andpromotefairnessisparamount.Researchontheethicalimplicationsof
GenAI-drivenfinancialadvicecouldinformthedevelopmentofguidelinesandregulations
toensurethesetechnologiesareusedresponsiblyandinthebestinterestsofconsumers.
AuthorContributions:Conceptualization,Q.Y.andY.-C.L.;methodology,Q.Y.andY.-C.L.;software,
Q.Y.;validation,Q.Y.andY.-C.L.;formalanalysis,Q.Y.andY.-C.L.;investigation,Q.Y.;datacuration,
Q.Y.andY.-C.L.; writing—originaldraftpreparation, Q.Y.; writing—reviewandediting, Y.-C.L.;
visualization,Q.Y.andY.-C.L.;supervision,Y.-C.L.Allauthorshavereadandagreedtothepublished
versionofthemanuscript.
Funding:Thisresearchreceivednoexternalfunding.
DataAvailabilityStatement:Thedatathatsupportthefindingsofthisstudyareavailablefromthe
authorsuponreasonablerequest.
ConflictsofInterest:Theauthorsdeclarenoconflictsofinterest.

J.RiskFinancialManag.2024,17,470 20of25
AppendixA
TableA1.Operationaldefinitionsandmeasurementitems.
Constructs Measurements Source(s)
1.IfeelthattheinvestmentsuggestionbytheGenAIisinline
withmypreferences.
2.IfeelthattheinvestmentsuggestionbytheGenAIisinline
Personalized
withmytaste.
Investment
3.TheinvestmentsuggestionbytheGenAIiswhatIam (Q.Chenetal.2022)
Suggestions
interestedin.
(PISs)
4.TheinvestmentsuggestionbytheGenAIisbetterthanthe
suggestionsIgetfromotherplaces.
5.IfeelthatthequalityofinvestmentsuggestionbytheGenAI
iswhatIwant.
6.MyoverallevaluationoftheGenAIinvestmentsuggestionis
veryhigh.
7.IthinkthetheGenAIinvestmentsuggestionsarevaluable.
8.TheinvestmentsuggestionsoftheGenAIisflexibleand
changeableaccordingtomyquestion.
1.TheGenAImakesmefeelwarm.
2.TheGenAImakesmefeelthatitcaresaboutmyneeds.
3.TheGenAImakesmefeelconcerned.
4.IfeelthattheGenAIservesmeattentively.
Human-Like 5.IfeelthattheGenAIputsmyinterestsfirst.
(Pelauetal.2021;Fuetal.
Empathy 6.TheGenAIgivesmepersonalizedattention.
2023;HuandBentler1999)
(HLE) 7.TheGenAIhasexpressedbeingabletoempathizewiththe
customer’sfeelings.
8.TheGenAIhasindicateditcouldputitselfwellinthe
customer’sshoes.
9.TheGenAIisabletoaccuratelyunderstandthe
customer’sconcerns.
10.TheGenAIcanadoptmyperspectiveandrecommending
thedesiredfinancialproducts.
11.TheGenAIispreoccupiedwithofferingmethebest
financialproducts.
1.TheGenAIcanlearnfrompastexperience.
2.TheGenAI’sabilityisenhancedthroughlearning.
3.Afteraperiodofuse,theGenAI’sperformanceisgetting
ContinuousImprovement(CI) betterandbetter. (Q.Chenetal.2022)
4.IcanfeeltheGenAIisconstantlyupgrading.
5.TheGenAIfixespreviouserrors.
6.IfeelthattheGenAIisgettingmoreandmoreadvanced.
7.ThefunctionoftheGenAIhasbeenenhanced.
1.WhenIthinkoftheGenAI,Iseeauniqueset
ofcharacteristics. (Voetal.2024;Mengetal.
PerceivedAuthenticity(PA)
2.IwouldthinkoftheGenAIasauniqueindividual. 2023)
3.UsingtheGenAIprovidedmewithgenuineexperiences.
1.TheGenaIisuseful.
2.TheGenAIisproductive.
UtilitarianAttitude
3.TheGenaIisnecessary. (PriyaandSharma2023)
(UA)
4.TheGenAIispractical.
5.TheGenAIisfunctional.

J.RiskFinancialManag.2024,17,470 21of25
TableA1.Cont.
Constructs Measurements Source(s)
1.Iamwillingtoreceivefinancialadvisoryservicesfrom
GenAI.
WillingnesstoCommunicate 2.IwillfeelhappytointeractwithGenAI.
(MaandHuo2023;Kimand
withGenAI 3.IamlikelytointeractwithGenAI.
Hur2023)
(WCG) 4.IwouldliketoutilizetheGenAI-poweredfinancialserviceif
thereisanopportunity.
5.IintendtoutilizetheGenAIfinancialadvisory
servicecontinuously.
6.IrecommendtheGenAIfinancialadvisoryserviceto
myfriends.
1.ThefinancialadvisoryserviceprovidedbytheGenAIis
processedinalesshumanizedmanner.
ResistancetoCommunicating 2.Ipreferhumancontactwhenlookingfor
(MaandHuo2023;Yangetal.
withGenAI investmentsuggestions.
2023)
(RCG) 3.Peopleneedemotionalexchangeduringservicetransactions.
4.InteractionwiththeGenAIlackssocialcontact.
5.TheexistingproblemswithGenAImakemetakea
wait-and-seeapproachtoit.
6.IdonotplantocontinueusingGenAI.
1.IcanuseAItosolveproblemsinvolvingtextandwords.
2.Iknowhowtodecidewhichdatatocollectandhowto
processthemfortrainingAImodelstosolveproblems. (Almatrafietal.2024;Kong
AILiteracy(AIL)
3.IknowhowtointerpretresultsobtainedfromAIto etal.2024)
solveproblems.
4.IknowhowtoselectAIalgorithmstosolveproblems.
5.IknowhowtoimprovemyabilitytouseAIfor
problem-solving.
6.IcanuseAItosolveproblemsinvolvingimagesandvideos.
References
Alboqami,Hassan.2023.TrustMe,I’manInfluencer!-CausalRecipesforCustomerTrustinArtificialIntelligenceInfluencersinthe
RetailIndustry.JournalofRetailingandConsumerServices72:103242.[CrossRef]
Aldunate,Ángeles,SebastiánMaldonado,CarlaVairetti,andGuillermoArmelini.2022.UnderstandingCustomerSatisfactionvia
DeepLearningandNaturalLanguageProcessing.ExpertSystemswithApplications209:118309.[CrossRef]
Ali,Hassnian,andAhmetFarukAysan. 2023. WhatWillChatGPTRevolutionizeinFinancialIndustry? Availableonline: https:
//papers.ssrn.com/sol3/papers.cfm?abstract_id=4403372(accessedon18August2024).
Alimamy,Saifeddin,andMohammadAminKuhail. 2023. IWillBewithYouAlexa! TheImpactofIntelligentVirtualAssistant’s
AuthenticityandPersonalizationonUserReusageIntentions.ComputersinHumanBehavior143:107711.[CrossRef]
Alimamy,Saifeddin,andSamerAl-Imamy.2022.CustomerPerceivedValuethroughQualityAugmentedRealityExperiencesinRetail:
TheMediatingEffectofCustomerAttitudes.JournalofMarketingCommunications28:428–47.[CrossRef]
Almatrafi,Omaima,AdityaJohri,andHyunaLee. 2024. ASystematicReviewofAILiteracyConceptualization,Constructs,and
ImplementationandAssessmentEfforts(2019–2023).ComputersandEducationOpen6:100173.[CrossRef]
Ameen,Nisreen,AliTarhini,AlexanderReppel,andAmitabhAnand.2021.CustomerExperiencesintheAgeofArtificialIntelligence.
ComputersinHumanBehavior114:106548.[CrossRef]
Ashta,Arvind,andHeinzHerrmann.2021.ArtificialIntelligenceandFintech:AnOverviewofOpportunitiesandRisksforBanking,
Investments,andMicrofinance.StrategicChange30:211–22.[CrossRef]
Attié,Elodie,andLarsMeyer-Waarden.2022.TheAcceptanceandUsageofSmartConnectedObjectsAccordingtoAdoptionStages:
AnEnhancedTechnologyAcceptanceModelIntegratingtheDiffusionofInnovation,UsesandGratificationandPrivacyCalculus
Theories.TechnologicalForecastingandSocialChange176:121485.[CrossRef]
Baabdullah,AbdullahM.,AliAbdallahAlalwan,RaedSalahAlgharabat,BhimarayaMetri,andNripendraP.Rana. 2022. Virtual
AgentsandFlowExperience:AnEmpiricalExaminationofAI-PoweredChatbots.TechnologicalForecastingandSocialChange181:
121772.[CrossRef]
Baek,TaeHyun,andMinseongKim.2023.IsChatGPTScaryGood?HowUserMotivationsAffectCreepinessandTrustinGenerative
ArtificialIntelligence.TelematicsandInformatics83:102030.[CrossRef]

J.RiskFinancialManag.2024,17,470 22of25
Bag,Surajit,GautamSrivastava,MdMamoonAlBashir,SushmaKumari,MihalisGiannakis,andAbdulChowdhury.2022.Journeyof
CustomersinthisDigitalEra:UnderstandingtheRoleofArtificialIntelligenceTechnologiesinUserEngagementandConversion.
Benchmarking29:2074–98.[CrossRef]
Baidoo-Anu,David,andLeticiaOwusuAnsah.2023.EducationintheEraofGenerativeArtificialIntelligence(AI):Understandingthe
PotentialBenefitsofChatGPTinPromotingTeachingandLearning.JournalofAI7:52–62.[CrossRef]
Bhatia, Ankita, Arti Chandani, Rajiv Divekar, Mita Mehta, and Neeraja Vijay. 2022. Digital Innovation in Wealth Management
Landscape:TheModeratingRoleofRoboAdvisorsinBehaviouralBiasesandInvestmentDecision-Making.InternationalJournal
ofInnovationScience14:693–712.[CrossRef]
Brenner,Lukas,andTobiasMeyll.2020.Robo-Advisors:ASubstituteforHumanFinancialAdvice?JournalofBehavioralandExperimental
Finance25:100275.[CrossRef]
Cardon,Peter,CarolinFleischmann,JolantaAritz,MinnaLogemann,andJeanetteHeidewald.2023.TheChallengesandOpportunities
ofAI-AssistedWriting: DevelopingAILiteracyfortheAIAge. BusinessandProfessionalCommunicationQuarterly86: 257–95.
[CrossRef]
Carolus,Astrid,MartinJakosusKoch,SamanthaStraka,MarcErichLatoschik,andCarolinWienrich.2023.MAILS—MetaAILiteracy
Scale:DevelopmentandTestingofanAILiteracyQuestionnaireBasedonWell-FoundedCompetencyModelsandPsychological
Change-andMeta-Competencies.ComputersinHumanBehavior1:100014.[CrossRef]
Chang,Tsung-Sheng,andWei-HungHsiao.2024.UnderstandResistUseOnlineCustomerServiceChatbot:AnIntegratedInnovation
ResistTheoryandNegativeEmotionPerspective.AslibJournal.[CrossRef]
Chen,Boyang,ZongxiaoWu,andRuoranZhao. 2023. FromFictiontoFact: TheGrowingRoleofGenerativeAIinBusinessand
Finance.JournalofChineseEconomicandBusinessStudies21:471–96.[CrossRef]
Chen,Qian,YemingGong,YaobinLu,andJingTang.2022.ClassifyingandMeasuringtheServiceQualityofAIChatbotinFrontline
Service.JournalofBusinessResearch145:552–68.[CrossRef]
Chi, Nguyen Thi Khanh, and Nam Hoang Vu. 2023. Investigating the Customer Trust in Artificial Intelligence: The Role of
Anthropomorphism,EmpathyResponse,andInteraction.CAAITransactionsonIntelligenceTechnology8:260–73.[CrossRef]
Chou,Szu-Yu,Chih-WeiLin,Yi-ChunChen,andJyh-ShenChiou.2023.TheComplementaryEffectsofBankIntangibleValueBinding
inCustomerRobo-AdvisoryAdoption.InternationalJournalofBankMarketing41:971–88.[CrossRef]
Chuah,StephanieHui-Wen,andJoanneYu.2021.TheFutureofService:ThePowerofEmotioninHuman-RobotInteraction.Journalof
RetailingandConsumerServices61:102551.[CrossRef]
Dewasiri,NarayanageJayantha,KarunarathnageSajithSenakaNuwansiriKarunarathna,MananageShanikaHansiniRathnasiri,
DunusingheDharmarathne,andKiranSood.2024.UnleashingtheChallengesofChatbotsandChatGPTintheBankingIndustry:
EvidencefromanEmergingEconomy.InTheFrameworkforResilientIndustry:AHolisticApproachforDevelopingEconomies.London:
Routledge,pp.23–37.
Dinh,Cong-Minh,andSungjunPark.2023.HowtoIncreaseConsumerIntentiontoUseChatbots?AnEmpiricalAnalysisofHedonic
andUtilitarianMotivationsonSocialPresenceandtheModeratingEffectsofFearacrossGenerations.ElectronicCommerceResearch
6:1–41.[CrossRef]
Du,Hua,YanchaoSun,HaozheJiang,A.Y.M.AtiquilIslam,andXiaoqingGu.2024.ExploringtheEffectsofAILiteracyinTeacher
Learning:AnEmpiricalStudy.HumanitiesandSocialSciencesCommunications11:559.[CrossRef]
EsmarkJones,CarolL.,TylerHancock,BrettKazandjian,andClayM.Voorhees.2022.EngagingtheAvatar:TheEffectsofAuthenticity
SignalsduringChat-BasedServiceRecoveries.JournalofBusinessResearch144:703–16.[CrossRef]
Fornell,Claes,andDavidF.Larcker.1981.StructuralEquationModelswithUnobservableVariablesandMeasurementError:Algebra
andStatistics.JournalofMarketingResearch18:39–50.[CrossRef]
Fu,Jindi,SamarMouakket,andYuanSun.2023.TheRoleofChatbots’Human-LikeCharacteristicsinOnlineShopping.Electronic
CommerceResearchandApplications61:101304.[CrossRef]
Fu,Xuemei.2024.UnderstandingtheAdoptionIntentionforElectricVehicles:TheRoleofHedonic-UtilitarianValues.Energy301:
131703.[CrossRef]
Fui-HoonNah,Fiona,RuilinZheng,JingyuanCai,KengSiau,andLangtaoChen.2023.GenerativeAIandChatGPT:Applications,
Challenges,andAI-HumanCollaboration.JournalofInformationTechnologyCaseandApplicationResearch25:277–304.[CrossRef]
Ghosh,Manimay.2024.EmpiricalStudyonConsumers’ReluctancetoMobilePaymentsinaDevelopingEconomy.JournalofScience
andTechnologyPolicyManagement15:67–92.[CrossRef]
Glikson,Ella,andOmriAsscher.2023.AI-MediatedApologyinaMultilingualWorkContext:ImplicationsforPerceivedAuthenticity
andWillingnesstoForgive.ComputersinHumanBehavior140:107592.[CrossRef]
Grönroos,Christian.2008.ServiceLogicRevisited:WhoCreatesValue?AndWhoCo-Creates?EuropeanBusinessReview20:298–314.
[CrossRef]
Gursoy,Dogan,OscarHengxuanChi,LuLu,andRobinNunkoo.2019.Consumers’AcceptanceofArtificiallyIntelligent(AI)Device
UseinServiceDelivery.InternationalJournalofInformationManagement49:157–69.[CrossRef]
Hair,JosephFranklin,MarceloLuizDiasdaSilvaGabriel,andVijayK.Patel. 2014. AMOSCovariance-BasedStructuralEquation
Modeling(CB-SEM):GuidelinesonitsApplicationasaMarketingResearchTool.BrazilJournalofMarketing13:1–15.[CrossRef]
Hsieh,Pi-Jung.2016.AnEmpiricalInvestigationofPatients’AcceptanceandResistanceTowardtheHealthCloud:TheDualFactor
Perspective.ComputersinHumanBehavior63:959–69.[CrossRef]

J.RiskFinancialManag.2024,17,470 23of25
Hu,Li-Tze,andPeterM.Bentler.1999.CutoffCriteriaforFitIndexesinCovarianceStructureAnalysis:ConventionalCriteriaVersus
NewAlternatives.StructuralEquationModeling6:1–55.[CrossRef]
Huang,Ming-Hui,andRolandT.Rust.2018.ArtificialIntelligenceinService.JournalofServiceResearch21:155–72.[CrossRef]
Huang,Ming-Hui,andRolandT.Rust. 2021. EngagedtoaRobot? TheRoleofAIinService. JournalofServiceResearch24: 30–41.
[CrossRef]
Jan,IhsanUllah,SeonggooJi,andChangjuKim.2023.What(De)MotivatesCustomerstoUseAI-PoweredConversationalAgentsfor
Shopping?TheExtendedBehavioralReasoningPerspective.JournalofRetailingandConsumerServices75:103440.[CrossRef]
Javaid,Mohd,AbidHaleem,andRaviPratapSingh.2023.AStudyonChatGPTforIndustry4.0:Background,Potentials,Challenges,
andEventualities.JournalofEconomyandTechnology1:127–43.[CrossRef]
Kelly, Sage, Sherrie-Anne Kaye, and Oscar Oviedo-Trespalacios. 2023. What Factors Contribute to the Acceptance of Artificial
Intelligence?ASystematicReview.TelematicsandInformatics77:101925.[CrossRef]
Kim,HeeWoong,HockChuanChan,andSumeetGupta.2007.Value-BasedAdoptionofMobileInternet:AnEmpiricalInvestigation.
DecisionSupportSystems43:111–26.[CrossRef]
Kim,Juran,SeungmookKang,andJoonheuiBae.2022.HumanLikenessandAttachmentEffectonthePerceivedInteractivityofAI
Speakers.JournalofBusinessResearch144:797–804.[CrossRef]
Kim,WooBin,andHeeJinHur. 2023. WhatMakesPeopleFeelEmpathyforAIChatbots? AssessingtheRoleofCompetenceand
Warmth.InternationalJournalofHuman–ComputerInteraction40:4674–87.[CrossRef]
Ko,Hyungjin,andJaewookLee. 2024. CanChatGPTImproveInvestmentDecisions? FromaPortfolioManagementPerspective.
FinanceResearchLetters64:105433.[CrossRef]
Kong,Siu-Cheung,WilliamMan-YinCheung,andOlsonTsang. 2024. DevelopinganArtificialIntelligenceLiteracyFramework:
EvaluationofaLiteracyCourseforSeniorSecondaryStudentsUsingaProject-BasedLearningApproach.Computers&Education:
ArtificialIntelligence6:100214.[CrossRef]
Kuhail,MohammadAmin,JustinThomas,SalwaAlramlawi,SyedJawadHussainShah,andErikThornquist.2022.Interactingwitha
Chatbot-BasedAdvisingSystem:UnderstandingtheEffectofChatbotPersonalityandUserGenderonBehavior.Informatics9:81.
[CrossRef]
Kwon,Jookyung,EklouAmendah,andJiseonAhn. 2024. MediatingRoleofPerceivedAuthenticityintheRelationshipbetween
LuxuryServiceExperienceandLifeSatisfaction.JournalofStrategicMarketing32:137–51.[CrossRef]
Lee,Garim,andHye-YoungKim.2024.Humanvs.AI:TheBattleforAuthenticityinFashionDesignandConsumerResponse.Journal
ofRetailingandConsumerServices77:103690.[CrossRef]
Li,Jian,JinsongHuang,andYaqiLi. 2023. ExaminingtheEffectsofAuthenticityFitandAssociationFit:ADigitalHumanAvatar
EndorsementModel.JournalofRetailingandConsumerServices71:103230.[CrossRef]
Lin,Hongxia,OscarHengxuanChi,andDoganGursoy.2020.AntecedentsofCustomers’AcceptanceofArtificiallyIntelligentRobotic
DeviceUseinHospitalityServices.JournalofHospitalityMarketingandManagement29:530–49.[CrossRef]
Ma,Xiaoyue,andYudiHuo.2023.AreUsersWillingtoEmbraceChatGPT?ExploringtheFactorsontheAcceptanceofChatbotsfrom
thePerspectiveofAIDUAFramework.TechnologyinSociety75:102362.[CrossRef]
Markovitch,DmitriG.,RustyA.Stough,andDonglingHuang. 2024. ConsumerReactionstoChatbotVersusHumanService: An
InvestigationintheRoleofOutcomeValenceandPerceivedEmpathy. JournalofRetailingandConsumerServices79: 103847.
[CrossRef]
Markus,André,JanPfister,AstridCarolus,AndreasHotho,andCarolinWienrich.2024.EffectsofAIUnderstanding-TrainingonAI
Literacy,Usage,Self-DeterminedInteractions,andAnthropomorphizationwithVoiceAssistants.Computers&EducationOpen6:
100176.[CrossRef]
Meng,Lu,TongmaoLi,XiaolinShi,andXinHuang.2023.Double-SidedMessagesImprovetheAcceptanceofChatbots.Annalsof
TourismResearch102:103644.[CrossRef]
Morhart,Felicitas,LuciaMalär,AmélieGuèvremont,FlorentGirardin,andBiancaGrohmann.2015.BrandAuthenticity:AnIntegrative
FrameworkandMeasurementScale.JournalofConsumerPsychology25:200–18.[CrossRef]
Musto,Cataldo,GiovanniSemeraro,PasqualeLops,MarcodeGemmis,andGeorgiosLekkas.2015.PersonalizedFinanceAdvisory
throughCase-BasedRecommenderSystemsandDiversificationStrategies.DecisionSupportSystem77:100–11.[CrossRef]
Napoli,Julie,SoniaJ.Dickinson,MichaelB.Beverland,andFrancisFarrelly.2014.MeasuringConsumer-BasedBrandAuthenticity.
JournalofBusinessResearch67:1090–98.[CrossRef]
Nazir,Anam,andZeWang.2023.AComprehensiveSurveyofChatGPT:Advancements,ProspectsApplications,andChallenges.
Meta-Radiology1:100022.[CrossRef]
Ng,DavyTszKit,JacKaLokLeung,SamuelKaiWahChu,andMaggieShenQiao.2021.ConceptualizingAILiteracy:AnExploratory
Review.Computers&Education:ArtificialIntelligence2:100041.[CrossRef]
Niu,Ben,andGustaveFlorentinNkoulouMvondo.2024.IAmChatGPT,theUltimateAIChatbot!InvestigatingtheDeterminantsof
Users’LoyaltyandEthicalUsageConcernsofChatGPT.JournalofRetailingandConsumerServices76:103562.[CrossRef]
Oehler,Andreas,andMatthiasHorn. 2024. DoesChatGPTProvideBetterAdvicethanRobo-Advisors? FinanceResearchLetters60:
104898.[CrossRef]
Pandey,Palima,andAlokKumarRai.2024.AnalyticalModelingofPerceivedAuthenticityinAIAssistants:ApplicationofPLS-Predict
AlgorithmandImportance-PerformanceMapAnalysis.SouthAsianJournalofBusinessStudies.[CrossRef]

J.RiskFinancialManag.2024,17,470 24of25
Paul, Justin, Akiko Ueno, and Charles Dennis. 2023. ChatGPT and Consumers: Benefits, Pitfalls and Future Research Agenda.
InternationalJournalofConsumerStudies47:1213–25.[CrossRef]
Pelau,Corina,Dan-CristianDabija,andIrinaEne.2021.WhatmakesanAIdevicehuman-like?Theroleofinteractionquality,empathy
andperceivedpsychologicalanthropomorphiccharacteristicsintheacceptanceofartificialintelligenceintheserviceindustry.
ComputersinHumanBehavior122:106855.[CrossRef]
Perchik,JordanD.,A.D.Smith,A.A.Elkassem,J.M.Park,S.A.Rothenberg,M.Tanwar,andH.Sotoudeh.2023.ArtificialIntelligence
Literacy:DevelopingaMulti-InstitutionalInfrastructureforAIEducation.AcademicRadiology30:1472–80.[CrossRef]
Pitardi,Valentina. 2023. PersonalizedandContextualArtificialIntelligence-BasedServicesExperience. InArtificialIntelligencein
CustomerService:TheNextFrontierforPersonalizedEngagement.Cham:Springer,pp.101–22.[CrossRef]
Podsakoff, PhilipM., andDennisW.Organ. 1986. Self-ReportsinOrganizationalResearch: ProblemsandProspects. Journalof
Management12:531–44.[CrossRef]
Priya,Bhanu,andVivekSharma.2023.ExploringUsers’AdoptionIntentionsofIntelligentVirtualAssistantsinFinancialServices:An
AnthropomorphicPerspectivesandSocio-PsychologicalPerspectives.ComputersinHumanBehavior148:107912.[CrossRef]
Raj,Rohit,ArpitSingh,VimalKumar,andPratimaVerma.2023.AnalyzingthePotentialBenefitsandUseCasesofChatGPTasaTool
forImprovingtheEfficiencyandEffectivenessofBusinessOperations.BenchCouncilTransactionsonBenchmarks,Standardsand
Evaluations3:100140.[CrossRef]
Raza,SyedA.,WasimQazi,KomaiAkramKhan,andJaveriaSalam.2021.SocialIsolationandAcceptanceoftheLearningManagement
System(LMS)intheTimeofCOVID-19Pandemic:AnExpansionoftheUTAUTModel.JournalofEducationalComputingResearch
59:183–208.[CrossRef]
Rese,Alexandra,LenaGanster,andDanielBaier. 2020. ChatbotsinRetailers’CustomerCommunication: HowtoMeasureTheir
Acceptance?JournalofRetailingandConsumerServices56:102176.[CrossRef]
Riikkinen, Mikko, Hannu Saarijärvi, Peter Sarlin, and Ilkka Lähteenmäki. 2018. Using Artificial Intelligence to Create Value in
Insurance.InternationalJournalofBankMarketing36:1145–68.[CrossRef]
Roh,Taewoo,ByungIlPark,andShufengXiao.2023.AdoptionofAI-EnabledRobo-AdvisorsinFintech:SimultaneousEmployment
of UTAUT and the Theory of Reasoned Action. Journal of Electronic Commerce Research 24: 29–47. Available online: https:
//api.semanticscholar.org/CorpusID:258835831(accessedon11October2024).
Roumeliotis,KonstantinosI.,andNikolaosD.Tselikas.2023.ChatGPTandOpen-AIModels:APreliminaryReview.FutureInternet15:
192.[CrossRef]
Seitz,Lennart.2024.ArtificialEmpathyinHealthcareChatbots:DoesitFeelAuthentic?ComputersinHumanBehavior:ArtificialHumans
2:100067.[CrossRef]
Shin,Donghee,AzmatRasul,andAnestisFotiadis.2022.WhyAmISeeingThis?DeconstructingAlgorithmLiteracythroughtheLens
ofUsers.InternetResearch32:1214–34.[CrossRef]
Sironi,Paolo.2016.FinTechInnovation:FromRobo-AdvisorstoGoalBasedInvestingandGamification.Hoboken:JohnWiley&Sons.
Sperling,Katarina,Carl-JohanStenberg,CormacMcGrath,AnnaÅkerfeldt,FredrikHeintz,andLinneaStenliden.2024.InSearchof
ArtificialIntelligence(AI)LiteracyinTeacherEducation:AScopingReview.ComputersandEducationOpen6:100169.[CrossRef]
Srinivasan, Srini S., Rolph Anderson, and Kishore Ponnavolu. 2002. Customer Loyalty in E-Commerce: An Exploration of its
AntecedentsandConsequences.JournalofRetailing78:41–50.[CrossRef]
Stahl, Bernd Carsten, and Damian Eke. 2024. The Ethics of ChatGPT–Exploring the Ethical Issues of an Emerging Technology.
InternationalJournalofInformationManagement74:102700.[CrossRef]
Tam,KarYan,andShukYingHo.2005.WebPersonalizationasaPersuasionStrategy:AnElaborationLikelihoodModelPerspective.
InformationSystemsResearch16:271–91.[CrossRef]
Tirado-Morueta,Ramón,JoséIgnacioAguaded-Gómez,andÁngelHernando-Gómez.2018.TheSocio-DemographicDivideinInternet
UsageModeratedbyDigitalLiteracySupport.TechnologyinSociety55:47–55.[CrossRef]
Ullah,Rafid,HishamuddinBinIsmail,MohammadTariqulIslamKhan,andAliZeb.2024.NexusbetweenChatGPTUsageDimensions
andInvestmentDecisionsMakinginPakistan:ModeratingRoleofFinancialLiteracy.TechnologyinSociety76:102454.[CrossRef]
VanTeijlingen,EdwinR.,andVanoraHundley.2002.Theimportanceofpilotstudies.SocialResearchUpdate35:1–4.Availableonline:
http://sru.soc.surrey.ac.uk/SRU35.html(accessedon11October2024).[CrossRef]
Vargo, StephenL., andRobertF.Lusch. 2004. EvolvingtoaNewDominantLogicforMarketing. JournalofMarketing68: 1–17.
[CrossRef]
Vargo,StephenL.,PaulP.Maglio,andMelissaArchpruAkaka.2008.OnValueandValueCo-Creation:AServiceSystemsandService
LogicPerspective.EuropeanManagementJournal26:145–52.[CrossRef]
Vesanen,Jari.2007.WhatisPersonalization?AConceptualFramework.EuropeanJournalofMarketing41:409–18.[CrossRef]
Vo,Diem-Trang,LongT.V.Nguyen,DuyDang-Pham,andAi-PhuongHoang. 2024. WhenYoungCustomersCo-CreateValueof
AI-PoweredBrandedApp:TheMediatingRoleofPerceivedAuthenticity.YoungConsumers25:557–78.[CrossRef]
Wang,Bingcheng,Pei-LuenRau,andTianyiYuan.2023.MeasuringUserCompetenceinUsingArtificialIntelligence:Validityand
ReliabilityofArtificialIntelligenceLiteracyScale.Behaviour&InformationTechnology42:1324–37.[CrossRef]
Wen,Haitao,LuluZhang,AoSheng,MingdaLi,andBingfengGuo.2022.From“Human-to-Human”to“Human-to-Non-Human”–
InfluenceFactorsofArtificialIntelligence-EnabledConsumerValueCo-CreationBehavior. FrontiersinPsychology13: 863313.
[CrossRef]

J.RiskFinancialManag.2024,17,470 25of25
Xia,Huosong,QianZhang,JustinZuopengZhang,andLevenJ.Zheng.2023.ExploringInvestors’WillingnesstoUseRobo-Advisors:
MediatingRoleofEmotionalResponse.IndustrialManagement&DataSystems123:2857–81.[CrossRef]
Yang, Bo, YongqiangSun, andXiao-LiangShen. 2023. UnderstandingAI-BasedCustomerServiceResistance: APerspectiveof
DefectiveAIFeaturesandTri-DimensionalDistrustingBeliefs.InformationProcessingandManagement60:103257.[CrossRef]
Zamil,AhmadM.A.,SaqibAli,MinhasAkbar,VaclavZubr,andFarhanRasool. 2023. TheConsumerPurchaseIntentiontoward
HybridElectricCar:AUtilitarian-HedonicAttitudeApproach.FrontiersinEnvironmentalScience11:1101258.[CrossRef]
Zhu,Hui,OlliVigren,andInga-LillSöderberg.2024.ImplementingArtificialIntelligenceEmpoweredFinancialAdvisoryServices:A
LiteratureReviewandCriticalResearchAgenda.JournalofBusinessResearch174:114494.[CrossRef]
Disclaimer/Publisher’sNote: Thestatements, opinionsanddatacontainedinallpublicationsaresolelythoseoftheindividual
author(s)andcontributor(s)andnotofMDPIand/ortheeditor(s).MDPIand/ortheeditor(s)disclaimresponsibilityforanyinjuryto
peopleorpropertyresultingfromanyideas,methods,instructionsorproductsreferredtointhecontent.