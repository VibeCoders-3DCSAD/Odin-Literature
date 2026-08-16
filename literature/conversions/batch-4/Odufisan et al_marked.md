---
conversion_metadata:
  converted_at: "2026-07-21T07:52:53Z"
  converter_tool: "markitdown"
  converter_version: "0.1.6"
  source_pdf: "Odufisan et al.pdf"
  source_pdf_sha256: "5c12b79f38f7084d29001f747a3886175f5c062b27fc3ae90eb23c958c28437d"
  page_count: 9
  markdown_char_count: 149094
---

<!-- PAGE-AWARE EXTRACTION (via pdfminer.six) -->

<!-- PAGE 1 -->

Journal of Economic Criminology 7 (2025) 100127

Contents lists available at ScienceDirect

Journal of Economic Criminology

journal homepage: www.journals.elsevier.com/journal-of-economic-criminology

Harnessing artificial intelligence and machine learning for fraud detection 
and prevention in Nigeria 
Oluwaseun Isaac Odufisana, Osekhonmen Victory Abhulimenb,⁎
a Department of Computer Engineering, The Federal University of Technology Akure, Ondo State PMB 704, Nigeria 
b Department of Information and Communication Engineering, Elizade University, Ilara-Mokin 340271, Ondo State PMB 002, Nigeria

, Erastus Olarenwaju Oguntia

]]]]

]]]]]]

A R T I C L E   I N F O

A B S T R A C T

Keywords: 
Artificial Intelligence 
Machine learning 
Fraud

Fraud  poses  a  significant  threat  to  Nigeria's  burgeoning  digital  economy,  impacting  sectors  like  finance,  e- 
commerce, healthcare, and education. Traditional methods struggle to keep pace with evolving fraud schemes. 
This  paper  investigates  the  potential  of  Artificial  Intelligence  (AI)  and  Machine  Learning  (ML)  for  enhanced 
fraud  detection  and  prevention  in  Nigeria.  We  explore  various  AI  methodologies,  including  supervised,  un-
supervised,  and deep  learning. We discuss their applications in anomaly detection, behavioural analysis, risk 
scoring, and network analysis. By leveraging AI's continuous learning capabilities, organizations can adapt to 
novel fraud tactics. The paper highlights the benefits of AI-powered fraud detection, including increased effi-
ciency,  improved  accuracy,  and proactive  risk  mitigation. However,  challenges  like  technical limitations  and 
regulatory considerations are acknowledged. Lastly, we examine the promising future of AI and ML in trans-
forming the financial crime prevention situation in Nigeria.

1.  Introduction

The  digital  revolution  has  undeniably  transformed  Nigeria,  en-
couraging  increased  connectedness  and  accelerating  growth.  From  e- 
commerce and digital banking to e-learning and telemedicine, the di-
gital  revolution  is  empowering  Nigerians  with  tools  to  bridge  infra-
structural  gaps,  access  global  opportunities,  and  drive  sustainable 
growth across various sectors (Okonkwo et al., 2024).

However,  despite  this  transformative  impact  of  the  digital  revolu-
tion in Nigeria, it has also given rise to a significant challenge: an in-
crease in fraud in several industries. Fraud has become a serious con-
cern, endangering not only businesses but also the country's financial 
stability,  affecting  everything  from  e-commerce  and  healthcare  to 
education. The consequences of these crimes go far beyond the lives of 
the specific victims; they affect the basis of the Nigerian economy itself. 
Companies  suffer  catastrophic  losses,  customer  confidence  declines, 
and there is a general decline in the perception of security associated 
with digital transactions (Okoye and Gbegi, 2013). This worrying pat-
tern presents a worrisome picture. Global reports on fintech and pay-
ments show that between 2023 and 2027, online payment fraud alone is 
projected  to  cost  firms  globally  more  than  $343  billion  (Juniper 
Research,  2022).  In  Nigeria,  the  effects  are  felt  not  only  by  large  or-
ganizations  but  also  by  regular  people  who  become  victims  of  fake

online  markets,  identity  theft,  and  various  other  forms  of  deception 
(Oluwole, 2024). The complexity of fraudsters is simply surpassing that 
of traditional systems of fraud detection, which rely on strict standards 
and  manual  checks.  A  paradigm  change  is  required  at  this  crucial 
juncture  to  create  a  new  line  of  defense  that  is  powered  by  artificial 
intelligence (AI) and machine learning (ML) (Kamuangu, 2024).

Artificial  Intelligence  is  the  capability  of  machines  to  imitate  in-
telligence in human behaviour, attained by examining how the human 
brain thinks and how it learns, decides, and works in solving a specific 
problem  (Abhulimen  and  Ogunti,  2021).  AI  aims  to  replicate  these 
capabilities in machines, enabling them to perform tasks that typically 
require human intelligence, such as reasoning, understanding language, 
recognizing patterns, and adapting to new inputs. AI can take various 
forms,  including  expert  systems,  speech  recognition  tools,  and  ad-
vanced robotics, and it is driven by methods that enable machines to act 
intelligently, even in complex or unpredictable situations.

Machine  learning,  on  the  other  hand,  is  a  subset  of  AI  that  uses 
algorithms  that  analyze  large  amounts  of  data,  identify  patterns,  and 
make predictions or decisions based on that information (Sarker, 2021). 
For instance, ML algorithms are designed to improve their accuracy and 
efficiency over time as they are exposed to more data. Unlike traditional 
programming, where developers write explicit rules, ML systems "learn" 
these rules automatically through training processes.

⁎

Corresponding author. 
E-mail addresses: oluwaseun.odufisan@gmail.com (O.I. Odufisan), osekhonmen.abhulimen@elizadeuniversity.edu.ng (O.V. Abhulimen),

eoogunti@futa.edu.ng (E.O. Ogunti).

https://doi.org/10.1016/j.jeconc.2025.100127 
Received 21 October 2024; Received in revised form 1 January 2025; Accepted 6 January 2025 
2949-7914/© 2025 The Author(s). Published by Elsevier Ltd. This is an open access article under the CC BY-NC-ND license (http://creativecommons.org/licenses/ 
by-nc-nd/4.0/).

---

<!-- PAGE 2 -->

O.I. Odufisan, O.V. Abhulimen and E.O. Ogunti

Journal of Economic Criminology 7 (2025) 100127

AI and machine learning developments are revolutionizing the fight 
against fraud and provide a glimmer of hope in the fight against these 
crimes. Real-time pattern recognition and data analysis are possible for 
AI  systems  because  of  their  capacity  to  emulate  human  cognitive 
functions.  Because  of  this,  they  can  detect  suspicious  activities  that 
would  go  undetected  by  conventional  means.  These  computers  may 
identify  irregularities  that  may  indicate  possible  fraud  attempts  in  a 
matter of seconds by filtering through enormous datasets at an aston-
ishingly fast pace (Gupta, 2023).

This paper looks into how AI and ML might be revolutionary tools in 
the  fight  against  fraud,  particularly  in  Nigeria.  We  will  examine  how 
companies and organizations across a variety of sectors, such as banking, 
e-commerce,  healthcare,  and  education,  may  use  these  technologies  to 
detect and prevent fraud. By evaluating massive volumes of data, spotting 
intricate trends, and making real-time modifications that will result in a 
more  lucrative  and  safer  digital  environment  for  Nigerians,  AI  and  ML 
offer a cutting-edge defense against the schemes of fraudsters.

Both primary and secondary data were used to explore the role of AI 
and ML in fraud detection and prevention in Nigeria. Secondary data 
was sourced from various credible academic publications, industry re-
ports, government records, and global fraud studies, including datasets 
on fraud trends, technological adoption, and sectorial impacts. Primary 
data,  though  limited,  consisted  of  expert  insights  obtained  through 
unstructured interviews with stakeholders in the Nigerian banking and 
finance, e-commerce, healthcare, and educational sectors. Additionally, 
anecdotal  evidence  based  on  our  experiences  as  residents  in  Nigeria 
provided contextual understanding. These sources provided a founda-
tion for understanding the broader context of fraud in Nigeria, the ef-
fectiveness of AI and ML technologies globally, and the practical chal-
lenges and adoption barriers.

2.  Economic impact of fraud in Nigeria across various sectors

The insidious nature of fraud extends far beyond the immediate fi-
nancial losses inflicted upon individuals and businesses. In a nation like 
Nigeria,  striving  for  economic  prosperity  and  digital  inclusion,  fraud 
acts as a pernicious force, eroding trust, hindering growth, and stifling 
innovation (Drammeh, 2023). This chapter explores how fraud affects 
the economy in many different ways, including banking and finance, e- 
commerce, healthcare, and education. It also emphasizes how urgently 
artificial  intelligence  (AI)  and  machine  learning  (ML)  are  needed  as 
revolutionary countermeasures.

2.1.  Banking and finance

Manyo  et  al.  (2023),  in  their  research,  revealed  that  the  financial 
sector is a frequent target for fraudsters, with consequences extending 
beyond  immediate  financial  losses.  The  research  further  reveals  that 
banks  facing  fraudulent  transactions  suffer  significant  financial  set-
backs, which negatively affect their profitability and ability to invest in 
crucial services. This disruption affects the flow of credit to both busi-
nesses and individuals, slowing down economic growth. Additionally, 
the  rise  in  financial  fraud  undermines  public  trust  in  the  banking 
system,  discouraging  the  use  of  digital  financial  services  and  thereby 
impeding  the  government's  efforts  to  promote  financial  inclusion, 
which is critical for poverty reduction and economic development.

A report by Akintaro (2023) highlighted the scale of the problem in 
Nigeria, where 24 commercial banks lost N5.79 billion to fraud in the 
second  quarter  (Q2)  of  2023  -  an  increase  of  1125 %  from  the  N472 
million lost in the first quarter (Q1) of the same year. The total value of 
fraudulent transactions also surged dramatically from N2.58 billion to 
N9.75 billion, increasing by nearly 278 % from Q1 to Q2. Fraudulent 
loans accounted for 94.35 % of these losses, revealing a serious flaw in 
the Nigerian banking system. These fraudulent loans divert funds from 
honest  businesses  and  entrepreneurs,  stifling  new  business  formation 
and job creation, which are crucial to economic development.

The report (Akintaro, 2023) also reveals that other types of fraud, 
including mobile and computer fraud, pose additional threats. Mobile 
fraud,  responsible  for  3.39 %  of  the  total  losses,  undermines  trust  in 
mobile banking platforms, a key driver of financial inclusion. Computer 
and  web  fraud,  amounting  to  N59.5  million,  highlights  the  ongoing 
vulnerability of online banking systems, deterring both consumers and 
businesses  from  engaging  with  digital  services,  thus  hindering  the 
growth of the digital economy.

2.2.  E-commerce

E-commerce in Nigeria has the potential to drive economic growth, 
foster  innovation,  and  open  new  opportunities.  However,  fraud  on 
payment platforms presents a significant barrier to this growth. Recent 
increases  in  fraud  have  made  the  e-commerce  environment  fearful, 
causing  consumers  to  be  hesitant  about  online  purchases  due  to  con-
cerns about payment security. This reluctance leads to a preference for 
cash-on-delivery,  slowing  the  government's  push  for  a  cashless 
economy (Okolie and Ojomo, 2020).

E-commerce fraud comes in many forms, affecting both consumers 
and merchants. Consumers face risks like account takeover, mobile SIM 
switch  fraud,  and  social  engineering  tactics  such  as  phishing.  These 
threats damage their trust in online transactions and increase the risk of 
financial  loss  (Komandla,  2024).  Merchants,  on  the  other  hand,  en-
counter  fraud  like  identity  theft,  chargeback  fraud,  and  man-in-the- 
middle  attacks,  which  result  in  financial  losses  and  discourage  other 
businesses  from  entering  the  e-commerce  space  (Mutemi  and  Bacao, 
2024).

Other types of fraud, such as card testing, refund fraud, friendly 
fraud,  triangulation  fraud  and  interception  fraud  add  to  the  com-
plexity of the problem. Card testing uses stolen credit card informa-
tion  for  small  purchases  to  test  its  validity,  while  refund  fraud  ex-
ploits  stolen  payment  information  to  claim  refunds  for  fake 
overpayments.  Friendly  fraud  occurs  when  customers  falsely  claim 
they  didn’t  receive  their  goods  to  get  a  refund. Triangulation  fraud 
involves  fake  online  stores  stealing  customer  information  to  make 
purchases from legitimate merchants. Interception fraud occurs when 
a  person  uses  a  stolen  card  with  the  provided  address  and  billing 
information  to  make  a  purchase,  then  intercepts  the  package  for 
themselves (AxiomQ, 2022).

The  economic  impact  of  e-commerce  fraud  in  Nigeria  is  clear.  It 
deters online purchases, hampers the growth of cashless transactions, 
and  creates  a  climate  of  distrust.  Merchants  face  significant  financial 
risks  and  become  hesitant  to  continue  in  the  industry,  stalling  the 
sector's growth potential.

Projections  indicates  a  significant  increase  in  financial  losses  over 
the coming years. It is expected to escalate globally from $44.3 billion 
in 2024 to $107 billion by 2029, marking a 14 % increase (Adewumi, 
2024). The rapid growth of Nigeria’s e-commerce market presents an 
increased opportunity for E-commerce fraudsters (Oloni, 2024)

2.3.  Healthcare

Healthcare fraud in Nigeria is a significant issue with serious eco-
nomic and social impacts, undermining the quality of care and the in-
tegrity of the healthcare system. Medical identity theft and fraudulent 
claims  divert  resources  from  patients  who  genuinely  need  care.  This 
leads to compromised healthcare delivery and creates inefficiencies in 
the system (Akokuwebe and Idemudia, 2023).

A  common  form  of  fraud  involves  submitting  inaccurate  or  mis-
leading information to health insurance companies, tricking them into 
paying for unapproved benefits. In Nigeria, healthcare providers often 
engage in double billing, charging for services multiple times, or billing 
for  treatments  that  were  never  received  (Yange,  2019).  This  practice 
burdens the National Health Insurance Scheme (NHIS), increasing costs 
and reducing the effectiveness of care.

2

---

<!-- PAGE 3 -->

O.I. Odufisan, O.V. Abhulimen and E.O. Ogunti

Journal of Economic Criminology 7 (2025) 100127

‘Ghost patients’ are another fraudulent tactic where claims are filed 
for individuals who do not exist. In addition, stolen identities are used 
to  submit  fraudulent  claims,  adding  further  complexity  to  the  issue 
(Thornton  et  al.,  2015).  There  is  also  a  risk  of  collusion  between  pa-
tients and healthcare professionals, where bribes are exchanged to fa-
cilitate false claims.

These  fraudulent activities  result  in  increased  administrative  costs 
and reduced profitability for insurance companies, ultimately leading to 
higher  premiums  for  average  Nigerians.  Patients  suffer  too,  as  false 
claims deplete the funds needed for essential healthcare infrastructure, 
resulting in reduced access to quality care for those in need.

2.4.  Education

The Nigerian education sector faces significant challenges from ex-
amination fraud falsified scholarship applications, and fake credentials, 
all of which erode public trust and weaken the integrity of the system. 
These dishonest practices harm the quality of education and workforce 
readiness, denying opportunities to deserving students while benefiting 
unqualified  individuals. As a  result, economic  growth and  innovation 
are  stifled  due  to  an  inadequately  trained  workforce  (Alordiah  et  al., 
2023).

Examination  fraud  undermines  fair  evaluation,  from  simple 
cheating  to  bribing  invigilators.  Students  who  cheat  gain  an  unfair 
advantage,  damaging  the  reputation  of  educational  institutions  and 
leading  to  a  generation  ill-prepared  for  their  careers.  Employers,  fru-
strated by unreliable academic credentials, struggle to hire competent 
workers, further hindering economic progress (Eneji et al., 2022).

Admission fraud is another concern, where students gain university 
entry through bribes or forged documents, bypassing academic merit. 
This  weakens  the  intellectual  standard  of  institutions,  diminishes  op-
portunities for deserving students, and results in unqualified graduates 
who are ill-equipped for the workforce (Noah and Adesope, 2022) This 
not only affects their financial prospects but also poses risks to public 
safety in fields that require technical expertise.

Contract cheating, where students outsource their academic work to 
third-party  services  (Ali,  and  Alhassan,  2021),  threatens  the  learning 
process by allowing students to "buy" their achievements. This erodes 
the development of critical thinking and knowledge acquisition, leading 
to  a  workforce  deficient  in  these  essential  skills,  further  stalling  eco-
nomic progress.

Lastly, teacher fraud, though less common, also contributes to aca-
demic decline. Teachers  may inflate grades or  use fake  credentials to 
secure  employment,  compromising  the  quality  of  teachers  (Akinniyi 
et al., 2021). This deprives students of necessary skills, affecting their 
future success and reducing the overall productivity of the workforce. 
Addressing these forms of educational fraud through strict measures 
and  fostering  a  culture  of  academic  honesty  is  crucial  to  improving 
Nigeria’s education system, workforce, and economy.

3.  Traditional method of fraud detection

To  safeguard  their  operations  and  customers,  organizations  have 
traditionally relied on a combination of pre-defined rules and manual 
analysis for fraud detection. While these methods have served a purpose 
in the past, they are increasingly proving inadequate in the face of ever- 
evolving threats.

Limitations in terms of adaptability are among the biggest problems 
with traditional fraud detection techniques (Bello et al., 2024). Usually, 
these systems work with a predetermined set of rules that identify ac-
tions  that  meet  predetermined  standards  or  surpass  predetermined 
bounds. These regulations may have worked well in the past, but they 
are unable to keep up with how fraud is changing. To get beyond these 
pre-established  red  flags,  fraudsters  are  always  coming  up  with  fresh 
ideas  and  strategies.  It  is  frequently  a  time-consuming  and  slow  pro-
cedure to update these rule-based systems to handle new threats (Liu

et al., 2021). There is a gap in the detection rules that allows for the 
introduction of new fraud strategies, which provides an opportunity for 
fraudsters to take advantage of (Takyar, 2024). A fraudster might easily 
get around an e-commerce platform regulation that flags transactions 
over a particular amount as possibly fraudulent by breaking up a large 
purchase  into  several  smaller  transactions,  each  of  which  falls  below 
the threshold and so avoids detection.

