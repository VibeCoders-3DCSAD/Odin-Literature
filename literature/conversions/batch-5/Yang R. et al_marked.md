---
conversion_metadata:
  converted_at: "2026-07-21T09:28:33Z"
  converter_tool: "markitdown"
  converter_version: "0.1.6"
  source_pdf: "Yang R. et al.pdf"
  source_pdf_sha256: "bcc0e5ac5d19b13229bdeaab2199b8b2d9119ab09839150787152f3617ec3e9d"
  page_count: 14
  markdown_char_count: 127638
---

<!-- PAGE-AWARE EXTRACTION (via pdfminer.six) -->

<!-- PAGE 1 -->

Transactions on Artificial Intelligence

https://www.sciltp.com/journals/tai

Review 
Recent Advances in Artificial Intelligence for Management 
and Financial Technology

Renwei Yang 1,†, Yun Wang 1,†, Yongcan Luo 1,†, Zhengjie Yang 1,2,*, Zhimin Zong 3   
and Dapeng Oliver Wu 1

1  Department of Computer Science, City University of Hong Kong, Hong Kong 
2  Hong Kong Generative AI Research and Development Center, The Hong Kong University of Science and Technology,

Hong Kong

3  Department of Electrical & Computer Engineering, University of Florida, Gainesville, FL 32611, USA 
*  Correspondence: zhengjie.yang@sydney.edu.au 
†  These authors contributed equally to this work.

How To Cite: Yang, R.; Wang, Y.; Luo, Y.; et al. Recent Advances in Artificial Intelligence for Management and Financial Technology. 
Transactions on Artificial Intelligence 2025, 1(1), 139–152. https://doi.org/10.53941/tai.2025.100009.

Received: 11 June 2025

Revised: 22 July 2025

Accepted: 28 July 2025 
Published: 6 August 2025

Abstract:  In  this  survey,  we  examine  contemporary  advancements  in  Artificial 
Intelligence (AI) applications for Financial Technology (FinTech), with a specific 
focus on three rapidly evolving domains: recommendation systems, risk analysis, 
and AI-generated commercial content (AIGC). For recommendation systems, self-
supervised learning and graph neural network methodologies facilitate  real-time, 
hyper-personalized financial product suggestions, optimizing the balance between 
conversion  efficacy  and  regulatory  adherence.  For  risk  analysis,  large  language 
models,  including  GPT-4  and  Llama  3,  enhanced  through  sophisticated  prompt 
engineering techniques, have significantly transformed credit assessment and stress 
testing processes for small and medium-sized enterprises, reducing analytical cycles 
from  weeks  to  minutes.  Concurrently,  multimodal  generative  models,  such  as 
DALL-E  3,  are  revolutionizing  advertising  through  the  automated  generation  of 
compliant and engaging content across textual, visual, and video formats, markedly 
compressing production timelines. The survey further critically addresses persistent 
challenges, encompassing data privacy, algorithmic transparency, and cultural bias 
within  AIGC,  while  delineating  future  research  trajectories  for  developing 
trustworthy and scalable AI solutions in FinTech.

Keywords: Artificial Intelligence; Financial Technology; large language models

1. Introduction

Over  the  last  decade,  the  fusion  of  Artificial  Intelligence  (AI)  and  Financial  Technology  (FinTech)  has 
progressed from proof-of-concept prototypes to mission-critical production systems. Fueled by the unprecedented 
growth of digital data, inexpensive cloud computing, and breakthroughs in deep learning, AI now permeates almost 
every layer of the financial value chain from front-office customer engagement to back-office risk management 
and compliance.

Yet, despite enthusiastic adoption, the practical impact of AI is still uneven. Financial institutions grapple 
with  highly  regulated  environments,  severe  class-imbalance  problems,  extreme  tail  risks,  and  rapidly  shifting 
consumer preferences, all of which  challenge the direct transplantation of generic AI techniques developed for 
other industries. Consequently, domain-specific innovation and rigorous evaluation remain essential. This survey 
aims to provide a concise, up-to-date overview of three rapidly evolving application areas that, in our view, have 
recently achieved the largest leap forward and the widest commercial uptake. Specifically, recent breakthroughs 
in  representation  learning,  graph  neural  networks,  and  reinforcement  learning  are  empowering  AI-driven 
recommendation systems to deliver real-time, hyper-personalized product suggestions that boost conversion rates