Traditional  methods  also  suffer  from  a  lack  of  sophistication  in 
pattern recognition. Fraudulent operations may involve complex links 
and connections between different data points (Hilal et al., 2022). The 
use of a new user account, a billing address that is different from the 
shipping  address,  and  an attempt  to  buy  a  remote  location are  a  few 
examples of the various components of a fraudulent transaction. Hand 
analysis or rule-based algorithms that focus on individual data points 
alone could overlook these subtle but significant patterns.

Finally,  traditional  methods  face  significant  scalability  challenges. 
An explosion of data characterizes the digital age (Theodorakopoulos 
et al., 2024). The amount of data points, user interactions, and online 
transactions is growing constantly, making human analysis of this data 
more challenging and time-consuming. Traditional methods may be ill- 
suited to effectively handle these enormous datasets. This may result in 
an accumulation of unprocessed data, which could give rise to chances 
for fraudulent operations to evade detection.

While traditional fraud detection methods have played a historical 
role  in  safeguarding  organizations,  their  limitations  are  becoming  in-
creasingly  apparent  in  today's  dynamic  digital  landscape.  Their  in-
ability  to  adapt  to  evolving  threats,  identify  complex  patterns,  and 
handle large datasets creates vulnerabilities that fraudsters can exploit 
(Bansal et al., 2024). As we move forward, there is a critical need for 
more robust and adaptable solutions to combat fraud.

4.  The urgency for AI intervention

Fraudulent  actions  undermine  confidence,  divert  resources,  and 
inhibit  innovation  in  a  variety  of  sectors,  including  financial  organi-
zations,  e-commerce platforms, healthcare  providers,  and educational 
institutions.  At  this pivotal  moment, machine  learning  (ML)  and  arti-
ficial  intelligence  (AI)  emerge  as  game-changing  solutions  to  tackle 
these ubiquitous problems (Sharma et al., 2024).

Traditional  methods  of  fraud  detection  have  proven  increasingly 
inadequate. Manual processes are slow, error-prone, and overwhelmed 
by  the  ever-evolving  tactics  of  fraudsters.  Legacy  systems  struggle  to 
identify  complex  patterns  hidden  within  vast  amounts  of  data.  (Hilal 
et al., 2022). This is where AI and ML offer a powerful solution.

AI's ability to analyze massive datasets and identify subtle anomalies 
makes it ideal for fraud detection. Machine learning algorithms can be 
trained on historical fraud cases to recognize patterns and predict fu-
ture  fraudulent  activities.  This  allows  for  real-time  monitoring  of 
transactions,  flagging  suspicious  activity  before  it  can  cause  financial 
harm (Bansal et al., 2024).

In  the  banking  and  finance sector,  AI  can analyze  customer beha-
vior,  spending  patterns,  and  account  activity  to  identify  potential 
fraudulent loans, unauthorized access attempts, and money laundering 
schemes (Hassan et al., 2023). This empowers financial institutions to 
take  proactive  measures,  such  as  account  freezes  or  additional  au-
thentication steps, to mitigate losses.

The e-commerce sector stands to gain immensely from AI-powered 
fraud  detection.  AI  can  analyze  customer  purchase  history,  IP  ad-
dresses, and device fingerprints to identify suspicious orders that may 
be  linked  to  stolen  credit  card  information  (Gayam,  2020).  Ad-
ditionally, AI can be used to detect fake reviews and identify fraudulent 
merchants  operating  on  e-commerce  platforms  (Paul  and  Nikolaev, 
2021).

The healthcare sector can leverage AI to combat fraudulent claims 
and  identity  theft.  AI  algorithms  can  analyze  medical  records,  billing 
data, and patient information to identify anomalies that may indicate

3

---

<!-- PAGE 4 -->

O.I. Odufisan, O.V. Abhulimen and E.O. Ogunti

Journal of Economic Criminology 7 (2025) 100127

fraudulent activity (Kasaraneni, 2024) This can help healthcare provi-
ders and insurance companies prevent misuse of resources and ensure 
that funds are directed towards genuine medical needs.

The  education  sector  can  utilize  AI  to  combat  examination  mal-
practice  and  admission  fraud.  AI-powered  proctoring systems  can  de-
tect  suspicious  behavior  during  online  exams  (Nagpal  et  al.,  2024), 
while  advanced  document verification tools  can identify  forged  certi-
ficates and transcripts (Boonkrong, 2024). Furthermore, AI can analyze 
student  performance  data  to  flag  potential  plagiarism  in  assignments 
and essays (Tripathi and Thakar, 2024).

The  urgency  for  AI  intervention  in  combating  fraud  cannot  be 
overstated.  By  leveraging  the  power  of  AI  and  ML,  Nigeria  can  safe-
guard its economy, build trust within critical sectors, and empower its 
citizens  to  participate  with  confidence  in  a  digital  future.  As  AI  con-
tinues  to  evolve,  its  capabilities  in  fraud  detection  will  only  become 
more sophisticated, paving the way for a more secure and prosperous 
Nigeria.

the interconnected neurons in the human brain, allowing them to learn 
and adapt with remarkable efficiency. CNNs excel at image recognition, 
making  them  ideal  for  analyzing  images  of  signatures,  checks,  or 
identification  documents  to  identify  forgeries  or  alterations  used  in 
fraudulent  attempts  (Emiroğlu,  2023).  Imagine  a  CNN  analyzing  a 
scanned copy of a driver's license. By recognizing subtle inconsistencies 
in  the  document's  formatting  or  identifying  signs  of  tampering,  CNN 
can  flag  the  document  as  potentially  fraudulent,  helping  to  prevent 
identity  theft.  RNNs,  on  the  other  hand,  are  adept  at  sequential  data 
analysis, making them valuable for fraud detection in financial trans-
actions where the order and timing of events can be crucial for iden-
tifying suspicious  activity (Bello et  al., 2022). An  RNN can analyze a 
series of bank transactions, paying close attention to the sequence and 
timing of each event. By identifying unusual patterns, such as a rapid 
succession of withdrawals from geographically distant ATMs, the RNN 
can flag the account for potentially fraudulent activity.

5.  AI and machine learning approaches for effective fraud 
detection and prevention

6.  Some common applications of machine learning in fraud 
detection and prevention

While  AI  provides  the  broad  framework  for  intelligent  systems, 
Machine Learning (ML) serves as the engine that drives its effectiveness 
in  fraud  detection.  Machine  Learning  (ML)  is  a  subset  of  AI  that  em-
powers machines to identify patterns and improve their performance on 
a specific task without explicit programming (Sarker, 2021). There are 
three main categories of Machine Learning algorithms particularly well- 
suited to combatting fraud in Nigeria's digital sectors.

5.1.  Supervised learning

One way to conceptualize supervised learning is as a pupil carefully 
studying  under  an  instructor.  The  teacher  is  the  labelled  data  in  this 
comparison, where each data point has a label that corresponds to its 
category  (fraudulent  or  valid  transaction,  for  example).  For  example, 
financial  institutions  can  use  transaction  data  from  the  past  to  train 
models  that  identify  trends  linked  to  fraud.  Like  the  student,  these 
models are always picking up new skills and honing the ones they al-
ready  have  in  recognizing  patterns.  Supervised  learning-enabled  AI 
systems  can  evaluate  fresh  transactions  in  real-time  and  mark  those 
with  questionable  patterns  for  additional  examination  (Afriyie  et  al., 
2023). This makes it possible to take preventative action, which may 
stop financial losses before they happen.

5.2.  Unsupervised learning

Unsupervised learning takes a different approach. It is particularly 
valuable  for  detecting  novel  fraud  schemes  that  do  not  conform  to 
known patterns. Anomaly detection, a common unsupervised learning 
technique, identifies outliers or deviations from the norm in a dataset 
(Hilal et al., 2022). In the context of fraud detection, this can be used to 
uncover  unusual  or  unexpected  behavior,  such  as  unusually  large 
transactions originating from unfamiliar locations or sudden spikes in 
account activity (Rai and Dwivedi, 2020). Imagine a scenario where a 
customer with a history of modest online purchases suddenly attempts 
to purchase a high-end electronic device from a new location. An un-
supervised learning model can detect this deviation from the norm and 
flag it for investigation, potentially preventing a fraudulent purchase.

5.3.  Deep Learning

Deep learning, a powerful subset of ML, has gained prominence for 
its ability to process vast amounts of data and extract intricate patterns. 
Neural  networks,  particularly  convolutional  neural  networks  (CNNs) 
and recurrent neural networks (RNNs), are at the core of deep learning 
(Chen and Lai, 2021). These complex algorithms function similarly to

The following are some common applications of machine learning in

fraud detection and prevention:

6.1.  User authentication and biometric recognition

Traditional  password-based  authentication  systems  are  susceptible 
to  brute-force  attacks  and  social  engineering.  Machine  learning  (ML) 
algorithms can significantly enhance security by analyzing user beha-
vior  and  biometric  data  (Castelblanco et  al., 2020).  These  algorithms 
can learn a user's typical login patterns, including factors like the device 
used, location, and time of day. Deviations from this established base-
line can trigger alerts for potential unauthorized access attempts. Bio-
metric  recognition,  such  as  fingerprint  or  facial  recognition, adds  an-
other layer of security. ML can be used to analyze and verify biometric 
data  in  real-time,  ensuring  only  authorized  users  gain  access.  Arslan 
et al. (2016) explored the application of ML in biometric authentication 
systems,  emphasizing  its  role  in  user  verification  and  security.  Their 
review  highlights  successful  implementations  of  machine  learning  al-
gorithms like Support Vector Machines (SVMs), Naive Bayes (NB), and 
Artificial Neural Networks (ANNs) in achieving high recognition rates 
(80–99 %)  and  also  emphasizing  the  potential  of  ML  for  liveness  de-
tection and spoofing prevention which is a crucial aspect for robust user 
authentication and fraud mitigation in financial institutions. The lim-
itations  of  traditional  passwords  were  recognized  by  Nnamoko  et  al. 
(2022) thereby presenting a compelling case for behavioral biometrics 
as  a  machine  learning  application  to  enhance  fraud  detection  and 
prevention  in  online  transactions.  They  focused  on  leveraging  users' 
inherent  behavioral  patterns,  such  as  keystroke  dynamics  and  mouse 
movements,  for  user  identification,  aiming  to  improve  authentication 
security  and  combat  identity  theft  in  the  financial  sector.  Abhulimen 
and  Ogunti  (2022)  explored  the  use  of  residual  convolutional  neural 
networks  for  age  estimation  in  a  possible  attempt  to  curb  age  falsifi-
cation crime with face images. Yousefi et al. (2019) also explored the 
convergence  of  machine  learning  and  user  authentication  methods 
specifically for credit card fraud detection in a survey highlighting the 
limitations of static password-based authentication and exploring how 
behavioral biometrics, like touch dynamics and signature patterns, can 
be  leveraged  with  machine  learning  to  create  more  robust  user  au-
thentication  schemes.  Machine  learning's  ability  to  analyze  biometric 
data offers an additional layer of security beyond traditional passwords 
or  PINs,  effectively  distinguishing  legitimate  users  from imposters  at-
tempting  fraudulent  transactions.  This  aligns  perfectly  with  Nigeria's 
growing  need  for  secure  biometric  identification  systems  to  combat 
fraud across various sectors.

4

---

<!-- PAGE 5 -->

O.I. Odufisan, O.V. Abhulimen and E.O. Ogunti

Journal of Economic Criminology 7 (2025) 100127

6.2.  Behavior analysis

Customer behavior  analysis is a powerful tool for fraud detection. 
ML algorithms can analyze a user's historical transaction data, spending 
habits, and online activity to establish a baseline for their typical be-
havior  (Jóhannsson,  2017).  Deviations  from  this  baseline,  such  as 
sudden spikes in purchase amounts, unusual purchases from unfamiliar 
locations,  or  a  rapid  increase  in  login  attempts  from  geographically 
distant locations, can all be red flags for potential fraudulent activity.  
Sadgali  et  al.  (2021)  offered  a  behavior  analysis  approach  that  uses 
cardholder  behavior  to  identify  credit  card  fraud.  Their  methodology 
makes use of a hybrid machine learning strategy that combines fuzzy 
logic,  association  rule  learning,  and  rough  set  theory  to  analyze  user 
behavior and produce rules for spotting fraudulent transactions while 
maintaining low processing times. For health insurance fraud detection,  
Lu et al. (2023a, 2023b) introduced a noteworthy behavioral analysis 
model, MHAMFD using attributed heterogeneous information networks 
(AHINs),  to  capture the  complex  interactions  that  exist between  phy-
sicians, hospitals, patients, and other healthcare providers. This meth-
odology  incorporates  behavioral  linkages  across  visits,  going  beyond 
individual  patient  data  analysis  and  by  giving  priority  to  the  most 
pertinent  relationships,  MHAMFD's  hierarchical  attention  mechanism 
improves the accuracy of fraud detection and provides comprehensible 
results  that  can  direct  the  inquiries  of  healthcare  practitioners.  By 
continuously  monitoring  behavior  patterns,  ML  systems  can  identify 
anomalies  and  flag suspicious  accounts  for  further  investigation. This 
proactive  approach  allows  organizations  to  take  preventive  measures 
before fraudulent transactions occur.

6.3.  Anomaly detection

Machine learning excels at anomaly detection, making it a powerful 
tool  for  fraud  prevention.  Anomaly  detection  algorithms  can  analyze 
various  amounts  of  data  in  real-time,  searching  for  deviations  from 
established  patterns  that  might  indicate  fraudulent  activity.  These 
patterns could include unusual transaction amounts, a sudden increase 
in  activity  from  a  dormant  account,  or  multiple  login  attempts  from 
geographically  disparate  locations  in  a  short  timeframe  (Hilal  et  al., 
2022). Researchers are exploring different machine learning techniques 
to enhance fraud detection in this area. For instance, Patrik et al. (2020) 
proposed a system that combines machine learning's strength in iden-
tifying  suspicious  transactions  with  the  power  of  graph  databases  to 
unearth connections between data points in an approach addressing the 
limitations of standalone machine learning methods, which might miss 
crucial relationships within the data, to achieved a high accuracy rate 
in fraud detection. Another is the research by Okechukwu et al. (2023) 
which utilizes a deep learning technique called a feed-forward neural 
network  to  achieve  a  97 %  detection  rate  for  fraudulent  credit  card 
transactions and phishing websites, demonstrating machine learning's 
effectiveness in identifying anomalies that deviate from normal banking 
activities.  Anomaly  detection  in  financial  statements  of  Vietnamese 
listed companies was investigated in a paper by Lokanan et al. (2019) 
that  not  only  confirm  the  effectiveness  of  machine  learning  in  un-
covering  irregularities  but  also  suggest  its  potential  for  ranking  com-
panies  based  on  their financial  health, particularly  valuable  in  devel-
oping economies. Real-time monitoring allows organizations to swiftly 
identify  and  respond  to  potential  fraud  attempts,  minimizing  losses. 
When anomalies are detected, the system can alert relevant personnel 
for further investigation.

6.4.  Risk assessment

ML  can  be  harnessed  to  create  robust  risk  assessment  models  to 
analyze  various  factors  associated  with  a  transaction,  such  as  the 
amount,  location,  type  of  purchase,  and  the  user's  past  behavior 
(Fraud.net,  2024).  By  assigning  a  risk  score  to  each  transaction,  the

system can prioritize which transactions require further scrutiny. One 
approach,  explored  by  Guan  et  al.  (2023),  combines  ML  with  human 
expertise  to  strengthen  credit  risk  assessments  in  a  that  research  de-
monstrates that ML models, particularly when trained on limited data, 
can benefit from the addition of Ripple-Down Rules (RDR) created by a 
domain expert. These RDRs capture valuable insights that can improve 
the  model's  accuracy  and  fairness,  especially  in  handling  cases  like 
fraud detection and prevention. A thorough framework using five dif-
ferent  algorithms  (Logistic  Regression,  SVM,  XGBoost,  GAN  with  au-
toencoder, and OCSVM) was developed by Lu et al. (2023a, 2023b) in 
research investigating machine learning's potential for corporate fraud 
detection in China. The merits of machine learning in risk assessment 
are  reinforced  by  their  findings  which  shows  supervised  learning 
techniques to be beneficial, as demonstrated by XGBoost's remarkable 
accuracy  in  spotting  fraudulent  organizations.  Using  such  techniques 
for risk assessment in fraud detection efforts is made more compelling 
by  the  alignment  of  machine  learning  algorithms  with  pertinent  fi-
nancial  data.  Risk assessment in  credit  transactions was  examined  by  
Malik et al. (2024), in a research that detailed the benefits of machine 
learning  (ML)  algorithms  fraud  detection  and  using  large  datasets  to 
produce  faster,  more  accurate  judgments  while  analyzing  the  draw-
backs  of  conventional  approaches.  Several  machine  learning  models, 
such  as  Support  Vector  Machines,  Random  Forests,  and  Logistic  Re-
gression, show how good they are at assessing credit risk, were studied. 
They also dug into feature engineering strategies for extracting useful 
information  from  financial  data,  which  adds  significantly  to  ML  and 
may be used to improve risk assessment procedures and create a more 
secure financial environment. This  risk-based approach will allow or-
ganizations  in  Nigeria  to  allocate  resources  efficiently.  High-risk 
transactions can be flagged for immediate investigation, while low-risk 
transactions can be processed smoothly, minimizing disruption for le-
gitimate users.

6.5.  Text analysis

The  digital  world  generates  a  vast  amount  of  text  data,  including 
emails, social media posts, and customer reviews. ML algorithms can be 
employed  to  analyze  this  unstructured  data  and  identify  patterns  or 
keywords that might indicate fraud or scams (Goyal et al., 2020). For 
example, ML can detect suspicious language or phrasing often used in 
phishing attempts, protecting unsuspecting users from falling victim to 
these  deceptive  tactics.  Phua  et  al.  (2010)  explored  the  use  of  text 
analysis and machine learning to detect fraudulent emails using a da-
taset of emails classified as valid or spam, employing algorithms such as 
Support  Vector  Machines  (SVM),  Random  Forest,  Naive  Bayes,  and 
Decision Tree classifiers. According to the results, SVM had the highest 
accuracy, hitting over 98 % and this shows how text analysis, enabled 
by  machine  learning  method,  may  greatly  enhance  the  detection  of 
fraud in email correspondence, which is a common medium for frau-
dulent activities. Oladimeji (2019) also investigated the application of 
machine learning for phishing email detection in Nigeria and suggested 
methods such as Naive Bayes and Support Vector Machines with the use 
of pre-processing techniques such as word embedding and stemming to 
categorize phishing attempts with high accuracy. This study opens the 
door for more investigation into the use of machine learning in Nigeria 
to  counteract  different  types  of  fraud  attempts  by  demonstrating  the 
technology's  potential  for textual  analysis-based  fraud  detection.  Text 
analysis applications can also be seen in financial data in research by Li 
et al. (2023), in China examining the effectiveness of ML in analyzing a 
firm's  Management  Discussion  and  Analysis  (MDA)  section  for  fraud 
detection  and  highlighting  the  potential  of  text  analysis.  This  paper 
demonstrated  how  machine  learning  (ML)  may  be  used  to  analyze 
sentiment,  readability,  and  forward-looking  statements  in  addition  to 
financial data and also to show that when textual analysis is added to 
financial  measures,  fraud  detection  algorithms  perform  better.  This 
Chinese study suggests that textual data analysis from financial reports

5

---

<!-- PAGE 6 -->

O.I. Odufisan, O.V. Abhulimen and E.O. Ogunti

Journal of Economic Criminology 7 (2025) 100127

and communications will serve as a potent tool for fraud identification 
and  prevention. These insightful  findings apply to the  Nigerian situa-
tion.

environment,  encouraging  economic  growth  and  empowering  its  citi-
zens to participate confidently in the digital age.

7.  Benefits of AI and ML in fraud detection

Fraudsters are continuously coming up with new plans, finding ways 
around restrictions, and taking advantage of regulation gaps. The pro-
blem  is  made  even  more  difficult  by  the  enormous  amount  of  data 
produced in today's digital environment. When handling large datasets, 
manual analysis becomes unreliable and ineffective, making organiza-
tions  susceptible  to  fraudulent  activity  that  goes  unnoticed  (Reurink, 
2018). By leveraging AI and ML, organizations may create resilient and 
flexible fraud detection systems to protect their operations.

One of the most compelling benefits of AI and ML in fraud detection 
lies  in  their  ability  to  perform  real-time  analysis.  Unlike  traditional 
methods  that  rely  on  historical  data  analysis,  AI  systems  can  con-
tinuously analyze data  streams  as  they occur. This  allows for  the  im-
mediate identification of anomalies in real time (Bansal et al., 2024). 
Imagine a scenario where a fraudster attempts to make an unauthorized 
withdrawal  from  a  bank  account.  An  AI-powered  system,  constantly 
monitoring  transaction  activity,  can  detect  this  anomaly  in  real-time 
and trigger an alert. This swift intervention can potentially prevent the 
fraudulent transaction from being completed, safeguarding the account 
holder's funds.

Furthermore, AI excels in handling scalability. An explosion of data 
characterizes the digital age (Theodorakopoulos et al., 2024). Financial 
institutions, e-commerce platforms, and other sectors generate massive 
datasets daily. Manually analyzing such vast quantities of data for po-
tential fraud is not only time-consuming but also prone to human error. 
AI  systems,  on  the  other  hand,  can  effortlessly  process  and  analyze 
these  large  datasets,  identifying  hidden  patterns  and  anomalies  that 
might  escape  human  scrutiny  (Khurana,  2020).  This  comprehensive 
analysis  strengthens  fraud  detection  efforts,  leading  to  a  more  secure 
digital environment for all stakeholders.

Another significant advantage of AI and ML is their ability to reduce 
false  positives  (Bansal  et  al.,  2024).  Conventional  fraud  detection 
techniques frequently result in a large percentage of false positives or 
transactions  that are  lawful  but are  incorrectly  marked  as  suspicious. 
This interferes with user experiences in addition to wasting expensive 
resources.  However,  to  reduce  false  positives,  AI  algorithms  can  be 
continuously trained and improved. Artificial intelligence (AI) systems 
grow  proficient  at  differentiating  between  authentic  and  fraudulent 
behavior by absorbing fresh information on fraudulent behaviors and 
learning from previous encounters. The utilization of a targeted strategy 
lessens the workload for human analysts, allowing them to concentrate 
their  skills  on  examining  the  most  crucial  instances.  This  results  in  a 
fraud detection system that is more effective and efficient.

The potential of AI and ML to reveal hidden patterns is perhaps its 
most exciting feature (Amiri et al., 2024). Even with their great skill, 
human  analysts  are  not  immune  to  the  subtle,  complicated  patterns 
hidden in large datasets. AI, on the other hand, is remarkably good at 
recognizing  patterns.  Artificial  intelligence  (AI)  systems  can  spot 
minute  links  and  connections  in  data  that  humans  might  miss.  This 
makes  it  possible  to  identify  fraudulent  activity  types  that  were  pre-
viously  unidentified,  allowing  for  the  proactive  adoption  of  counter-
measures  before  the  development  of  widespread  risks.  Consider  the 
scenario  where  an  artificial  intelligence  system  discovers  a  new 
phishing scheme aimed at gullible internet buyers. AI can protect the 
integrity  of  the  e-commerce  ecosystem  and  stop  many  people  from 
becoming victims by recognizing the telltale signals of this fraudulent 
scam (Bansal et al., 2024).

8.  Challenges in AI-powered fraud detection systems

Although  machine  learning  (ML)  and  artificial  intelligence  (AI) 
provide a potent tool in the battle against fraud, there are obstacles in 
the  way  of  their  application.  When  implementing  AI-powered  fraud 
detection systems, organizations need to be ready to face a variety of 
challenges from technological constraints to legal issues.

The  availability  and  quality  of  data  present  one  difficulty  (Lin, 
2024).  High-quality  and  pertinent  data  is  essential  for  AI  systems  to 
train  and  improve  their  detection  models.  Inaccurate,  out-of-date,  or 
incomplete  data  can  seriously  impair  these  algorithms'  performance. 
The matter is made more complex by privacy concerns and data rules, 
which may restrict the number of extensive datasets that are available 
for AI systems to use for learning (Mothukuri et al., 2021). Organiza-
tions need to become adept at striking a careful balance between pro-
tecting access to essential information, guaranteeing data integrity, and 
adhering to privacy rules.

Another  challenge  is  integrating  AI  fraud  detection  solutions  with 
the current infrastructure (Bello and Olufemi, 2024). Modern AI and ML 
technologies  might  not  be  easily  integrated  with  legacy  systems,  re-
quiring major modifications or  even total rebuilds. During the transi-
tion phase, there may be downtime or decreased functionality due to 
this resource-intensive and disruptive integration procedure. AI system 
integration requires meticulous planning and execution on the part of 
organizations  to  minimize  interruptions  and  guarantee  a  seamless 
transition (Challoumis, 2024).

Another  big  obstacle  is  that  fraud  is  a  constantly  changing  field. 
Fraudsters are always coming up with new strategies and plans to get 
around detection systems (Hilal et al., 2022). No matter how sophisti-
cated, AI models need to be updated frequently with the most recent 
information  on  fraudulent  activity  to  be  successful.  This  means  that 
continual training of the AI system is required to keep it flexible and 
proactive in the battle against fraud. AI systems that are static and non- 
adaptive  become  vulnerable  when  scammers  create  new  methods 
(Adhikari et al., 2024).

Beyond moral and legal obligations, there are other barriers to ef-
ficient AI-powered fraud detection. Ensuring compliance with relevant 
regulations,  such  as  privacy  and  data  protection  statutes  like  the 
Nigeria  Data  Protection  Regulation  (NDPR),  is  imperative  for  organi-
zations (BanwoandIghodalo, 2023). When AI is used in decision-making 
processes,  ethical  concerns  arise.  Certain  client  segments  may  be 
treated  unfairly  as  a  result  of  algorithmic  biases  (Akter  et  al.,  2021). 
Businesses must carefully traverse a variety of ethical and legal situa-
tions when utilizing AI for fraud detection to maintain ethical standards 
and assure compliance.

Data quality, system integration, the evolving threat landscape, and 
regulatory considerations all demand careful attention. By proactively 
addressing  these  challenges  and  fostering  a  culture  of  continuous 
learning and adaptation, organizations can leverage the power of AI to 
create  robust  and  ethical  fraud  detection  systems,  safeguarding  their 
digital operations and fostering trust with their customers.

9.  The future of AI and machine learning in redefining financial 
crime prevention in Nigeria

As we move forward, advancements in AI and ML technologies hold 
immense promise for creating a more robust and secure financial eco-
system. Here we explore the exciting possibilities that lie ahead in the 
future of AI and ML in financial crime prevention.

Real-time  analysis,  scalability,  reduced  false  positives,  and  the 
ability  to  uncover  hidden  patterns  are  just  a  few  of  the  compelling 
benefits  that  AI  and  ML  bring  to  the  table.  By  embracing  these  ad-
vancements, Nigeria can create a more secure and trustworthy digital

AI systems are capable of constant learning and evolution, in con-
trast to conventional fraud detection techniques that depend on static 
rules. AI models may continuously improve their detection capabilities 
by  being  exposed  to  massive  volumes  of  data,  including  past  fraud

6

---

<!-- PAGE 7 -->

O.I. Odufisan, O.V. Abhulimen and E.O. Ogunti

Journal of Economic Criminology 7 (2025) 100127

attempts,  new  threats,  and  even  successful  fraudulent  behaviors 
(Hassan  et  al.,  2023).  This  guarantees  that  the  system  remains  in-
novative,  adjusting  to  the  ever-evolving  strategies  employed  by  con 
artists.  AI  systems  that  can  recognize  not  only  conventional  money 
laundering schemes but also cutting-edge methods that take advantage 
of newly available financial goods or social engineering advances will 
be available in the near future (Bello and Olufemi, 2024).

Transformers, known for their success in natural language proces-
sing  (NLP)  and  sequence  modelling,  are  emerging  as  transformative 
tools in fraud detection. Their ability to model sequential dependencies 
makes  them  ideal  for  identifying  fraud  patterns  in  transaction  se-
quences and detecting sophisticated schemes, such as synthetic identity 
fraud and collusion. Transformers provide deeper insights into complex 
typologies,  helping  organizations  stay  ahead  of  increasingly  sophisti-
cated threats (Vaswani et al., 2017; Wang et al., 2023).

More than just responding to current threats is in store for AI and 
ML in the future. The potential for proactive fraud prevention exists in 
many domains of advancement. AI models can forecast, with growing 
accuracy, the location and timing of fraud attempts by sifting through 
enormous volumes of previous data, looking for trends linked to frau-
dulent  activity  (Martins  and  Fonkem,  2024).  With  the  help  of  this 
predictive capability, businesses can avert fraudulent acts before they 
do  harm  by  enforcing  stricter  security  procedures  or  putting  in  place 
real-time transaction monitoring (Bansal et al., 2024). An artificial in-
telligence  system  that  can  recognize  suspicious  transactions  based  on 
historical data and emerging patterns and forecast which user profiles 
or  accounts  are  most  susceptible  to  future  fraud  attempts  is  one  ex-
ample.

In  addition,  a  more  comprehensive  method  of  fraud  detection  is 
anticipated  as  AI  and  ML  become  more  prevalent  in  financial  crime 
prevention. Nowadays, several organizations frequently concentrate on 
their own internal data while conducting fraud detection operations in 
silos  (Gade,  2024).  These  silos,  however,  can  be  dismantled  by  AI- 
powered solutions, which also make it possible to analyze data from a 
wide range of sources, including social media platforms, banks, telecom 
companies,  and  government  agencies  (Ola-Oluwa,  2024).  A  more 
comprehensive understanding of fraudulent activity will be provided by 
this cooperative approach, enabling law enforcement to more success-
fully locate and take down intricate criminal networks.

The fusion of AI and other technologies to build a more complete 
security  ecosystem  is  another  fascinating  trend.  For  example,  block-
chain technology provides an immutable record of transactions, which 
makes it an ideal match for AI-driven fraud detection systems (Taher 
et al., 2024). Also, quantum computing introduces the potential to solve 
complex fraud detection challenges by rapidly analyzing vast datasets 
and uncovering intricate patterns that classical computing struggle to 
process using AI (Innan et al., 2024). Through the integration of these 
technologies,  organizations  can  establish  a  more  secure  environment 
that not only identifies fraudulent actions but also stops them entirely 
and rapidly. The likelihood of fraudulent transactions being completed 
can  be  considerably  decreased  by  this  smooth  combination  of  block-
chain, quantum computing and AI.

Finally, the future holds promise for the development of more so-
phisticated AI algorithms. These algorithms will be capable of not only 
detecting  existing  fraud  typologies  but  also  identifying  entirely  new 
ones as they emerge. This will be fueled by the ever-increasing volume 
and  variety  of  data  available  for  AI  models  to  learn  from  (Bello  and 
Olufemi,  2024).  Imagine  an  AI  system  that  can  not  only  recognize 
traditional phishing attempts based on email language patterns but can 
also detect novel social engineering tactics that exploit emerging social 
media trends or leverage deepfakes to impersonate legitimate entities. 
By staying ahead of the curve and continuously adapting to new threats, 
AI will become a powerful weapon in the fight against financial crime. 
There is enormous potential for AI and machine learning to combat 
financial  crime  in  Nigeria  in  the  future.  AI  provides  an  impressive 
toolkit  that  includes  sophisticated  algorithms  capable  of  identifying

new  fraud  schemes,  interacting  with  existing  security  systems,  and 
proactive protection. Nigeria can protect its people and enterprises in 
the digital era by embracing these innovations and encouraging cross- 
sector collaboration to build a stronger and more secure financial en-
vironment.

10.  Conclusion

Fraud across various sectors in Nigeria is a major economic threat, 
and  traditional  methods  are  failing  due  to  constantly  evolving  fraud 
schemes and the vast amount of data. This paper explores how Artificial 
Intelligence  (AI)  and  Machine  Learning  (ML)  can  revolutionize  fraud 
detection.  AI  and  ML  excel  at  recognizing  patterns  in  large  datasets, 
enabling  real-time  anomaly  detection  and  proactive  measures.  The 
benefits  include  improved  accuracy,  adaptability,  and  efficient  data 
handling. Challenges like data quality and ethical considerations exist, 
but advancements in AI and ML algorithms, integration with technol-
ogies like blockchain, and a focus on prevention hold immense promise 
for  the  future.  By  embracing  AI  and  ML  responsibly,  collaborating 
across sectors, and prioritizing ethics, Nigeria can create a more secure 
digital environment that safeguards its citizens and businesses.

To  build  a  safer  digital  future  in  Nigeria,  several  key  re-
commendations  are  essential.  Firstly,  financial  institutions,  govern-
ments, and businesses should invest in AI and ML for fraud detection. 
Secondly, robust data security practices and adherence to privacy laws 
are crucial for building trust in AI. Thirdly, cross-sector collaboration 
between banks, telecoms, and government agencies is needed to fight 
complex  financial  crimes.  Finally,  public  awareness  campaigns  can 
educate  citizens  about  online  safety  and  evolving  fraud  tactics,  em-
powering them to protect themselves.

CRediT authorship contribution statement

Erastus  Olarenwaju  Ogunti:  Supervision,  Conceptualization. 
Osekhonmen  Victory  Abhulimen:  Writing  –  review  &  editing, 
Validation, Project administration, Formal analysis. Oluwaseun Isaac 
Odufisan: Writing – original draft, Investigation.

Declaration of Competing Interest

The authors declare that they have no known competing financial 
interests  or  personal  relationships  that  could  have  appeared  to  influ-
ence the work reported in this paper.

Declaration of Generative AI And AI-Assisted Technologies in the 
Writing Process

During the preparation of this work the author(s) used ChatGPT in 
order to improve language and readability ONLY. After using this tool, 
the author(s) reviewed and edited the content as needed and take(s) full 
responsibility for the content of the publication.

References

Abhulimen, O., Ogunti, E., 2021. Facial age estimation using deep learning: a review. 
methods 8 (5) http://www.jmest.org/wp-content/uploads/JMESTN42353774.pdf.

Abhulimen, V.O., Ogunti, O.E., 2022. Automatic age estimation of persons with dark skin 
tone using deep learning approach. Int. J. Comput. Digit. Syst. 12 (1), 1183–1189. 
https://doi.org/10.12785/ijcds/120194

Adewumi, B., 2024. Nigeria: Artificial Intelligence to push E-Commerce fraud to &107bln.

Niger. Trib https://www.zawya.com/en/economy/africa/nigeria-artificial-in-
telligence-to-push-ecommerce-fraud-to-107bln-xvcqts0q (Accessed 25 October 
2024).

Adhikari, P., Hamal, P., Baidoo, F., 2024. Artificial Intelligence in fraud detection: re-

volutionizing financial security. Int. J. Sci. Res. Arch. 13 (01), 1457–1472. https:// 
doi.org/10.30574/ijsra.2024.13.1.1860

Afriyie, J.K., Tawiah, K., Pels, W.A., Addai-Henne, S., Dwamena, H.A., Owiredu, E.O.,

Ayeh, S.A., Eshun, J., 2023. A supervised machine learning algorithm for detecting 
and predicting fraud in credit card transactions. Decis. Anal. J. 6, 100163. https:// 
doi.org/10.1016/j.dajour.2023.100163

7

---

<!-- PAGE 8 -->

O.I. Odufisan, O.V. Abhulimen and E.O. Ogunti

Journal of Economic Criminology 7 (2025) 100127

Akinniyi, A.J., Erinsakin, O.A., Emma-Ayire, S.O., 2021. Corruption in the Nigerian

education sector: causes and remedies. KIU Interdiscip. J. Humanit. Soc. Sci. 2 (2), 
1–13.

Akintaro, S., 2023. Banks’ losses to frauds hit N5.79 billion in Q2 2023 – FITC – 
Nairametrics. https://nairametrics.com/2023/08/24/banks-losses-to-frauds/ 
(Accessed 18 March 2024).

Akokuwebe, M.E., Idemudia, E.S., 2023. Fraud within the Nigerian health system, a