Copyright:  ©  2025  by  the  authors. This is  an open  access  article  under the terms  and  conditions  of the  Creative Commons 
Attribution (CC BY) license (https://creativecommons.org/licenses/by/4.0/). 
Publisher’s Note: Scilight stays neutral with regard to jurisdictional claims in published maps and institutional affiliations.

---

<!-- PAGE 2 -->

Yang et al.

Trans. Artif. Intell. 2025, 1(1), 139–152

while meeting strict suitability and fairness regulations. Simultaneously, prompt-based large language models such 
as  GPT-4  and  Llama  3  (steered  through  meticulous  prompt  engineering)  are  revolutionizing  risk  analysis  by 
automating  credit  assessment,  scenario  generation,  stress  testing,  and  early-warning  detection,  compressing 
analytic cycles from weeks to minutes; and, in parallel, multimodal generative models are ushering in an era of 
AI-generated commercial advertising capable of producing compliant, captivating marketing assets across text, 
image, and video formats, dramatically reducing production timelines and enabling rapid A/B experimentation for 
financial products.

Most existing surveys provide broad overviews of AI applications in FinTech, focusing on areas such as 
smart finance, risk, and customer adoption [1–5]. In contrast, our work offers a focused and up-to-date review of 
three  emerging  directions:  self-supervised  and  graph-based  recommendation  systems,  large  language  model-
driven  risk  analysis,  and  AI-generated  commercial  content,  with  particular  attention  to  their  recent  technical 
advances and practical challenges.

The remainder of this survey is organized as follows. Section 2 reviews recent advances in recommendation 
algorithms  tailored  for  financial  products  and  omni-channel  marketing.  Section  3  discusses  how  prompt 
engineering and large language models reshape contemporary risk analysis workflows for Small and Medium-
sized  Enterprises  (SMEs).  Section  4  surveys  the  emerging  field  of  AI-generated  commercial  advertising, 
highlighting design patterns, governance considerations, and empirical performance. Finally, we conclude with 
open research challenges and future directions for trustworthy, scalable, and human-centric AI in FinTech.

2. AI in Recommendation Systems for Financial Marketing

With the advent of the digital age, marketing faces unprecedented opportunities and challenges. In the context 
of massive data and intense competition, how to accurately reach target customers and provide personalized service 
experiences  has  become  the  key  to  success  for  enterprises.  The  rapid  development  of  AI  technology  offers  a 
solution to this problem. Specifically, AI-driven personalized recommendation systems are revolutionizing the 
landscape of marketing, bringing significant competitive advantages to businesses. By analyzing user behavior, 
preferences,  and  historical  data,  AI  generates  personalized  recommendations  in  real-time,  enhancing  user 
experience and conversion rates. Machine learning algorithms continuously optimize recommendation models to 
ensure their relevance and accuracy, enabling businesses to utilize resources more effectively and maximize profits. 
The importance of AI in personalized recommendations cannot be overlooked. In today’s era of burgeoning deep 
learning, companies that embrace AI technology will stand out in the competition. In the following, we will explore 
AI-based  personalized  recommendation  technology  from  four  perspectives:  working  principles,  advantages, 
application cases, and future prospects.

2.1. Related Works

Recommendation systems have become a vital tool for discovering users’ interests, enhancing user experience, 
and driving revenue in various e-commerce platforms [6]. Modern recommendation systems, powered by advanced 
deep neural network architectures, have achieved remarkable success. For instance, Covington et al. [7] introduce 
deep neural networks for YouTube recommendations, Cheng et al. [8] propose the Wide & Deep Learning framework 
to balance recommendation precision and generalization, and Zhou et al. [9] develop the Deep Interest Network (DIN) 
for  click-through  rate  prediction.  Other  innovations  include  the  personalized  and  interpretable  substitute 
recommendation model by Chen et al. [10] and the joint modeling of users’ interests and mobility patterns in point-
of-interest recommendations by Yin et al. [11].

Despite these innovations, deep recommendation models are inherently data-hungry and face challenges due 
to  data  sparsity,  as  most  users  interact  with  only  a  small  subset  of  available  items  [12].  This  sparsity  issue 
significantly limits the performance of deep learning-based recommendation systems, as highlighted in the survey 
by Zhang et al. [13].

To address this challenge, Self-supervised Learning (SSL) [14] has emerged as a promising solution. Early 
works  explored  dimensionality  reduction  techniques  using  neural  networks  [15]  and  robust  feature  extraction 
through denoising autoencoders [16]. Several studies have investigated its transferability to downstream tasks [17], 
and  the  distinction  between  generative  and  contrastive  approaches  [18].  Wu  et  al.  [19]  propose  collaborative 
denoising autoencoders, which use corrupted input data to reconstruct the original input, effectively preventing 
overfitting and setting the foundation for subsequent advancements in self-supervised recommendation techniques. 
Additionally,  research  has  focused  on  large-scale  SSL  experiments  [20],  as  well  as  unsupervised  edge   
learning [21]. Other studies have revisited the role of data augmentation [22] and improved pre-training and self-
training techniques [23]. More recent works address representation learning via invariant causal mechanisms [24]

https://doi.org/10.53941/tai.2025.100009

140

---

<!-- PAGE 3 -->

Yang et al.

Trans. Artif. Intell. 2025, 1(1), 139–152

and feature decorrelation in SSL [25]. Liu et al. [18] discuss the potential of SSL in recommendation scenarios, 
emphasizing its ability to leverage unlabeled data for learning useful representations. Early prototypes of Self-
supervised Recommendation (SSR) date back to unsupervised methods such as autoencoder-based models.

2.2. Working Principles of Personalized Recommendation Systems

Personalized  recommendation  systems  rely  on  big  data  and  machine  learning  algorithms  to  analyze  user 
behavior data, preferences, and historical records, predicting user needs and providing tailored product and service 
recommendations.  As  shown  in  Figure  1,  the  primary  working  principles  are  as  follows:  (1)  Data  Collection: 
Collect  user  data  through  various  channels  (e.g.,  browsing  history,  purchase  records,  search  keywords,  etc.).   
(2) Data Preprocessing: Cleanse, normalize, and preprocess the collected data to ensure its quality and consistency. 
(3)  Feature  Extraction:  Use  feature  engineering  techniques  to  extract  useful  features  for  the  recommendation 
system from the preprocessed data. (4) Model Training: Train the recommendation model using machine learning 
algorithms such as collaborative filtering, matrix factorization, and deep learning. (5) Recommendation Generation: 
Generate personalized recommendations in real-time based on the trained model and display them to the user.

Figure 1. Workflow of AI recommendation system.

2.3. Regulatory, Trust, and Risk-Return Considerations

This section further discusses several core financial characteristics of financial AI recommendation systems, 
specifically focusing on regulatory restrictions, user trust mechanisms, and the balance between return and risk, as 
summarized in Table. 1.

Table 1. Comparison of literature on key financial AI recommendation system themes.

Key Points

Summary of Approaches

Theme

Representative 
Literature

Regulatory 
Restrictions

[26–29]

User Trust 
Mechanisms

[30–34]

Emphasize compliance with 
regulations (client suitability, 
transparency, and data 
protection).

Focus on transparency, 
fairness, and explainability to 
build trust.

Return and Risk 
Balance

[30,35–38]

Aim to maximize returns 
while managing risk per 
investor preferences.

Algorithms are designed to match 
investor profiles, ensure explainability, 
and adhere to region-specific 
requirements. 
Adoption of explainable AI, fairness-
aware models, and usercentered 
evaluation to increase user engagement 
and trust. 
Use of Modern Portfolio Theory, mean-
variance analysis, deep reinforcement 
learning, risk-aware optimization, and 
hybrid approaches for portfolio 
management.

Financial recommendation systems are subject to regulatory restrictions that shape their design and operation 
[26–29]. Regulations in various regions require systems to ensure client suitability, transparency, and robust data 
protection. These constraints necessitate that algorithms are designed to align recommendations with individual 
investor profiles while maintaining compliance.

User trust mechanisms are also essential for widespread adoption and sustained use [30–34]. Factors such as 
transparency, fairness, and the explainability of algorithms have a significant influence on user trust. The adoption

https://doi.org/10.53941/tai.2025.100009

141

---

<!-- PAGE 4 -->

Yang et al.

Trans. Artif. Intell. 2025, 1(1), 139–152

of explainable AI techniques has been proposed to help users better understand system recommendations, thereby 
increasing trust and engagement.

In  addition,  achieving  an  appropriate  balance  between  return  and  risk  remains  a  fundamental  financial 
objective [30,35–38]. Financial recommendation systems must consider both maximizing returns and managing 
risk  according  to  investors’  preferences.  Classical  approaches  such  as  Modern  Portfolio  Theory  are  frequently 
employed,  and  recent  research  incorporates  machine  learning  to  further  optimize  portfolio  allocation  and   
risk control.

In summary, regulatory compliance, user trust, and the management of return and risk are all crucial factors

in the development and evaluation of financial AI recommendation systems.

2.4. Advantages of AI-Powered Personalized Recommendation Systems

AI-powered personalized recommendation systems [9–14,17–25] play a crucial role in modern information

technology, with advantages that stand out in several areas.

Precision is one of the major highlights of AI recommendation systems. By analyzing massive amounts of 
data, including users’ historical behaviors, browsing records, search habits, and social network interactions, AI 
can deeply understand users’ interests and needs. This granular analysis enables the recommendation system to 
provide highly relevant content,  far surpassing traditional methods. Traditional recommendations often rely on 
simple  rules  or  limited  data,  while  AI  can  integrate  complex,  multi-dimensional  information  to  deliver  more 
accurate predictions and recommendations.

Real-time responsiveness is another significant feature of AI recommendation systems. These systems can 
instantly respond to changes in user behavior and update recommendations in real-time. For instance, when a user 
searches for or consumes new types of content on a platform, the AI system can quickly adjust its recommendation 
strategy to ensure the user always receives the most relevant and up-to-date suggestions. This dynamic adjustment 
capability not only enhances user experience but also strengthens the platform’s competitiveness.

Scalability demonstrates great flexibility and adaptability in AI recommendation systems. As the scale of 
user data grows and algorithms continuously improve, system performance and recommendation quality can keep 
improving. Whether for small applications or large platforms, AI systems can operate efficiently and consistently 
provide  high-quality  recommendations.  This  scalability  ensures  that  AI  recommendation  systems  can  adapt  to 
various application scenarios, from e-commerce platforms to streaming services, maximizing their utility across 
different environments.

Enhanced user experience is the most direct advantage of AI recommendation systems. Through personalized 
recommendations, users can access content that better aligns with their interests and enjoy a smoother and more 
enjoyable experience. This personalized service significantly increases user satisfaction and loyalty, encouraging 
users to spend more time on the platform and improving user engagement and activity. This deep user involvement 
not only drives growth in the user base but also brings significant commercial value to the platform.

2.5. Application Cases of AI-Powered Personalized Recommendation Systems

Today, AI-powered personalized recommendation systems are widely used by many businesses. Below are

examples from four fields: content platforms, social media, e-commerce platforms, and physical retail.

In  social  media,  platforms  like  Facebook,  Instagram,  and  Weibo  utilize  AI  recommendation  systems  to 
deliver personalized content and advertisements, significantly improving user engagement and ad conversion rates. 
On  e-commerce  platforms  such  as  Amazon  and  Alibaba,  AI  recommendation  systems  provide  personalized 
product recommendations, enhancing purchase rates and average transaction values.

On content platforms like Netflix and YouTube, recommendation systems leverage AI technology to improve 
users’ viewing experiences, particularly by using latent semantic models for personalized recommendations, as 
shown in Figure 2. The core of latent semantic models lies in their ability to capture the underlying relationships 
between users and content. First, the system analyzes a large amount of user behavior data and content features to 
generate labels for users and content. These labels may include users’ viewing histories, preferences, and the types 
and themes of the content. Subsequently, the system can push content more accurately based on the labels.

Latent semantic model technology employs mathematical methods like matrix factorization to map users and 
content  into  an  abstract  “latent  space”.  In  this  space,  user  and  content  features  are  represented  as  vectors.  By 
calculating the similarity between these vectors, the system can predict content that users might find interesting. 
This method considers not only explicit features but also uncovers users’ hidden preferences, making it widely 
applied in recommendation systems.

https://doi.org/10.53941/tai.2025.100009

142

---

<!-- PAGE 5 -->

Yang et al.

Trans. Artif. Intell. 2025, 1(1), 139–152

Figure 2. Latent semantic model in recommendation system.

In physical retail environments, AI recommendation systems have demonstrated significant utility. Nestle 
provides a clear example of this. They adopted an AI-driven order recommendation system that offers scientific 
product suggestions to sales personnel. This system showcases products that perform well in other retail stores and 
recommends complementary products to popular items, improving sales combinations. By analyzing purchasing 
patterns, similar buying behaviors, and sales history data, Nestle’s system provides precise recommendations.

According  to  data,  Nestle  has  successfully  implemented  this  AI  product  recommendation  system  in  over 
100,000 retail stores, effectively improving consumers’ shopping experiences [39]. In the first half of 2022, their 
sales revenue increased by 6%. In addition, this system has helped Nestle reduce costs and attract more customers 
through digital channels. Larissa Frias, Nestle’s Director of Data Analytics, noted that these experiences provided 
valuable references for future collaborations and project implementations, offering confidence and motivation for 
the team. This successful case highlights the immense potential of AI in the retail industry and provides valuable 
insights for other businesses in their digital transformation and efforts to enhance user experiences.

2.6. Challenges and Future of AI-Powered Personalized Recommendation Systems

Currently,  AI-powered  personalized  recommendation  systems  still  face  several  challenges,  such  as  data 
privacy, algorithm transparency, and the cold-start problem. Data privacy involves how to use user data reasonably 
while protecting their privacy to prevent leaks or misuse. Algorithm transparency requires systems to explain the 
rationale behind recommendations, enhancing user trust, such as by providing reasons to help users understand the 
recommendation logic. The cold-start problem refers to how to provide accurate recommendations for new users 
or new  items when  there is  a lack  of  historical  data,  which requires  additional methods  to compensate  for  the   
data shortage.

Despite these challenges, the industry places great emphasis on the technology of AI-powered personalized 
recommendation systems due to their commercial value. For example, Tom Alison, Head of Facebook at Meta, 
mentioned  in  his  article  “The  Future  of  Facebook”  [40]  (published  31  May  2024)  that  their  R&D  team  has 
conducted  multiple  optimizations  and  upgrades  to  AI  recommendation  systems.  He  also  noted  that  they  are 
developing  a  large-scale  AI  recommendation  model  to  support  Meta’s  video  services  and  provide  more 
personalized  and  precise  recommendation  experiences.  This  project  has  been  included  in  Meta’s  technology 
roadmap and is expected to be realized in the coming years. It is foreseeable that with the continuous development 
and deepening of AI technology, AI recommendation systems will become more mature and refined, providing 
users with more personalized and valuable experiences and showcasing even broader commercial prospects.

3. Prompt in Risk Analysis for Enterprises

In the modern business environment, Small and Medium-sized Enterprises (SMEs) face various risks, ranging 
from  market  fluctuations  and  operational  challenges  to  changes  in  laws  and  regulations,  all  of  which  can 
significantly impact their survival and growth. Traditional risk management methods often rely on historical data 
and subjective judgment, which are not only time-consuming but also prone to bias. With the advancement of AI 
technologies, particularly the emergence of language models such as ChatGPT and Llama, businesses can perform 
risk  analysis  more  efficiently.  By  designing  precise  prompts,  these  AI  models  can  provide  deep  insights  and 
support, optimizing risk management strategies for enterprises.

https://doi.org/10.53941/tai.2025.100009

143

---

<!-- PAGE 6 -->

Yang et al.

3.1. Background

Trans. Artif. Intell. 2025, 1(1), 139–152

Small  and  micro  enterprises  often  face  several  key  challenges  in  risk  management.  First,  the  uncertainty 
caused  by  market  fluctuations  significantly  impacts  their  financial  stability.  Unlike  larger  companies,  SMEs 
typically lack financial buffers and resources, making them more sensitive to market changes. Moreover, their 
vulnerability during economic downturns is more pronounced due to limited financing channels. The globalization 
of markets has also led to increased legal and compliance risks, as businesses must navigate constantly evolving 
legal  and  regulatory  requirements,  adding  to  their  compliance  burden.  In  supply  chain  management,  high 
dependency on specific suppliers makes these enterprises highly susceptible to disruptions, which can severely 
affect their operations. Traditional risk management approaches of ten struggle to respond promptly to these issues. 
However, the introduction of AI technologies offers new solutions for these enterprises.

From a macroeconomic perspective, SMEs are subject to broader economic indicators such as interest rate 
volatility,  inflation,  and  global  economic  cycles,  all  of  which  can  impact  consumer  demand  and  financing 
availability. Conversely, from a microeconomic perspective, risks such as internal operational inefficiencies, cost 
mismanagement,  or flawed  pricing  strategies  often  arise  from  firm-specific  characteristics.  AI-enabled  prompt 
design can assist in identifying both types of risk: macro-level trends via large-scale news and financial reports, 
and micro-level insights through analysis of firm operations, supply chain data, or internal narratives.

The  application  of  AI  in  risk  management  has  significantly  grown  in  recent  years.  AI  can  process  vast 
amounts of data in real-time, automatically identifying potential risks and greatly reducing the time required for 
manual  analysis.  By  employing  machine  learning  techniques,  AI  models  effectively  predict  market  shifts  and 
emerging risks, enabling proactive decision-making within businesses. Moreover, AI-driven tools offer optimized 
decision support based on analytical outcomes, significantly improving the timeliness and accuracy of enterprise 
risk responses.

3.2. Related Works

Recent  advances  in  Natural  Language  Processing  (NLP)  have  made  Large  Language  Models  (LLMs) 
indispensable for financial analysis. Their capacity to parse intricate financial disclosures, fuse heterogeneous data 
sources, forecast market dynamics, and gauge investor sentiment now underpins many state-of-the-art prediction 
systems.  For  instance,  Co-CPC  [41]  explicitly  couples  macro-  and  micro-economic  factors  to  mitigate  the 
uncertainty inherent in equity price movements. Complementary lines of work exploit unstructured text from news 
outlets [42,43] and Twitter streams [44–46] to distill sentiment signals that anticipate future returns. CapTE [47] 
advances this idea by pairing a transformer encoder (which captures deep semantic cues in social media) with a 
capsule network for direction-of-movement classification. Beyond prediction, Wang et al. [48] demonstrate how 
pre-trained LLMs automate the drafting of corporate financial reports, while Niu et al. [49] fuse knowledge-graph 
reasoning  with  LLM  outputs  to  forecast  volatility.  Purpose-built  domain  models  such  as  FinBert  [50]  and   
PIXIU [51], trained on large-scale sector-specific corpora, consistently achieve superior price-direction accuracy, 
making forecasting performance a benchmark for financial NLP.

Explainable AI (XAI) has also emerged as a critical component of AI-driven financial risk analysis, especially 
in regulated domains. For instance, Bussmann et al. [52] demonstrate the use of interpretable machine learning 
models in fintech risk management scenarios, such as loan default prediction and fraud detection. Their findings 
support the integration of transparency-focused design into AI systems used for financial decision-making.

Parallel research emphasises qualitative insight extraction from narrative data including earnings-call transcripts, 
real-time news, and community forums to infer market mood and anticipate price shifts. Wang et al. [53] show that 
sentiment signals mined from Wall Street message boards improve return predictions. Ding et al. [54] apply Open 
Information Extraction to transform vast web text into structured event records that drive an event-centric prediction 
model, and later encode these events as knowledge-graph vectors to embed market context [55]. Nguyen et al. [56] 
jointly model latent topics and their polarities via an LDA-inspired framework, while Ang et al. [57] integrate multi-
modal cues and evolving inter-firm relations through attention mechanisms. Collectively, these studies highlight that 
richer  qualitative  signals  (when  systematically  structured)  complement  numerical  indicators  and  enhance  the 
robustness of stock-trend forecasting.

Several studies have enhanced language models’ capabilities for financial data analysis and stock prediction 
by  employing  specialized  prompts  and  Chain  of  Thought  (CoT)  techniques.  Yu  et  al.  [58]  leverage  GPT-4  to 
effectively  summarize  weekly  and  monthly  financial  market  news,  construct  detailed  company  profiles  for 
enhanced  knowledge  representation,  and  generate  explainable  predictions.  Similarly,  Xie  et  al.  [59]  evaluate 
ChatGPT’s  zero-shot  performance  in  multimodal  stock  price  forecasting,  underscoring  the  necessity  for 
specialized training or fine-tuning to overcome prediction challenges. Jiang et al. [60] note that despite the inherent

https://doi.org/10.53941/tai.2025.100009

144

---

<!-- PAGE 7 -->

Yang et al.

Trans. Artif. Intell. 2025, 1(1), 139–152

potential  of  powerful  language  models  such  as  ChatGPT  in  financial  analysis,  their  direct  application  through 
simple  prompts  or  CoT  methods  still  trails  traditional  forecasting  approaches.  This  finding  emphasizes  the 
importance of carefully crafted prompts for successful financial prediction tasks.

3.3. Prompt Example

Assume a small or medium-sized manufacturing company is facing financial risks, particularly during times 
of economic instability. The company wants to leverage AI technology to analyze and predict future cash flow 
risks in order to ensure financial stability. The company primarily relies on multiple suppliers for raw materials 
and also faces issues such as delayed customer payments. The financial risks for the company are mainly derived 
from three aspects: raw material price fluctuations leading to increased costs, cash flow issues caused by customer 
payment delays, and sales risks due to market demand changes. The company seeks to use AI’s predictive analysis 
capabilities to better manage these risks.

To  effectively  utilize  AI  models  for  financial  risk  forecasting,  we  need  to  guide  the  model  step  by  step, 
focusing on specific risk areas. Using the Chain of Thought (CoT) method, complex financial risk issues can be 
broken down into smaller, more manageable problems, gradually guiding the AI to perform in-depth analysis and 
reasoning. Here’s an example of a Chain of Thought analysis:

1.

Initial Prompt Design: “Analyze the impact of current economic uncertainty on the financial situation of a 
manufacturing company, including risks from raw material price fluctuations, customer payment delays, and 
market demand changes.”

2.  Refined Prompt to Focus on Specific Issues: “Assume that raw material prices may rise by 10% over the next 
six months. How much will the company’s procurement costs increase, and what procurement strategies can 
be adopted to mitigate this impact?”

AI  Analysis  Example  Output:  “If  raw  material  prices  increase  by  10%  procurement  costs  could  rise  by   
$100,000. The company can address this by negotiating price locks with suppliers, increasing the proportion of 
local suppliers, and stocking up in advance.”

3.  Further Analysis of Cash Flow Risks Due to Customer Payment Delays: “Under future economic uncertainty, 
assume  the  payment  cycle  for  major  clients  is  extended  by  30  days.  What  impact  will  this  have  on  the 
company’s cash flow? What strategies can be employed to mitigate this cash flow risk?”

AI Analysis Example Output: “An extension of the customer payment cycle by 30 days may lead to a cash 
flow shortfall of $50,000. The company could consider strategies such as installment payment plans, implementing 
accounts receivable insurance, or offering early payment discounts.”

4.  Comprehensive Analysis of Sales Risks from Market Demand Changes: “Considering potential changes in 
market demand, forecast the impact of sales fluctuations over the next six months on cash flow and profits. 
How should the company adjust its product mix and pricing strategy to adapt to these changes?”

AI Analysis Example Output: “Based on current market data, sales are predicted to decrease by 15% over 
the next six months, resulting in a $150,000 revenue loss. The company can mitigate this by adjusting its product 
mix to meet new market demand, optimizing its pricing strategy, and launching promotional campaigns”.

4. AI in Commercial Advertising

As  technology  rapidly  advances,  the  application  of  Artificial  Intelligence  Generated  Content  (AIGC)  [61]  in 
advertising is becoming increasingly widespread. AIGC uses AI technology to automatically create text, images, and 
videos, offering limitless possibilities for companies’ advertising efforts and setting a new trend in marketing. Moreover, 
tools like ControlNet [62–66] and other advanced control methods now allow for fine-grained manipulation of generated 
images,  enabling  advertisers  to  specify  structural  or  semantic  constraints  directly  in  the  generation  process.  These 
techniques greatly enhance creative flexibility and regulatory compliance, ensuring that visual content aligns with brand 
guidelines and cultural sensitivities. Advertising, a highly creative and visually-driven industry, is gradually adopting 
AIGC technology to enhance efficiency and precision. This article explores the innovative applications of AIGC in 
advertising through examples of AI models like ChatGPT [67] and DALL-E 3 [68] generating ad texts, images, and 
videos. Practice has shown that AIGC not only significantly improves the efficiency of ad production but also greatly 
enhances the accuracy and effectiveness of advertising [69–72]. With these technologies, advertisers can more precisely 
reach their target audience, boosting the appeal and impact of their ads, bringing transformative change to the industry.

https://doi.org/10.53941/tai.2025.100009

145

---

<!-- PAGE 8 -->

Yang et al.

4.1. Background

Trans. Artif. Intell. 2025, 1(1), 139–152

AIGC refers to content generated using Generative AI (GAI) technology, rather than being created by human 
authors  [73].  It  can  automatically  create  large  volumes  of  content  in  a  short  period.  For  example,  ChatGPT, 
developed by OpenAI, is a language model designed for building conversational AI systems that can effectively 
understand and respond meaningfully to human language input. Similarly, Diffusion Models such as DALL-E 3 
and Stable Diffusion excel at synthesizing unique, high-quality images from textual descriptions [68,74–76]. These 
models can be further enhanced by frameworks like ControlNet [62], which allow for explicit control over image 
attributes  such  as  pose,  structure,  or  layout  during  generation,  making  them  highly  suitable  for  customized 
advertising campaigns and brand-specific requirements. As AIGC technology progresses, more experts believe it 
will  set  new  benchmarks  in  AI,  with  a  profound  impact  on  sectors  from  advertising  to  content  creation, 
revolutionizing the way we interact with information and media and ushering in a new era of efficiency, precision, 
and innovation.

4.2. Application of AIGC in Advertising Copywriting

Social  media platforms  like  Facebook  and  Xiaohongshu have  become an  indispensable part  of daily  life. 
AIGC can automatically generate personalized ad copy based on users’ profiles and interests. For instance, on 
Xiaohongshu,  ChatGPT  can  use  human-provided  ad  templates  to  create  high-quality,  customized  advertising 
content. A question and answer example is illustrated in Figure 3.

(a)

(b)

Figure 3. A question example (a) and an answer example (b) generated by ChatGPT.

4.3. Application of AIGC in Advertising Images

DALL-E 3, developed by OpenAI, is an AI image generation model that uses a diffusion model architecture 
and techniques like language-image contrastive learning to create images from text descriptions. Using the DALL-
E 3 model, advertisers can input product descriptions, target audience information, and ad style preferences to 
generate high-quality advertising images quickly. For example, as shown in Figure 4, if a restaurant owner wants 
to advertise a delicious steak, they just need to enter the food name and other details into the model. This allows 
them to generate a series of attractive restaurant food advertisements at a low cost. This approach not only saves 
production costs but also precisely targets the market, enhancing the appeal and effectiveness of the advertisements.

https://doi.org/10.53941/tai.2025.100009

146

---

<!-- PAGE 9 -->

Yang et al.

Trans. Artif. Intell. 2025, 1(1), 139–152

Figure 4. Schematic diagram of a steak generated by the DALL-E 3 model.

4.4. Current Solutions to Copyright and Cultural Misuse in AIGC

Recent  years  have  witnessed  a  rapid  surge  in  both  research  and  practical  initiatives  aimed  at  mitigating

copyright infringement and cultural misappropriation in AIGC.

Data  Governance  and  Copyright  Protection.  To  address  these  challenges,  leading  AIGC  platforms  are 
adopting  increasingly  robust  data  governance  frameworks.  These  efforts  [77,78]  include  the  deployment  of 
watermarking  technologies,  provenance-tracking  systems,  and  advanced  copyright  detection  tools  designed  to 
safeguard  against  the  unauthorized  use  of  protected  works.  Furthermore,  model  developers  are placing  greater 
emphasis  on  curating  training  datasets  to  exclude  copyrighted  or  culturally  sensitive  materials,  unless  explicit 
rights and permissions have been obtained. This proactive approach not only helps prevent infringement but also 
supports the responsible and ethical deployment of generative models.

Cultural  Sensitivity  Filters.  In  tandem  with  data  governance  improvements,  state-of-the-art  generative 
models are integrating sophisticated cultural sensitivity filters and auditing mechanisms [79–81]. These systems 
are engineered to detect and flag potentially insensitive or appropriative content before it reaches the public. The 
adoption  of  human-in-the-loop  review  processes,  particularly  in  commercial  advertising  workflows,  further 
reinforces  cultural  respect  and  helps  ensure  that  AI-generated  content  honors  traditional  elements  without 
distortion or misrepresentation. By embedding these safeguards into both the development and deployment stages, 
organizations are working to minimize the risk of cultural misuse. Besides, both academia and industry are actively 
pursuing technical and policy-oriented strategies to strengthen the regulatory landscape of AIGC.

Explainable and Auditable AI. There is a growing emphasis on the development of explainable AI (XAI) [82–85] 
and content auditing tools, which facilitate transparency and accountability. These technologies enable stakeholders to 
trace  how  specific  pieces  of  content  are  generated  and  to  assess  whether  they  comply  with  copyright  and  cultural 
standards. In addition, innovative approaches such as embedding provenance metadata and leveraging blockchain for 
immutable copyright records are being explored to reinforce trust and traceability in AIGC.

Bias and Misuse Detection. Considerable attention is also being given to the creation of automated methods for 
detecting and mitigating both bias and misuse, including copyright violations and cultural appropriation [86–88]. This 
research spans interventions at both the dataset level—such as advanced filtering and rebalancing strategies—and at 
the output level, where real-time content moderation can help prevent the dissemination of problematic content.

Ethical Frameworks. Finally, interdisciplinary collaborations are yielding new ethical frameworks that merge 
legal,  ethical,  and  technical  considerations  [89].  These  comprehensive  frameworks  are designed  to  ensure  that 
innovation  in  generative  AI  proceeds  in  tandem  with  responsible  content  creation,  particularly  in  commercial 
contexts  where  the  impact  of  misuse  can  be  significant.  The  overarching  goal  is  to  strike  a  balance  between 
technological advancement and the protection of intellectual property and cultural heritage.

4.5. Future Prospects and Challenges

Recently, in an interview, ZeroOne Data Science CEO Feng Jian mentioned that designer teams are the first 
to  benefit  from  AIGC  software.  After  introducing  AIGC,  the  workload  that  previously  required  at  least  five 
designers a week to complete can now be finished in two to three days. Furthermore, AIGC can create virtual hosts 
or presenters for advertising in the near future, providing immersive experiences and increasing user interaction. 
AI-automated content generation drastically reduces the technical time required for ad creation. AIGC can also 
quickly optimize and adjust ad content based on creator feedback. By using AIGC for ad creation, not only is time

https://doi.org/10.53941/tai.2025.100009

147

---

<!-- PAGE 10 -->

Yang et al.

Trans. Artif. Intell. 2025, 1(1), 139–152

saved,  but  ad  creators  can  focus  on  creative  ideas  and  content  exploration,  producing  more  impactful  and 
influential ads. However, despite the immense potential and advantages of AIGC, its output heavily depends on 
human-provided data resources, which can lead to training defects and copyright infringement risks [86]. AI may 
fabricate information when dealing with complex issues, leading to the misuse of cultural elements, damaging the 
essence  of  ads,  and  harming  the  brand  image.  Additionally,  AI  has  a  probability  of  generating  seemingly 
reasonable but incorrect answers when handling complex, ambiguous, or open-ended questions. When ad creators 
use AI to handle related creative content, if they fail to detect errors in cultural element stitching, misinterpretation 
of cultural customs, or inappropriate handling of sensitive culture, it could lead to the misuse of traditional elements 
due to the limitations of AIGC [90]. Such misuse could not only destroy the cultural essence of the ad but also 
cause irreparable damage to the brand image. In conclusion, with the continuous development of AIGC technology, 
its application in advertising shows tremendous potential and advantages. Although there are data dependency and 
potential copyright issues, by exploring more reasonable usage methods and establishing appropriate regulatory 
mechanisms [91], AIGC is expected to further drive breakthroughs and transformations in ad production on the 
existing foundation, continually optimizing its application effects.

5. Conclusions

The  emerging  utilization  of  AI  in  FinTech  has  progressed  beyond  experimental  prototypes  to  become 
indispensable across the financial value chain. Recommendation systems, under-pinned by SSL to mitigate data 
sparsity, have emerged as pivotal instruments for enhancing personalized marketing and recommendation accuracy. 
LLMs, leveraged through advanced prompt engineering, have facilitated accessibility to sophisticated risk analysis 
for SMEs, enabling accelerated and more transparent financial decision-making. Similarly, AIGC has transformed 
advertising  workflows,  offering  cost-efficient  and  scalable  content  generation,  albeit  concurrently  highlighting 
significant governance and ethical considerations.

Nevertheless, critical challenges necessitate resolution to ensure the sustainable advancement of AI in FinTech. 
Robust frameworks are imperative to reconcile data privacy imperatives with innovation requirements. Algorithmic 
transparency  and  interpretability  remain  paramount  for  fostering  trust  in  AI-driven  decisions,  particularly  within 
regulated financial contexts. Regarding AIGC, issues pertaining to copyright infringement, cultural misappropriation, 
and content authenticity demand systematic governance structures and technical safeguards.

Future research and development should prioritize human-centric, scalable solutions in ethical principles and 
regulatory  compliance.  Key  directions  include  enhancing  the  crossdomain  transferability  of  SSL  models, 
improving the contextual reasoning capabilities of LLMs in complex risk scenarios, and developing generative 
models intrinsically aligned with diverse cultural and legal frameworks. Through interdisciplinary collaboration 
and  the  adoption  of  rigorous evaluation  standards,  the  FinTech  sector  can  realize  the  potential  of  AI  to  foster 
inclusive, efficient, and trustworthy financial services.

Author Contributions

R.Y.: Conceptualization, investigation, writing, and revision. Y.W.: Conceptualization, investigation, writing, 
and revision. Y.L.: Conceptualization, investigation, writing, and revision. Z.Y.: Conceptualization, investigation, 
writing,  and  revision.  Z.Z.:  Conceptualization,  investigation,  writing,  and  revision.  D.W.:  Conceptualization, 
investigation, writing, and revision. All authors have read and agreed to the published version of the manuscript.

Funding

This work is supported in part by the InnoHK Initiative, in part by the Government of the HKSAR, and in

part by the Laboratory for AI-Powered Financial Technologies.

Conflicts of Interest

The  authors  declare  no  conflict  of  interest.  Given  the  role  as  Editor-in-Chief,  Dapeng  Oliver  Wu  had  no 
involvement in the peer review of this paper and had no access to information regarding its peer-review process. 
Full responsibility for the editorial process of this paper was delegated to another editor of the journal.

References

1. 
Cao, L.; Yang, Q.; Yu, P.S. Data science and ai in fintech: An overview. Int. J. Data Sci. Anal. 2021, 12, 81–99. 
2.  Ashta,  A.;  Herrmann,  H.  Artificial  intelligence  and  fintech:  An  overview  of  opportunities  and  risks  for  banking,

investments, and microfinance. Strateg. Chang. 2021, 30, 211–222. 
Cao, L.; Yuan, G.; Leung, T.; et al. Special issue on ai and fintech: The challenge ahead. IEEE Intell. Syst. 2020, 35, 3–6.

3.

https://doi.org/10.53941/tai.2025.100009

148

---

<!-- PAGE 11 -->

Yang et al.

Trans. Artif. Intell. 2025, 1(1), 139–152

4.

Belanche, D.; Casalo, L.V.; Flavia, C. Artificial intelligence in fintech: Understanding robo-advisors adoption among 
customers. Ind. Manag. Data Syst. 2019, 119, 1411–1430.

5.  Kamuangu, P.K. Advancements of ai and machine learning in fintech industry (2016–2020). J. Econ. Financ. Account.

6.

7.

8.

9.

Stud. 2024, 6, 23–31. 
Ricci, F.; Rokach, L.; Shapira, B. Introduction to recommender systems handbook. In Recommender Systems Handbook; 
Springer: Berlin/Heidelberg, Germany, 2011; pp. 1–35. 
Covington, P.; Adams, J.; Sargin, E. Deep neural networks for youtube recommendations. In Proceedings of the 10th 
ACM Conference on Recommender Systems, Boston, MA, USA, 15–19 September 2016; pp. 191–198. 
Cheng, H.-T.; Koc, L.; Harmsen, J.; et al. Wide & deep learning for recommender systems. In Proceedings of the 1st 
Workshop on Deep Learning for Recommender Systems, Boston, MA, USA, 15 September 2016; pp. 7–10. 
Zhou, G.; Zhu, X.; Song, C.; et al. Deep interest network for click-through rate prediction. In Proceedings of the 24th 
ACM SIGKDD International Conference on Knowledge Discovery & Data Mining, London UK, 19–23 August 2018; 
pp. 1059–1068.

10.  Chen,  T.;  Yin,  H.;  Ye,  G.;  et  al.  Try  this  instead:  Personalized  and  interpretable  substitute  recommendation.  In 
Proceedings of the 43rd International ACM SIGIR Conference on Research and Development in Information Retrieval, 
Virtual, 25–30 July 2020; pp. 891–900.

11.  Yin,  H.;  Cui,  B.;  Huang,  Z.;  et  al.  Joint  modeling  of  users’  interests  and  mobility  patterns  for  point-of-interest 
recommendation. In Proceedings of the 23rd ACM International Conference on Multimedia, Brisbane, Australia, 26–30 
October 2015; pp. 819–822.

12.  Sarwar,  B.M.  Sparsity,  Scalability  and  Distribution  in  Recommender  Systems.  Ph.D.  Dissertation,  University  of

Minnesota, Minneapolis, MN, USA, 2001.

13.  Zhang, S.;  Yao, L.;  Sun,  A.;  et  al.  Deep learning-based  recommender  system:  A  survey  and new perspectives.  ACM

Comput. Surv. 2019, 52, 1–38.

14.  Yu, J.; Yin, H.; Xia, X.; et al. Self-supervised learning for recommender systems: A survey. IEEE Trans. Knowl. Data

Eng. 2023, 36, 335–355.

15.  Hinton, G.E.; Salakhutdinov, R.R. Reducing the dimensionality of data with neural networks. Science 2006, 313, 504–507. 
16.  Vincent, Y.B.P.; Larochelle, H.; Manzagol, P.-A. Extracting and composing robust features with denoising autoencoders. 
In Proceedings of the International Conference on Machine Learning, Helsinki, Finland, 5–9 July 2008; pp. 1096–1103. 
17.  Ericsson, H.G.L.; Hospedales, T.M. How well do selfsupervised models transfer? In Proceedings of the IEEE Conference

on Computer Vision and Pattern Recognition, Nashville, TN, USA, 20–25 June 2021; pp. 5414–5423.

18.  Liu, X.; Zhang, F.; Hou, Z.; et al. Self-supervised learning: Generative or contrastive. IEEE Trans. Knowl. Data Eng.

2023, 35, 857–876.

19.  Wu,  Y.;  DuBois,  C.;  Zheng,  A.X.;  et  al.  Collaborative  denoising  auto-encoders  for  top-n  recommender  systems.  In 
Proceedings of the Ninth ACM International Conference on Web Search and Data Mining, San Francisco, CA, USA,   
22–25 February 2016; pp. 153–162.

20.  Pinto, L.; Gupta, A. Supersizing self-supervision: Learning to grasp from 50k tries and 700 robot hours. In Proceedings of

the IEEE International Conference on Robotics and Automation, Stockholm, Sweden, 16–21 May 2016; pp. 3406–3413.

21.  Li, J.M.R.Y.; Paluri, M.; Dolla, P. Unsupervised learning of edges. In Proceedings of the IEEE Conference on Computer

Vision and Pattern Recognition, Las Vegas, NV, USA, 27–30 June 2016; pp. 1619–1627.

22.  Lee, S.J.H.H.; Shin, J. Rethinking data augmentation: Selfsupervision and self-distillation. arXiv 2019, arXiv:1910.05872. 
23.  Zoph,  B.;  Ghiasi,  G.;  Lin,  T.Y.;  et  al.  Rethinking  pre-training  and  self-training.  In  Proceedings  of  the  International 
Conference on Neural Information Processing Systems, Vancouver, BC, Canada, 6–12 December 2020; pp. 3833–3845. 
24.  Mitrovic,  J.;  McWilliams,  B.;  Walker,  L.B.J.;  et  al.  Representation  learning  via  invariant  causal  mechanisms.  In

Proceedings of the International Conference on Learning Representations, Virtual, 3–7 May 2021; pp. 1–19.

25.  Hua,  T.;  Wang,  W.;  Xue,  Z.;  et  al.  On  feature  decorrelation  in  self-supervised  learning.  In  Proceedings  of  the  IEEE

International Conference on Computer Vision, Montreal, BC, Canada, 11–17 October 2021; pp. 9598–9608.

26.  Alam, M.A.; Mahatab, G.; Sarna, S.A. Enhancing regulatory frameworks to prevent financial crises. Am. J. Econ. Bus.

Manag. 2025, 8, 1351–1359.

27.  Horobets, N.; Reznik, O.; Maliyk, V.; et al. Artificial intelligence technologies in banking: Challenges and opportunities 
for anti-money laundering in the context of eu regulatory initiatives. J. Money Laund. Control. 2025, 28, 210–225. 
28.  Penikas, H. Review of bank of russia-nes workshop: Identification and measurement of macroprudential policies effects.

Russ. J. Money Financ. 2021, 80, 94–104.

29.  Uch, R.; Miyamoto, H.; Kakinaka, M. Effects of a banking crisis on credit growth in developing countries. Financ. Res.

Lett. 2021, 43, 102004.

30.  Li, Y.-M.; Lin, L.-F.; Hsieh, C.-Y.; et al. A social investing approach for portfolio recommendation. Inf. Manag. 2021,

58, 103536.

https://doi.org/10.53941/tai.2025.100009

149

---

<!-- PAGE 12 -->

Yang et al.

Trans. Artif. Intell. 2025, 1(1), 139–152

31.  Song,  Y.;  Sun,  C.;  Peng,  Y.;  et  al.  Research  on  multidimensional  trust  evaluation  mechanism  of  fintech  based  on

blockchain. IEEE Access 2022, 10, 57025–57036.

32.  Cheng, X.; Guo, F.; Chen, J. et al. Exploring the trust influencing mechanism of robo-advisor service: A mixed-method

approach. Sustainability 2022, 14, 5284.

33.  Ru, A.; Berger, B.; Hess, T. The ambivalent effect of transparency on trust in robo-advisors: An experimental investigation. 
In Proceedings of the 24th Pacific Asia Conference on Information Systems (PACIS 2021), Virtual, 12–14 July 2021. 
34.  Li, T.; Song, J. Deep learning-powered financial product recommendation system in banks: Integration of transformer

and transfer learning. J. Organ. End User Comput. 2024, 36, 1–29.

35.  Zhang, L.; Wu, X.; Zhao, H.; et al. Personalized recommendation in P2P lending based on risk-return management: A

multi-objective perspective. IEEE Trans. Big Data 2022, 8, 1141–1154.

36.  Soleymani,  F.;  Paquet,  E.  Deep  graph  convolutional  reinforcement  learning  for  financial  portfolio  management—

DeepPocket. Expert Syst. Appl. 2021, 185, 115127.

37.  Wu,  L.;  Zhang,  J.  Continuous  control  with  stacked  deep  dynamic  recurrent  reinforcement  learning  for  portfolio

optimization. Expert Syst. Appl. 2021, 165, 113891.

38.  Yu, C.; Liu, Y. A personalized mean-CVaR portfolio optimization model for individual investment. Math. Probl. Eng.

2021, 2021, 8863597.

39.  Club, E. O Recomendador de Produtos Que Sabe Exatamente Como o Pequeno Varejo Pode Vender Mais. September 
2022. Available online: https://ciandt.com/br/pt-br/in-the-news/recomendador-de-produtos-que-sabe-exatamente-como-
o-pequeno-varejo-pode-vender-mais (accessed on 22 April 2025).

40.  Alison,  T.  The  Future  of  Facebook.  May  2024.  Available  online:  https://about.fb.com/news/2024/05/the-future-of-

facebook/ (accessed on 22 April 2025).

41.  Wang, G.; Cao, L.; Zhao, H.; et al. Coupling macro-sector-micro financial indicators for learning stock representations 
with less uncertainty. In Proceedings of the AAAI Conference on Artificial Intelligence, Virtual, 2–9 February 2021;   
pp. 4418–4426.

42.  Du, X.; Tanaka-Ishii, K. Stock embeddings acquired from news articles and price history, and an application to portfolio 
optimization.  In  Proceedings  of  the  58th  Annual  Meeting  of  the  Association  for  Computational  Linguistics,  Virtual,   
5–10 July 2020; pp. 3353–3363.

43.  Liu, Q.; Cheng, X.; Su, S.; et al. Hierarchical complementary attention network for predicting stock price movements 
with news. In Proceedings of the 27th International Conference on Information and Knowledge Management, Turin, Italy, 
22–26 October 2018; pp. 1603–1606.

44.  Hu, Z.; Lu, W.; Bian, J.; et al. Listening to chaotic whispers: A deep learning framework for news-oriented stock trend 
prediction. In Proceedings of the Eleventh ACM International Conference on Web Search and Data Mining, Los Angeles, 
CA, USA, 5–9 February 2018; pp. 261–269.

45.  Si, J.; Mukherjee, A.; Liu, B.; et al. Exploiting topic based twitter sentiment for stock prediction. In Proceedings of the

51st Annual Meeting of the Association for Computational Linguistics, Sofia, Bulgaria, 4–9 August 2013; pp. 24–29.

46.  Luo, Y.; Zheng, J.; Yang, Z.; et al. Pleno-alignment framework for stock trend prediction. IEEE Trans. Neural Netw.

Learn. Syst. 2025, early access.

47.  Liu, J.; Lin, H.; Liu, X.; et al. Transformer-based capsule network for stock movement prediction. In Proceedings of the First 
Workshop on Financial Technology and Natural Language Processing, Macao, China, 10–12 August 2019; pp. 66–73. 
48.  Wang, Z.; Zhang, X.; Du, H. Mutual information guided financial report generation with domain adaption. IEEE Trans.

Emerg. Top. Comput. Intell. 2024, 8, 627–640.

49.  Niu, H.; Xiong, Y.; Wang, X.; et al. KeFVP: Knowledge-enhanced financial volatility prediction. Find. Assoc. Comput.

Linguist. 2023, 2023, 11499–11513.

50.  Yi,  Y.;  Uy,  M.C.S.;  Huang,  A.  Finbert:  A  pretrained  language  model  for  financial  communications.  arXiv  2020,

arXiv:2006.08097.

51.  Xie, Q.; Han, W.H.; Zhang, X.; et al. Pixiu: A comprehensive benchmark, instruction dataset and large language model

for finance. Adv. Neural Inf. Process. Syst. 2023, 36, 33469–33484.

52.  Bussmann, N.; Giudici, P.; Marinelli, D.; et al. Explainable ai in fintech risk management. Front. Artif. Intell. 2020, 3, 26. 
53.  Wang, C.; Luo, B. Predicting $GME stock price movement using sentiment from Reddit r/wallstreetbets. In Proceedings 
of the Third Workshop on Financial Technology and Natural Language Processing, Online, 19 August 2021; pp. 22–30. 
54.  Ding, X.; Zhang, Y.; Liu, T.; et al. Using structured events to predict stock price movement: An empirical investigation. 
In  Proceedings  of  the  2014  Conference  on  Empirical  Methods  in  Natural  Language  Processing,  Doha,  Qatar,  25–29 
October 2014; pp. 1415–1425.

55.  Ding, X.; Zhang, Y.; Liu, T.; et al. Knowledge-driven event embedding for stock prediction. In Proceedings of Coling 2016, 
the 26th International Conference on Computational Linguistics, Osaka, Japan, 11–16 December 2016; pp. 2133–2142.

https://doi.org/10.53941/tai.2025.100009

150

---

<!-- PAGE 13 -->

Yang et al.

Trans. Artif. Intell. 2025, 1(1), 139–152

56.  Nguyen,  T.H.;  Shirai,  K.  Topic  modeling  based  sentiment  analysis  on  social  media  for  stock  market  prediction.  In 
Proceedings of the 53rd Annual Meeting of the Association for Computational Linguistics and the 7th International Joint 
Conference on Natural Language Processing, Beijing, China, 26–31 July 2015; pp. 1354–1364.

57.  Ang, G.; Lim, E.-P. Guided attention multimodal multitask financial forecasting with inter-company relationships and 
global and local news. In Proceedings of the 60th Annual Meeting of the Association for Computational Linguistics, 
Dublin, Ireland, 22–27 May 2022; pp. 6313–6326.

58.  Yu, X.; Chen, Z.; Ling, Y.; et al. Temporal data meets llm—explainable financial time series forecasting. arXiv 2023,

arXiv:2306.11025.

59.  Xie,  Q.;  Han,  W.;  Lai,  Y.;  et  al.  The  wall  street  neophyte:  A  zero-shot  analysis  of  chatgpt  over  multimodal  stock

60.

movement prediction challenges. arXiv 2023, arXiv:2304.05351. 
Jiang, Y.; Pan, Z.; Zhang, X.; et al. Empowering time series analysis with large language models: A survey. arXiv 2024, 
arXiv:2402.0318.

61.  Cao, Y.; Li, S.; Liu, Y.; et al. A comprehensive survey of aigenerated content (aigc): A history of generative ai from gan

to chatgpt. arXiv 2023, arXiv:2303.04226.

62.  Zhang, L.; Rao, A.; Agrawala, M. Adding conditional control to text-to-image diffusion models. In Proceedings of the

IEEE/CVF International Conference on Computer Vision, Paris, France, 2–6 October 2023.

63.  Li, M.; Yang, T.; Kuang, H.; et al. Controlnet++: Improving conditional controls with efficient consistency feedback. In

Computer Vision—ECCV 2024; Springer: Cham, Switzerland, 2024; pp. 129–147.

64.  Zhang, Z.; Zhang, Q.; Li, G.; et al. Dyartbank: Diverse artistic style transfer via pre-trained stable diffusion and dynamic

style prompt artbank. Knowl. Based Syst. 2025, 310, 112959.

65.  Zhang, Z.; Li, Y.; Xia, R.; et al. Lgast: Towards high-quality arbitrary style transfer with local–global style learning.

Neurocomputing 2025, 623, 129434.

66.  Zhang, Z.; Zhang, Q.; Luan, J.; et al. Vectorsketcher: Learning to create a vector-based free-hand sketch. Eng. Appl. Artif.

Intell. 2025, 156, 111005.

67.  Roumeliotis, K.I.; Tselikas, N.D. Chatgpt and open-ai models: A preliminary review. Future Internet 2023, 15, 192. 
68.  Ramesh, A.; Pavlov, M.; Goh, G.; et al. Zero-shot text-to-image generation. In Proceedings of the 38th International

Conference on Machine Learning, Virtual, 18–24 July 2021; pp. 8821–8831.

69.  Haleem, A.; Javaid, M.; Qadri, M.A.; et al. Artificial intelligence (ai) applications for marketing: A literature-based study.

Int. J. Intell. Netw. 2022, 3, 119–132.

70.  Qin, X.; Jiang, Z. The impact of ai on the advertising process: The Chinese experience. J. Advert. 2019, 48, 338–346. 
71.  Huh, J.; Nelson, M.R.; Russell, C.A. Chatgpt, ai advertising, and advertising research and education. J. Advert. 2023, 52,

477–482.

72.  Ford, J.; Jain, V.; Wadhwani, K.; et al. Ai advertising: An overview and guidelines. J. Bus. Res. 2023, 166, 114124. 
73.  Wu, J.; Gan, W.; Chen, Z.; et al. Ai-generated content (aigc): A survey. arXiv 2023, arXiv:2304.06632. 
74.  Rombach,  R.;  Blattmann,  A.;  Lorenz,  D.;  et  al.  High-resolution  image  synthesis  with  latent  diffusion  models.  In 
Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition, New Orleans, LA, USA, 18–24 
June 2022; pp. 10684–10695.

75.  Zhang, Z.; Zhang, Q.; Lin, H.; et al. Towards highly realistic artistic style transfer via stable diffusion with step-aware 
and layer-aware prompt. In Proceedings of the Thirty-Third International Joint Conference on Artificial Intelligence, Jeju, 
Republic of Korea, 3–9 August 2024; pp. 7814–7822.

76.  Zhang, Z.; Zhang, Q.; Xing, W.; et al. Artbank: Artistic style transfer with pre-trained diffusion model and implicit style prompt 
bank. In Proceedings of the AAAI Conference on Artificial Intelligence, Vancouver, BC, Canada, 20–27 February 2024. 
77.  Li, Z.; Zhang, W.; Zhang, H.; et al. Global digital compact: A mechanism for the governance of online discriminatory

and misleading content generation. Int. J. Hum. Comput. Interact. 2025, 41, 1381–1396.

78.  Dzuong, J.; Wang, Z.; Zhang, W. Uncertain boundaries: Multidisciplinary approaches to copyright issues in generative

ai. arXiv 2024, arXiv:2404.08221.

79.  Balasubramaniam, S.; Chirchi, V.; Kadry, S.; et al. The road ahead: Emerging trends, unresolved issues, and concluding

remarks in generative ai—A comprehensive review. Int. J. Intell. Syst. 2024, 2024, 4013195.

80.  Chen,  H.;  Chan-Olmsted,  S.;  Thai,  M.  Culture  sensitivity  and  information  access:  A  qualitative  study  among  ethnic

groups. Qual. Rep. 28, 2504–2522, 2023.

81.  Wang, Y.; Zheng, J.; Zhang, C.; et al. Dualnet: Robust self-supervised stereo matching with pseudo-label supervision. In

Proceedings of the AAAI Conference on Artificial Intelligence, Philadelphia, PA, USA, 25 February–4 March 2025.

82.  Dwivedi, R.; Dave, D.; Naik, H.; et al. Explainable ai (xai): Core ideas, techniques, and solutions. ACM Comput. Surv.

2023, 55, 1–33.

83.  Wang,  Y.;  Wang,  L.;  Li,  K.;  et  al.  Cost  volume  aggregation  in  stereo  matching  revisited:  A  disparity  classification

perspective. IEEE Trans. Image Process. 2024, 33, 6425–6438.

https://doi.org/10.53941/tai.2025.100009

151

---

<!-- PAGE 14 -->

Yang et al.

Trans. Artif. Intell. 2025, 1(1), 139–152

84.  Das,  A.;  Rad,  P.  Opportunities  and  challenges  in  explainable  artificial  intelligence  (xai):  A  survey.  arXiv  2020,

arXiv:2006.11371.

85.  Arrieta, A.B.; Herrera, F.; Chatilaf, R.; et al. Explainable artificial intelligence (xai): Concepts, taxonomies, opportunities

and challenges toward responsible AI. Inf. Fusion 2019, 58, 82–115.

86.  Wang, T.; Zhang, Y.; Qi, S.; et al. Security and privacy on generative data in aigc: A survey. ACM Comput. Surv. 2024,

57, 1–34.

87.  Lucchi, N. Chatgpt: A case study on copyright challenges for generative artificial intelligence systems. Eur. J. Risk Regul.

2024, 15, 602–624.

88.  Verma, A. The copyright problem with emerging generative ai. J. Intell. Prot. Stud. 2023, 7, 69. 
89.  Wang, Z.; Shen, L.; Kuang, E.; et al. Exploring the impact of artificial intelligence-generated content (aigc) tools on 
social  dynamics  in  ux  collaboration.  In  Proceedings  of  the  2024  ACM  Designing  Interactive  Systems  Conference, 
Copenhagen, Denmark, 1–5 July 2024.

90.  Baidoo-Anu, D.; Ansah, L.O. Education in the era of generative artificial intelligence (AI): Understanding the potential

benefits of chatgpt in promoting teaching and learning. J. AI 2023, 7, 52–62.

91.  Franks, E.; Lee, B.; Xu, H. Report: China’s new ai regulations. Glob. Priv. Law Rev. 2024, 5, 43–49.

https://doi.org/10.53941/tai.2025.100009

152

<!-- MARKITDOWN CONVERSION -->

<!-- Full MarkItDown conversion for formatting fidelity. -->

Transactions on Artificial Intelligence

https://www.sciltp.com/journals/tai

Review
Recent Advances in Artificial Intelligence for Management
and Financial Technology

Renwei Yang 1,†, Yun Wang 1,†, Yongcan Luo 1,†, Zhengjie Yang 1,2,*, Zhimin Zong 3
and Dapeng Oliver Wu 1

1  Department of Computer Science, City University of Hong Kong, Hong Kong
2  Hong Kong Generative AI Research and Development Center, The Hong Kong University of Science and Technology,

Hong Kong

3  Department of Electrical & Computer Engineering, University of Florida, Gainesville, FL 32611, USA
*  Correspondence: zhengjie.yang@sydney.edu.au
†  These authors contributed equally to this work.

How To Cite: Yang, R.; Wang, Y.; Luo, Y.; et al. Recent Advances in Artificial Intelligence for Management and Financial Technology.
Transactions on Artificial Intelligence 2025, 1(1), 139–152. https://doi.org/10.53941/tai.2025.100009.

Received: 11 June 2025

Revised: 22 July 2025

Accepted: 28 July 2025
Published: 6 August 2025

Abstract:  In  this  survey,  we  examine  contemporary  advancements  in  Artificial
Intelligence (AI) applications for Financial Technology (FinTech), with a specific
focus on three rapidly evolving domains: recommendation systems, risk analysis,
and AI-generated commercial content (AIGC). For recommendation systems, self-
supervised learning and graph neural network methodologies facilitate  real-time,
hyper-personalized financial product suggestions, optimizing the balance between
conversion  efficacy  and  regulatory  adherence.  For  risk  analysis,  large  language
models,  including  GPT-4  and  Llama  3,  enhanced  through  sophisticated  prompt
engineering techniques, have significantly transformed credit assessment and stress
testing processes for small and medium-sized enterprises, reducing analytical cycles
from  weeks  to  minutes.  Concurrently,  multimodal  generative  models,  such  as
DALL-E  3,  are  revolutionizing  advertising  through  the  automated  generation  of
compliant and engaging content across textual, visual, and video formats, markedly
compressing production timelines. The survey further critically addresses persistent
challenges, encompassing data privacy, algorithmic transparency, and cultural bias
within  AIGC,  while  delineating  future  research  trajectories  for  developing
trustworthy and scalable AI solutions in FinTech.

Keywords: Artificial Intelligence; Financial Technology; large language models

1. Introduction

Over  the  last  decade,  the  fusion  of  Artificial  Intelligence  (AI)  and  Financial  Technology  (FinTech)  has
progressed from proof-of-concept prototypes to mission-critical production systems. Fueled by the unprecedented
growth of digital data, inexpensive cloud computing, and breakthroughs in deep learning, AI now permeates almost
every layer of the financial value chain from front-office customer engagement to back-office risk management
and compliance.

Yet, despite enthusiastic adoption, the practical impact of AI is still uneven. Financial institutions grapple
with  highly  regulated  environments,  severe  class-imbalance  problems,  extreme  tail  risks,  and  rapidly  shifting
consumer preferences, all of which  challenge the direct transplantation of generic AI techniques developed for
other industries. Consequently, domain-specific innovation and rigorous evaluation remain essential. This survey
aims to provide a concise, up-to-date overview of three rapidly evolving application areas that, in our view, have
recently achieved the largest leap forward and the widest commercial uptake. Specifically, recent breakthroughs
in  representation  learning,  graph  neural  networks,  and  reinforcement  learning  are  empowering  AI-driven
recommendation systems to deliver real-time, hyper-personalized product suggestions that boost conversion rates

Copyright:  ©  2025  by  the  authors. This is  an open  access  article  under the terms  and  conditions  of the  Creative Commons
Attribution (CC BY) license (https://creativecommons.org/licenses/by/4.0/).
Publisher’s Note: Scilight stays neutral with regard to jurisdictional claims in published maps and institutional affiliations.

Yang et al.

Trans. Artif. Intell. 2025, 1(1), 139–152

while meeting strict suitability and fairness regulations. Simultaneously, prompt-based large language models such
as  GPT-4  and  Llama  3  (steered  through  meticulous  prompt  engineering)  are  revolutionizing  risk  analysis  by
automating  credit  assessment,  scenario  generation,  stress  testing,  and  early-warning  detection,  compressing
analytic cycles from weeks to minutes; and, in parallel, multimodal generative models are ushering in an era of
AI-generated commercial advertising capable of producing compliant, captivating marketing assets across text,
image, and video formats, dramatically reducing production timelines and enabling rapid A/B experimentation for
financial products.

Most existing surveys provide broad overviews of AI applications in FinTech, focusing on areas such as
smart finance, risk, and customer adoption [1–5]. In contrast, our work offers a focused and up-to-date review of
three  emerging  directions:  self-supervised  and  graph-based  recommendation  systems,  large  language  model-
driven  risk  analysis,  and  AI-generated  commercial  content,  with  particular  attention  to  their  recent  technical
advances and practical challenges.

The remainder of this survey is organized as follows. Section 2 reviews recent advances in recommendation
algorithms  tailored  for  financial  products  and  omni-channel  marketing.  Section  3  discusses  how  prompt
engineering and large language models reshape contemporary risk analysis workflows for Small and Medium-
sized  Enterprises  (SMEs).  Section  4  surveys  the  emerging  field  of  AI-generated  commercial  advertising,
highlighting design patterns, governance considerations, and empirical performance. Finally, we conclude with
open research challenges and future directions for trustworthy, scalable, and human-centric AI in FinTech.

2. AI in Recommendation Systems for Financial Marketing

With the advent of the digital age, marketing faces unprecedented opportunities and challenges. In the context
of massive data and intense competition, how to accurately reach target customers and provide personalized service
experiences  has  become  the  key  to  success  for  enterprises.  The  rapid  development  of  AI  technology  offers  a
solution to this problem. Specifically, AI-driven personalized recommendation systems are revolutionizing the
landscape of marketing, bringing significant competitive advantages to businesses. By analyzing user behavior,
preferences,  and  historical  data,  AI  generates  personalized  recommendations  in  real-time,  enhancing  user
experience and conversion rates. Machine learning algorithms continuously optimize recommendation models to
ensure their relevance and accuracy, enabling businesses to utilize resources more effectively and maximize profits.
The importance of AI in personalized recommendations cannot be overlooked. In today’s era of burgeoning deep
learning, companies that embrace AI technology will stand out in the competition. In the following, we will explore
AI-based  personalized  recommendation  technology  from  four  perspectives:  working  principles,  advantages,
application cases, and future prospects.

2.1. Related Works

Recommendation systems have become a vital tool for discovering users’ interests, enhancing user experience,
and driving revenue in various e-commerce platforms [6]. Modern recommendation systems, powered by advanced
deep neural network architectures, have achieved remarkable success. For instance, Covington et al. [7] introduce
deep neural networks for YouTube recommendations, Cheng et al. [8] propose the Wide & Deep Learning framework
to balance recommendation precision and generalization, and Zhou et al. [9] develop the Deep Interest Network (DIN)
for  click-through  rate  prediction.  Other  innovations  include  the  personalized  and  interpretable  substitute
recommendation model by Chen et al. [10] and the joint modeling of users’ interests and mobility patterns in point-
of-interest recommendations by Yin et al. [11].

Despite these innovations, deep recommendation models are inherently data-hungry and face challenges due
to  data  sparsity,  as  most  users  interact  with  only  a  small  subset  of  available  items  [12].  This  sparsity  issue
significantly limits the performance of deep learning-based recommendation systems, as highlighted in the survey
by Zhang et al. [13].

To address this challenge, Self-supervised Learning (SSL) [14] has emerged as a promising solution. Early
works  explored  dimensionality  reduction  techniques  using  neural  networks  [15]  and  robust  feature  extraction
through denoising autoencoders [16]. Several studies have investigated its transferability to downstream tasks [17],
and  the  distinction  between  generative  and  contrastive  approaches  [18].  Wu  et  al.  [19]  propose  collaborative
denoising autoencoders, which use corrupted input data to reconstruct the original input, effectively preventing
overfitting and setting the foundation for subsequent advancements in self-supervised recommendation techniques.
Additionally,  research  has  focused  on  large-scale  SSL  experiments  [20],  as  well  as  unsupervised  edge
learning [21]. Other studies have revisited the role of data augmentation [22] and improved pre-training and self-
training techniques [23]. More recent works address representation learning via invariant causal mechanisms [24]

https://doi.org/10.53941/tai.2025.100009

140

Yang et al.

Trans. Artif. Intell. 2025, 1(1), 139–152

and feature decorrelation in SSL [25]. Liu et al. [18] discuss the potential of SSL in recommendation scenarios,
emphasizing its ability to leverage unlabeled data for learning useful representations. Early prototypes of Self-
supervised Recommendation (SSR) date back to unsupervised methods such as autoencoder-based models.

2.2. Working Principles of Personalized Recommendation Systems

Personalized  recommendation  systems  rely  on  big  data  and  machine  learning  algorithms  to  analyze  user
behavior data, preferences, and historical records, predicting user needs and providing tailored product and service
recommendations.  As  shown  in  Figure  1,  the  primary  working  principles  are  as  follows:  (1)  Data  Collection:
Collect  user  data  through  various  channels  (e.g.,  browsing  history,  purchase  records,  search  keywords,  etc.).
(2) Data Preprocessing: Cleanse, normalize, and preprocess the collected data to ensure its quality and consistency.
(3)  Feature  Extraction:  Use  feature  engineering  techniques  to  extract  useful  features  for  the  recommendation
system from the preprocessed data. (4) Model Training: Train the recommendation model using machine learning
algorithms such as collaborative filtering, matrix factorization, and deep learning. (5) Recommendation Generation:
Generate personalized recommendations in real-time based on the trained model and display them to the user.

Figure 1. Workflow of AI recommendation system.

2.3. Regulatory, Trust, and Risk-Return Considerations

This section further discusses several core financial characteristics of financial AI recommendation systems,
specifically focusing on regulatory restrictions, user trust mechanisms, and the balance between return and risk, as
summarized in Table. 1.

Table 1. Comparison of literature on key financial AI recommendation system themes.

Key Points

Summary of Approaches

Theme

Representative
Literature

Regulatory
Restrictions

[26–29]

User Trust
Mechanisms

[30–34]

Emphasize compliance with
regulations (client suitability,
transparency, and data
protection).

Focus on transparency,
fairness, and explainability to
build trust.

Return and Risk
Balance

[30,35–38]

Aim to maximize returns
while managing risk per
investor preferences.

Algorithms are designed to match
investor profiles, ensure explainability,
and adhere to region-specific
requirements.
Adoption of explainable AI, fairness-
aware models, and usercentered
evaluation to increase user engagement
and trust.
Use of Modern Portfolio Theory, mean-
variance analysis, deep reinforcement
learning, risk-aware optimization, and
hybrid approaches for portfolio
management.

Financial recommendation systems are subject to regulatory restrictions that shape their design and operation
[26–29]. Regulations in various regions require systems to ensure client suitability, transparency, and robust data
protection. These constraints necessitate that algorithms are designed to align recommendations with individual
investor profiles while maintaining compliance.

User trust mechanisms are also essential for widespread adoption and sustained use [30–34]. Factors such as
transparency, fairness, and the explainability of algorithms have a significant influence on user trust. The adoption

https://doi.org/10.53941/tai.2025.100009

141

Yang et al.

Trans. Artif. Intell. 2025, 1(1), 139–152

of explainable AI techniques has been proposed to help users better understand system recommendations, thereby
increasing trust and engagement.

In  addition,  achieving  an  appropriate  balance  between  return  and  risk  remains  a  fundamental  financial
objective [30,35–38]. Financial recommendation systems must consider both maximizing returns and managing
risk  according  to  investors’  preferences.  Classical  approaches  such  as  Modern  Portfolio  Theory  are  frequently
employed,  and  recent  research  incorporates  machine  learning  to  further  optimize  portfolio  allocation  and
risk control.

In summary, regulatory compliance, user trust, and the management of return and risk are all crucial factors

in the development and evaluation of financial AI recommendation systems.

2.4. Advantages of AI-Powered Personalized Recommendation Systems

AI-powered personalized recommendation systems [9–14,17–25] play a crucial role in modern information

technology, with advantages that stand out in several areas.

Precision is one of the major highlights of AI recommendation systems. By analyzing massive amounts of
data, including users’ historical behaviors, browsing records, search habits, and social network interactions, AI
can deeply understand users’ interests and needs. This granular analysis enables the recommendation system to
provide highly relevant content,  far surpassing traditional methods. Traditional recommendations often rely on
simple  rules  or  limited  data,  while  AI  can  integrate  complex,  multi-dimensional  information  to  deliver  more
accurate predictions and recommendations.

Real-time responsiveness is another significant feature of AI recommendation systems. These systems can
instantly respond to changes in user behavior and update recommendations in real-time. For instance, when a user
searches for or consumes new types of content on a platform, the AI system can quickly adjust its recommendation
strategy to ensure the user always receives the most relevant and up-to-date suggestions. This dynamic adjustment
capability not only enhances user experience but also strengthens the platform’s competitiveness.

Scalability demonstrates great flexibility and adaptability in AI recommendation systems. As the scale of
user data grows and algorithms continuously improve, system performance and recommendation quality can keep
improving. Whether for small applications or large platforms, AI systems can operate efficiently and consistently
provide  high-quality  recommendations.  This  scalability  ensures  that  AI  recommendation  systems  can  adapt  to
various application scenarios, from e-commerce platforms to streaming services, maximizing their utility across
different environments.

Enhanced user experience is the most direct advantage of AI recommendation systems. Through personalized
recommendations, users can access content that better aligns with their interests and enjoy a smoother and more
enjoyable experience. This personalized service significantly increases user satisfaction and loyalty, encouraging
users to spend more time on the platform and improving user engagement and activity. This deep user involvement
not only drives growth in the user base but also brings significant commercial value to the platform.

2.5. Application Cases of AI-Powered Personalized Recommendation Systems

Today, AI-powered personalized recommendation systems are widely used by many businesses. Below are

examples from four fields: content platforms, social media, e-commerce platforms, and physical retail.

In  social  media,  platforms  like  Facebook,  Instagram,  and  Weibo  utilize  AI  recommendation  systems  to
deliver personalized content and advertisements, significantly improving user engagement and ad conversion rates.
On  e-commerce  platforms  such  as  Amazon  and  Alibaba,  AI  recommendation  systems  provide  personalized
product recommendations, enhancing purchase rates and average transaction values.

On content platforms like Netflix and YouTube, recommendation systems leverage AI technology to improve
users’ viewing experiences, particularly by using latent semantic models for personalized recommendations, as
shown in Figure 2. The core of latent semantic models lies in their ability to capture the underlying relationships
between users and content. First, the system analyzes a large amount of user behavior data and content features to
generate labels for users and content. These labels may include users’ viewing histories, preferences, and the types
and themes of the content. Subsequently, the system can push content more accurately based on the labels.

Latent semantic model technology employs mathematical methods like matrix factorization to map users and
content  into  an  abstract  “latent  space”.  In  this  space,  user  and  content  features  are  represented  as  vectors.  By
calculating the similarity between these vectors, the system can predict content that users might find interesting.
This method considers not only explicit features but also uncovers users’ hidden preferences, making it widely
applied in recommendation systems.

https://doi.org/10.53941/tai.2025.100009

142

Yang et al.

Trans. Artif. Intell. 2025, 1(1), 139–152

Figure 2. Latent semantic model in recommendation system.

In physical retail environments, AI recommendation systems have demonstrated significant utility. Nestle
provides a clear example of this. They adopted an AI-driven order recommendation system that offers scientific
product suggestions to sales personnel. This system showcases products that perform well in other retail stores and
recommends complementary products to popular items, improving sales combinations. By analyzing purchasing
patterns, similar buying behaviors, and sales history data, Nestle’s system provides precise recommendations.

According  to  data,  Nestle  has  successfully  implemented  this  AI  product  recommendation  system  in  over
100,000 retail stores, effectively improving consumers’ shopping experiences [39]. In the first half of 2022, their
sales revenue increased by 6%. In addition, this system has helped Nestle reduce costs and attract more customers
through digital channels. Larissa Frias, Nestle’s Director of Data Analytics, noted that these experiences provided
valuable references for future collaborations and project implementations, offering confidence and motivation for
the team. This successful case highlights the immense potential of AI in the retail industry and provides valuable
insights for other businesses in their digital transformation and efforts to enhance user experiences.

2.6. Challenges and Future of AI-Powered Personalized Recommendation Systems

Currently,  AI-powered  personalized  recommendation  systems  still  face  several  challenges,  such  as  data
privacy, algorithm transparency, and the cold-start problem. Data privacy involves how to use user data reasonably
while protecting their privacy to prevent leaks or misuse. Algorithm transparency requires systems to explain the
rationale behind recommendations, enhancing user trust, such as by providing reasons to help users understand the
recommendation logic. The cold-start problem refers to how to provide accurate recommendations for new users
or new  items when  there is  a lack  of  historical  data,  which requires  additional methods  to compensate  for  the
data shortage.

Despite these challenges, the industry places great emphasis on the technology of AI-powered personalized
recommendation systems due to their commercial value. For example, Tom Alison, Head of Facebook at Meta,
mentioned  in  his  article  “The  Future  of  Facebook”  [40]  (published  31  May  2024)  that  their  R&D  team  has
conducted  multiple  optimizations  and  upgrades  to  AI  recommendation  systems.  He  also  noted  that  they  are
developing  a  large-scale  AI  recommendation  model  to  support  Meta’s  video  services  and  provide  more
personalized  and  precise  recommendation  experiences.  This  project  has  been  included  in  Meta’s  technology
roadmap and is expected to be realized in the coming years. It is foreseeable that with the continuous development
and deepening of AI technology, AI recommendation systems will become more mature and refined, providing
users with more personalized and valuable experiences and showcasing even broader commercial prospects.

3. Prompt in Risk Analysis for Enterprises

In the modern business environment, Small and Medium-sized Enterprises (SMEs) face various risks, ranging
from  market  fluctuations  and  operational  challenges  to  changes  in  laws  and  regulations,  all  of  which  can
significantly impact their survival and growth. Traditional risk management methods often rely on historical data
and subjective judgment, which are not only time-consuming but also prone to bias. With the advancement of AI
technologies, particularly the emergence of language models such as ChatGPT and Llama, businesses can perform
risk  analysis  more  efficiently.  By  designing  precise  prompts,  these  AI  models  can  provide  deep  insights  and
support, optimizing risk management strategies for enterprises.

https://doi.org/10.53941/tai.2025.100009

143

Yang et al.

3.1. Background

Trans. Artif. Intell. 2025, 1(1), 139–152

Small  and  micro  enterprises  often  face  several  key  challenges  in  risk  management.  First,  the  uncertainty
caused  by  market  fluctuations  significantly  impacts  their  financial  stability.  Unlike  larger  companies,  SMEs
typically lack financial buffers and resources, making them more sensitive to market changes. Moreover, their
vulnerability during economic downturns is more pronounced due to limited financing channels. The globalization
of markets has also led to increased legal and compliance risks, as businesses must navigate constantly evolving
legal  and  regulatory  requirements,  adding  to  their  compliance  burden.  In  supply  chain  management,  high
dependency on specific suppliers makes these enterprises highly susceptible to disruptions, which can severely
affect their operations. Traditional risk management approaches of ten struggle to respond promptly to these issues.
However, the introduction of AI technologies offers new solutions for these enterprises.

From a macroeconomic perspective, SMEs are subject to broader economic indicators such as interest rate
volatility,  inflation,  and  global  economic  cycles,  all  of  which  can  impact  consumer  demand  and  financing
availability. Conversely, from a microeconomic perspective, risks such as internal operational inefficiencies, cost
mismanagement,  or flawed  pricing  strategies  often  arise  from  firm-specific  characteristics.  AI-enabled  prompt
design can assist in identifying both types of risk: macro-level trends via large-scale news and financial reports,
and micro-level insights through analysis of firm operations, supply chain data, or internal narratives.

The  application  of  AI  in  risk  management  has  significantly  grown  in  recent  years.  AI  can  process  vast
amounts of data in real-time, automatically identifying potential risks and greatly reducing the time required for
manual  analysis.  By  employing  machine  learning  techniques,  AI  models  effectively  predict  market  shifts  and
emerging risks, enabling proactive decision-making within businesses. Moreover, AI-driven tools offer optimized
decision support based on analytical outcomes, significantly improving the timeliness and accuracy of enterprise
risk responses.

3.2. Related Works

Recent  advances  in  Natural  Language  Processing  (NLP)  have  made  Large  Language  Models  (LLMs)
indispensable for financial analysis. Their capacity to parse intricate financial disclosures, fuse heterogeneous data
sources, forecast market dynamics, and gauge investor sentiment now underpins many state-of-the-art prediction
systems.  For  instance,  Co-CPC  [41]  explicitly  couples  macro-  and  micro-economic  factors  to  mitigate  the
uncertainty inherent in equity price movements. Complementary lines of work exploit unstructured text from news
outlets [42,43] and Twitter streams [44–46] to distill sentiment signals that anticipate future returns. CapTE [47]
advances this idea by pairing a transformer encoder (which captures deep semantic cues in social media) with a
capsule network for direction-of-movement classification. Beyond prediction, Wang et al. [48] demonstrate how
pre-trained LLMs automate the drafting of corporate financial reports, while Niu et al. [49] fuse knowledge-graph
reasoning  with  LLM  outputs  to  forecast  volatility.  Purpose-built  domain  models  such  as  FinBert  [50]  and
PIXIU [51], trained on large-scale sector-specific corpora, consistently achieve superior price-direction accuracy,
making forecasting performance a benchmark for financial NLP.

Explainable AI (XAI) has also emerged as a critical component of AI-driven financial risk analysis, especially
in regulated domains. For instance, Bussmann et al. [52] demonstrate the use of interpretable machine learning
models in fintech risk management scenarios, such as loan default prediction and fraud detection. Their findings
support the integration of transparency-focused design into AI systems used for financial decision-making.

Parallel research emphasises qualitative insight extraction from narrative data including earnings-call transcripts,
real-time news, and community forums to infer market mood and anticipate price shifts. Wang et al. [53] show that
sentiment signals mined from Wall Street message boards improve return predictions. Ding et al. [54] apply Open
Information Extraction to transform vast web text into structured event records that drive an event-centric prediction
model, and later encode these events as knowledge-graph vectors to embed market context [55]. Nguyen et al. [56]
jointly model latent topics and their polarities via an LDA-inspired framework, while Ang et al. [57] integrate multi-
modal cues and evolving inter-firm relations through attention mechanisms. Collectively, these studies highlight that
richer  qualitative  signals  (when  systematically  structured)  complement  numerical  indicators  and  enhance  the
robustness of stock-trend forecasting.

Several studies have enhanced language models’ capabilities for financial data analysis and stock prediction
by  employing  specialized  prompts  and  Chain  of  Thought  (CoT)  techniques.  Yu  et  al.  [58]  leverage  GPT-4  to
effectively  summarize  weekly  and  monthly  financial  market  news,  construct  detailed  company  profiles  for
enhanced  knowledge  representation,  and  generate  explainable  predictions.  Similarly,  Xie  et  al.  [59]  evaluate
ChatGPT’s  zero-shot  performance  in  multimodal  stock  price  forecasting,  underscoring  the  necessity  for
specialized training or fine-tuning to overcome prediction challenges. Jiang et al. [60] note that despite the inherent

https://doi.org/10.53941/tai.2025.100009

144

Yang et al.

Trans. Artif. Intell. 2025, 1(1), 139–152

potential  of  powerful  language  models  such  as  ChatGPT  in  financial  analysis,  their  direct  application  through
simple  prompts  or  CoT  methods  still  trails  traditional  forecasting  approaches.  This  finding  emphasizes  the
importance of carefully crafted prompts for successful financial prediction tasks.

3.3. Prompt Example

Assume a small or medium-sized manufacturing company is facing financial risks, particularly during times
of economic instability. The company wants to leverage AI technology to analyze and predict future cash flow
risks in order to ensure financial stability. The company primarily relies on multiple suppliers for raw materials
and also faces issues such as delayed customer payments. The financial risks for the company are mainly derived
from three aspects: raw material price fluctuations leading to increased costs, cash flow issues caused by customer
payment delays, and sales risks due to market demand changes. The company seeks to use AI’s predictive analysis
capabilities to better manage these risks.

To  effectively  utilize  AI  models  for  financial  risk  forecasting,  we  need  to  guide  the  model  step  by  step,
focusing on specific risk areas. Using the Chain of Thought (CoT) method, complex financial risk issues can be
broken down into smaller, more manageable problems, gradually guiding the AI to perform in-depth analysis and
reasoning. Here’s an example of a Chain of Thought analysis:

1.

Initial Prompt Design: “Analyze the impact of current economic uncertainty on the financial situation of a
manufacturing company, including risks from raw material price fluctuations, customer payment delays, and
market demand changes.”

2.  Refined Prompt to Focus on Specific Issues: “Assume that raw material prices may rise by 10% over the next
six months. How much will the company’s procurement costs increase, and what procurement strategies can
be adopted to mitigate this impact?”

AI  Analysis  Example  Output:  “If  raw  material  prices  increase  by  10%  procurement  costs  could  rise  by
$100,000. The company can address this by negotiating price locks with suppliers, increasing the proportion of
local suppliers, and stocking up in advance.”

3.  Further Analysis of Cash Flow Risks Due to Customer Payment Delays: “Under future economic uncertainty,
assume  the  payment  cycle  for  major  clients  is  extended  by  30  days.  What  impact  will  this  have  on  the
company’s cash flow? What strategies can be employed to mitigate this cash flow risk?”

AI Analysis Example Output: “An extension of the customer payment cycle by 30 days may lead to a cash
flow shortfall of $50,000. The company could consider strategies such as installment payment plans, implementing
accounts receivable insurance, or offering early payment discounts.”

4.  Comprehensive Analysis of Sales Risks from Market Demand Changes: “Considering potential changes in
market demand, forecast the impact of sales fluctuations over the next six months on cash flow and profits.
How should the company adjust its product mix and pricing strategy to adapt to these changes?”

AI Analysis Example Output: “Based on current market data, sales are predicted to decrease by 15% over
the next six months, resulting in a $150,000 revenue loss. The company can mitigate this by adjusting its product
mix to meet new market demand, optimizing its pricing strategy, and launching promotional campaigns”.

4. AI in Commercial Advertising

As  technology  rapidly  advances,  the  application  of  Artificial  Intelligence  Generated  Content  (AIGC)  [61]  in
advertising is becoming increasingly widespread. AIGC uses AI technology to automatically create text, images, and
videos, offering limitless possibilities for companies’ advertising efforts and setting a new trend in marketing. Moreover,
tools like ControlNet [62–66] and other advanced control methods now allow for fine-grained manipulation of generated
images,  enabling  advertisers  to  specify  structural  or  semantic  constraints  directly  in  the  generation  process.  These
techniques greatly enhance creative flexibility and regulatory compliance, ensuring that visual content aligns with brand
guidelines and cultural sensitivities. Advertising, a highly creative and visually-driven industry, is gradually adopting
AIGC technology to enhance efficiency and precision. This article explores the innovative applications of AIGC in
advertising through examples of AI models like ChatGPT [67] and DALL-E 3 [68] generating ad texts, images, and
videos. Practice has shown that AIGC not only significantly improves the efficiency of ad production but also greatly
enhances the accuracy and effectiveness of advertising [69–72]. With these technologies, advertisers can more precisely
reach their target audience, boosting the appeal and impact of their ads, bringing transformative change to the industry.

https://doi.org/10.53941/tai.2025.100009

145

Yang et al.

4.1. Background

Trans. Artif. Intell. 2025, 1(1), 139–152

AIGC refers to content generated using Generative AI (GAI) technology, rather than being created by human
authors  [73].  It  can  automatically  create  large  volumes  of  content  in  a  short  period.  For  example,  ChatGPT,
developed by OpenAI, is a language model designed for building conversational AI systems that can effectively
understand and respond meaningfully to human language input. Similarly, Diffusion Models such as DALL-E 3
and Stable Diffusion excel at synthesizing unique, high-quality images from textual descriptions [68,74–76]. These
models can be further enhanced by frameworks like ControlNet [62], which allow for explicit control over image
attributes  such  as  pose,  structure,  or  layout  during  generation,  making  them  highly  suitable  for  customized
advertising campaigns and brand-specific requirements. As AIGC technology progresses, more experts believe it
will  set  new  benchmarks  in  AI,  with  a  profound  impact  on  sectors  from  advertising  to  content  creation,
revolutionizing the way we interact with information and media and ushering in a new era of efficiency, precision,
and innovation.

4.2. Application of AIGC in Advertising Copywriting

Social  media platforms  like  Facebook  and  Xiaohongshu have  become an  indispensable part  of daily  life.
AIGC can automatically generate personalized ad copy based on users’ profiles and interests. For instance, on
Xiaohongshu,  ChatGPT  can  use  human-provided  ad  templates  to  create  high-quality,  customized  advertising
content. A question and answer example is illustrated in Figure 3.

(a)

(b)

Figure 3. A question example (a) and an answer example (b) generated by ChatGPT.

4.3. Application of AIGC in Advertising Images

DALL-E 3, developed by OpenAI, is an AI image generation model that uses a diffusion model architecture
and techniques like language-image contrastive learning to create images from text descriptions. Using the DALL-
E 3 model, advertisers can input product descriptions, target audience information, and ad style preferences to
generate high-quality advertising images quickly. For example, as shown in Figure 4, if a restaurant owner wants
to advertise a delicious steak, they just need to enter the food name and other details into the model. This allows
them to generate a series of attractive restaurant food advertisements at a low cost. This approach not only saves
production costs but also precisely targets the market, enhancing the appeal and effectiveness of the advertisements.

https://doi.org/10.53941/tai.2025.100009

146

Yang et al.

Trans. Artif. Intell. 2025, 1(1), 139–152

Figure 4. Schematic diagram of a steak generated by the DALL-E 3 model.

4.4. Current Solutions to Copyright and Cultural Misuse in AIGC

Recent  years  have  witnessed  a  rapid  surge  in  both  research  and  practical  initiatives  aimed  at  mitigating

copyright infringement and cultural misappropriation in AIGC.

Data  Governance  and  Copyright  Protection.  To  address  these  challenges,  leading  AIGC  platforms  are
adopting  increasingly  robust  data  governance  frameworks.  These  efforts  [77,78]  include  the  deployment  of
watermarking  technologies,  provenance-tracking  systems,  and  advanced  copyright  detection  tools  designed  to
safeguard  against  the  unauthorized  use  of  protected  works.  Furthermore,  model  developers  are placing  greater
emphasis  on  curating  training  datasets  to  exclude  copyrighted  or  culturally  sensitive  materials,  unless  explicit
rights and permissions have been obtained. This proactive approach not only helps prevent infringement but also
supports the responsible and ethical deployment of generative models.

Cultural  Sensitivity  Filters.  In  tandem  with  data  governance  improvements,  state-of-the-art  generative
models are integrating sophisticated cultural sensitivity filters and auditing mechanisms [79–81]. These systems
are engineered to detect and flag potentially insensitive or appropriative content before it reaches the public. The
adoption  of  human-in-the-loop  review  processes,  particularly  in  commercial  advertising  workflows,  further
reinforces  cultural  respect  and  helps  ensure  that  AI-generated  content  honors  traditional  elements  without
distortion or misrepresentation. By embedding these safeguards into both the development and deployment stages,
organizations are working to minimize the risk of cultural misuse. Besides, both academia and industry are actively
pursuing technical and policy-oriented strategies to strengthen the regulatory landscape of AIGC.

Explainable and Auditable AI. There is a growing emphasis on the development of explainable AI (XAI) [82–85]
and content auditing tools, which facilitate transparency and accountability. These technologies enable stakeholders to
trace  how  specific  pieces  of  content  are  generated  and  to  assess  whether  they  comply  with  copyright  and  cultural
standards. In addition, innovative approaches such as embedding provenance metadata and leveraging blockchain for
immutable copyright records are being explored to reinforce trust and traceability in AIGC.

Bias and Misuse Detection. Considerable attention is also being given to the creation of automated methods for
detecting and mitigating both bias and misuse, including copyright violations and cultural appropriation [86–88]. This
research spans interventions at both the dataset level—such as advanced filtering and rebalancing strategies—and at
the output level, where real-time content moderation can help prevent the dissemination of problematic content.

Ethical Frameworks. Finally, interdisciplinary collaborations are yielding new ethical frameworks that merge
legal,  ethical,  and  technical  considerations  [89].  These  comprehensive  frameworks  are designed  to  ensure  that
innovation  in  generative  AI  proceeds  in  tandem  with  responsible  content  creation,  particularly  in  commercial
contexts  where  the  impact  of  misuse  can  be  significant.  The  overarching  goal  is  to  strike  a  balance  between
technological advancement and the protection of intellectual property and cultural heritage.

4.5. Future Prospects and Challenges

Recently, in an interview, ZeroOne Data Science CEO Feng Jian mentioned that designer teams are the first
to  benefit  from  AIGC  software.  After  introducing  AIGC,  the  workload  that  previously  required  at  least  five
designers a week to complete can now be finished in two to three days. Furthermore, AIGC can create virtual hosts
or presenters for advertising in the near future, providing immersive experiences and increasing user interaction.
AI-automated content generation drastically reduces the technical time required for ad creation. AIGC can also
quickly optimize and adjust ad content based on creator feedback. By using AIGC for ad creation, not only is time

https://doi.org/10.53941/tai.2025.100009

147

Yang et al.

Trans. Artif. Intell. 2025, 1(1), 139–152

saved,  but  ad  creators  can  focus  on  creative  ideas  and  content  exploration,  producing  more  impactful  and
influential ads. However, despite the immense potential and advantages of AIGC, its output heavily depends on
human-provided data resources, which can lead to training defects and copyright infringement risks [86]. AI may
fabricate information when dealing with complex issues, leading to the misuse of cultural elements, damaging the
essence  of  ads,  and  harming  the  brand  image.  Additionally,  AI  has  a  probability  of  generating  seemingly
reasonable but incorrect answers when handling complex, ambiguous, or open-ended questions. When ad creators
use AI to handle related creative content, if they fail to detect errors in cultural element stitching, misinterpretation
of cultural customs, or inappropriate handling of sensitive culture, it could lead to the misuse of traditional elements
due to the limitations of AIGC [90]. Such misuse could not only destroy the cultural essence of the ad but also
cause irreparable damage to the brand image. In conclusion, with the continuous development of AIGC technology,
its application in advertising shows tremendous potential and advantages. Although there are data dependency and
potential copyright issues, by exploring more reasonable usage methods and establishing appropriate regulatory
mechanisms [91], AIGC is expected to further drive breakthroughs and transformations in ad production on the
existing foundation, continually optimizing its application effects.

5. Conclusions

The  emerging  utilization  of  AI  in  FinTech  has  progressed  beyond  experimental  prototypes  to  become
indispensable across the financial value chain. Recommendation systems, under-pinned by SSL to mitigate data
sparsity, have emerged as pivotal instruments for enhancing personalized marketing and recommendation accuracy.
LLMs, leveraged through advanced prompt engineering, have facilitated accessibility to sophisticated risk analysis
for SMEs, enabling accelerated and more transparent financial decision-making. Similarly, AIGC has transformed
advertising  workflows,  offering  cost-efficient  and  scalable  content  generation,  albeit  concurrently  highlighting
significant governance and ethical considerations.

Nevertheless, critical challenges necessitate resolution to ensure the sustainable advancement of AI in FinTech.
Robust frameworks are imperative to reconcile data privacy imperatives with innovation requirements. Algorithmic
transparency  and  interpretability  remain  paramount  for  fostering  trust  in  AI-driven  decisions,  particularly  within
regulated financial contexts. Regarding AIGC, issues pertaining to copyright infringement, cultural misappropriation,
and content authenticity demand systematic governance structures and technical safeguards.

Future research and development should prioritize human-centric, scalable solutions in ethical principles and
regulatory  compliance.  Key  directions  include  enhancing  the  crossdomain  transferability  of  SSL  models,
improving the contextual reasoning capabilities of LLMs in complex risk scenarios, and developing generative
models intrinsically aligned with diverse cultural and legal frameworks. Through interdisciplinary collaboration
and  the  adoption  of  rigorous evaluation  standards,  the  FinTech  sector  can  realize  the  potential  of  AI  to  foster
inclusive, efficient, and trustworthy financial services.

Author Contributions

R.Y.: Conceptualization, investigation, writing, and revision. Y.W.: Conceptualization, investigation, writing,
and revision. Y.L.: Conceptualization, investigation, writing, and revision. Z.Y.: Conceptualization, investigation,
writing,  and  revision.  Z.Z.:  Conceptualization,  investigation,  writing,  and  revision.  D.W.:  Conceptualization,
investigation, writing, and revision. All authors have read and agreed to the published version of the manuscript.

Funding

This work is supported in part by the InnoHK Initiative, in part by the Government of the HKSAR, and in

part by the Laboratory for AI-Powered Financial Technologies.

Conflicts of Interest

The  authors  declare  no  conflict  of  interest.  Given  the  role  as  Editor-in-Chief,  Dapeng  Oliver  Wu  had  no
involvement in the peer review of this paper and had no access to information regarding its peer-review process.
Full responsibility for the editorial process of this paper was delegated to another editor of the journal.

References

1.
Cao, L.; Yang, Q.; Yu, P.S. Data science and ai in fintech: An overview. Int. J. Data Sci. Anal. 2021, 12, 81–99.
2.  Ashta,  A.;  Herrmann,  H.  Artificial  intelligence  and  fintech:  An  overview  of  opportunities  and  risks  for  banking,

investments, and microfinance. Strateg. Chang. 2021, 30, 211–222.
Cao, L.; Yuan, G.; Leung, T.; et al. Special issue on ai and fintech: The challenge ahead. IEEE Intell. Syst. 2020, 35, 3–6.

3.

https://doi.org/10.53941/tai.2025.100009

148

Yang et al.

Trans. Artif. Intell. 2025, 1(1), 139–152

4.

Belanche, D.; Casalo, L.V.; Flavia, C. Artificial intelligence in fintech: Understanding robo-advisors adoption among
customers. Ind. Manag. Data Syst. 2019, 119, 1411–1430.

5.  Kamuangu, P.K. Advancements of ai and machine learning in fintech industry (2016–2020). J. Econ. Financ. Account.

6.

7.

8.

9.

Stud. 2024, 6, 23–31.
Ricci, F.; Rokach, L.; Shapira, B. Introduction to recommender systems handbook. In Recommender Systems Handbook;
Springer: Berlin/Heidelberg, Germany, 2011; pp. 1–35.
Covington, P.; Adams, J.; Sargin, E. Deep neural networks for youtube recommendations. In Proceedings of the 10th
ACM Conference on Recommender Systems, Boston, MA, USA, 15–19 September 2016; pp. 191–198.
Cheng, H.-T.; Koc, L.; Harmsen, J.; et al. Wide & deep learning for recommender systems. In Proceedings of the 1st
Workshop on Deep Learning for Recommender Systems, Boston, MA, USA, 15 September 2016; pp. 7–10.
Zhou, G.; Zhu, X.; Song, C.; et al. Deep interest network for click-through rate prediction. In Proceedings of the 24th
ACM SIGKDD International Conference on Knowledge Discovery & Data Mining, London UK, 19–23 August 2018;
pp. 1059–1068.

10.  Chen,  T.;  Yin,  H.;  Ye,  G.;  et  al.  Try  this  instead:  Personalized  and  interpretable  substitute  recommendation.  In
Proceedings of the 43rd International ACM SIGIR Conference on Research and Development in Information Retrieval,
Virtual, 25–30 July 2020; pp. 891–900.

11.  Yin,  H.;  Cui,  B.;  Huang,  Z.;  et  al.  Joint  modeling  of  users’  interests  and  mobility  patterns  for  point-of-interest
recommendation. In Proceedings of the 23rd ACM International Conference on Multimedia, Brisbane, Australia, 26–30
October 2015; pp. 819–822.

12.  Sarwar,  B.M.  Sparsity,  Scalability  and  Distribution  in  Recommender  Systems.  Ph.D.  Dissertation,  University  of

Minnesota, Minneapolis, MN, USA, 2001.

13.  Zhang, S.;  Yao, L.;  Sun,  A.;  et  al.  Deep learning-based  recommender  system:  A  survey  and new perspectives.  ACM

Comput. Surv. 2019, 52, 1–38.

14.  Yu, J.; Yin, H.; Xia, X.; et al. Self-supervised learning for recommender systems: A survey. IEEE Trans. Knowl. Data

Eng. 2023, 36, 335–355.

15.  Hinton, G.E.; Salakhutdinov, R.R. Reducing the dimensionality of data with neural networks. Science 2006, 313, 504–507.
16.  Vincent, Y.B.P.; Larochelle, H.; Manzagol, P.-A. Extracting and composing robust features with denoising autoencoders.
In Proceedings of the International Conference on Machine Learning, Helsinki, Finland, 5–9 July 2008; pp. 1096–1103.
17.  Ericsson, H.G.L.; Hospedales, T.M. How well do selfsupervised models transfer? In Proceedings of the IEEE Conference

on Computer Vision and Pattern Recognition, Nashville, TN, USA, 20–25 June 2021; pp. 5414–5423.

18.  Liu, X.; Zhang, F.; Hou, Z.; et al. Self-supervised learning: Generative or contrastive. IEEE Trans. Knowl. Data Eng.

2023, 35, 857–876.

19.  Wu,  Y.;  DuBois,  C.;  Zheng,  A.X.;  et  al.  Collaborative  denoising  auto-encoders  for  top-n  recommender  systems.  In
Proceedings of the Ninth ACM International Conference on Web Search and Data Mining, San Francisco, CA, USA,
22–25 February 2016; pp. 153–162.

20.  Pinto, L.; Gupta, A. Supersizing self-supervision: Learning to grasp from 50k tries and 700 robot hours. In Proceedings of

the IEEE International Conference on Robotics and Automation, Stockholm, Sweden, 16–21 May 2016; pp. 3406–3413.

21.  Li, J.M.R.Y.; Paluri, M.; Dolla, P. Unsupervised learning of edges. In Proceedings of the IEEE Conference on Computer

Vision and Pattern Recognition, Las Vegas, NV, USA, 27–30 June 2016; pp. 1619–1627.

22.  Lee, S.J.H.H.; Shin, J. Rethinking data augmentation: Selfsupervision and self-distillation. arXiv 2019, arXiv:1910.05872.
23.  Zoph,  B.;  Ghiasi,  G.;  Lin,  T.Y.;  et  al.  Rethinking  pre-training  and  self-training.  In  Proceedings  of  the  International
Conference on Neural Information Processing Systems, Vancouver, BC, Canada, 6–12 December 2020; pp. 3833–3845.
24.  Mitrovic,  J.;  McWilliams,  B.;  Walker,  L.B.J.;  et  al.  Representation  learning  via  invariant  causal  mechanisms.  In

Proceedings of the International Conference on Learning Representations, Virtual, 3–7 May 2021; pp. 1–19.

25.  Hua,  T.;  Wang,  W.;  Xue,  Z.;  et  al.  On  feature  decorrelation  in  self-supervised  learning.  In  Proceedings  of  the  IEEE

International Conference on Computer Vision, Montreal, BC, Canada, 11–17 October 2021; pp. 9598–9608.

26.  Alam, M.A.; Mahatab, G.; Sarna, S.A. Enhancing regulatory frameworks to prevent financial crises. Am. J. Econ. Bus.

Manag. 2025, 8, 1351–1359.

27.  Horobets, N.; Reznik, O.; Maliyk, V.; et al. Artificial intelligence technologies in banking: Challenges and opportunities
for anti-money laundering in the context of eu regulatory initiatives. J. Money Laund. Control. 2025, 28, 210–225.
28.  Penikas, H. Review of bank of russia-nes workshop: Identification and measurement of macroprudential policies effects.

Russ. J. Money Financ. 2021, 80, 94–104.

29.  Uch, R.; Miyamoto, H.; Kakinaka, M. Effects of a banking crisis on credit growth in developing countries. Financ. Res.

Lett. 2021, 43, 102004.

30.  Li, Y.-M.; Lin, L.-F.; Hsieh, C.-Y.; et al. A social investing approach for portfolio recommendation. Inf. Manag. 2021,

58, 103536.

https://doi.org/10.53941/tai.2025.100009

149

Yang et al.

Trans. Artif. Intell. 2025, 1(1), 139–152

31.  Song,  Y.;  Sun,  C.;  Peng,  Y.;  et  al.  Research  on  multidimensional  trust  evaluation  mechanism  of  fintech  based  on

blockchain. IEEE Access 2022, 10, 57025–57036.

32.  Cheng, X.; Guo, F.; Chen, J. et al. Exploring the trust influencing mechanism of robo-advisor service: A mixed-method

approach. Sustainability 2022, 14, 5284.

33.  Ru, A.; Berger, B.; Hess, T. The ambivalent effect of transparency on trust in robo-advisors: An experimental investigation.
In Proceedings of the 24th Pacific Asia Conference on Information Systems (PACIS 2021), Virtual, 12–14 July 2021.
34.  Li, T.; Song, J. Deep learning-powered financial product recommendation system in banks: Integration of transformer

and transfer learning. J. Organ. End User Comput. 2024, 36, 1–29.

35.  Zhang, L.; Wu, X.; Zhao, H.; et al. Personalized recommendation in P2P lending based on risk-return management: A

multi-objective perspective. IEEE Trans. Big Data 2022, 8, 1141–1154.

36.  Soleymani,  F.;  Paquet,  E.  Deep  graph  convolutional  reinforcement  learning  for  financial  portfolio  management—

DeepPocket. Expert Syst. Appl. 2021, 185, 115127.

37.  Wu,  L.;  Zhang,  J.  Continuous  control  with  stacked  deep  dynamic  recurrent  reinforcement  learning  for  portfolio

optimization. Expert Syst. Appl. 2021, 165, 113891.

38.  Yu, C.; Liu, Y. A personalized mean-CVaR portfolio optimization model for individual investment. Math. Probl. Eng.

2021, 2021, 8863597.

39.  Club, E. O Recomendador de Produtos Que Sabe Exatamente Como o Pequeno Varejo Pode Vender Mais. September
2022. Available online: https://ciandt.com/br/pt-br/in-the-news/recomendador-de-produtos-que-sabe-exatamente-como-
o-pequeno-varejo-pode-vender-mais (accessed on 22 April 2025).

40.  Alison,  T.  The  Future  of  Facebook.  May  2024.  Available  online:  https://about.fb.com/news/2024/05/the-future-of-

facebook/ (accessed on 22 April 2025).

41.  Wang, G.; Cao, L.; Zhao, H.; et al. Coupling macro-sector-micro financial indicators for learning stock representations
with less uncertainty. In Proceedings of the AAAI Conference on Artificial Intelligence, Virtual, 2–9 February 2021;
pp. 4418–4426.

42.  Du, X.; Tanaka-Ishii, K. Stock embeddings acquired from news articles and price history, and an application to portfolio
optimization.  In  Proceedings  of  the  58th  Annual  Meeting  of  the  Association  for  Computational  Linguistics,  Virtual,
5–10 July 2020; pp. 3353–3363.

43.  Liu, Q.; Cheng, X.; Su, S.; et al. Hierarchical complementary attention network for predicting stock price movements
with news. In Proceedings of the 27th International Conference on Information and Knowledge Management, Turin, Italy,
22–26 October 2018; pp. 1603–1606.

44.  Hu, Z.; Lu, W.; Bian, J.; et al. Listening to chaotic whispers: A deep learning framework for news-oriented stock trend
prediction. In Proceedings of the Eleventh ACM International Conference on Web Search and Data Mining, Los Angeles,
CA, USA, 5–9 February 2018; pp. 261–269.

45.  Si, J.; Mukherjee, A.; Liu, B.; et al. Exploiting topic based twitter sentiment for stock prediction. In Proceedings of the

51st Annual Meeting of the Association for Computational Linguistics, Sofia, Bulgaria, 4–9 August 2013; pp. 24–29.

46.  Luo, Y.; Zheng, J.; Yang, Z.; et al. Pleno-alignment framework for stock trend prediction. IEEE Trans. Neural Netw.

Learn. Syst. 2025, early access.

47.  Liu, J.; Lin, H.; Liu, X.; et al. Transformer-based capsule network for stock movement prediction. In Proceedings of the First
Workshop on Financial Technology and Natural Language Processing, Macao, China, 10–12 August 2019; pp. 66–73.
48.  Wang, Z.; Zhang, X.; Du, H. Mutual information guided financial report generation with domain adaption. IEEE Trans.

Emerg. Top. Comput. Intell. 2024, 8, 627–640.

49.  Niu, H.; Xiong, Y.; Wang, X.; et al. KeFVP: Knowledge-enhanced financial volatility prediction. Find. Assoc. Comput.

Linguist. 2023, 2023, 11499–11513.

50.  Yi,  Y.;  Uy,  M.C.S.;  Huang,  A.  Finbert:  A  pretrained  language  model  for  financial  communications.  arXiv  2020,

arXiv:2006.08097.

51.  Xie, Q.; Han, W.H.; Zhang, X.; et al. Pixiu: A comprehensive benchmark, instruction dataset and large language model

for finance. Adv. Neural Inf. Process. Syst. 2023, 36, 33469–33484.

52.  Bussmann, N.; Giudici, P.; Marinelli, D.; et al. Explainable ai in fintech risk management. Front. Artif. Intell. 2020, 3, 26.
53.  Wang, C.; Luo, B. Predicting $GME stock price movement using sentiment from Reddit r/wallstreetbets. In Proceedings
of the Third Workshop on Financial Technology and Natural Language Processing, Online, 19 August 2021; pp. 22–30.
54.  Ding, X.; Zhang, Y.; Liu, T.; et al. Using structured events to predict stock price movement: An empirical investigation.
In  Proceedings  of  the  2014  Conference  on  Empirical  Methods  in  Natural  Language  Processing,  Doha,  Qatar,  25–29
October 2014; pp. 1415–1425.

55.  Ding, X.; Zhang, Y.; Liu, T.; et al. Knowledge-driven event embedding for stock prediction. In Proceedings of Coling 2016,
the 26th International Conference on Computational Linguistics, Osaka, Japan, 11–16 December 2016; pp. 2133–2142.

https://doi.org/10.53941/tai.2025.100009

150

Yang et al.

Trans. Artif. Intell. 2025, 1(1), 139–152

56.  Nguyen,  T.H.;  Shirai,  K.  Topic  modeling  based  sentiment  analysis  on  social  media  for  stock  market  prediction.  In
Proceedings of the 53rd Annual Meeting of the Association for Computational Linguistics and the 7th International Joint
Conference on Natural Language Processing, Beijing, China, 26–31 July 2015; pp. 1354–1364.

57.  Ang, G.; Lim, E.-P. Guided attention multimodal multitask financial forecasting with inter-company relationships and
global and local news. In Proceedings of the 60th Annual Meeting of the Association for Computational Linguistics,
Dublin, Ireland, 22–27 May 2022; pp. 6313–6326.

58.  Yu, X.; Chen, Z.; Ling, Y.; et al. Temporal data meets llm—explainable financial time series forecasting. arXiv 2023,

arXiv:2306.11025.

59.  Xie,  Q.;  Han,  W.;  Lai,  Y.;  et  al.  The  wall  street  neophyte:  A  zero-shot  analysis  of  chatgpt  over  multimodal  stock

60.

movement prediction challenges. arXiv 2023, arXiv:2304.05351.
Jiang, Y.; Pan, Z.; Zhang, X.; et al. Empowering time series analysis with large language models: A survey. arXiv 2024,
arXiv:2402.0318.

61.  Cao, Y.; Li, S.; Liu, Y.; et al. A comprehensive survey of aigenerated content (aigc): A history of generative ai from gan

to chatgpt. arXiv 2023, arXiv:2303.04226.

62.  Zhang, L.; Rao, A.; Agrawala, M. Adding conditional control to text-to-image diffusion models. In Proceedings of the

IEEE/CVF International Conference on Computer Vision, Paris, France, 2–6 October 2023.

63.  Li, M.; Yang, T.; Kuang, H.; et al. Controlnet++: Improving conditional controls with efficient consistency feedback. In

Computer Vision—ECCV 2024; Springer: Cham, Switzerland, 2024; pp. 129–147.

64.  Zhang, Z.; Zhang, Q.; Li, G.; et al. Dyartbank: Diverse artistic style transfer via pre-trained stable diffusion and dynamic

style prompt artbank. Knowl. Based Syst. 2025, 310, 112959.

65.  Zhang, Z.; Li, Y.; Xia, R.; et al. Lgast: Towards high-quality arbitrary style transfer with local–global style learning.

Neurocomputing 2025, 623, 129434.

66.  Zhang, Z.; Zhang, Q.; Luan, J.; et al. Vectorsketcher: Learning to create a vector-based free-hand sketch. Eng. Appl. Artif.

Intell. 2025, 156, 111005.

67.  Roumeliotis, K.I.; Tselikas, N.D. Chatgpt and open-ai models: A preliminary review. Future Internet 2023, 15, 192.
68.  Ramesh, A.; Pavlov, M.; Goh, G.; et al. Zero-shot text-to-image generation. In Proceedings of the 38th International

Conference on Machine Learning, Virtual, 18–24 July 2021; pp. 8821–8831.

69.  Haleem, A.; Javaid, M.; Qadri, M.A.; et al. Artificial intelligence (ai) applications for marketing: A literature-based study.

Int. J. Intell. Netw. 2022, 3, 119–132.

70.  Qin, X.; Jiang, Z. The impact of ai on the advertising process: The Chinese experience. J. Advert. 2019, 48, 338–346.
71.  Huh, J.; Nelson, M.R.; Russell, C.A. Chatgpt, ai advertising, and advertising research and education. J. Advert. 2023, 52,

477–482.

72.  Ford, J.; Jain, V.; Wadhwani, K.; et al. Ai advertising: An overview and guidelines. J. Bus. Res. 2023, 166, 114124.
73.  Wu, J.; Gan, W.; Chen, Z.; et al. Ai-generated content (aigc): A survey. arXiv 2023, arXiv:2304.06632.
74.  Rombach,  R.;  Blattmann,  A.;  Lorenz,  D.;  et  al.  High-resolution  image  synthesis  with  latent  diffusion  models.  In
Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition, New Orleans, LA, USA, 18–24
June 2022; pp. 10684–10695.

75.  Zhang, Z.; Zhang, Q.; Lin, H.; et al. Towards highly realistic artistic style transfer via stable diffusion with step-aware
and layer-aware prompt. In Proceedings of the Thirty-Third International Joint Conference on Artificial Intelligence, Jeju,
Republic of Korea, 3–9 August 2024; pp. 7814–7822.

76.  Zhang, Z.; Zhang, Q.; Xing, W.; et al. Artbank: Artistic style transfer with pre-trained diffusion model and implicit style prompt
bank. In Proceedings of the AAAI Conference on Artificial Intelligence, Vancouver, BC, Canada, 20–27 February 2024.
77.  Li, Z.; Zhang, W.; Zhang, H.; et al. Global digital compact: A mechanism for the governance of online discriminatory

and misleading content generation. Int. J. Hum. Comput. Interact. 2025, 41, 1381–1396.

78.  Dzuong, J.; Wang, Z.; Zhang, W. Uncertain boundaries: Multidisciplinary approaches to copyright issues in generative

ai. arXiv 2024, arXiv:2404.08221.

79.  Balasubramaniam, S.; Chirchi, V.; Kadry, S.; et al. The road ahead: Emerging trends, unresolved issues, and concluding

remarks in generative ai—A comprehensive review. Int. J. Intell. Syst. 2024, 2024, 4013195.

80.  Chen,  H.;  Chan-Olmsted,  S.;  Thai,  M.  Culture  sensitivity  and  information  access:  A  qualitative  study  among  ethnic

groups. Qual. Rep. 28, 2504–2522, 2023.

81.  Wang, Y.; Zheng, J.; Zhang, C.; et al. Dualnet: Robust self-supervised stereo matching with pseudo-label supervision. In

Proceedings of the AAAI Conference on Artificial Intelligence, Philadelphia, PA, USA, 25 February–4 March 2025.

82.  Dwivedi, R.; Dave, D.; Naik, H.; et al. Explainable ai (xai): Core ideas, techniques, and solutions. ACM Comput. Surv.

2023, 55, 1–33.

83.  Wang,  Y.;  Wang,  L.;  Li,  K.;  et  al.  Cost  volume  aggregation  in  stereo  matching  revisited:  A  disparity  classification

perspective. IEEE Trans. Image Process. 2024, 33, 6425–6438.

https://doi.org/10.53941/tai.2025.100009

151

Yang et al.

Trans. Artif. Intell. 2025, 1(1), 139–152

84.  Das,  A.;  Rad,  P.  Opportunities  and  challenges  in  explainable  artificial  intelligence  (xai):  A  survey.  arXiv  2020,

arXiv:2006.11371.

85.  Arrieta, A.B.; Herrera, F.; Chatilaf, R.; et al. Explainable artificial intelligence (xai): Concepts, taxonomies, opportunities

and challenges toward responsible AI. Inf. Fusion 2019, 58, 82–115.

86.  Wang, T.; Zhang, Y.; Qi, S.; et al. Security and privacy on generative data in aigc: A survey. ACM Comput. Surv. 2024,

57, 1–34.

87.  Lucchi, N. Chatgpt: A case study on copyright challenges for generative artificial intelligence systems. Eur. J. Risk Regul.

2024, 15, 602–624.

88.  Verma, A. The copyright problem with emerging generative ai. J. Intell. Prot. Stud. 2023, 7, 69.
89.  Wang, Z.; Shen, L.; Kuang, E.; et al. Exploring the impact of artificial intelligence-generated content (aigc) tools on
social  dynamics  in  ux  collaboration.  In  Proceedings  of  the  2024  ACM  Designing  Interactive  Systems  Conference,
Copenhagen, Denmark, 1–5 July 2024.

90.  Baidoo-Anu, D.; Ansah, L.O. Education in the era of generative artificial intelligence (AI): Understanding the potential

benefits of chatgpt in promoting teaching and learning. J. AI 2023, 7, 52–62.

91.  Franks, E.; Lee, B.; Xu, H. Report: China’s new ai regulations. Glob. Priv. Law Rev. 2024, 5, 43–49.

https://doi.org/10.53941/tai.2025.100009

152