double threat for resilience of a health system and the response to the COVID-19 
pandemic: a review. Pan Afr. Med. J. 45 (1) https://www.ajol.info/index.php/pamj/ 
article/view/266454/251429.

Akter, S., McCarthy, G., Sajib, S., Michael, K., Dwivedi, Y.K., D’Ambra, J., Shen, K.N.,

2021. Algorithmic bias in data-driven innovation in the age of AI. Int. J. Inf. Manag. 
60, 102387. https://doi.org/10.1016/j.ijinfomgt.2021.102387

Ali, H.I.H., Alhassan, A., 2021. Fighting contract cheating and ghostwriting in Higher 
Education: Moving towards a multidimensional approach. Cogent Educ. 8 (1), 
1885837. https://doi.org/10.1080/2331186X.2021.1885837

Alordiah, C., Omumu, F., Kaizar, V., 2023. Investigating why students in Nigeria perceive 
education as a scam. J. Appl. Learn. Teach. 6 (1), 234–243 https://journals.sfu.ca/ 
jalt/index.php/jalt/article/download/685/589.

Amiri, Z., Heidari, A., Navimipour, N.J., Unal, M., Mousavi, A., 2024. Adventures in data 
analysis: a systematic review of Deep Learning techniques for pattern recognition in 
cyber-physical-social systems. Multimed. Tools Appl. 83 (8), 22909–22973. https:// 
doi.org/10.1007/s11042-023-16382-x

Arslan, B., Yorulmaz, E., Akca, B., Sagiroglu, S., 2016. Security Perspective of Biometric 
Recognition and Machine Learning Techniques, pp. 492–497. https://doi.org/10. 
1109/ICMLA.2016.0087.

AxiomQ, 2022. 6 Types Of eCommerce Fraud and How To Prevent Them. Retrieved from: 
https://axiomq.com/blog/6-types-of-ecommerce-fraud-and-how-to-prevent-them/ 
(Accessed 18 March 2024).

Bansal, U., Bharatwal, S., Bagiyam, D.S., Kismawadi, E.R., 2024. Fraud detection in the

era of AI: Harnessing technology for a safer digital economy. In: AI-Driven 
Decentralized Finance and the Future of Finance. IGI Global, pp. 139–160. https:// 
doi.org/10.4018/979-8-3693-6321-8.ch006

Banwo&Ighodalo, 2023. Nigeria Data Protection Act: What Individuals, Businesses And 
Organizations Should Know. https://banwo-ighodalo.com/assets/grey-matter/ 
908710c62e3fce362d559eaf7ee7932f.pdf (Accessed 10 October 2024).

Bello, O.A., Folorunso, A., Ogundipe, A., Kazeem, O., Budale, A., Zainab, F., Ejiofor, O.E.,

2022. Enhancing cyber financial fraud detection using deep learning techniques: a 
study on neural networks and anomaly detection. Int. J. Netw. Commun. Res. 7 (1), 
90–113 https://tudr.org/id/eprint/3107.

Hassan, M., Aziz, L.A.R., Andriansyah, Y., 2023. The role artificial intelligence in modern 
banking: an exploration of AI-driven approaches for enhanced fraud prevention, risk 
management, and regulatory compliance. Rev. Contemp. Bus. Anal. 6 (1), 110–132 
https://researchberg.com/index.php/rcba/article/download/153/148.

Hilal, W., Gadsden, S.A., Yawney, J., 2022. Financial fraud: a review of anomaly detec-
tion techniques and recent advances. Expert Syst. Appl. 193, 116429. https://doi. 
org/10.1016/j.eswa.2021.116429. https://www.grrbe.in/Vol-10-issue-05/GRRBE_L_ 
100100910201121320.pdf.

Innan, N., Sawaika, A., Dhor, A., Dutta, S., Thota, S., Gokal, H., ... Bennai, M., 2024.

Financial fraud detection using quantum graph neural networks. Quant. Mach. Intell. 
6 (1), 7. https://doi.org/10.1007/s42484-024-00143-6.

Jóhannsson, J., 2017. Detecting fraudulent users using behaviour analysis. [Online].

Available: https://api.semanticscholar.org/CorpusID:79756.

Juniper Research, 2022. Online Payment Fraud Losses to Exceed $343 Billion Globally. 
https://www.juniperresearch.com/press/online-payment-fraud-losses-to-exceed- 
343bn/ (Accessed 17 March 2024).  https://www.juniperresearch.com/press/online- 
payment-fraud-losses-to-exceed-343bn/ (Accessed 17 March 2024).

Kamuangu, P., 2024. A Review on Financial Fraud Detection using AI and Machine

Learning. J. Econ. Financ. Account. Stud. 6 (1), 67–77. https://doi.org/10.32996/ 
jefas.2024.6.1.7

Kasaraneni, B.P., 2024. Machine learning models for fraud detection in health insurance 
claims: techniques, applications, and real-world case studies. J. Mach. Learn. Pharm. 
Res. 4 (1), 110–147 https://pharmapub.org/index.php/jmlpr/article/download/ 
42/40.

Khurana, R., 2020. Fraud detection in ecommerce payment systems: The role of pre-

dictive ai in real-time transaction security and risk management. Int. J. Appl. Mach. 
Learn. Comput. Intell. 10 (6), 1–32 https://neuralslate.com/index.php/Machine- 
Learning-Computational-I/article/view/155.

Komandla, V., 2024. Enhancing Security and Fraud Prevention in Fintech: Comprehensive 
Strategies for Secure Online Account Opening. Glob. Res. Rev. Bus. Econ. 10 (5), 
102–112.

Li, J., Li, N., Xia, T., Guo, J., 2023. Textual analysis and detection of financial fraud:

Evidence from Chinese manufacturing firms. Econ. Model. 126, 106428. https://doi. 
org/10.1016/j.econmod.2023.106428

Lin, A.K., 2024. The AI revolution in financial services: emerging methods for fraud de-
tection and prevention. J. Galaksi 1 (1), 43–51. https://doi.org/10.70103/galaksi. 
v1i1.5

Liu, Q., Hagenmeyer, V., Keller, H.B., 2021. A review of rule learning-based intrusion

detection systems and their prospects in smart grids. IEEE Access 9, 57542–57564. 
https://doi.org/10.1109/ACCESS.2021.3071263

Bello, H.O., Ige, A.B., Ameyaw, M.N., 2024. Adaptive machine learning models: concepts 
for real-time financial fraud prevention in dynamic environments. World J. Adv. Eng. 
Technol. Sci. 12 (02), 021–034. https://doi.org/10.30574/wjaets.2024.12.2.0266

Bello, O.A., Olufemi, K., 2024. Artificial intelligence in fraud prevention: exploring

Lokanan, M., Tran, V., Vuong, N.H., 2019. Detecting anomalies in financial statements 
using machine learning algorithm: the case of Vietnamese listed firms. Asian J. 
Account. Res. 4 (2), 181–201. https://doi.org/10.1108/AJAR-09-2018-0032 
Lu, Q., Fu, C., Nan, K., Fang, Y., Xu, J., Liu, J., Bellotti, A.G., Lee, B.G., 2023. Chinese

techniques and applications challenges and opportunities. Comput. Sci. IT Res. J. 5 
(6), 1505–1520. https://doi.org/10.51594/csitrj.v5i6.1252

corporate fraud risk assessment with machine learning. Intell. Syst. Appl. 20, 200294. 
https://doi.org/10.1016/j.iswa.2023.200294

Boonkrong, S., 2024. Design of an academic document forgery detection system. Int. J.

Inf. Technol. 1–13. https://doi.org/10.1007/s41870-024-02006-6

Castelblanco, A., Solano, J., Lopez, C., Rivera, E., Tengana, L., Ochoa, M., 2020. Machine

Learning Techniques for Identity Document Verification in Uncontrolled 
Environments: A Case Study. pp. 271–281. https://doi.org/10.1007/978-3-030- 
49076-8_26.

Challoumis, C., 2024. the Future of Business-integrating AI Into the Financial Cycle. XIV

Int. Sci. Conf. 44–78.

Chen, J., Lai, K.L., 2021. Deep convolution neural network model for credit-card fraud 
detection and alert. J. Artif. Intell. Capsul. Netw. 3 (1), 101–112. https://doi.org/10. 
36548/jaicn.2021.2.003

Drammeh, F., 2023. Trust and Fraud in Nigeria: A Comprehensive Analysis of

Socioeconomic Factors and Regulatory Measures. https://dx.doi.org/10.2139/ssrn. 
4475135.

Emiroğlu, E.E., 2023. Texture Analysis and Classification by Deep Architectures for Paper 
Fraud Detection (Doctoral dissertation, Middle East Technical University (Turkey)). 
https://open.metu.edu.tr/bitstream/handle/11511/105954/thesis.pdf.

Eneji, C.V.O., Petters, J.S., Esuabana, S.B., Onnoghen, N.U., Udumo, B.O., Ambe, B.A., 
Essien, E.E., Unimna, F.A., Alawa, D.A., Ikutal, A., 2022. University academic dis-
honesty and graduate quality for national development and global competitiveness: 
Nigerian universities in perspective. Int. J. Learn., Teach. Educ. Res. 21 (5), 401–427. 
https://doi.org/10.26803/ijlter.21.5.20

Fraud.net, 2024. How to use machine learning for fraud detection and prevention.

https://fraud.net/n/how-to-use-machine-learning-for-fraud-detection-and-preven-
tion/ (Accessed 19 March 2024).

Gade, K.R., 2024. Beyond data quality: building a culture of data trust. J. Comput. Inf. 
Technol. 4 (1) https://universe-publisher.com/index.php/jcit/article/download/ 
5/5.

Gayam, S.R., 2020. AI-driven fraud detection in E-commerce: advanced techniques for

anomaly detection, transaction monitoring, and risk mitigation. Distrib. Learn. Broad 
Appl. Sci. Res. 6, 124–151 https://dlabi.org/index.php/journal/article/download/ 
108/105.

Goyal, M.A., Singh, M.S., Sharma, E.S., 2020. Fraud detection on social media using data 
analytics. Int. J. Eng. Res. Technol. 9. https://doi.org/10.17577/IJERTV9IS010204 
Guan, C., Suryanto, H., Mahidadia, A., Bain, M., Compton, P., 2023. Responsible credit 
risk assessment with machine learning and knowledge acquisition. Hum. -Centr 
Intell. Syst. 3 (3), 232–243. https://doi.org/10.1007/s44230-023-00035-1

Gupta, P., 2023. Leveraging machine learning and artificial intelligence for fraud pre-
vention. SSRG Int. J. Comput. Sci. Eng. 10 (5), 47–52. https://doi.org/10.14445/ 
23488387/IJCSE-V10I5P107

Lu, J., Lin, K., Chen, R., Lin, M., Chen, X., Lu, P., 2023. Health insurance fraud detection 
by using an attributed heterogeneous information network with a hierarchical at-
tention mechanism. BMC Med. Inform. Decis. Mak. 23 (1), 62. https://doi.org/10. 
1186/s12911-023-02152-0

Malik, P., Anand, A., Baliyan, A.K., Dongre, A., Panwar, P., 2024. Credit risk assessment 
and fraud detection in financial transactions using machine learning. J. Electr. Syst. 
20, 2061–2069. https://doi.org/10.52783/jes.1807

Manyo, T.S., Walter, M.H., Bassey, O.E., Wonah, O.G., Omang, B.A., Ekpo, N.S., Chike, 
E.C., 2023. Effect of fraud on commercial banks’ performance in Nigeria. Front. 
Manag. Sci. 2 (2), 69–78. https://doi.org/10.56397/FMS.2023.04.08

Martins, O., Fonkem, B., 2024. Leveraging big data analytics to combat emerging fi-
nancial fraud schemes in the USA. A Lit. Rev. Pract. Implic. https://doi.org/10. 
30574/wjarr.2024.24.1.2999

Mothukuri, V., Parizi, R.M., Pouriyeh, S., Huang, Y., Dehghantanha, A., Srivastava, G.,

2021. A survey on security and privacy of federated learning. Future Gener. Comput. 
Syst. 115, 619–640. https://doi.org/10.1016/j.future.2020.10.007

Mutemi, A., Bacao, F., 2024. E-commerce fraud detection based on machine learning

techniques: systematic literature review. Big Data Min. Anal. 7 (2), 419–444 https:// 
ieeexplore.ieee.org/iel7/8254253/10506765/10506811.pdf.

Nagpal, N., Srivastava, A., Verma, P., 2024. AI-powered proctoring: safeguarding online 
assessment in the education 5.0. In: Explainable AI for Education: Recent Trends and 
Challenges. Springer Nature Switzerland, Cham, pp. 271–285. https://doi.org/10. 
1007/978-3-031-72410-7_15

Nnamoko, N., Barrowclough, J., Liptrott, M., Korkontzelos, I., 2022. A behaviour bio-
metrics dataset for user identification and authentication. Data Brief. 45, 108728. 
https://doi.org/10.1016/j.dib.2022.108728

Noah, A.O.K., Adesope, J.A., 2022. Phenomenon of Corrupt Practices: Admission rack-
eteering by Staff in Public Tertiary Institutions in Lagos. Nigeria, pp. 194–208.

Okechukwu, O.P., Okechukwu, G.N., Mbonu, C.E., Paul, R.U., 2023. A deep learning 
model for detecting anomalies in the banking sector using a feed-forward neural 
network. Int. J. Sci. Eng. Res. 14, 322–327 ISSN 2229-5518.

Okolie, U.C., Ojomo, A.H., 2020. E-commerce in Nigeria: benefits and challenges.

Humanit. Soc. Sci. Latv. 28 (2). https://doi.org/10.22364/hssl.28.2.05

Okonkwo, N.O., Idika, N.K., Kalu, S.A., 2024. DIgital economy and its implications for

sustainable economic growth in Nigeria. Adv. J. Arts, Humanit. Soc. Sci. 7 (3), 40–53 
https://aspjournals.org/ajahss/index.php/ajahss/article/view/100.

Okoye, E.I., Gbegi, D.O., 2013. An evaluation of the effect of fraud and related financial

crimes on the Nigerian economy.  856 (33), 1–23. https://doi.org/10.12816/0001221 
Oladimeji, O.O., 2019. Text analysis and machine learning approach to phished email

detection. Int. J. Comput. Appl. 182 (36). https://doi.org/10.5120/ijca2019918354

8

---

<!-- PAGE 9 -->

O.I. Odufisan, O.V. Abhulimen and E.O. Ogunti

Journal of Economic Criminology 7 (2025) 100127

Ola-Oluwa, J.A., 2024. Impact of Artificial Intelligence (AI) in enhancing knowledge

sharing and boosting organizational efficiency in Nigerian enterprises. Afr. J. Manag. 
Bus. Res. 17 (1), 76–95. https://doi.org/10.62154/ajmbr

Oloni, V., 2024. From Brick to Click: E-commerce and the Future of Retail. https://www. 
verivafrica.com/insights/from-brick-to-click-e-commerce-and-the-future-of-retail 
(Accessed 24 October 2024).

Oluwole, V., 2024. 4 African countries with highest scam losses in 2024. Business Insider 
Africa. https://africa.businessinsider.com/local/markets/african-countries-with- 
highest-scam-losses/wrvpj5k (Accessed 15 December 2024).

Paul, H., Nikolaev, A., 2021. Fake review detection on online E-commerce platforms: a 
systematic literature review. Data Min. Knowl. Discov. 35 (5), 1830–1881. https:// 
doi.org/10.1007/s10618-021-00772-6

Phua, C., Lee, V., Smith, K., Gayler, R., 2010. A comprehensive survey of data mining-

based fraud detection research. arXiv Prepr. arXiv 1009.6119.

Finance: Bias, Ethics, and Security. IGI Global, pp. 90–120. https://doi.org/10.4018/ 
979-8-3693-2185-0.ch005

Taher, S.S., Ameen, S.Y., Ahmed, J.A., 2024. Advanced fraud detection in blockchain

transactions: an ensemble learning and explainable AI approach. Eng. Technol. Appl. 
Sci. Res. 14 (1), 12822–12830. https://doi.org/10.48084/etasr.6641

Takyar, A., 2024. Financial fraud detection using machine learning models. https://www.

leewayhertz.com/build-financial-fraud-detection-system-using-ML-models/ 
(Accessed 19 March 2024).

Theodorakopoulos, L., Theodoropoulou, A., Stamatiou, Y., 2024. A state-of-the-art review 
in big data management engineering: real-life case studies, challenges, and future 
research directions. Eng 5 (3), 1266–1297. https://doi.org/10.3390/eng5030068 
Thornton, D., Brinkhuis, M., Amrit, C., Aly, R., 2015. Categorizing and describing the

types of fraud in healthcare. Procedia Comput. Sci. 64, 713–720. https://doi.org/10. 
1016/j.procs.2015.08.594

Pratik, S., Ashwin, Suresh, G., Sushant, I., 2020. Anomaly detection using machine

Tripathi, A., Thakar, S.V., 2024. Ethical use of AI for academic integrity: preventing

learning. Int. J. Innov. Sci. Res. Technol. (IJISRT 5 (3), 1458–1461 https://bit.ly/ 
2ycrxti.

Rai, A.K., Dwivedi, R.K., 2020. Fraud detection in credit card data using unsupervised 
machine learning based scheme. In: 2020 International Conference on Electronics 
and Sustainable Communication Systems (ICESC). IEEE, pp. 421–426. https://doi. 
org/10.1109/icesc48915.2020.9155615

Reurink, A., 2018. Financial fraud: a literature review. J. Econ. Surv. 32 (5), 1292–1325.

https://doi.org/10.1111/joes.12294

Sadgali, I., Sael, N., Benabbou, F., 2021. Human behavior scoring in credit card fraud

detection. IAES Int. J. Artif. Intell. 10 (3), 698. https://doi.org/10.11591/ijai.v10.i3. 
pp698-706

plagiarism and cheating. Ethic Framew. Spec. Educ.: A Guide Res. 91.

Vaswani, A., Shazeer, N., Parmar, N., Uszkoreit, J., Jones, L., Gomez, A.N., Kaiser, L.,

Polosukhin, I., 2017. Attention is all you need. Adv. Neural Inf. Process. Syst https:// 
user.phil.hhu.de/∼cwurm/wp-content/uploads/2020/01/7181-attention-is-all-you- 
need.pdf.

Wang, H., Zheng, J., Carvajal-Roca, I.E., Chen, L., Bai, M., 2023, August, August.

Financial fraud detection based on deep learning: towards large-scale pre-training 
transformer models. In: China Conference on Knowledge Graph and Semantic 
Computing. Springer Nature Singapore, Singapore, pp. 163–177. https://doi.org/10. 
1007/978-981-99-7224-1_13

Yange, T.S., 2019. A fraud detection system for health insurance in Nigeria. J. Health

Sarker, I.H., 2021. Machine learning: algorithms, real-world applications and research 
directions. SN Comput. Sci. 2, 160. https://doi.org/10.1007/s42979-021-00592-x

Inform. Afr. 6 (2), 64–73. https://doi.org/10.12856/JHIA-2019-v6-i2-256 
Yousefi, N., Alaghband, M., Garibay, I., 2019. A comprehensive survey on machine

Sharma, R., Mehta, K., Sharma, P., 2024. Role of artificial intelligence and machine

learning in fraud detection and prevention. In: Risks and Challenges of AI-Driven

learning techniques and user authentication approaches for credit card fraud detec-
tion. Retrieved from: arXiv preprint arXiv:1912.02629.

9

<!-- MARKITDOWN CONVERSION -->

<!-- Full MarkItDown conversion for formatting fidelity. -->

Journal of Economic Criminology 7 (2025) 100127

Contents lists available at ScienceDirect

Journal of Economic Criminology

journal homepage: www.journals.elsevier.com/journal-of-economic-criminology

Harnessing artificial intelligence and machine learning for fraud detection
and prevention in Nigeria
Oluwaseun Isaac Odufisana, Osekhonmen Victory Abhulimenb,⁎
a Department of Computer Engineering, The Federal University of Technology Akure, Ondo State PMB 704, Nigeria
b Department of Information and Communication Engineering, Elizade University, Ilara-Mokin 340271, Ondo State PMB 002, Nigeria

, Erastus Olarenwaju Oguntia

]]]]

]]]]]]

A R T I C L E   I N F O

A B S T R A C T

Keywords:
Artificial Intelligence
Machine learning
Fraud

Fraud  poses  a  significant  threat  to  Nigeria's  burgeoning  digital  economy,  impacting  sectors  like  finance,  e-
commerce, healthcare, and education. Traditional methods struggle to keep pace with evolving fraud schemes.
This  paper  investigates  the  potential  of  Artificial  Intelligence  (AI)  and  Machine  Learning  (ML)  for  enhanced
fraud  detection  and  prevention  in  Nigeria.  We  explore  various  AI  methodologies,  including  supervised,  un-
supervised,  and deep  learning. We discuss their applications in anomaly detection, behavioural analysis, risk
scoring, and network analysis. By leveraging AI's continuous learning capabilities, organizations can adapt to
novel fraud tactics. The paper highlights the benefits of AI-powered fraud detection, including increased effi-
ciency,  improved  accuracy,  and proactive  risk  mitigation. However,  challenges  like  technical limitations  and
regulatory considerations are acknowledged. Lastly, we examine the promising future of AI and ML in trans-
forming the financial crime prevention situation in Nigeria.

1.  Introduction

The  digital  revolution  has  undeniably  transformed  Nigeria,  en-
couraging  increased  connectedness  and  accelerating  growth.  From  e-
commerce and digital banking to e-learning and telemedicine, the di-
gital  revolution  is  empowering  Nigerians  with  tools  to  bridge  infra-
structural  gaps,  access  global  opportunities,  and  drive  sustainable
growth across various sectors (Okonkwo et al., 2024).

However,  despite  this  transformative  impact  of  the  digital  revolu-
tion in Nigeria, it has also given rise to a significant challenge: an in-
crease in fraud in several industries. Fraud has become a serious con-
cern, endangering not only businesses but also the country's financial
stability,  affecting  everything  from  e-commerce  and  healthcare  to
education. The consequences of these crimes go far beyond the lives of
the specific victims; they affect the basis of the Nigerian economy itself.
Companies  suffer  catastrophic  losses,  customer  confidence  declines,
and there is a general decline in the perception of security associated
with digital transactions (Okoye and Gbegi, 2013). This worrying pat-
tern presents a worrisome picture. Global reports on fintech and pay-
ments show that between 2023 and 2027, online payment fraud alone is
projected  to  cost  firms  globally  more  than  $343  billion  (Juniper
Research,  2022).  In  Nigeria,  the  effects  are  felt  not  only  by  large  or-
ganizations  but  also  by  regular  people  who  become  victims  of  fake

online  markets,  identity  theft,  and  various  other  forms  of  deception
(Oluwole, 2024). The complexity of fraudsters is simply surpassing that
of traditional systems of fraud detection, which rely on strict standards
and  manual  checks.  A  paradigm  change  is  required  at  this  crucial
juncture  to  create  a  new  line  of  defense  that  is  powered  by  artificial
intelligence (AI) and machine learning (ML) (Kamuangu, 2024).

Artificial  Intelligence  is  the  capability  of  machines  to  imitate  in-
telligence in human behaviour, attained by examining how the human
brain thinks and how it learns, decides, and works in solving a specific
problem  (Abhulimen  and  Ogunti,  2021).  AI  aims  to  replicate  these
capabilities in machines, enabling them to perform tasks that typically
require human intelligence, such as reasoning, understanding language,
recognizing patterns, and adapting to new inputs. AI can take various
forms,  including  expert  systems,  speech  recognition  tools,  and  ad-
vanced robotics, and it is driven by methods that enable machines to act
intelligently, even in complex or unpredictable situations.

Machine  learning,  on  the  other  hand,  is  a  subset  of  AI  that  uses
algorithms  that  analyze  large  amounts  of  data,  identify  patterns,  and
make predictions or decisions based on that information (Sarker, 2021).
For instance, ML algorithms are designed to improve their accuracy and
efficiency over time as they are exposed to more data. Unlike traditional
programming, where developers write explicit rules, ML systems "learn"
these rules automatically through training processes.

⁎

Corresponding author.
E-mail addresses: oluwaseun.odufisan@gmail.com (O.I. Odufisan), osekhonmen.abhulimen@elizadeuniversity.edu.ng (O.V. Abhulimen),

eoogunti@futa.edu.ng (E.O. Ogunti).

https://doi.org/10.1016/j.jeconc.2025.100127
Received 21 October 2024; Received in revised form 1 January 2025; Accepted 6 January 2025
2949-7914/© 2025 The Author(s). Published by Elsevier Ltd. This is an open access article under the CC BY-NC-ND license (http://creativecommons.org/licenses/
by-nc-nd/4.0/).

O.I. Odufisan, O.V. Abhulimen and E.O. Ogunti

Journal of Economic Criminology 7 (2025) 100127

AI and machine learning developments are revolutionizing the fight
against fraud and provide a glimmer of hope in the fight against these
crimes. Real-time pattern recognition and data analysis are possible for
AI  systems  because  of  their  capacity  to  emulate  human  cognitive
functions.  Because  of  this,  they  can  detect  suspicious  activities  that
would  go  undetected  by  conventional  means.  These  computers  may
identify  irregularities  that  may  indicate  possible  fraud  attempts  in  a
matter of seconds by filtering through enormous datasets at an aston-
ishingly fast pace (Gupta, 2023).

This paper looks into how AI and ML might be revolutionary tools in
the  fight  against  fraud,  particularly  in  Nigeria.  We  will  examine  how
companies and organizations across a variety of sectors, such as banking,
e-commerce,  healthcare,  and  education,  may  use  these  technologies  to
detect and prevent fraud. By evaluating massive volumes of data, spotting
intricate trends, and making real-time modifications that will result in a
more  lucrative  and  safer  digital  environment  for  Nigerians,  AI  and  ML
offer a cutting-edge defense against the schemes of fraudsters.

Both primary and secondary data were used to explore the role of AI
and ML in fraud detection and prevention in Nigeria. Secondary data
was sourced from various credible academic publications, industry re-
ports, government records, and global fraud studies, including datasets
on fraud trends, technological adoption, and sectorial impacts. Primary
data,  though  limited,  consisted  of  expert  insights  obtained  through
unstructured interviews with stakeholders in the Nigerian banking and
finance, e-commerce, healthcare, and educational sectors. Additionally,
anecdotal  evidence  based  on  our  experiences  as  residents  in  Nigeria
provided contextual understanding. These sources provided a founda-
tion for understanding the broader context of fraud in Nigeria, the ef-
fectiveness of AI and ML technologies globally, and the practical chal-
lenges and adoption barriers.

2.  Economic impact of fraud in Nigeria across various sectors

The insidious nature of fraud extends far beyond the immediate fi-
nancial losses inflicted upon individuals and businesses. In a nation like
Nigeria,  striving  for  economic  prosperity  and  digital  inclusion,  fraud
acts as a pernicious force, eroding trust, hindering growth, and stifling
innovation (Drammeh, 2023). This chapter explores how fraud affects
the economy in many different ways, including banking and finance, e-
commerce, healthcare, and education. It also emphasizes how urgently
artificial  intelligence  (AI)  and  machine  learning  (ML)  are  needed  as
revolutionary countermeasures.

2.1.  Banking and finance

Manyo  et  al.  (2023),  in  their  research,  revealed  that  the  financial
sector is a frequent target for fraudsters, with consequences extending
beyond  immediate  financial  losses.  The  research  further  reveals  that
banks  facing  fraudulent  transactions  suffer  significant  financial  set-
backs, which negatively affect their profitability and ability to invest in
crucial services. This disruption affects the flow of credit to both busi-
nesses and individuals, slowing down economic growth. Additionally,
the  rise  in  financial  fraud  undermines  public  trust  in  the  banking
system,  discouraging  the  use  of  digital  financial  services  and  thereby
impeding  the  government's  efforts  to  promote  financial  inclusion,
which is critical for poverty reduction and economic development.

A report by Akintaro (2023) highlighted the scale of the problem in
Nigeria, where 24 commercial banks lost N5.79 billion to fraud in the
second  quarter  (Q2)  of  2023  -  an  increase  of  1125 %  from  the  N472
million lost in the first quarter (Q1) of the same year. The total value of
fraudulent transactions also surged dramatically from N2.58 billion to
N9.75 billion, increasing by nearly 278 % from Q1 to Q2. Fraudulent
loans accounted for 94.35 % of these losses, revealing a serious flaw in
the Nigerian banking system. These fraudulent loans divert funds from
honest  businesses  and  entrepreneurs,  stifling  new  business  formation
and job creation, which are crucial to economic development.

The report (Akintaro, 2023) also reveals that other types of fraud,
including mobile and computer fraud, pose additional threats. Mobile
fraud,  responsible  for  3.39 %  of  the  total  losses,  undermines  trust  in
mobile banking platforms, a key driver of financial inclusion. Computer
and  web  fraud,  amounting  to  N59.5  million,  highlights  the  ongoing
vulnerability of online banking systems, deterring both consumers and
businesses  from  engaging  with  digital  services,  thus  hindering  the
growth of the digital economy.

2.2.  E-commerce

E-commerce in Nigeria has the potential to drive economic growth,
foster  innovation,  and  open  new  opportunities.  However,  fraud  on
payment platforms presents a significant barrier to this growth. Recent
increases  in  fraud  have  made  the  e-commerce  environment  fearful,
causing  consumers  to  be  hesitant  about  online  purchases  due  to  con-
cerns about payment security. This reluctance leads to a preference for
cash-on-delivery,  slowing  the  government's  push  for  a  cashless
economy (Okolie and Ojomo, 2020).

E-commerce fraud comes in many forms, affecting both consumers
and merchants. Consumers face risks like account takeover, mobile SIM
switch  fraud,  and  social  engineering  tactics  such  as  phishing.  These
threats damage their trust in online transactions and increase the risk of
financial  loss  (Komandla,  2024).  Merchants,  on  the  other  hand,  en-
counter  fraud  like  identity  theft,  chargeback  fraud,  and  man-in-the-
middle  attacks,  which  result  in  financial  losses  and  discourage  other
businesses  from  entering  the  e-commerce  space  (Mutemi  and  Bacao,
2024).

Other types of fraud, such as card testing, refund fraud, friendly
fraud,  triangulation  fraud  and  interception  fraud  add  to  the  com-
plexity of the problem. Card testing uses stolen credit card informa-
tion  for  small  purchases  to  test  its  validity,  while  refund  fraud  ex-
ploits  stolen  payment  information  to  claim  refunds  for  fake
overpayments.  Friendly  fraud  occurs  when  customers  falsely  claim
they  didn’t  receive  their  goods  to  get  a  refund. Triangulation  fraud
involves  fake  online  stores  stealing  customer  information  to  make
purchases from legitimate merchants. Interception fraud occurs when
a  person  uses  a  stolen  card  with  the  provided  address  and  billing
information  to  make  a  purchase,  then  intercepts  the  package  for
themselves (AxiomQ, 2022).

The  economic  impact  of  e-commerce  fraud  in  Nigeria  is  clear.  It
deters online purchases, hampers the growth of cashless transactions,
and  creates  a  climate  of  distrust.  Merchants  face  significant  financial
risks  and  become  hesitant  to  continue  in  the  industry,  stalling  the
sector's growth potential.

Projections  indicates  a  significant  increase  in  financial  losses  over
the coming years. It is expected to escalate globally from $44.3 billion
in 2024 to $107 billion by 2029, marking a 14 % increase (Adewumi,
2024). The rapid growth of Nigeria’s e-commerce market presents an
increased opportunity for E-commerce fraudsters (Oloni, 2024)

2.3.  Healthcare

Healthcare fraud in Nigeria is a significant issue with serious eco-
nomic and social impacts, undermining the quality of care and the in-
tegrity of the healthcare system. Medical identity theft and fraudulent
claims  divert  resources  from  patients  who  genuinely  need  care.  This
leads to compromised healthcare delivery and creates inefficiencies in
the system (Akokuwebe and Idemudia, 2023).

A  common  form  of  fraud  involves  submitting  inaccurate  or  mis-
leading information to health insurance companies, tricking them into
paying for unapproved benefits. In Nigeria, healthcare providers often
engage in double billing, charging for services multiple times, or billing
for  treatments  that  were  never  received  (Yange,  2019).  This  practice
burdens the National Health Insurance Scheme (NHIS), increasing costs
and reducing the effectiveness of care.

2

O.I. Odufisan, O.V. Abhulimen and E.O. Ogunti

Journal of Economic Criminology 7 (2025) 100127

‘Ghost patients’ are another fraudulent tactic where claims are filed
for individuals who do not exist. In addition, stolen identities are used
to  submit  fraudulent  claims,  adding  further  complexity  to  the  issue
(Thornton  et  al.,  2015).  There  is  also  a  risk  of  collusion  between  pa-
tients and healthcare professionals, where bribes are exchanged to fa-
cilitate false claims.

These  fraudulent activities  result  in  increased  administrative  costs
and reduced profitability for insurance companies, ultimately leading to
higher  premiums  for  average  Nigerians.  Patients  suffer  too,  as  false
claims deplete the funds needed for essential healthcare infrastructure,
resulting in reduced access to quality care for those in need.

2.4.  Education

The Nigerian education sector faces significant challenges from ex-
amination fraud falsified scholarship applications, and fake credentials,
all of which erode public trust and weaken the integrity of the system.
These dishonest practices harm the quality of education and workforce
readiness, denying opportunities to deserving students while benefiting
unqualified  individuals. As a  result, economic  growth and  innovation
are  stifled  due  to  an  inadequately  trained  workforce  (Alordiah  et  al.,
2023).

Examination  fraud  undermines  fair  evaluation,  from  simple
cheating  to  bribing  invigilators.  Students  who  cheat  gain  an  unfair
advantage,  damaging  the  reputation  of  educational  institutions  and
leading  to  a  generation  ill-prepared  for  their  careers.  Employers,  fru-
strated by unreliable academic credentials, struggle to hire competent
workers, further hindering economic progress (Eneji et al., 2022).

Admission fraud is another concern, where students gain university
entry through bribes or forged documents, bypassing academic merit.
This  weakens  the  intellectual  standard  of  institutions,  diminishes  op-
portunities for deserving students, and results in unqualified graduates
who are ill-equipped for the workforce (Noah and Adesope, 2022) This
not only affects their financial prospects but also poses risks to public
safety in fields that require technical expertise.

Contract cheating, where students outsource their academic work to
third-party  services  (Ali,  and  Alhassan,  2021),  threatens  the  learning
process by allowing students to "buy" their achievements. This erodes
the development of critical thinking and knowledge acquisition, leading
to  a  workforce  deficient  in  these  essential  skills,  further  stalling  eco-
nomic progress.

Lastly, teacher fraud, though less common, also contributes to aca-
demic decline. Teachers  may inflate grades or  use fake  credentials to
secure  employment,  compromising  the  quality  of  teachers  (Akinniyi
et al., 2021). This deprives students of necessary skills, affecting their
future success and reducing the overall productivity of the workforce.
Addressing these forms of educational fraud through strict measures
and  fostering  a  culture  of  academic  honesty  is  crucial  to  improving
Nigeria’s education system, workforce, and economy.

3.  Traditional method of fraud detection

To  safeguard  their  operations  and  customers,  organizations  have
traditionally relied on a combination of pre-defined rules and manual
analysis for fraud detection. While these methods have served a purpose
in the past, they are increasingly proving inadequate in the face of ever-
evolving threats.

Limitations in terms of adaptability are among the biggest problems
with traditional fraud detection techniques (Bello et al., 2024). Usually,
these systems work with a predetermined set of rules that identify ac-
tions  that  meet  predetermined  standards  or  surpass  predetermined
bounds. These regulations may have worked well in the past, but they
are unable to keep up with how fraud is changing. To get beyond these
pre-established  red  flags,  fraudsters  are  always  coming  up  with  fresh
ideas  and  strategies.  It  is  frequently  a  time-consuming  and  slow  pro-
cedure to update these rule-based systems to handle new threats (Liu

et al., 2021). There is a gap in the detection rules that allows for the
introduction of new fraud strategies, which provides an opportunity for
fraudsters to take advantage of (Takyar, 2024). A fraudster might easily
get around an e-commerce platform regulation that flags transactions
over a particular amount as possibly fraudulent by breaking up a large
purchase  into  several  smaller  transactions,  each  of  which  falls  below
the threshold and so avoids detection.

Traditional  methods  also  suffer  from  a  lack  of  sophistication  in
pattern recognition. Fraudulent operations may involve complex links
and connections between different data points (Hilal et al., 2022). The
use of a new user account, a billing address that is different from the
shipping  address,  and  an attempt  to  buy  a  remote  location are  a  few
examples of the various components of a fraudulent transaction. Hand
analysis or rule-based algorithms that focus on individual data points
alone could overlook these subtle but significant patterns.

Finally,  traditional  methods  face  significant  scalability  challenges.
An explosion of data characterizes the digital age (Theodorakopoulos
et al., 2024). The amount of data points, user interactions, and online
transactions is growing constantly, making human analysis of this data
more challenging and time-consuming. Traditional methods may be ill-
suited to effectively handle these enormous datasets. This may result in
an accumulation of unprocessed data, which could give rise to chances
for fraudulent operations to evade detection.

While traditional fraud detection methods have played a historical
role  in  safeguarding  organizations,  their  limitations  are  becoming  in-
creasingly  apparent  in  today's  dynamic  digital  landscape.  Their  in-
ability  to  adapt  to  evolving  threats,  identify  complex  patterns,  and
handle large datasets creates vulnerabilities that fraudsters can exploit
(Bansal et al., 2024). As we move forward, there is a critical need for
more robust and adaptable solutions to combat fraud.

4.  The urgency for AI intervention

Fraudulent  actions  undermine  confidence,  divert  resources,  and
inhibit  innovation  in  a  variety  of  sectors,  including  financial  organi-
zations,  e-commerce platforms, healthcare  providers,  and educational
institutions.  At  this pivotal  moment, machine  learning  (ML)  and  arti-
ficial  intelligence  (AI)  emerge  as  game-changing  solutions  to  tackle
these ubiquitous problems (Sharma et al., 2024).

Traditional  methods  of  fraud  detection  have  proven  increasingly
inadequate. Manual processes are slow, error-prone, and overwhelmed
by  the  ever-evolving  tactics  of  fraudsters.  Legacy  systems  struggle  to
identify  complex  patterns  hidden  within  vast  amounts  of  data.  (Hilal
et al., 2022). This is where AI and ML offer a powerful solution.

AI's ability to analyze massive datasets and identify subtle anomalies
makes it ideal for fraud detection. Machine learning algorithms can be
trained on historical fraud cases to recognize patterns and predict fu-
ture  fraudulent  activities.  This  allows  for  real-time  monitoring  of
transactions,  flagging  suspicious  activity  before  it  can  cause  financial
harm (Bansal et al., 2024).

In  the  banking  and  finance sector,  AI  can analyze  customer beha-
vior,  spending  patterns,  and  account  activity  to  identify  potential
fraudulent loans, unauthorized access attempts, and money laundering
schemes (Hassan et al., 2023). This empowers financial institutions to
take  proactive  measures,  such  as  account  freezes  or  additional  au-
thentication steps, to mitigate losses.

The e-commerce sector stands to gain immensely from AI-powered
fraud  detection.  AI  can  analyze  customer  purchase  history,  IP  ad-
dresses, and device fingerprints to identify suspicious orders that may
be  linked  to  stolen  credit  card  information  (Gayam,  2020).  Ad-
ditionally, AI can be used to detect fake reviews and identify fraudulent
merchants  operating  on  e-commerce  platforms  (Paul  and  Nikolaev,
2021).

The healthcare sector can leverage AI to combat fraudulent claims
and  identity  theft.  AI  algorithms  can  analyze  medical  records,  billing
data, and patient information to identify anomalies that may indicate

3

O.I. Odufisan, O.V. Abhulimen and E.O. Ogunti

Journal of Economic Criminology 7 (2025) 100127

fraudulent activity (Kasaraneni, 2024) This can help healthcare provi-
ders and insurance companies prevent misuse of resources and ensure
that funds are directed towards genuine medical needs.

The  education  sector  can  utilize  AI  to  combat  examination  mal-
practice  and  admission  fraud.  AI-powered  proctoring systems  can  de-
tect  suspicious  behavior  during  online  exams  (Nagpal  et  al.,  2024),
while  advanced  document verification tools  can identify  forged  certi-
ficates and transcripts (Boonkrong, 2024). Furthermore, AI can analyze
student  performance  data  to  flag  potential  plagiarism  in  assignments
and essays (Tripathi and Thakar, 2024).

The  urgency  for  AI  intervention  in  combating  fraud  cannot  be
overstated.  By  leveraging  the  power  of  AI  and  ML,  Nigeria  can  safe-
guard its economy, build trust within critical sectors, and empower its
citizens  to  participate  with  confidence  in  a  digital  future.  As  AI  con-
tinues  to  evolve,  its  capabilities  in  fraud  detection  will  only  become
more sophisticated, paving the way for a more secure and prosperous
Nigeria.

the interconnected neurons in the human brain, allowing them to learn
and adapt with remarkable efficiency. CNNs excel at image recognition,
making  them  ideal  for  analyzing  images  of  signatures,  checks,  or
identification  documents  to  identify  forgeries  or  alterations  used  in
fraudulent  attempts  (Emiroğlu,  2023).  Imagine  a  CNN  analyzing  a
scanned copy of a driver's license. By recognizing subtle inconsistencies
in  the  document's  formatting  or  identifying  signs  of  tampering,  CNN
can  flag  the  document  as  potentially  fraudulent,  helping  to  prevent
identity  theft.  RNNs,  on  the  other  hand,  are  adept  at  sequential  data
analysis, making them valuable for fraud detection in financial trans-
actions where the order and timing of events can be crucial for iden-
tifying suspicious  activity (Bello et  al., 2022). An  RNN can analyze a
series of bank transactions, paying close attention to the sequence and
timing of each event. By identifying unusual patterns, such as a rapid
succession of withdrawals from geographically distant ATMs, the RNN
can flag the account for potentially fraudulent activity.

5.  AI and machine learning approaches for effective fraud
detection and prevention

6.  Some common applications of machine learning in fraud
detection and prevention

While  AI  provides  the  broad  framework  for  intelligent  systems,
Machine Learning (ML) serves as the engine that drives its effectiveness
in  fraud  detection.  Machine  Learning  (ML)  is  a  subset  of  AI  that  em-
powers machines to identify patterns and improve their performance on
a specific task without explicit programming (Sarker, 2021). There are
three main categories of Machine Learning algorithms particularly well-
suited to combatting fraud in Nigeria's digital sectors.

5.1.  Supervised learning

One way to conceptualize supervised learning is as a pupil carefully
studying  under  an  instructor.  The  teacher  is  the  labelled  data  in  this
comparison, where each data point has a label that corresponds to its
category  (fraudulent  or  valid  transaction,  for  example).  For  example,
financial  institutions  can  use  transaction  data  from  the  past  to  train
models  that  identify  trends  linked  to  fraud.  Like  the  student,  these
models are always picking up new skills and honing the ones they al-
ready  have  in  recognizing  patterns.  Supervised  learning-enabled  AI
systems  can  evaluate  fresh  transactions  in  real-time  and  mark  those
with  questionable  patterns  for  additional  examination  (Afriyie  et  al.,
2023). This makes it possible to take preventative action, which may
stop financial losses before they happen.

5.2.  Unsupervised learning

Unsupervised learning takes a different approach. It is particularly
valuable  for  detecting  novel  fraud  schemes  that  do  not  conform  to
known patterns. Anomaly detection, a common unsupervised learning
technique, identifies outliers or deviations from the norm in a dataset
(Hilal et al., 2022). In the context of fraud detection, this can be used to
uncover  unusual  or  unexpected  behavior,  such  as  unusually  large
transactions originating from unfamiliar locations or sudden spikes in
account activity (Rai and Dwivedi, 2020). Imagine a scenario where a
customer with a history of modest online purchases suddenly attempts
to purchase a high-end electronic device from a new location. An un-
supervised learning model can detect this deviation from the norm and
flag it for investigation, potentially preventing a fraudulent purchase.

5.3.  Deep Learning

Deep learning, a powerful subset of ML, has gained prominence for
its ability to process vast amounts of data and extract intricate patterns.
Neural  networks,  particularly  convolutional  neural  networks  (CNNs)
and recurrent neural networks (RNNs), are at the core of deep learning
(Chen and Lai, 2021). These complex algorithms function similarly to

The following are some common applications of machine learning in

fraud detection and prevention:

6.1.  User authentication and biometric recognition

Traditional  password-based  authentication  systems  are  susceptible
to  brute-force  attacks  and  social  engineering.  Machine  learning  (ML)
algorithms can significantly enhance security by analyzing user beha-
vior  and  biometric  data  (Castelblanco et  al., 2020).  These  algorithms
can learn a user's typical login patterns, including factors like the device
used, location, and time of day. Deviations from this established base-
line can trigger alerts for potential unauthorized access attempts. Bio-
metric  recognition,  such  as  fingerprint  or  facial  recognition, adds  an-
other layer of security. ML can be used to analyze and verify biometric
data  in  real-time,  ensuring  only  authorized  users  gain  access.  Arslan
et al. (2016) explored the application of ML in biometric authentication
systems,  emphasizing  its  role  in  user  verification  and  security.  Their
review  highlights  successful  implementations  of  machine  learning  al-
gorithms like Support Vector Machines (SVMs), Naive Bayes (NB), and
Artificial Neural Networks (ANNs) in achieving high recognition rates
(80–99 %)  and  also  emphasizing  the  potential  of  ML  for  liveness  de-
tection and spoofing prevention which is a crucial aspect for robust user
authentication and fraud mitigation in financial institutions. The lim-
itations  of  traditional  passwords  were  recognized  by  Nnamoko  et  al.
(2022) thereby presenting a compelling case for behavioral biometrics
as  a  machine  learning  application  to  enhance  fraud  detection  and
prevention  in  online  transactions.  They  focused  on  leveraging  users'
inherent  behavioral  patterns,  such  as  keystroke  dynamics  and  mouse
movements,  for  user  identification,  aiming  to  improve  authentication
security  and  combat  identity  theft  in  the  financial  sector.  Abhulimen
and  Ogunti  (2022)  explored  the  use  of  residual  convolutional  neural
networks  for  age  estimation  in  a  possible  attempt  to  curb  age  falsifi-
cation crime with face images. Yousefi et al. (2019) also explored the
convergence  of  machine  learning  and  user  authentication  methods
specifically for credit card fraud detection in a survey highlighting the
limitations of static password-based authentication and exploring how
behavioral biometrics, like touch dynamics and signature patterns, can
be  leveraged  with  machine  learning  to  create  more  robust  user  au-
thentication  schemes.  Machine  learning's  ability  to  analyze  biometric
data offers an additional layer of security beyond traditional passwords
or  PINs,  effectively  distinguishing  legitimate  users  from imposters  at-
tempting  fraudulent  transactions.  This  aligns  perfectly  with  Nigeria's
growing  need  for  secure  biometric  identification  systems  to  combat
fraud across various sectors.

4

O.I. Odufisan, O.V. Abhulimen and E.O. Ogunti

Journal of Economic Criminology 7 (2025) 100127

6.2.  Behavior analysis

Customer behavior  analysis is a powerful tool for fraud detection.
ML algorithms can analyze a user's historical transaction data, spending
habits, and online activity to establish a baseline for their typical be-
havior  (Jóhannsson,  2017).  Deviations  from  this  baseline,  such  as
sudden spikes in purchase amounts, unusual purchases from unfamiliar
locations,  or  a  rapid  increase  in  login  attempts  from  geographically
distant locations, can all be red flags for potential fraudulent activity.
Sadgali  et  al.  (2021)  offered  a  behavior  analysis  approach  that  uses
cardholder  behavior  to  identify  credit  card  fraud.  Their  methodology
makes use of a hybrid machine learning strategy that combines fuzzy
logic,  association  rule  learning,  and  rough  set  theory  to  analyze  user
behavior and produce rules for spotting fraudulent transactions while
maintaining low processing times. For health insurance fraud detection,
Lu et al. (2023a, 2023b) introduced a noteworthy behavioral analysis
model, MHAMFD using attributed heterogeneous information networks
(AHINs),  to  capture the  complex  interactions  that  exist between  phy-
sicians, hospitals, patients, and other healthcare providers. This meth-
odology  incorporates  behavioral  linkages  across  visits,  going  beyond
individual  patient  data  analysis  and  by  giving  priority  to  the  most
pertinent  relationships,  MHAMFD's  hierarchical  attention  mechanism
improves the accuracy of fraud detection and provides comprehensible
results  that  can  direct  the  inquiries  of  healthcare  practitioners.  By
continuously  monitoring  behavior  patterns,  ML  systems  can  identify
anomalies  and  flag suspicious  accounts  for  further  investigation. This
proactive  approach  allows  organizations  to  take  preventive  measures
before fraudulent transactions occur.

6.3.  Anomaly detection

Machine learning excels at anomaly detection, making it a powerful
tool  for  fraud  prevention.  Anomaly  detection  algorithms  can  analyze
various  amounts  of  data  in  real-time,  searching  for  deviations  from
established  patterns  that  might  indicate  fraudulent  activity.  These
patterns could include unusual transaction amounts, a sudden increase
in  activity  from  a  dormant  account,  or  multiple  login  attempts  from
geographically  disparate  locations  in  a  short  timeframe  (Hilal  et  al.,
2022). Researchers are exploring different machine learning techniques
to enhance fraud detection in this area. For instance, Patrik et al. (2020)
proposed a system that combines machine learning's strength in iden-
tifying  suspicious  transactions  with  the  power  of  graph  databases  to
unearth connections between data points in an approach addressing the
limitations of standalone machine learning methods, which might miss
crucial relationships within the data, to achieved a high accuracy rate
in fraud detection. Another is the research by Okechukwu et al. (2023)
which utilizes a deep learning technique called a feed-forward neural
network  to  achieve  a  97 %  detection  rate  for  fraudulent  credit  card
transactions and phishing websites, demonstrating machine learning's
effectiveness in identifying anomalies that deviate from normal banking
activities.  Anomaly  detection  in  financial  statements  of  Vietnamese
listed companies was investigated in a paper by Lokanan et al. (2019)
that  not  only  confirm  the  effectiveness  of  machine  learning  in  un-
covering  irregularities  but  also  suggest  its  potential  for  ranking  com-
panies  based  on  their financial  health, particularly  valuable  in  devel-
oping economies. Real-time monitoring allows organizations to swiftly
identify  and  respond  to  potential  fraud  attempts,  minimizing  losses.
When anomalies are detected, the system can alert relevant personnel
for further investigation.

6.4.  Risk assessment

ML  can  be  harnessed  to  create  robust  risk  assessment  models  to
analyze  various  factors  associated  with  a  transaction,  such  as  the
amount,  location,  type  of  purchase,  and  the  user's  past  behavior
(Fraud.net,  2024).  By  assigning  a  risk  score  to  each  transaction,  the

system can prioritize which transactions require further scrutiny. One
approach,  explored  by  Guan  et  al.  (2023),  combines  ML  with  human
expertise  to  strengthen  credit  risk  assessments  in  a  that  research  de-
monstrates that ML models, particularly when trained on limited data,
can benefit from the addition of Ripple-Down Rules (RDR) created by a
domain expert. These RDRs capture valuable insights that can improve
the  model's  accuracy  and  fairness,  especially  in  handling  cases  like
fraud detection and prevention. A thorough framework using five dif-
ferent  algorithms  (Logistic  Regression,  SVM,  XGBoost,  GAN  with  au-
toencoder, and OCSVM) was developed by Lu et al. (2023a, 2023b) in
research investigating machine learning's potential for corporate fraud
detection in China. The merits of machine learning in risk assessment
are  reinforced  by  their  findings  which  shows  supervised  learning
techniques to be beneficial, as demonstrated by XGBoost's remarkable
accuracy  in  spotting  fraudulent  organizations.  Using  such  techniques
for risk assessment in fraud detection efforts is made more compelling
by  the  alignment  of  machine  learning  algorithms  with  pertinent  fi-
nancial  data.  Risk assessment in  credit  transactions was  examined  by
Malik et al. (2024), in a research that detailed the benefits of machine
learning  (ML)  algorithms  fraud  detection  and  using  large  datasets  to
produce  faster,  more  accurate  judgments  while  analyzing  the  draw-
backs  of  conventional  approaches.  Several  machine  learning  models,
such  as  Support  Vector  Machines,  Random  Forests,  and  Logistic  Re-
gression, show how good they are at assessing credit risk, were studied.
They also dug into feature engineering strategies for extracting useful
information  from  financial  data,  which  adds  significantly  to  ML  and
may be used to improve risk assessment procedures and create a more
secure financial environment. This  risk-based approach will allow or-
ganizations  in  Nigeria  to  allocate  resources  efficiently.  High-risk
transactions can be flagged for immediate investigation, while low-risk
transactions can be processed smoothly, minimizing disruption for le-
gitimate users.

6.5.  Text analysis

The  digital  world  generates  a  vast  amount  of  text  data,  including
emails, social media posts, and customer reviews. ML algorithms can be
employed  to  analyze  this  unstructured  data  and  identify  patterns  or
keywords that might indicate fraud or scams (Goyal et al., 2020). For
example, ML can detect suspicious language or phrasing often used in
phishing attempts, protecting unsuspecting users from falling victim to
these  deceptive  tactics.  Phua  et  al.  (2010)  explored  the  use  of  text
analysis and machine learning to detect fraudulent emails using a da-
taset of emails classified as valid or spam, employing algorithms such as
Support  Vector  Machines  (SVM),  Random  Forest,  Naive  Bayes,  and
Decision Tree classifiers. According to the results, SVM had the highest
accuracy, hitting over 98 % and this shows how text analysis, enabled
by  machine  learning  method,  may  greatly  enhance  the  detection  of
fraud in email correspondence, which is a common medium for frau-
dulent activities. Oladimeji (2019) also investigated the application of
machine learning for phishing email detection in Nigeria and suggested
methods such as Naive Bayes and Support Vector Machines with the use
of pre-processing techniques such as word embedding and stemming to
categorize phishing attempts with high accuracy. This study opens the
door for more investigation into the use of machine learning in Nigeria
to  counteract  different  types  of  fraud  attempts  by  demonstrating  the
technology's  potential  for textual  analysis-based  fraud  detection.  Text
analysis applications can also be seen in financial data in research by Li
et al. (2023), in China examining the effectiveness of ML in analyzing a
firm's  Management  Discussion  and  Analysis  (MDA)  section  for  fraud
detection  and  highlighting  the  potential  of  text  analysis.  This  paper
demonstrated  how  machine  learning  (ML)  may  be  used  to  analyze
sentiment,  readability,  and  forward-looking  statements  in  addition  to
financial data and also to show that when textual analysis is added to
financial  measures,  fraud  detection  algorithms  perform  better.  This
Chinese study suggests that textual data analysis from financial reports

5

O.I. Odufisan, O.V. Abhulimen and E.O. Ogunti

Journal of Economic Criminology 7 (2025) 100127

and communications will serve as a potent tool for fraud identification
and  prevention. These insightful  findings apply to the  Nigerian situa-
tion.

environment,  encouraging  economic  growth  and  empowering  its  citi-
zens to participate confidently in the digital age.

7.  Benefits of AI and ML in fraud detection

Fraudsters are continuously coming up with new plans, finding ways
around restrictions, and taking advantage of regulation gaps. The pro-
blem  is  made  even  more  difficult  by  the  enormous  amount  of  data
produced in today's digital environment. When handling large datasets,
manual analysis becomes unreliable and ineffective, making organiza-
tions  susceptible  to  fraudulent  activity  that  goes  unnoticed  (Reurink,
2018). By leveraging AI and ML, organizations may create resilient and
flexible fraud detection systems to protect their operations.

One of the most compelling benefits of AI and ML in fraud detection
lies  in  their  ability  to  perform  real-time  analysis.  Unlike  traditional
methods  that  rely  on  historical  data  analysis,  AI  systems  can  con-
tinuously analyze data  streams  as  they occur. This  allows for  the  im-
mediate identification of anomalies in real time (Bansal et al., 2024).
Imagine a scenario where a fraudster attempts to make an unauthorized
withdrawal  from  a  bank  account.  An  AI-powered  system,  constantly
monitoring  transaction  activity,  can  detect  this  anomaly  in  real-time
and trigger an alert. This swift intervention can potentially prevent the
fraudulent transaction from being completed, safeguarding the account
holder's funds.

Furthermore, AI excels in handling scalability. An explosion of data
characterizes the digital age (Theodorakopoulos et al., 2024). Financial
institutions, e-commerce platforms, and other sectors generate massive
datasets daily. Manually analyzing such vast quantities of data for po-
tential fraud is not only time-consuming but also prone to human error.
AI  systems,  on  the  other  hand,  can  effortlessly  process  and  analyze
these  large  datasets,  identifying  hidden  patterns  and  anomalies  that
might  escape  human  scrutiny  (Khurana,  2020).  This  comprehensive
analysis  strengthens  fraud  detection  efforts,  leading  to  a  more  secure
digital environment for all stakeholders.

Another significant advantage of AI and ML is their ability to reduce
false  positives  (Bansal  et  al.,  2024).  Conventional  fraud  detection
techniques frequently result in a large percentage of false positives or
transactions  that are  lawful  but are  incorrectly  marked  as  suspicious.
This interferes with user experiences in addition to wasting expensive
resources.  However,  to  reduce  false  positives,  AI  algorithms  can  be
continuously trained and improved. Artificial intelligence (AI) systems
grow  proficient  at  differentiating  between  authentic  and  fraudulent
behavior by absorbing fresh information on fraudulent behaviors and
learning from previous encounters. The utilization of a targeted strategy
lessens the workload for human analysts, allowing them to concentrate
their  skills  on  examining  the  most  crucial  instances.  This  results  in  a
fraud detection system that is more effective and efficient.

The potential of AI and ML to reveal hidden patterns is perhaps its
most exciting feature (Amiri et al., 2024). Even with their great skill,
human  analysts  are  not  immune  to  the  subtle,  complicated  patterns
hidden in large datasets. AI, on the other hand, is remarkably good at
recognizing  patterns.  Artificial  intelligence  (AI)  systems  can  spot
minute  links  and  connections  in  data  that  humans  might  miss.  This
makes  it  possible  to  identify  fraudulent  activity  types  that  were  pre-
viously  unidentified,  allowing  for  the  proactive  adoption  of  counter-
measures  before  the  development  of  widespread  risks.  Consider  the
scenario  where  an  artificial  intelligence  system  discovers  a  new
phishing scheme aimed at gullible internet buyers. AI can protect the
integrity  of  the  e-commerce  ecosystem  and  stop  many  people  from
becoming victims by recognizing the telltale signals of this fraudulent
scam (Bansal et al., 2024).

8.  Challenges in AI-powered fraud detection systems

Although  machine  learning  (ML)  and  artificial  intelligence  (AI)
provide a potent tool in the battle against fraud, there are obstacles in
the  way  of  their  application.  When  implementing  AI-powered  fraud
detection systems, organizations need to be ready to face a variety of
challenges from technological constraints to legal issues.

The  availability  and  quality  of  data  present  one  difficulty  (Lin,
2024).  High-quality  and  pertinent  data  is  essential  for  AI  systems  to
train  and  improve  their  detection  models.  Inaccurate,  out-of-date,  or
incomplete  data  can  seriously  impair  these  algorithms'  performance.
The matter is made more complex by privacy concerns and data rules,
which may restrict the number of extensive datasets that are available
for AI systems to use for learning (Mothukuri et al., 2021). Organiza-
tions need to become adept at striking a careful balance between pro-
tecting access to essential information, guaranteeing data integrity, and
adhering to privacy rules.

Another  challenge  is  integrating  AI  fraud  detection  solutions  with
the current infrastructure (Bello and Olufemi, 2024). Modern AI and ML
technologies  might  not  be  easily  integrated  with  legacy  systems,  re-
quiring major modifications or  even total rebuilds. During the transi-
tion phase, there may be downtime or decreased functionality due to
this resource-intensive and disruptive integration procedure. AI system
integration requires meticulous planning and execution on the part of
organizations  to  minimize  interruptions  and  guarantee  a  seamless
transition (Challoumis, 2024).

Another  big  obstacle  is  that  fraud  is  a  constantly  changing  field.
Fraudsters are always coming up with new strategies and plans to get
around detection systems (Hilal et al., 2022). No matter how sophisti-
cated, AI models need to be updated frequently with the most recent
information  on  fraudulent  activity  to  be  successful.  This  means  that
continual training of the AI system is required to keep it flexible and
proactive in the battle against fraud. AI systems that are static and non-
adaptive  become  vulnerable  when  scammers  create  new  methods
(Adhikari et al., 2024).

Beyond moral and legal obligations, there are other barriers to ef-
ficient AI-powered fraud detection. Ensuring compliance with relevant
regulations,  such  as  privacy  and  data  protection  statutes  like  the
Nigeria  Data  Protection  Regulation  (NDPR),  is  imperative  for  organi-
zations (BanwoandIghodalo, 2023). When AI is used in decision-making
processes,  ethical  concerns  arise.  Certain  client  segments  may  be
treated  unfairly  as  a  result  of  algorithmic  biases  (Akter  et  al.,  2021).
Businesses must carefully traverse a variety of ethical and legal situa-
tions when utilizing AI for fraud detection to maintain ethical standards
and assure compliance.

Data quality, system integration, the evolving threat landscape, and
regulatory considerations all demand careful attention. By proactively
addressing  these  challenges  and  fostering  a  culture  of  continuous
learning and adaptation, organizations can leverage the power of AI to
create  robust  and  ethical  fraud  detection  systems,  safeguarding  their
digital operations and fostering trust with their customers.

9.  The future of AI and machine learning in redefining financial
crime prevention in Nigeria

As we move forward, advancements in AI and ML technologies hold
immense promise for creating a more robust and secure financial eco-
system. Here we explore the exciting possibilities that lie ahead in the
future of AI and ML in financial crime prevention.

Real-time  analysis,  scalability,  reduced  false  positives,  and  the
ability  to  uncover  hidden  patterns  are  just  a  few  of  the  compelling
benefits  that  AI  and  ML  bring  to  the  table.  By  embracing  these  ad-
vancements, Nigeria can create a more secure and trustworthy digital

AI systems are capable of constant learning and evolution, in con-
trast to conventional fraud detection techniques that depend on static
rules. AI models may continuously improve their detection capabilities
by  being  exposed  to  massive  volumes  of  data,  including  past  fraud

6

O.I. Odufisan, O.V. Abhulimen and E.O. Ogunti

Journal of Economic Criminology 7 (2025) 100127

attempts,  new  threats,  and  even  successful  fraudulent  behaviors
(Hassan  et  al.,  2023).  This  guarantees  that  the  system  remains  in-
novative,  adjusting  to  the  ever-evolving  strategies  employed  by  con
artists.  AI  systems  that  can  recognize  not  only  conventional  money
laundering schemes but also cutting-edge methods that take advantage
of newly available financial goods or social engineering advances will
be available in the near future (Bello and Olufemi, 2024).

Transformers, known for their success in natural language proces-
sing  (NLP)  and  sequence  modelling,  are  emerging  as  transformative
tools in fraud detection. Their ability to model sequential dependencies
makes  them  ideal  for  identifying  fraud  patterns  in  transaction  se-
quences and detecting sophisticated schemes, such as synthetic identity
fraud and collusion. Transformers provide deeper insights into complex
typologies,  helping  organizations  stay  ahead  of  increasingly  sophisti-
cated threats (Vaswani et al., 2017; Wang et al., 2023).

More than just responding to current threats is in store for AI and
ML in the future. The potential for proactive fraud prevention exists in
many domains of advancement. AI models can forecast, with growing
accuracy, the location and timing of fraud attempts by sifting through
enormous volumes of previous data, looking for trends linked to frau-
dulent  activity  (Martins  and  Fonkem,  2024).  With  the  help  of  this
predictive capability, businesses can avert fraudulent acts before they
do  harm  by  enforcing  stricter  security  procedures  or  putting  in  place
real-time transaction monitoring (Bansal et al., 2024). An artificial in-
telligence  system  that  can  recognize  suspicious  transactions  based  on
historical data and emerging patterns and forecast which user profiles
or  accounts  are  most  susceptible  to  future  fraud  attempts  is  one  ex-
ample.

In  addition,  a  more  comprehensive  method  of  fraud  detection  is
anticipated  as  AI  and  ML  become  more  prevalent  in  financial  crime
prevention. Nowadays, several organizations frequently concentrate on
their own internal data while conducting fraud detection operations in
silos  (Gade,  2024).  These  silos,  however,  can  be  dismantled  by  AI-
powered solutions, which also make it possible to analyze data from a
wide range of sources, including social media platforms, banks, telecom
companies,  and  government  agencies  (Ola-Oluwa,  2024).  A  more
comprehensive understanding of fraudulent activity will be provided by
this cooperative approach, enabling law enforcement to more success-
fully locate and take down intricate criminal networks.

The fusion of AI and other technologies to build a more complete
security  ecosystem  is  another  fascinating  trend.  For  example,  block-
chain technology provides an immutable record of transactions, which
makes it an ideal match for AI-driven fraud detection systems (Taher
et al., 2024). Also, quantum computing introduces the potential to solve
complex fraud detection challenges by rapidly analyzing vast datasets
and uncovering intricate patterns that classical computing struggle to
process using AI (Innan et al., 2024). Through the integration of these
technologies,  organizations  can  establish  a  more  secure  environment
that not only identifies fraudulent actions but also stops them entirely
and rapidly. The likelihood of fraudulent transactions being completed
can  be  considerably  decreased  by  this  smooth  combination  of  block-
chain, quantum computing and AI.

Finally, the future holds promise for the development of more so-
phisticated AI algorithms. These algorithms will be capable of not only
detecting  existing  fraud  typologies  but  also  identifying  entirely  new
ones as they emerge. This will be fueled by the ever-increasing volume
and  variety  of  data  available  for  AI  models  to  learn  from  (Bello  and
Olufemi,  2024).  Imagine  an  AI  system  that  can  not  only  recognize
traditional phishing attempts based on email language patterns but can
also detect novel social engineering tactics that exploit emerging social
media trends or leverage deepfakes to impersonate legitimate entities.
By staying ahead of the curve and continuously adapting to new threats,
AI will become a powerful weapon in the fight against financial crime.
There is enormous potential for AI and machine learning to combat
financial  crime  in  Nigeria  in  the  future.  AI  provides  an  impressive
toolkit  that  includes  sophisticated  algorithms  capable  of  identifying

new  fraud  schemes,  interacting  with  existing  security  systems,  and
proactive protection. Nigeria can protect its people and enterprises in
the digital era by embracing these innovations and encouraging cross-
sector collaboration to build a stronger and more secure financial en-
vironment.

10.  Conclusion

Fraud across various sectors in Nigeria is a major economic threat,
and  traditional  methods  are  failing  due  to  constantly  evolving  fraud
schemes and the vast amount of data. This paper explores how Artificial
Intelligence  (AI)  and  Machine  Learning  (ML)  can  revolutionize  fraud
detection.  AI  and  ML  excel  at  recognizing  patterns  in  large  datasets,
enabling  real-time  anomaly  detection  and  proactive  measures.  The
benefits  include  improved  accuracy,  adaptability,  and  efficient  data
handling. Challenges like data quality and ethical considerations exist,
but advancements in AI and ML algorithms, integration with technol-
ogies like blockchain, and a focus on prevention hold immense promise
for  the  future.  By  embracing  AI  and  ML  responsibly,  collaborating
across sectors, and prioritizing ethics, Nigeria can create a more secure
digital environment that safeguards its citizens and businesses.

To  build  a  safer  digital  future  in  Nigeria,  several  key  re-
commendations  are  essential.  Firstly,  financial  institutions,  govern-
ments, and businesses should invest in AI and ML for fraud detection.
Secondly, robust data security practices and adherence to privacy laws
are crucial for building trust in AI. Thirdly, cross-sector collaboration
between banks, telecoms, and government agencies is needed to fight
complex  financial  crimes.  Finally,  public  awareness  campaigns  can
educate  citizens  about  online  safety  and  evolving  fraud  tactics,  em-
powering them to protect themselves.

CRediT authorship contribution statement

Erastus  Olarenwaju  Ogunti:  Supervision,  Conceptualization.
Osekhonmen  Victory  Abhulimen:  Writing  –  review  &  editing,
Validation, Project administration, Formal analysis. Oluwaseun Isaac
Odufisan: Writing – original draft, Investigation.

Declaration of Competing Interest

The authors declare that they have no known competing financial
interests  or  personal  relationships  that  could  have  appeared  to  influ-
ence the work reported in this paper.

Declaration of Generative AI And AI-Assisted Technologies in the
Writing Process

During the preparation of this work the author(s) used ChatGPT in
order to improve language and readability ONLY. After using this tool,
the author(s) reviewed and edited the content as needed and take(s) full
responsibility for the content of the publication.

References

Abhulimen, O., Ogunti, E., 2021. Facial age estimation using deep learning: a review.
methods 8 (5) http://www.jmest.org/wp-content/uploads/JMESTN42353774.pdf.

Abhulimen, V.O., Ogunti, O.E., 2022. Automatic age estimation of persons with dark skin
tone using deep learning approach. Int. J. Comput. Digit. Syst. 12 (1), 1183–1189.
https://doi.org/10.12785/ijcds/120194

Adewumi, B., 2024. Nigeria: Artificial Intelligence to push E-Commerce fraud to &107bln.

Niger. Trib https://www.zawya.com/en/economy/africa/nigeria-artificial-in-
telligence-to-push-ecommerce-fraud-to-107bln-xvcqts0q (Accessed 25 October
2024).

Adhikari, P., Hamal, P., Baidoo, F., 2024. Artificial Intelligence in fraud detection: re-

volutionizing financial security. Int. J. Sci. Res. Arch. 13 (01), 1457–1472. https://
doi.org/10.30574/ijsra.2024.13.1.1860

Afriyie, J.K., Tawiah, K., Pels, W.A., Addai-Henne, S., Dwamena, H.A., Owiredu, E.O.,

Ayeh, S.A., Eshun, J., 2023. A supervised machine learning algorithm for detecting
and predicting fraud in credit card transactions. Decis. Anal. J. 6, 100163. https://
doi.org/10.1016/j.dajour.2023.100163

7

O.I. Odufisan, O.V. Abhulimen and E.O. Ogunti

Journal of Economic Criminology 7 (2025) 100127

Akinniyi, A.J., Erinsakin, O.A., Emma-Ayire, S.O., 2021. Corruption in the Nigerian

education sector: causes and remedies. KIU Interdiscip. J. Humanit. Soc. Sci. 2 (2),
1–13.

Akintaro, S., 2023. Banks’ losses to frauds hit N5.79 billion in Q2 2023 – FITC –
Nairametrics. https://nairametrics.com/2023/08/24/banks-losses-to-frauds/
(Accessed 18 March 2024).

Akokuwebe, M.E., Idemudia, E.S., 2023. Fraud within the Nigerian health system, a

double threat for resilience of a health system and the response to the COVID-19
pandemic: a review. Pan Afr. Med. J. 45 (1) https://www.ajol.info/index.php/pamj/
article/view/266454/251429.

Akter, S., McCarthy, G., Sajib, S., Michael, K., Dwivedi, Y.K., D’Ambra, J., Shen, K.N.,

2021. Algorithmic bias in data-driven innovation in the age of AI. Int. J. Inf. Manag.
60, 102387. https://doi.org/10.1016/j.ijinfomgt.2021.102387

Ali, H.I.H., Alhassan, A., 2021. Fighting contract cheating and ghostwriting in Higher
Education: Moving towards a multidimensional approach. Cogent Educ. 8 (1),
1885837. https://doi.org/10.1080/2331186X.2021.1885837

Alordiah, C., Omumu, F., Kaizar, V., 2023. Investigating why students in Nigeria perceive
education as a scam. J. Appl. Learn. Teach. 6 (1), 234–243 https://journals.sfu.ca/
jalt/index.php/jalt/article/download/685/589.

Amiri, Z., Heidari, A., Navimipour, N.J., Unal, M., Mousavi, A., 2024. Adventures in data
analysis: a systematic review of Deep Learning techniques for pattern recognition in
cyber-physical-social systems. Multimed. Tools Appl. 83 (8), 22909–22973. https://
doi.org/10.1007/s11042-023-16382-x

Arslan, B., Yorulmaz, E., Akca, B., Sagiroglu, S., 2016. Security Perspective of Biometric
Recognition and Machine Learning Techniques, pp. 492–497. https://doi.org/10.
1109/ICMLA.2016.0087.

AxiomQ, 2022. 6 Types Of eCommerce Fraud and How To Prevent Them. Retrieved from:
https://axiomq.com/blog/6-types-of-ecommerce-fraud-and-how-to-prevent-them/
(Accessed 18 March 2024).

Bansal, U., Bharatwal, S., Bagiyam, D.S., Kismawadi, E.R., 2024. Fraud detection in the

era of AI: Harnessing technology for a safer digital economy. In: AI-Driven
Decentralized Finance and the Future of Finance. IGI Global, pp. 139–160. https://
doi.org/10.4018/979-8-3693-6321-8.ch006

Banwo&Ighodalo, 2023. Nigeria Data Protection Act: What Individuals, Businesses And
Organizations Should Know. https://banwo-ighodalo.com/assets/grey-matter/
908710c62e3fce362d559eaf7ee7932f.pdf (Accessed 10 October 2024).

Bello, O.A., Folorunso, A., Ogundipe, A., Kazeem, O., Budale, A., Zainab, F., Ejiofor, O.E.,

2022. Enhancing cyber financial fraud detection using deep learning techniques: a
study on neural networks and anomaly detection. Int. J. Netw. Commun. Res. 7 (1),
90–113 https://tudr.org/id/eprint/3107.

Hassan, M., Aziz, L.A.R., Andriansyah, Y., 2023. The role artificial intelligence in modern
banking: an exploration of AI-driven approaches for enhanced fraud prevention, risk
management, and regulatory compliance. Rev. Contemp. Bus. Anal. 6 (1), 110–132
https://researchberg.com/index.php/rcba/article/download/153/148.

Hilal, W., Gadsden, S.A., Yawney, J., 2022. Financial fraud: a review of anomaly detec-
tion techniques and recent advances. Expert Syst. Appl. 193, 116429. https://doi.
org/10.1016/j.eswa.2021.116429. https://www.grrbe.in/Vol-10-issue-05/GRRBE_L_
100100910201121320.pdf.

Innan, N., Sawaika, A., Dhor, A., Dutta, S., Thota, S., Gokal, H., ... Bennai, M., 2024.

Financial fraud detection using quantum graph neural networks. Quant. Mach. Intell.
6 (1), 7. https://doi.org/10.1007/s42484-024-00143-6.

Jóhannsson, J., 2017. Detecting fraudulent users using behaviour analysis. [Online].

Available: https://api.semanticscholar.org/CorpusID:79756.

Juniper Research, 2022. Online Payment Fraud Losses to Exceed $343 Billion Globally.
https://www.juniperresearch.com/press/online-payment-fraud-losses-to-exceed-
343bn/ (Accessed 17 March 2024).  https://www.juniperresearch.com/press/online-
payment-fraud-losses-to-exceed-343bn/ (Accessed 17 March 2024).

Kamuangu, P., 2024. A Review on Financial Fraud Detection using AI and Machine

Learning. J. Econ. Financ. Account. Stud. 6 (1), 67–77. https://doi.org/10.32996/
jefas.2024.6.1.7

Kasaraneni, B.P., 2024. Machine learning models for fraud detection in health insurance
claims: techniques, applications, and real-world case studies. J. Mach. Learn. Pharm.
Res. 4 (1), 110–147 https://pharmapub.org/index.php/jmlpr/article/download/
42/40.

Khurana, R., 2020. Fraud detection in ecommerce payment systems: The role of pre-

dictive ai in real-time transaction security and risk management. Int. J. Appl. Mach.
Learn. Comput. Intell. 10 (6), 1–32 https://neuralslate.com/index.php/Machine-
Learning-Computational-I/article/view/155.

Komandla, V., 2024. Enhancing Security and Fraud Prevention in Fintech: Comprehensive
Strategies for Secure Online Account Opening. Glob. Res. Rev. Bus. Econ. 10 (5),
102–112.

Li, J., Li, N., Xia, T., Guo, J., 2023. Textual analysis and detection of financial fraud:

Evidence from Chinese manufacturing firms. Econ. Model. 126, 106428. https://doi.
org/10.1016/j.econmod.2023.106428

Lin, A.K., 2024. The AI revolution in financial services: emerging methods for fraud de-
tection and prevention. J. Galaksi 1 (1), 43–51. https://doi.org/10.70103/galaksi.
v1i1.5

Liu, Q., Hagenmeyer, V., Keller, H.B., 2021. A review of rule learning-based intrusion

detection systems and their prospects in smart grids. IEEE Access 9, 57542–57564.
https://doi.org/10.1109/ACCESS.2021.3071263

Bello, H.O., Ige, A.B., Ameyaw, M.N., 2024. Adaptive machine learning models: concepts
for real-time financial fraud prevention in dynamic environments. World J. Adv. Eng.
Technol. Sci. 12 (02), 021–034. https://doi.org/10.30574/wjaets.2024.12.2.0266

Bello, O.A., Olufemi, K., 2024. Artificial intelligence in fraud prevention: exploring

Lokanan, M., Tran, V., Vuong, N.H., 2019. Detecting anomalies in financial statements
using machine learning algorithm: the case of Vietnamese listed firms. Asian J.
Account. Res. 4 (2), 181–201. https://doi.org/10.1108/AJAR-09-2018-0032
Lu, Q., Fu, C., Nan, K., Fang, Y., Xu, J., Liu, J., Bellotti, A.G., Lee, B.G., 2023. Chinese

techniques and applications challenges and opportunities. Comput. Sci. IT Res. J. 5
(6), 1505–1520. https://doi.org/10.51594/csitrj.v5i6.1252

corporate fraud risk assessment with machine learning. Intell. Syst. Appl. 20, 200294.
https://doi.org/10.1016/j.iswa.2023.200294

Boonkrong, S., 2024. Design of an academic document forgery detection system. Int. J.

Inf. Technol. 1–13. https://doi.org/10.1007/s41870-024-02006-6

Castelblanco, A., Solano, J., Lopez, C., Rivera, E., Tengana, L., Ochoa, M., 2020. Machine

Learning Techniques for Identity Document Verification in Uncontrolled
Environments: A Case Study. pp. 271–281. https://doi.org/10.1007/978-3-030-
49076-8_26.

Challoumis, C., 2024. the Future of Business-integrating AI Into the Financial Cycle. XIV

Int. Sci. Conf. 44–78.

Chen, J., Lai, K.L., 2021. Deep convolution neural network model for credit-card fraud
detection and alert. J. Artif. Intell. Capsul. Netw. 3 (1), 101–112. https://doi.org/10.
36548/jaicn.2021.2.003

Drammeh, F., 2023. Trust and Fraud in Nigeria: A Comprehensive Analysis of

Socioeconomic Factors and Regulatory Measures. https://dx.doi.org/10.2139/ssrn.
4475135.

Emiroğlu, E.E., 2023. Texture Analysis and Classification by Deep Architectures for Paper
Fraud Detection (Doctoral dissertation, Middle East Technical University (Turkey)).
https://open.metu.edu.tr/bitstream/handle/11511/105954/thesis.pdf.

Eneji, C.V.O., Petters, J.S., Esuabana, S.B., Onnoghen, N.U., Udumo, B.O., Ambe, B.A.,
Essien, E.E., Unimna, F.A., Alawa, D.A., Ikutal, A., 2022. University academic dis-
honesty and graduate quality for national development and global competitiveness:
Nigerian universities in perspective. Int. J. Learn., Teach. Educ. Res. 21 (5), 401–427.
https://doi.org/10.26803/ijlter.21.5.20

Fraud.net, 2024. How to use machine learning for fraud detection and prevention.

https://fraud.net/n/how-to-use-machine-learning-for-fraud-detection-and-preven-
tion/ (Accessed 19 March 2024).

Gade, K.R., 2024. Beyond data quality: building a culture of data trust. J. Comput. Inf.
Technol. 4 (1) https://universe-publisher.com/index.php/jcit/article/download/
5/5.

Gayam, S.R., 2020. AI-driven fraud detection in E-commerce: advanced techniques for

anomaly detection, transaction monitoring, and risk mitigation. Distrib. Learn. Broad
Appl. Sci. Res. 6, 124–151 https://dlabi.org/index.php/journal/article/download/
108/105.

Goyal, M.A., Singh, M.S., Sharma, E.S., 2020. Fraud detection on social media using data
analytics. Int. J. Eng. Res. Technol. 9. https://doi.org/10.17577/IJERTV9IS010204
Guan, C., Suryanto, H., Mahidadia, A., Bain, M., Compton, P., 2023. Responsible credit
risk assessment with machine learning and knowledge acquisition. Hum. -Centr
Intell. Syst. 3 (3), 232–243. https://doi.org/10.1007/s44230-023-00035-1

Gupta, P., 2023. Leveraging machine learning and artificial intelligence for fraud pre-
vention. SSRG Int. J. Comput. Sci. Eng. 10 (5), 47–52. https://doi.org/10.14445/
23488387/IJCSE-V10I5P107

Lu, J., Lin, K., Chen, R., Lin, M., Chen, X., Lu, P., 2023. Health insurance fraud detection
by using an attributed heterogeneous information network with a hierarchical at-
tention mechanism. BMC Med. Inform. Decis. Mak. 23 (1), 62. https://doi.org/10.
1186/s12911-023-02152-0

Malik, P., Anand, A., Baliyan, A.K., Dongre, A., Panwar, P., 2024. Credit risk assessment
and fraud detection in financial transactions using machine learning. J. Electr. Syst.
20, 2061–2069. https://doi.org/10.52783/jes.1807

Manyo, T.S., Walter, M.H., Bassey, O.E., Wonah, O.G., Omang, B.A., Ekpo, N.S., Chike,
E.C., 2023. Effect of fraud on commercial banks’ performance in Nigeria. Front.
Manag. Sci. 2 (2), 69–78. https://doi.org/10.56397/FMS.2023.04.08

Martins, O., Fonkem, B., 2024. Leveraging big data analytics to combat emerging fi-
nancial fraud schemes in the USA. A Lit. Rev. Pract. Implic. https://doi.org/10.
30574/wjarr.2024.24.1.2999

Mothukuri, V., Parizi, R.M., Pouriyeh, S., Huang, Y., Dehghantanha, A., Srivastava, G.,

2021. A survey on security and privacy of federated learning. Future Gener. Comput.
Syst. 115, 619–640. https://doi.org/10.1016/j.future.2020.10.007

Mutemi, A., Bacao, F., 2024. E-commerce fraud detection based on machine learning

techniques: systematic literature review. Big Data Min. Anal. 7 (2), 419–444 https://
ieeexplore.ieee.org/iel7/8254253/10506765/10506811.pdf.

Nagpal, N., Srivastava, A., Verma, P., 2024. AI-powered proctoring: safeguarding online
assessment in the education 5.0. In: Explainable AI for Education: Recent Trends and
Challenges. Springer Nature Switzerland, Cham, pp. 271–285. https://doi.org/10.
1007/978-3-031-72410-7_15

Nnamoko, N., Barrowclough, J., Liptrott, M., Korkontzelos, I., 2022. A behaviour bio-
metrics dataset for user identification and authentication. Data Brief. 45, 108728.
https://doi.org/10.1016/j.dib.2022.108728

Noah, A.O.K., Adesope, J.A., 2022. Phenomenon of Corrupt Practices: Admission rack-
eteering by Staff in Public Tertiary Institutions in Lagos. Nigeria, pp. 194–208.

Okechukwu, O.P., Okechukwu, G.N., Mbonu, C.E., Paul, R.U., 2023. A deep learning
model for detecting anomalies in the banking sector using a feed-forward neural
network. Int. J. Sci. Eng. Res. 14, 322–327 ISSN 2229-5518.

Okolie, U.C., Ojomo, A.H., 2020. E-commerce in Nigeria: benefits and challenges.

Humanit. Soc. Sci. Latv. 28 (2). https://doi.org/10.22364/hssl.28.2.05

Okonkwo, N.O., Idika, N.K., Kalu, S.A., 2024. DIgital economy and its implications for

sustainable economic growth in Nigeria. Adv. J. Arts, Humanit. Soc. Sci. 7 (3), 40–53
https://aspjournals.org/ajahss/index.php/ajahss/article/view/100.

Okoye, E.I., Gbegi, D.O., 2013. An evaluation of the effect of fraud and related financial

crimes on the Nigerian economy.  856 (33), 1–23. https://doi.org/10.12816/0001221
Oladimeji, O.O., 2019. Text analysis and machine learning approach to phished email

detection. Int. J. Comput. Appl. 182 (36). https://doi.org/10.5120/ijca2019918354

8

O.I. Odufisan, O.V. Abhulimen and E.O. Ogunti

Journal of Economic Criminology 7 (2025) 100127

Ola-Oluwa, J.A., 2024. Impact of Artificial Intelligence (AI) in enhancing knowledge

sharing and boosting organizational efficiency in Nigerian enterprises. Afr. J. Manag.
Bus. Res. 17 (1), 76–95. https://doi.org/10.62154/ajmbr

Oloni, V., 2024. From Brick to Click: E-commerce and the Future of Retail. https://www.
verivafrica.com/insights/from-brick-to-click-e-commerce-and-the-future-of-retail
(Accessed 24 October 2024).

Oluwole, V., 2024. 4 African countries with highest scam losses in 2024. Business Insider
Africa. https://africa.businessinsider.com/local/markets/african-countries-with-
highest-scam-losses/wrvpj5k (Accessed 15 December 2024).

Paul, H., Nikolaev, A., 2021. Fake review detection on online E-commerce platforms: a
systematic literature review. Data Min. Knowl. Discov. 35 (5), 1830–1881. https://
doi.org/10.1007/s10618-021-00772-6

Phua, C., Lee, V., Smith, K., Gayler, R., 2010. A comprehensive survey of data mining-

based fraud detection research. arXiv Prepr. arXiv 1009.6119.

Finance: Bias, Ethics, and Security. IGI Global, pp. 90–120. https://doi.org/10.4018/
979-8-3693-2185-0.ch005

Taher, S.S., Ameen, S.Y., Ahmed, J.A., 2024. Advanced fraud detection in blockchain

transactions: an ensemble learning and explainable AI approach. Eng. Technol. Appl.
Sci. Res. 14 (1), 12822–12830. https://doi.org/10.48084/etasr.6641

Takyar, A., 2024. Financial fraud detection using machine learning models. https://www.

leewayhertz.com/build-financial-fraud-detection-system-using-ML-models/
(Accessed 19 March 2024).

Theodorakopoulos, L., Theodoropoulou, A., Stamatiou, Y., 2024. A state-of-the-art review
in big data management engineering: real-life case studies, challenges, and future
research directions. Eng 5 (3), 1266–1297. https://doi.org/10.3390/eng5030068
Thornton, D., Brinkhuis, M., Amrit, C., Aly, R., 2015. Categorizing and describing the

types of fraud in healthcare. Procedia Comput. Sci. 64, 713–720. https://doi.org/10.
1016/j.procs.2015.08.594

Pratik, S., Ashwin, Suresh, G., Sushant, I., 2020. Anomaly detection using machine

Tripathi, A., Thakar, S.V., 2024. Ethical use of AI for academic integrity: preventing

learning. Int. J. Innov. Sci. Res. Technol. (IJISRT 5 (3), 1458–1461 https://bit.ly/
2ycrxti.

Rai, A.K., Dwivedi, R.K., 2020. Fraud detection in credit card data using unsupervised
machine learning based scheme. In: 2020 International Conference on Electronics
and Sustainable Communication Systems (ICESC). IEEE, pp. 421–426. https://doi.
org/10.1109/icesc48915.2020.9155615

Reurink, A., 2018. Financial fraud: a literature review. J. Econ. Surv. 32 (5), 1292–1325.

https://doi.org/10.1111/joes.12294

Sadgali, I., Sael, N., Benabbou, F., 2021. Human behavior scoring in credit card fraud

detection. IAES Int. J. Artif. Intell. 10 (3), 698. https://doi.org/10.11591/ijai.v10.i3.
pp698-706

plagiarism and cheating. Ethic Framew. Spec. Educ.: A Guide Res. 91.

Vaswani, A., Shazeer, N., Parmar, N., Uszkoreit, J., Jones, L., Gomez, A.N., Kaiser, L.,

Polosukhin, I., 2017. Attention is all you need. Adv. Neural Inf. Process. Syst https://
user.phil.hhu.de/∼cwurm/wp-content/uploads/2020/01/7181-attention-is-all-you-
need.pdf.

Wang, H., Zheng, J., Carvajal-Roca, I.E., Chen, L., Bai, M., 2023, August, August.

Financial fraud detection based on deep learning: towards large-scale pre-training
transformer models. In: China Conference on Knowledge Graph and Semantic
Computing. Springer Nature Singapore, Singapore, pp. 163–177. https://doi.org/10.
1007/978-981-99-7224-1_13

Yange, T.S., 2019. A fraud detection system for health insurance in Nigeria. J. Health

Sarker, I.H., 2021. Machine learning: algorithms, real-world applications and research
directions. SN Comput. Sci. 2, 160. https://doi.org/10.1007/s42979-021-00592-x

Inform. Afr. 6 (2), 64–73. https://doi.org/10.12856/JHIA-2019-v6-i2-256
Yousefi, N., Alaghband, M., Garibay, I., 2019. A comprehensive survey on machine

Sharma, R., Mehta, K., Sharma, P., 2024. Role of artificial intelligence and machine

learning in fraud detection and prevention. In: Risks and Challenges of AI-Driven

learning techniques and user authentication approaches for credit card fraud detec-
tion. Retrieved from: arXiv preprint arXiv:1912.02629.

9

