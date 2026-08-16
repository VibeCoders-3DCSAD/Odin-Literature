---
conversion_metadata:
  converted_at: "2026-07-22T12:04:01Z"
  converter_tool: "markitdown"
  converter_version: "0.1.6"
  source_pdf: "Ashta.pdf"
  source_pdf_sha256: "6d0992701d2afe4cb1f54cd6b4036929d0e29e0eca1188b6f9e0561bb9ffaab9"
  page_count: 32
  markdown_char_count: 189420
---

<!-- PAGE-AWARE EXTRACTION (via pdfminer.six) -->

<!-- PAGE 1 -->

Artificial Intelligence in Microfinance and Financial Inclusion: 
Applications, Issues, and Future Directions

Dr. Arvind Ashta

Researcher/Consultant, BHAI: Building Humane Advances and Institutions

Adjunct faculty, Toulouse School of Management, Université Libre de Bruxelles

arvindashta@gmail.com

Abstract 
Artificial intelligence (AI) is emerging as a transformative force in microfinance and financial 
inclusion, addressing long-standing barriers such as credit invisibility, high operational costs, and 
limited access to formal financial services. This paper systematically examines AI applications 
across key financial domains (payments, savings, lending, insurance, investments) highlighting 
how machine learning, natural language processing, and generative AI are enabling innovative 
solutions tailored to the needs of marginalized populations. Drawing on contemporary research 
and case studies from the Global South, the analysis demonstrates AI’s potential to democratize 
financial services through alternative credit scoring, automated underwriting, and adaptive 
tools.

However, the deployment of AI also presents significant challenges, including algorithmic bias, 
proxy discrimination, privacy violations, and the risk of exacerbating digital divides. The paper 
underscores the need for robust governance frameworks, ethical oversight, and inclusive 
policies to mitigate these risks and ensure that AI-driven financial inclusion serves the most 
vulnerable without creating new forms of exclusion. Future directions include advancing 
fairness-aware AI, improving transparency, and fostering cross-sector collaboration to align 
technological innovation with social justice and human dignity.

Keywords: Artificial Intelligence, Microfinance, Financial Inclusion, Machine Learning, Alternative 
Credit Scoring, Algorithmic Bias, Digital Divide, Ethical AI, Global South

JEL: G21, G23, 016, O33, D81, I25, C45, C55

1

---

<!-- PAGE 2 -->

1.  Introduction

Artificial intelligence (AI) comprises computer systems that can perform tasks typically requiring 
human intelligence such as pattern recognition, decision-making, and language understanding. 
It is rapidly emerging as a critical driver of financial inclusion by enabling access to essential 
financial services for historically underserved populations. Financial inclusion represents one of 
finance's greatest challenges, with two billion adults worldwide unable to access loans, 
insurance, or banking services because they lack traditional credit histories ((World Bank, 2021). 
Credit invisibility occurs when individuals have no footprint in conventional credit bureaus—no 
credit cards, mortgages, or installment loans that demonstrate repayment behavior. Even those 
with "thin files" face exclusion; traditional FICO scores require at least six months of credit 
activity across multiple accounts (Consumer Financial Protection Bureau, 2015).

The integration of AI allows financial institutions to break through legacy barriers such as high 
costs, lack of infrastructure, and information asymmetries, improving the reach, efficiency, and 
personalization of offerings (Akanfe, Bhatt, & Lawong, 2025; Björkegren & Grissen, 2019; 
Kshetri, 2021; Vuković, Dekpo-Adza, & Matović, 2025). AI leverages machine learning 
(algorithms that improve automatically through experience), natural language processing 
(NLP)—technology enabling computers to understand and generate human language—and 
algorithmic analytics to empower payments, savings, lending, insurance and investments 
(Mhlanga, 2020).

This paper systematically explores AI applications in each financial need area, highlighting 
current research, real-world implementations from the Global South, and implications for 
inclusive development.

2.  Methodology

This study employs a critical review of academic and gray literature, combined with a targeted 
analysis of multiple real-world case studies from the Global South.

The literature review draws on peer-reviewed articles, working papers, and reports from 
international organizations (e.g., World Bank, CGAP, OECD) to explore the theoretical and 
empirical landscape of AI in financial inclusion, with a focus on emerging trends, gaps, and 
controversies.

The qualitative analysis examines multiple purposively selected case studies of AI-driven 
financial services—including digital payment platforms (e.g., M-Pesa, GCash), micro-lending 
apps (e.g., Tala, Branch), and insurtech solutions (e.g., BIMA, Pula)—to identify recurring 
patterns, operational challenges, and humane dilemmas. For this analysis, the BHAI framework 
is adopted (Arvind Ashta, 2025). The BHAI philosophy advocates for humane AI development 
through multidimensional inclusion—political, economic, and social—alongside environmental 
consciousness, calling for adaptive institutional oversight that guides how technologies are 
applied rather than rigidly controlling innovation. It emphasizes context-sensitive governance

2

---

<!-- PAGE 3 -->

with transparent accountability to ensure AI advances benefit all people, especially marginalized 
populations, while addressing interconnected technological, environmental, and societal 
challenges through the lens of dignity, ethics, and social impact. The framework operationalizes 
this vision through six core components—innovation assessment, human dignity and justice, 
ethical oversight, inclusion and social impact, contextual sensitivity drawing on literary and 
philosophical sources, and actionable reflection—using an interpretative-constructivist 
approach that prioritizes context-rich, nuanced insights over universal generalizations to guide 
humane and equitable AI development (Arvind Ashta, 2025).

By triangulating these sources, the paper offers a nuanced assessment of AI’s role in 
microfinance, while acknowledging the limitations of a non-systematic review approach.

3.  Findings

3.1  Payments

3.1.1 Digital Identity Verification & Onboarding 
The adoption of AI-powered digital Know Your Customer (KYC) processes in payment platforms 
has fundamentally transformed onboarding experiences for unbanked populations by 
automating identity verification using biometric scans (fingerprints, facial recognition, iris scans), 
document analytics powered by computer vision (AI systems that can 'see' and interpret 
images), and liveness detection (technology that confirms a person is physically present rather 
than using a photo or video) (Kuraku, Gollangi, & Sunkara, 2020). These systems typically 
employ supervised learning—where algorithms are trained on labeled datasets of genuine 
versus fraudulent documents—combined with deep learning neural networks (interconnected 
layers of algorithms inspired by the human brain) for facial recognition.

Mobile money providers like M-Pesa1 in Kenya have pioneered AI-enhanced KYC that allows 
users to register using basic mobile phones and biometric verification, reaching millions of 
previously unbanked individuals. In India, the Aadhaar biometric identity system2, integrated 
with payment platforms like Paytm and PhonePe, uses AI-powered iris and fingerprint matching 
to onboard over 400 million digital payment users3. NuBank was able to reach millions of 
unbanked people in Brazil through its online credit card which used automated KYC checks (Chu, 
Laranjeira, & Levindo, 2020).

1 https://www.safaricom.co.ke/annualreport_2022/our-technology/  
2 https://www.biometricupdate.com/202508/uidai-celebrates-2b-aadhaar-face-biometric-
authentications-milestone  
3 https://www.indiatvnews.com/technology/news/google-pay-phonepe-and-paytm-users-now-use-your-
face-or-fingerprint-for-upi-payments-making-them-pin-free-2025-10-08-1011756

3

---

<!-- PAGE 4 -->

These innovations minimize manual errors, dramatically accelerate access to financial services 
from weeks to minutes, and increase trust in digital payments for those previously excluded 
from the formal financial sector while ensuring regulatory compliance and scalability even in 
markets characterized by limited infrastructure.

3.1.2 Fraud Detection & Transaction Security 
Machine learning models enable sophisticated real-time fraud detection in payment platforms, 
identifying anomalies, fraudulent activities, and irregular behavioral patterns as transactions 
occur across networks (Mhlanga, 2020). These systems predominantly use supervised learning 
trained on historical fraud cases, combined with unsupervised learning (algorithms that find 
hidden patterns in data without labeled examples) to detect novel fraud schemes not seen 
before. Advanced implementations employ ensemble methods (combining multiple AI models 
for better accuracy) that perform better than a single classifier (Dietterich, 2000).  Anomaly 
detection algorithms can flag deviations from normal transaction patterns.

Flutterwave, a Nigerian payment gateway processing transactions across Africa, uses AI-
powered fraud detection that analyzes multiple behavioral and transactional features in real-
time, reducing fraud losses while enabling cross-border payments for small businesses4. GCash 
in the Philippines employs machine learning to monitor transactions of over 94 million users5, 
detecting suspicious patterns like account takeovers or merchant fraud that would be 
impossible for human analysts to identify at scale. Kenya's Safaricom uses AI to protect M-Pesa 
transactions from SIM-swap fraud and account compromise, analyzing device fingerprints, 
location patterns, and behavioral biometrics6.

By processing massive datasets with unprecedented speed and accuracy, these AI systems can 
flag suspicious activity instantly, dynamically adapting risk thresholds and security protocols to 
evolving user behavior patterns and emerging threat landscapes, which significantly improves 
payment security while building customer confidence, especially critical for first-time users 
entering the digital financial ecosystem.

3.1.3 Personalization & User Segmentation 
AI enables payment systems to tailor services precisely to individual users through clustering 
algorithms (unsupervised learning methods that group similar users together) and classification 
models (supervised learning that predicts user categories) based on transactional patterns, 
behavioral analytics, geographic data, and temporal usage trends. Recommendation systems, 
similar to those used by e-commerce platforms, employ collaborative filtering (predicting user 
preferences based on similar users' behavior) to suggest relevant payment features, cashback 
offers, and financial products.

4 https://thepaymentsassociation.org/article/flutterwave-2024-report-highlights-record-growth-
expansion-and-innovation/  
5 https://www.philstar.com/opinion/2024/11/12/2399421/gcash  
6 https://kenyanwallstreet.com/how-safaricom-is-leveraging-ai-to-bolster-m-pesa-security-and-efficiency

4

---

<!-- PAGE 5 -->

WeChat Pay and Alipay in China pioneered AI-driven personalization in digital payments (Torre 
& Xu, 2020), analyzing billions of transactions to offer customized merchant recommendations, 
targeted promotions, and differentiated service tiers based on user behavior. India's PhonePe 
employs AI to customize its interface and product recommendations for diverse user segments, 
from urban professionals to rural farmers, ensuring relevance across literacy levels and use 
cases7.

Platforms can offer customized payment options, personalized loyalty rewards, and 
differentiated access mechanisms, rising above traditional one-size-fits-all approaches that often 
fail to meet diverse user needs. This sophisticated personalization builds stronger user 
engagement, encourages sustained participation in the financial ecosystem, and enables rapid 
response to evolving customer needs, ensuring that financial services genuinely serve the 
populations they aim to reach.

3.1.4 Embedded Finance & Cross-Platform Integration 
AI-driven embedded payment solutions facilitate seamless integration with other essential daily 
services including utility management, e-commerce platforms, public transportation systems, or 
mobile wallet applications, substantially amplifying reach and user convenience (Bélanger, 
Ashta, & Mason, 2025). These systems use API-based integration (application programming 
interfaces that allow different software systems to communicate) enhanced with AI-powered 
risk scoring and real-time fraud detection operating across platforms. Reinforcement learning 
(algorithms that learn optimal strategies through trial and error with rewards for successful 
outcomes) can optimize payment routing, fee structures, and approval rates across integrated 
channels.

Grab in Southeast Asia embeds AI-enhanced payments within ride-hailing, food delivery, and 
financial services, processing millions of micro-transactions daily across eight countries with 
intelligent fraud prevention adapted to each use case8. Indonesia's Gojek similarly integrates 
payments across transportation, food, logistics, and financial services using AI to detect 
fraudulent merchants and protect users across ecosystem touchpoints9. In Africa, companies 
like Jumia and Konga embed AI-powered payment scoring into e-commerce checkout, enabling 
instant credit decisions for purchases. Jumia is driving its brand with AI-driven customer service 
and product recommendation, while Konga is deploying predictive analytics and personalised 
marketing10.

Real-time fraud detection capabilities and adaptive user authentication processes minimize 
security risks while enabling service providers to deliver faster, more reliable payment 
experiences across multiple touchpoints. By embedding financial services within familiar 
contexts rather than requiring separate banking interactions, AI helps overcome psychological

7 https://brandwell.ai/blog/how-to-customize-phonepe-payment-solutions-with-ai-complete-guide/  
8 https://bytebridge.medium.com/comprehensive-report-on-grab-holdings-daa9e7d3918f  
9 https://techwireasia.com/2020/11/gojek-sees-profitability-ahead-after-a-decade-of-rapid-growth/  
10 https://thenationonlineng.net/revealed-nigerian-brands-banking-on-robots-ai/

5

---

<!-- PAGE 6 -->

barriers to adoption and creates natural pathways for previously excluded populations to enter 
the formal financial system. In one study, 70% reported that the use of artificial intelligence in 
risk assessment and social impact evaluation improves decision making (Manta, Vasile, & Rusu, 
2025).

3.1.5 Humane Considerations 
While AI transforms payment accessibility, critical ethical concerns demand attention. Dignity 
and justice require that biometric data collection respects privacy and obtains informed 
consent, particularly from vulnerable populations who may not fully understand data 
implications or have limited alternatives.

Cases of biometric data breaches in India's Aadhaar system and concerns about Chinese 
payment platforms' data practices highlight risks of surveillance capitalism where user data 
becomes a commodity (Zuboff, 2019).

Governance frameworks must ensure AI systems do not perpetuate discrimination through 
biased algorithms that systematically disadvantage certain demographics—for instance, fraud 
detection models trained predominantly on urban transaction patterns may incorrectly flag 
legitimate rural transactions as suspicious, effectively excluding rural users (Solon Barocas & 
Selbst, 2016).

Inclusion efforts must bridge digital divides by ensuring that AI-powered payment solutions 
remain accessible to those with limited digital literacy, unreliable internet connectivity, or older 
devices—many AI-enhanced payment apps require smartphones and stable internet, potentially 
excluding the most marginalized (V. Bumacov, Ashta, & Singh, 2014; Hurley & Adebayo, 2016).

Transparency in algorithmic decision-making, particularly around why accounts are frozen or 
transactions blocked, robust data protection measures that prevent unauthorized sharing of 
financial data, and accessible recourse mechanisms when AI systems make errors are essential 
to building trust. They ensure that AI-driven payment innovations genuinely empower rather 
than exploit marginalized communities (Akanfe et al., 2025).

3.2  Savings & Pensions

3.2. 1 Behavioral Nudges & Automated Savings 
AI's capacity for micro-segmentation and predictive analytics enables savings platforms to 
create highly personalized savings mechanisms that adapt to individual users' unique 
employment patterns, income volatility cycles, and financial goals. These systems employ 
supervised learning models trained on historical savings behavior to predict optimal savings 
amounts and timing, combined with reinforcement learning algorithms that continuously 
optimize nudging strategies based on user responses. Behavioral economics principles are 
operationalized through AI-powered interventions such as automated round-up features (saving 
spare change from transactions), goal-based savings trackers, and timely motivational

6

---

<!-- PAGE 7 -->

messages(Cook & McKay, 2015; Makunda & Matiko, 2023).  Table 1 shows some of the 
behavioral finance features incorporated by digital savings accounts.

Table 1: Behavioural finance nudges in digital savings

Behavioural Principle  Digital Savings Nudge

Result

Present Bias

Makes saving instant & 
frictionless.

Reduces procrastination.

Mental Accounting

Creates a separate "Savings" 
account.

Protects savings from daily 
spending.

Loss Aversion

Offers interest (a "gain").

Frames “not saving” as a loss.

Commitment Device

"Lock Savings" feature.

Feedback Loop

Links savings to loan eligibility.

Enforces discipline by restricting 
access.

Rewards saving with a tangible, 
valuable

Now, artificial intelligence can take this further. By analysing the payment patters based on bank 
of mobile payments, AI can analyze transaction patterns and automatically suggest personalized 
savings amounts based on predicted future income, enabling millions of informal workers to 
build emergency funds.  Savings and investement fintechs can use machine learning to create 
customized automated savings plans that adapt to users' irregular income streams.

In India, micro-savings platforms like Jar use AI to invest small amounts automatically in digital 
gold, with algorithms determining optimal purchase timing based on price patterns and user 
affordability11. These AI-driven interventions motivate users to save regularly by aligning 
financial products with their actual circumstances rather than imposing rigid structures, 
improving client loyalty and helping close critical inclusion gaps in retirement planning and 
emergency savings, ultimately contributing to more financially secure populations across diverse 
socioeconomic contexts.

3.2.2 Pension Optimization & Retirement Planning 
Generative AI and simulation models can forecast personalized retirement outcomes for 
individual users, creating detailed scenario analyses showing how different savings strategies, 
contribution levels, and investment allocations affect long-term financial security. These 
systems use Monte Carlo simulations (running thousands of possible future scenarios with

11 https://www.forbesindia.com/article/leadership/jar-how-to-build-your-own-pot-of-gold/93180/1

7

---

<!-- PAGE 8 -->

different economic conditions) combined with supervised learning models that predict life 
expectancy, healthcare costs, and inflation impacts based on individual characteristics. Time-
series forecasting algorithms (models specialized in predicting sequential data points) project 
pension growth under various economic scenarios.

In Latin America, Mexico's CONSAR (pension regulator) has piloted AI tools that help informal 
workers understand retirement needs through simplified projections based on irregular income 
patterns. It has also used AI to detect potentially suspicious websites aimed at pension savers 12.

According to a CFA Institute report (Hayman, 2024), AI can be applied across the pension value 
chain to enhance personalization, efficiency, and accuracy in addressing key retirement system 
challenges. AI applications include improving member engagement through chatbots and 
personalized communications, automating recordkeeping and fraud detection, streamlining 
governance processes through document analysis and covenant assessments, enhancing 
investment decision-making via predictive analytics and portfolio optimization, and supporting 
better decumulation strategies in the payout phase. The technology can help pension funds 
analyze large datasets to improve trustee decision-making, provide personalized retirement 
planning tools tailored to individual member characteristics, reduce administrative burdens, and 
enhance both DB and DC plan management through machine learning models that optimize 
asset allocation and risk management.

South Africa's pension administrators are implementing AI-driven tools to project retirement 
adequacy for workers transitioning between formal and informal employment. This adaptive 
guidance significantly enhances financial understanding across literacy levels, increases 
meaningful engagement with retirement planning, and empowers users to make confident, 
informed decisions about their long-term financial stability. By translating complex financial 
concepts into accessible scenarios and visualizations, AI strengthens the inclusive impact of 
digital savings platforms, making sophisticated financial planning tools available to populations 
that previously lacked access to professional financial advice.

3.2.3 Humane Considerations 
AI-driven savings innovations must uphold human dignity by ensuring that automated nudging 
systems do not exploit vulnerable savers through manipulative dark patterns (design choices 
that trick users into actions against their interests) or opaque fee structures disguised as helpful 
features. Governance mechanisms must prevent algorithmic manipulation that encourages 
excessive risk-taking or inappropriate long-term lockups for users who may face emergencies 
requiring liquidity—several African digital savings platforms have faced criticism for making 
withdrawals difficult while aggressively pushing savings deposits.

Ethical frameworks should ensure that personalization respects cultural values around money, 
family obligations, and retirement expectations rather than imposing Western financial planning

12 https://www.nortonrosefulbright.com/en-419/knowledge/publications/ba2b4dbd/pensions-regulator-
develops-ai-tool-to-detect-potentially-suspicious-pension-websites

8

---

<!-- PAGE 9 -->

models—in many cultures, supporting extended family takes precedence over individual 
retirement savings, yet AI systems may penalize such transfers as 'poor savings discipline' 
(Anderson, Baland, & Moene, 2009).

Inclusion requires addressing the reality that informal workers often face irregular income 
streams, making rigid automated savings schedules counterproductive—AI systems should 
accommodate rather than penalize income variability.

The CFA report (Hayman, 2024) emphasizes that while AI offers significant potential to improve 
retirement outcomes and operational efficiency, successful implementation requires balancing 
automation with human oversight, ensuring data privacy and security, maintaining transparency 
and explainability in AI-driven decisions, and using technology to augment rather than replace 
human judgment in fiduciary responsibilities. Transparent communication about investment 
performance, accessible withdrawal options during genuine emergencies without excessive 
penalties, protection against algorithmic errors that could devastate retirement security (such as 
incorrect contribution calculations or failed transfers), and ensuring that predictive models don't 
discriminate based on factors like gender or geography when projecting retirement needs are 
fundamental requirements for ethical AI deployment in savings and pensions.

3.3  Lending & Credit

3.3.1 Alternative Credit Scoring & Data Analytics

A credit score is a number based on an analysis of a person's credit files, to represent the 
creditworthiness of an individual. It has been used in developed countries for many decades but 
was introduced more recently to microcredit (Vitalie Bumacov, Ashta, & Singh, 2017). Credit 
invisibility occurs when individuals have no footprint in conventional credit bureaus: no credit 
cards, mortgages, or installment loans that demonstrate repayment behavior. Traditional credit 
scoring creates a paradox that locks out entire populations: you cannot get your first loan 
without credit history, but you cannot build credit history without getting loans (World Bank, 
2021).

In the United States alone, 45 million adults are either completely credit invisible or have credit 
files too thin to generate reliable scores, representing 20% of the adult population, 
disproportionately concentrated among minority communities and lower-income households 
(Consumer Financial Protection Bureau, 2015).

Now, AI leverages alternative data sources (see Table 2) including mobile phone usage patterns, 
e-commerce transaction histories, utility payment records, social network data, and smartphone 
sensor data (like GPS patterns indicating stable employment) for sophisticated credit scoring 
that addresses exclusion of populations with thin files or those without formal credit histories 
(Björkegren & Grissen, 2019; Gambacorta, Huang, Qiu, & Wang, 2019; Nuka & Ogunola, 2024).

9

---

<!-- PAGE 10 -->

Research demonstrates that telecommunications payment data shows particularly strong 
predictive power—studies across multiple markets find correlations of 0.65 to 0.72 between 
mobile phone bill payment consistency and loan repayment rates, comparable to traditional 
FICO scores (Björkegren & Grissen, 2019).

Table 2: Traditional versus Alternative Data

Data Type

Traditional Data

Alternative Data

Income

Formal employment income

Gig economy and freelance earnings

Payment History

Credit 
repayments

card

and

loan

Rental payments, utility bills

Spending 
Patterns

Bank account transactions

Mobile money and digital wallets

Assets

Property ownership

Informal savings groups and investments

Demographics

Age, marital status

Social media and online activity

Credit History

Bank credit reports

Alternative lending platform histories

Behavioral Data

N/A

Psychometric  testing,  online  behavior 
analytics

Source: The first five rows (Nuka & Ogunola, 2024) and the last two rows added by author.

These systems employ supervised learning with classification algorithms such as gradient 
boosting machines, random forests (ensemble methods that combine multiple decision trees), 
and neural networks trained on historical repayment data to predict default probability 
(Jonnalagadda & Babu, 2025). Alternative data scoring overwhelmingly relies on gradient 
boosted tree methods, particularly XGBoost and LightGBM, which power 70-80% of production 
systems at companies like Affirm, Upstart, and Kabbage because they automatically detect non-
linear relationships and handle the messy, incomplete nature of alternative data (Khandani, Kim, 
& Lo, 2010).

Where traditional scoring uses 5-10 variables from credit bureaus, ML models might incorporate 
500-5,000 features extracted from alternative sources and this reduces default rates (Berg, 
Burg, Gombović, & Puri, 2019). Feature engineering (the process of selecting and transforming 
raw data into useful predictors) identifies hundreds of behavioral indicators from alternative

10

---

<!-- PAGE 11 -->

data—call patterns, SMS metadata, app usage, mobile money transactions—that correlate with 
creditworthiness (Gambacorta et al., 2019).

Kenya's Branch and Tala pioneered smartphone-based credit scoring analyzing over 10,000 data 
points from users' phones to predict repayment likelihood, disbursing billions in microloans to 
borrowers with no formal credit history. In India, companies like ZestMoney and KreditBee use 
AI models incorporating e-commerce behavior, digital wallet usage, and education data to score 
young borrowers entering credit markets. Nigeria's Carbon (formerly Paylater) analyzes bank 
transaction data, mobile money flows, and social media presence to assess creditworthiness for 
millions of borrowers (Olajide et al., 2025). China's Ant Financial developed Zhima Credit, which 
scores over 1 billion users based on consumption behavior, money transfer networks, and 
fulfillment of commitments13.

By recognizing reliability demonstrated through non-traditional channels, these AI-powered 
alternative credit scoring systems fundamentally transform credit accessibility. They open 
lending markets to billions previously deemed unscoreable or too risky based solely on absence 
from traditional credit bureaus. This enables entrepreneurs, smallholder farmers, and gig 
economy workers to access productive capital (Djeundje, Crook, Calabrese, & Hamid, 2021; 
Jagtiani & Lemieux, 2019; Nuka & Ogunola, 2024).

3.3.2 Automated Credit Risk Assessment 
Automated underwriting systems leverage ensemble machine learning methods combining 
multiple supervised learning algorithms (logistic regression for baseline probability, gradient 
boosting for complex patterns, and neural networks for non-linear relationships) for fast, 
accurate risk evaluations in microfinance and small-to-medium enterprise lending (Milana & 
Ashta, 2021). These systems process loan applications in real-time, analyzing hundreds of 
variables simultaneously including alternative credit scores, cash flow patterns, business sector 
risks, and macroeconomic indicators to generate risk ratings and recommend loan terms. 
Natural language processing analyzes loan applications and business descriptions to assess 
viability, while computer vision can evaluate collateral photos submitted via mobile apps.

India's Aye Finance uses AI underwriting to assess micro-enterprises' creditworthiness by 
analyzing GST filings, bank statements, and business characteristics, approving loans within 72 
hours for businesses traditional banks reject14. Kenya's Musoni uses machine learning models to 
underwrite agricultural loans based on mobile money transaction history, farm size data from 
satellite imagery, and weather patterns, serving smallholder farmers efficiently. Brazil's Creditas 
employs AI to underwrite asset-backed loans for lower-income borrowers using alternative data 
combined with vehicle and property valuations. Bangladesh's bKash integrates AI-powered 
micro-lending directly into its mobile money platform, using transaction history to automatically 
pre-approve small loans for merchants and users.

13 https://en.wikipedia.org/wiki/Zhima_Credit  
14 https://www.ayefin.com/wp-content/uploads/2024/12/Aye-Finance-Limited-Industry-Report.pdf

11

---

<!-- PAGE 12 -->

By reducing decision-making costs from hundreds of dollars per loan to pennies, and processing 
times from weeks to minutes, AI-powered underwriting makes credit accessible to borrowers 
seeking smaller loan amounts that would be unprofitable under traditional manual underwriting 
processes, enabling financial inclusion at unprecedented scale (Jagtiani & Lemieux, 2019).

3.3.3 Flexible Loan Products & Dynamic Pricing 
AI enables lenders to create highly tailored lending products for diverse populations including 
gig workers, self-employed individuals, seasonal laborers, and small entrepreneurs by using 
reinforcement learning to continuously optimize loan terms, repayment schedules, and interest 
rates based on borrower behavior and repayment success. Predictive models employing time-
series analysis forecast income volatility and optimal repayment timing for borrowers with 
irregular cash flows. Dynamic pricing algorithms adjust interest rates based on individual risk 
profiles, competitive market conditions, and the lender's liquidity needs, making credit more 
accessible while maintaining profitability.

Argentina’s Ualá uses AI to offer flexible credit lines that adapt to users' spending and 
repayment patterns, with personalized limits and interest rates reflecting individual behavior 
rather than rigid categorical rules15. In Kenya, Apollo Agriculture combines AI credit scoring with 
flexible repayment schedules aligned to harvest cycles, providing smallholder farmers with 
inputs financing that accommodates seasonal income patterns16. Philippines-based Robocash 
uses machine learning to dynamically adjust loan terms and pricing based on borrower 
engagement and partial repayment behavior, reducing defaults while expanding access17. India's 
KreditBee employs AI to offer flexible tenure options and personalized interest rates for young 
professionals with variable income streams18.

This sophisticated segmentation moves beyond one-size-fits-all credit products that often fail to 
serve non-traditional borrowers effectively, recognizing that different economic activities 
require different financial structures. Personalized lending increases repayment success rates 
while expanding access to populations whose income variability previously disqualified them 
from credit, ultimately fostering entrepreneurship and economic development across diverse 
economic sectors.

3.3.4 Humane Considerations 
AI-powered lending raises profound ethical concerns around dignity and justice, particularly 
regarding algorithmic bias that may perpetuate historical discrimination in credit access 
(Djeundje et al., 2021). Alternative data can encode existing societal inequalities: low-income

15 https://www.bnamericas.com/en/news/argentinas-uala-working-on-integrating-2-banks-into-its-tech-
stack  
16 https://nation.africa/kenya/news/gender/meet-the-don-teaching-machines-to-speak-africa-s-
languages-one-algorithm-at-a-time-5186224  
17 https://juicyscore.ai/en/case-studies/robocash-reduces-high-risk-application-flow-by-75-with-
juicyscore  
18 https://www.kreditbee.in/flexi-personal-loan

12

---

<!-- PAGE 13 -->

neighborhoods generate fewer digital footprints simply because residents have older phones, 
less reliable internet, and lower e-commerce participation.

When machine learning trains on this data, it may learn that sparse digital activity predicts 
default—not because sparse activity causes default, but because it correlates with poverty. This 
creates proxy discrimination: the model never sees race, but zip code, device type, and app 
usage patterns serve as proxies (Solon Barocas & Selbst, 2016). Studies have revealed that even 
alternative credit scoring models can encode proxy discrimination—for instance, smartphone 
models, app usage patterns, or social media behavior may correlate with protected 
characteristics like race or ethnicity, leading to discriminatory outcomes despite not explicitly 
using these variables.

Governance frameworks must ensure transparency in credit scoring algorithms, including model 
explainability (the ability to understand why an AI system made a specific decision), allowing 
borrowers to understand and effectively contest automated decisions affecting their economic 
opportunities (Bracke, Datta, Jung, & Sen, 2019). Individuals should be granted an opportunity 
to challenge adverse decisions based on artificial intelligence generated scores (Citron & 
Pasquale, 2014).

Predatory lending practices can be amplified by AI systems that identify vulnerable populations 
and target them with exploitative terms disguised as personalized offers. Debt creates an entire 
industry profiting from exploitation (Rona-Tas & Guseva, 2018).

Inclusion requires that alternative data usage respects privacy boundaries—analyzing call logs, 
SMS content, or social networks raises serious privacy concerns, especially when users aren't 
fully informed about data usage (Citron & Pasquale, 2014).

Fair lending principles would require that AI systems do not punish poverty by charging 
exponentially higher rates to those already economically marginalized: differential pricing 
should reflect actual risk, not merely exploit price insensitivity among desperate borrowers.

Algorithmic credit expansion must not create debt traps through inappropriate loan approvals 
or inflexible collection practices, but rather provide genuine pathways to economic 
empowerment through responsible, affordable credit that borrowers can realistically repay (A. 
Ashta & Hudon, 2012).

3.4  Insurance

3.4.1 Risk Profiling & Insurability Assessment 
AI builds comprehensive insurability profiles by assessing digital footprints and alternative data 
to evaluate risk levels when traditional actuarial data is limited or nonexistent, enabling insurers 
to expand coverage into previously underserved markets (Vuković et al., 2025). These systems 
employ supervised learning with classification models (typically ensemble methods like XGBoost

13

---

<!-- PAGE 14 -->

or neural networks) trained on claims history, lifestyle indicators extracted from mobile usage, 
geographic risk factors from satellite imagery, and health proxies derived from activity patterns. 
Computer vision analyzes submitted photos of homes, vehicles, or farms to assess insurability 
and detect pre-existing damage, while satellite imagery and weather data inform agricultural 
insurance risk models (Lobell, Thau, Seifert, Engle, & Little, 2015).

BIMA, operating across Africa and Asia, uses AI-powered micro-insurance assessment based on 
mobile phone data and basic health questions to provide life and health insurance to over 45 
million low-income customers who lack traditional medical records19. In India, Toffee Insurance 
uses machine learning to offer bite-sized insurance products personalized to individual risk 
profiles derived from smartphone data and payment histories20. Kenya's M-Pesa partners with 
insurance providers to offer micro-insurance scored based on transaction patterns and mobile 
usage, automatically enrolling users in appropriate coverage tiers.

By recognizing patterns that correlate with insurance claims experience across diverse data 
sources, AI enables evidence-based risk pricing that makes insurance economically viable for 
both providers and low-income customers. This innovation transforms insurance accessibility by 
moving beyond stereotypes and limited data to data-driven individual risk assessment, opening 
insurance markets to billions previously deemed too risky or expensive to serve profitably.

3.4.2 Automated Underwriting & Claims Processing 
Machine learning automates complex insurance underwriting and accelerates claims processing 
through computer vision for damage assessment, natural language processing for claims 
documentation analysis, and predictive models for fraud detection. Supervised learning models 
trained on historical claims data classify claim validity, estimate loss amounts, and detect 
fraudulent patterns. Deep learning with convolutional neural networks (specialized 
architectures for analyzing images) can assess crop damage, vehicle accidents, or property 
destruction from photos submitted via mobile apps, providing near-instant loss estimates. In 
parametric insurance (coverage that pays out automatically when specific measurable events 
occur), AI monitors trigger conditions like rainfall levels, earthquake magnitude, or temperature 
thresholds using IoT sensors and satellite data.

In Nigeria Pula uses AI-powered parametric insurance for smallholder farmers, automatically 
triggering payouts based on satellite-derived vegetation health indices and weather station 
data, eliminating lengthy manual claims processes (Hernandez, Goslinga, & Wang, 2018). 
Kenya's Britam Insurance employs computer vision to assess vehicle damage from smartphone 
photos, reducing claims processing time from weeks to hours21. India's Acko uses fully

19 https://www.cgap.org/about/people/bima  
20 https://wishboxstudio.in/toffee-insurance-a-case-study/  
21 https://thedailywhistle.co.ke/faster-claims-fewer-headaches-ai-is-transforming-kenyas-insurance-
industry/

14

---

<!-- PAGE 15 -->

automated claims processing with AI analyzing photos, policy terms, and repair cost databases 
to approve and disburse claims within minutes for cyber insurance and product protection22.

By processing risk factors continuously and updating models with emerging data, AI enables 
dynamic pricing that reflects actual risk rather than outdated assumptions, making innovative 
insurance products financially sustainable and allowing insurers to offer coverage for climate-
related disasters, crop failures, and health emergencies that disproportionately affect poor 
communities.

3.4.3 Micro-Insurance Products & Parametric Coverage 
AI creates highly flexible micro-insurance products and specialized offerings like harvest-linked 
agricultural insurance, weather-indexed coverage, and health micro-insurance tailored for 
farmers, informal workers, and micro-entrepreneurs facing context-specific risks. Machine 
learning models employing regression analysis (predicting continuous numerical outcomes) and 
time-series forecasting assess correlations between observable parameters (rainfall, 
temperature, vegetation indices) and actual losses, enabling parametric triggers that are 
objective and verifiable (Burke & Lobell, 2017). Clustering algorithms segment users based on 
occupation, location, and risk exposure to design targeted products.

Nigeria's Pula Advisors partners with mobile money platforms to offer index-based crop 
insurance integrated directly into agricultural input purchases, with AI determining coverage 
amounts and monitoring weather patterns to trigger automatic payouts via mobile money 
without requiring manual claims (Hernandez et al., 2018). In Ghana, ACRE Africa uses machine 
learning combined with satellite data and weather station networks to offer parametric 
insurance covering drought and excess rainfall risks for smallholder farmers, with payouts 
automatically triggered when rainfall deviates from optimal levels (Waithaka, Kramer, Kivuva, & 
Cecchi, 2023). India's Skymet combines AI weather prediction models with blockchain-based 
smart contracts to automate parametric insurance payouts for millions of farmers, reducing 
administrative costs and preventing payout delays23. Kenya's Turaco offers device insurance, life 
insurance, and health coverage bundled with mobile money services, using AI to price policies 
dynamically based on risk profiles24.

This customization increases insurance value for policyholders while improving risk pools for 
insurers, creating sustainable insurance markets that protect vulnerable populations from 
shocks that could otherwise destroy livelihoods.

3.4.4 Humane Considerations 
AI-driven insurance must respect dignity by avoiding discriminatory risk profiling that unfairly 
penalizes vulnerable populations for factors beyond their control. Algorithmic redlining concerns 
are particularly acute in insurance—AI systems trained on historical data may systematically

22 https://digiqt.com/blog/acko-insurance-automation/  
23 https://www.skymetweather.com/corporate/cropinsurance.html  
24 https://www.turaco.insure/about-us

15

---

<!-- PAGE 16 -->

deny coverage or charge prohibitive premiums to marginalized communities, perpetuating 
rather than addressing inequality (Solon Barocas & Selbst, 2016). For instance, using geolocation 
data may result in higher premiums for residents of informal settlements regardless of 
individual risk factors, effectively excluding the poor. Governance mechanisms must prevent 
proxy discrimination where AI uses variables like smartphone type, social network 
characteristics, or consumption patterns that correlate with protected characteristics like race, 
religion, or caste.

Justice would require that micro-insurance pricing remains genuinely affordable and that claims 
processing does not become opaque or systematically deny legitimate claims through 
algorithmic gatekeeping—some parametric insurance schemes have faced criticism for setting 
triggers that rarely activate despite farmers experiencing losses. Commitment to expanding 
genuine protection rather than simply extracting premiums from poor communities requires 
that insurance products actually transfer meaningful risk and provide timely payouts when 
losses occur, not just collect premiums while minimizing payouts through restrictive AI-
determined conditions.

Inclusion requires recognizing that alternative data usage for risk assessment must not become 
invasive surveillance that commodifies poverty or exploits vulnerable populations by extracting 
intimate behavioral data in exchange for basic insurance coverage (Zuboff, 2019).

Ethical deployment demands transparency about how AI determines insurability, with clear 
explanations of why someone might be denied coverage or charged higher premiums (S. 
Barocas, Hardt, & Narayanan, 2019). Accessible appeals processes for denied claims or disputed 
risk ratings are essential, ensuring that algorithmic decisions can be challenged.

3.5  Investments

3.5.1 Automated Portfolio Management & Robo-Advisory 
AI-powered robo-advisors (automated platforms providing financial planning and investment 
management) democratize access to sophisticated portfolio management previously available 
only through expensive human advisors (Kshetri, 2021). These systems employ supervised 
learning algorithms for asset allocation (determining optimal distribution across stocks, bonds, 
and other investments), regression models for return prediction, and optimization algorithms 
(mathematical methods for finding the best solution under constraints) to build diversified 
portfolios aligned with individual risk tolerance and goals. Reinforcement learning can 
continuously adjust strategies based on market conditions and portfolio performance, learning 
optimal rebalancing policies over time. Natural language processing enables conversational 
interfaces that guide novice investors through onboarding and ongoing portfolio management in 
accessible language.

16

---

<!-- PAGE 17 -->

Brazil's Nubank offers AI-driven investment products to over 120 million customers in Brazil, 
Mexico, and Colombia, many first-time investors, with automated portfolio construction based 
on individual risk profiles and goals25. Mexico's Flink uses robo-advisory with micro-investing 
features, allowing users to start with as little as 30 pesos while AI builds diversified portfolios 
adapted to Latin American markets26. Kenya's Ndovu provides automated investment 
management accessible via mobile money integration, using AI to create portfolios suitable for 
African market conditions and investor profiles ranging from urban professionals to rural 
savers27. India's Groww platform use machine learning to recommend thematic investment 
portfolios and mutual funds tailored to users' financial situations, education levels, and 
investment horizons28.

By providing professional-grade portfolio management at fraction of traditional costs, AI enables 
small-scale investors to participate in wealth-building opportunities historically reserved for the 
affluent.

3.5.2 Risk-Based Asset Allocation & Market Intelligence 
Machine learning systems comprehensively assess investor risk profiles and dynamically allocate 
assets using portfolio optimization algorithms that balance expected returns against volatility. 
These systems employ supervised learning for risk tolerance classification, time-series 
forecasting models (LSTM neural networks—long short-term memory networks specialized for 
sequential data—and ARIMA models) to predict market movements (Krishnan, Ashta, & Babu, 
2021), and reinforcement learning to discover optimal long-term investment strategies that 
adapt to changing market regimes. Sentiment analysis using natural language processing 
extracts market signals from news articles, social media, and financial reports to inform 
investment decisions. Volatility prediction models and correlation analysis ensure diversification 
across assets with different risk characteristics.

Colombia's Tyba uses AI to assess users' risk profiles through behavioral questions and financial 
data, automatically allocating investments across diverse assets while continuously rebalancing 
based on market conditions and individual circumstances29. Chile's Fintual employs machine 
learning to construct portfolios optimized for different life stages and goals, with AI-driven 
rebalancing responding to market volatility while maintaining target risk levels30. In India, ET 
Money uses AI to recommend mutual fund portfolios combining risk assessment with tax 
optimization strategies, while continuously monitoring portfolio health and suggesting

25 https://international.nubank.com.br/company/with-122-million-customers-nubank-creates-products-
capable-of-gaining-global-scale/  
26 https://www.latamfintech.co/articles/mexican-neobroker-flink-raised-57-m-in-a-series-b-round-to-
boost-financial-inclusion-in-latam  
27 https://www.ndovu.co/about-ndovu-rw  
28 https://yourstory.com/2019/11/groww-leverages-technology-eliminate-hassle  
29 https://alpaca.markets/blog/tyba-creating-investment-access-in-latin-america/  
30 https://www.hi.vc/insights/an-ai-tool-for-analyzing-investment-statements-fintuals-new-bet

17

---

<!-- PAGE 18 -->

adjustments31. Nigeria's Risevest allows diaspora and local investors to access global markets 
through AI-curated portfolios that manage currency risk and optimize returns for naira-based 
investors32.

For novice investors lacking sophisticated financial knowledge, automated risk management 
provides professional-grade portfolio oversight, helping them build wealth over time while 
avoiding common pitfalls like panic selling during downturns, excessive concentration in high-
risk assets, or overly conservative allocations that fail to generate real returns after inflation.

3.5.3 Humane Considerations 
AI-powered investment platforms must uphold dignity by ensuring that democratized access 
does not expose financially vulnerable populations to inappropriate risks through algorithmic 
recommendations that prioritize platform profits over investor welfare. Governance frameworks 
must prevent conflicts of interest where AI systems recommend high-fee products or 
investments generating higher commissions for platforms rather than better returns for 
investors—some robo-advisors have faced criticism for steering users toward proprietary funds 
with higher fees. Ethical deployment demands that AI investment tools genuinely serve wealth-
building goals rather than extracting fees from novice investors through frequent trading or 
complex products (Kalluri, 2020). Clear disclosure of conflicts of interest, commitment to 
fiduciary responsibility (legal obligation to act in clients' best interests) in automated investment 
advice, and protection against algorithmic failures that could cause significant portfolio losses 
are essential.

Justice requires transparency in how algorithms allocate investments and assess suitability, with 
clear explanations of automated decisions affecting people's financial futures. Model 
explainability is crucial—investors should understand why they received specific 
recommendations and what assumptions drive their portfolio allocation (Bracke et al., 2019).

Inclusion requires recognizing that investment literacy varies dramatically, necessitating 
protective guardrails against algorithmic manipulation while preserving investor autonomy—
overly aggressive risk profiling might push unsophisticated investors into volatile assets they 
don't understand, while overly conservative approaches might leave them unable to build 
wealth.

Ensuring that robo-advisors account for local market conditions, currency risks, and tax 
implications relevant to Global South investors—rather than simply adapting algorithms 
designed for developed markets—is crucial for genuine financial inclusion in investment 
services.

31 https://www.etmoney.com/tax-saving  
32 https://risevest.com/why-rise

18

---

<!-- PAGE 19 -->

4.  Discussion

This systematic examination of AI applications across five critical financial sectors reveals both 
remarkable technological advances and persistent ethical challenges that must be addressed to 
ensure truly inclusive and humane financial systems. The evidence demonstrates that AI is not 
merely automating existing processes but fundamentally transforming how financial services 
can reach and serve marginalized populations.

4.1 AI Technologies Across Financial Sectors 
To understand the diverse AI applications described in this paper's findings, it is essential to first 
grasp the foundational machine learning paradigms that underpin these systems. Machine 
learning—the core technology driving AI-enabled financial inclusion—comprises three primary 
learning approaches, each suited to different types of problems:

Supervised learning involves training algorithms on labeled datasets where the correct answer 
is known (for example, historical loan data labeled as "repaid" or "defaulted"). The algorithm 
learns patterns that map inputs to outputs, enabling it to make predictions on new, unseen 
data. This approach powers most classification tasks (is this transaction fraudulent?) and 
regression tasks (what return can be expected?).

Unsupervised learning discovers hidden patterns in data without pre-labeled examples. Rather 
than predicting a known outcome, these algorithms identify natural groupings, detect 
anomalies, or find underlying structures in data. This approach excels at segmentation (grouping 
similar customers) and anomaly detection (finding unusual patterns that might indicate fraud).

Reinforcement learning takes a fundamentally different approach: algorithms learn optimal 
strategies through trial and error, receiving rewards for successful actions and penalties for 
unsuccessful ones. Over many iterations, the system discovers which decisions lead to the best 
long-term outcomes. This paradigm is particularly powerful for sequential decision-making 
problems like portfolio management or dynamic pricing.

Within each of these three paradigms, specific techniques and algorithms have proven 
particularly effective for financial inclusion applications. Additionally, certain cross-cutting 
technologies—natural language processing and computer vision—can employ any of these 
learning paradigms depending on the specific task. Table 3 organizes all AI technologies 
discussed in this paper's findings section according to these learning paradigms and shows 
which techniques are deployed across the five financial sectors.

Table 3: AI Technologies by Financial Sector (Hierarchical Structure)

Learning 
Paradigm

Specific 
Technique/Application

Payments

Savings & 
Pensions

Lending & 
Credit

Insurance

Investment
s

19

---

<!-- PAGE 20 -->

SUPERVISED 
LEARNING

Classification (fraud, 
risk, default)

KYC 
verification, 
fraud 
detection

Savings 
behavior 
prediction

Gradient Boosting 
(XGBoost/LightGBM)

-

Neural Networks (CNNs 
for images)

Regression Models

Time-Series Forecasting 
(labeled)

Biometric 
recognition 
(face, iris, 
fingerprint)

-

-

UNSUPERVISED 
LEARNING

Anomaly Detection

Clustering/Segmentatio
n

REINFORCEMEN
T LEARNING

Strategy Optimization

Novel fraud 
pattern 
detection

User 
segmentation, 
personalizatio
n

Payment 
routing, fee 
optimization

CROSS-CUTTING 
TECHNIQUES

Natural Language 
Processing

-

Credit 
scoring, 
default 
prediction

Alternative 
credit 
scoring (70-
80% of 
systems)

-

-

-

-

-

Pension 
projections 
(ARIMA)

Income 
volatility 
prediction

-

-

Novel fraud 
schemes

Borrower 
segmentatio
n

Risk 
classification, 
claims validity

Risk 
tolerance 
classificatio
n

Risk profiling

Damage 
assessment 
from photos

-

-

Parametric 
loss prediction

Return 
prediction

-

-

Market 
prediction 
(LSTM, 
ARIMA)

-

Risk-based 
groups

Investor 
profiling

Nudging 
strategy 
optimizatio
n

Chatbots 
for 
guidance

Dynamic 
pricing

-

Portfolio 
strategy 
optimizatio
n

Application 
analysis

Claims 
documentatio
n

Sentiment 
analysis, 
chatbots

Computer Vision

Document 
verification, 
liveness 
detection

-

Collateral 
photos

-

Satellite 
imagery, 
damage 
photos

STATISTICAL 
METHODS

Monte Carlo Simulation

-

Retirement 
scenarios

-

-

Risk 
scenarios

This hierarchical organization reveals several critical patterns about how AI technologies are 
being deployed for financial inclusion:

20

---

<!-- PAGE 21 -->

First, supervised learning dominates across all five sectors, reflecting both its technical 
maturity and the availability of labeled training data in financial services. Every sector employs 
supervised classification or regression for core predictive tasks—fraud detection in payments, 
credit scoring in lending, risk assessment in insurance, and return prediction in investments. This 
prevalence indicates that financial institutions possess sufficient historical data (transactions, 
defaults, claims, returns) to train supervised models effectively. The success of supervised 
learning in financial inclusion stems from its ability to learn from past patterns and apply those 
lessons to new cases at scale.

Second, gradient boosting methods—specifically XGBoost and LightGBM—have emerged as 
the dominant technique for alternative credit scoring, powering 70-80% of production systems 
in lending as documented in the findings. This near-universal adoption is not accidental. These 
ensemble methods excel at handling the messy, incomplete, heterogeneous nature of 
alternative data (mobile phone metadata, e-commerce transactions, utility payments) that 
characterizes credit-invisible populations. Unlike simpler models that assume clean, structured 
data, gradient boosting automatically detects complex non-linear relationships, handles missing 
values gracefully, and combines insights from multiple decision trees to achieve robust 
predictions. This technical advantage explains why virtually every successful alternative lending 
platform—from Kenya's Tala and Branch to India's ZestMoney and KreditBee—relies on gradient 
boosting as its core technology.

Third, deep learning neural networks find specific applications where they provide unique 
capabilities, particularly in payments and insurance. Convolutional Neural Networks (CNNs) 
power biometric authentication systems that enable digital identity verification for unbanked 
populations—analyzing facial features, iris patterns, and fingerprints to confirm identity without 
requiring traditional documentation. Similarly, CNNs assess damage from photographs in 
insurance claims processing, extracting insights from visual data that traditional algorithms 
cannot process. The pattern is clear: deep learning is deployed where the input data is 
fundamentally unstructured (images, audio, video) rather than tabular, and where its superior 
pattern recognition capabilities justify the higher computational costs and data requirements.

Fourth, unsupervised learning plays a more limited but critical role, primarily in fraud detection 
and customer segmentation. Anomaly detection algorithms identify novel fraud patterns that 
supervised models—trained only on historical fraud examples—would miss entirely. This 
capability is essential because fraudsters constantly adapt their tactics; purely supervised 
approaches would always lag behind. Similarly, clustering algorithms enable customer 
segmentation without requiring pre-defined categories, allowing platforms to discover natural 
groupings in their user bases and personalize services accordingly. The combination of 
supervised learning (for known patterns) and unsupervised learning (for unknown patterns) 
provides more comprehensive coverage than either approach alone.

Fifth, reinforcement learning remains relatively rare, appearing primarily in optimization 
contexts—payment routing, automated savings nudging, dynamic loan pricing, and portfolio

21

---

<!-- PAGE 22 -->

management. This limited deployment reflects reinforcement learning's significant challenges: it 
requires extensive trial-and-error learning (potentially costly if errors harm real customers), 
demands careful reward function design (mis-specified rewards can lead to perverse outcomes), 
and exhibits sample inefficiency (requiring many iterations to learn effective policies). Where 
reinforcement learning does appear, it addresses sequential decision-making problems where 
the optimal action depends on long-term consequences rather than immediate predictions, and 
where simulation or safe experimentation is possible.

Sixth, cross-cutting technologies—Natural Language Processing and Computer Vision—bridge 
multiple learning paradigms and extend AI's reach into previously inaccessible data modalities. 
NLP enables conversational interfaces (chatbots providing pension guidance or investment 
advice), analyzes unstructured text (loan applications, business descriptions, claims 
documentation), and extracts market sentiment from news and social media. Computer Vision 
processes identity documents, assesses collateral from photos, evaluates crop damage from 
satellite imagery, and verifies physical presence through liveness detection. These technologies 
transform unstructured human-generated content into structured data that supervised, 
unsupervised, or reinforcement learning algorithms can then process.

Finally, the table reveals important sector-specific technological profiles. Payments 
emphasizes real-time supervised classification (fraud detection) combined with biometric neural 
networks and reinforcement learning for routing optimization—reflecting the sector's need for 
instant decisions and continuous system optimization. Lending concentrates supervised learning 
intensity, particularly gradient boosting for alternative credit scoring, reflecting the core 
challenge of predicting creditworthiness from diverse data sources. Insurance uniquely 
combines supervised classification with computer vision for damage assessment and regression 
models for parametric triggers, reflecting its need to process both visual evidence and 
quantifiable parameters. Investments employs the most diverse toolkit (supervised 
classification, time-series forecasting, reinforcement learning, and NLP) reflecting the multi-
faceted challenges of asset allocation, market prediction, risk management, and investor 
communication. Savings & Pensions occupies a middle ground, using supervised learning for 
behavioral prediction and reinforcement learning for nudging optimization, but lacking the 
visual or textual analysis needs that drive other sectors.

This systematic mapping reveals that AI-driven financial inclusion is not monolithic but rather 
comprises a sophisticated ecosystem of complementary technologies, each addressing specific 
challenges through appropriate learning paradigms. The dominance of supervised learning 
reflects pragmatic choices based on data availability and problem structure, while the selective 
deployment of unsupervised learning, reinforcement learning, and advanced techniques like 
deep learning indicates thoughtful matching of tools to tasks. Understanding this technological 
landscape is essential for evaluating both the opportunities and risks that AI presents for 
financial inclusion, as different techniques carry distinct implications for fairness, transparency, 
and accountability: issues we turn to next in examining humane considerations.

22

---

<!-- PAGE 23 -->

4.2 Humane Challenges Across Financial Sectors

While AI's technical capabilities are impressive, Table 4 reveals that each sector confronts 
profound ethical challenges that threaten to undermine financial inclusion goals if not 
adequately addressed.

Table 4: Humane Considerations by Financial Sector

Payments

Savings & Pensions

Lending & Credit

Insurance

Investments

Humane 
Challenge 
Algorithmic Bias 
& 
Discrimination

Fraud models flag rural 
transactions as suspicious

Gender/geography 
discrimination in 
projections

Privacy 
Violations

Biometric data breaches, 
surveillance capitalism

Data privacy and 
security concerns

Digital Divide & 
Exclusion

Smartphone/internet 
requirements exclude 
marginalized groups

Irregular income 
penalized by rigid 
systems

Lack of 
Transparency

Manipulative 
Practices

Cultural 
Insensitivity

Inadequate 
Recourse

Governance 
Gaps

Opaque account 
freezing/transaction 
blocking

Opaque fee structures, 
withdrawal difficulties

Dark patterns, 
excessive risk 
encouragement

Western financial 
models imposed, 
family obligations 
penalized 
Liquidity lockups 
during emergencies

Insufficient human 
oversight in fiduciary 
decisions

No contestation 
mechanisms for 
automated decisions 
Insufficient data 
protection, weak 
oversight

Proxy 
discrimination 
through alternative 
data, historical bias 
perpetuation 
Invasive alternative 
data collection (call 
logs, SMS, social 
networks) 
Sparse digital 
footprints from 
poverty misread as 
risk 
Non-explainable 
credit decisions, 
black-box scoring 
Predatory lending 
targeting vulnerable 
populations

Biased risk 
assessment

Discriminatory 
risk profiling, 
algorithmic 
redlining

Invasive 
behavioral 
surveillance

Geolocation-
based premium 
increases

Limited access for 
low digital literacy 
populations

Unclear denial 
reasons, opaque 
claims processing 
Restrictive 
parametric 
triggers, premium 
extraction

Conflicts of 
interest, 
algorithm opacity 
Fee optimization 
over returns, 
inappropriate risk 
pushing 
One-size-fits-all 
approaches

No ability to 
challenge adverse 
decisions 
Insufficient fairness 
auditing, weak 
explainability 
requirements

Denied claims 
without 
explanation 
Inadequate 
disparate impact 
testing

Algorithmic 
failures without 
accountability 
Weak fiduciary 
enforcement

The systematic analysis reveals recurring themes across sectors. Algorithmic bias and proxy 
discrimination emerge as perhaps the most pervasive challenge. Even when protected 
characteristics like race, ethnicity, or gender are explicitly excluded from models, AI systems 
learn to use proxy variables—zip code, device type, app usage patterns, social network 
characteristics—that correlate with these protected attributes, thereby perpetuating historical 
discrimination under the guise of objective assessment. This is particularly pernicious because it

23

---

<!-- PAGE 24 -->

operates invisibly: the model never explicitly considers race, yet systematically disadvantages 
racial minorities.

Privacy violations constitute another cross-cutting concern. The alternative data powering AI-
driven financial inclusion—mobile phone metadata, social media activity, e-commerce behavior, 
location patterns—represents intimate behavioral surveillance that most users neither fully 
understand nor meaningfully consent to. The Aadhaar biometric breaches in India and concerns 
about Chinese payment platform data practices illustrate how financial inclusion can become a 
pathway to surveillance capitalism, where user data becomes a commodity extracted in 
exchange for financial access.

The digital divide paradoxically threatens to make AI-driven financial inclusion exclusionary. 
Many AI-enhanced services require smartphones, stable internet connectivity, and digital 
literacy—prerequisites that exclude the most marginalized populations who need financial 
inclusion most urgently. When fraud detection systems are trained predominantly on urban 
digital transaction patterns, they may incorrectly flag legitimate rural transactions as suspicious, 
effectively excluding rural users. Similarly, sparse digital footprints generated by poverty—older 
phones, limited internet, low e-commerce participation—get misread by AI as risk indicators, 
creating a vicious cycle where poverty itself becomes a disqualifying factor.

Lack of transparency and explainability undermines user agency and prevents meaningful 
contestation of automated decisions. When an AI system denies credit, freezes an account, or 
increases insurance premiums, users rarely receive comprehensible explanations of why the 
decision was made or how they might improve their situation. This opacity violates principles of 
due process and prevents users from effectively challenging erroneous automated decisions 
that can have devastating consequences for their economic opportunities.

Manipulative practices disguised as personalization represent a particularly insidious risk. AI 
systems can identify vulnerable populations and target them with exploitative terms—predatory 
loans at usurious rates, insurance products with restrictive triggers unlikely to activate, 
investment products generating high fees with poor returns—all optimized through machine 
learning to maximize provider profits while minimizing payouts. Behavioral nudging can cross 
the line into manipulation when it encourages excessive risk-taking by vulnerable savers or locks 
users into illiquid products they cannot access during emergencies.

Cultural insensitivity reflects how AI models trained predominantly on Western financial 
behaviors may misinterpret culturally appropriate patterns as risk indicators. In many cultures, 
supporting extended family takes precedence over individual savings, yet AI systems may 
penalize such transfers as "poor financial discipline." Irregular income reflecting seasonal 
agriculture gets flagged as "income instability" rather than recognized as normal for smallholder 
farmers. These cultural blind spots can make ostensibly inclusive AI systems systematically 
disadvantage non-Western populations.

24

---

<!-- PAGE 25 -->

4.3 The Inclusion Paradox 
Perhaps the most troubling finding is what might be termed the "inclusion paradox": AI enables 
access to financial services for previously excluded populations, but often at exploitative terms. 
Alternative credit scoring allows lending to the credit invisible, but frequently at 30-40% APR or 
higher—rates that provide access while potentially trapping borrowers in debt spirals. Micro-
insurance reaches poor populations, but with parametric triggers set to rarely activate despite 
farmers experiencing losses. Automated investment platforms democratize wealth 
management, but may steer novice investors into high-fee proprietary products.

This paradox raises fundamental questions about whether AI-driven expansion of financial 
access should be celebrated as inclusion or critiqued as exploitation. The answer likely depends 
on implementation details—interest rates, fee structures, transparency, recourse mechanisms, 
and genuine commitment to serving rather than extracting from marginalized communities. 
Technology alone is neutral; the ethical valence depends entirely on how it is deployed and 
governed.

4.4 Toward Humane AI-Driven Financial Inclusion 
Achieving genuinely humane and inclusive AI-driven financial services requires multifaceted 
interventions across technical, regulatory, and institutional domains:

Technical interventions can address fairness, transparency, and privacy challenges through 
several approaches that make AI systems more accountable.

Making algorithms transparent rather than black-box requires explainability techniques. Often, 
when AI denies credit or increases insurance premiums, users receive little explanation. 
Counterfactual explanations flip this paradigm by showing exactly what would need to change: 
"If your mobile payment consistency increased from 60% to 80%, you would qualify for this 
loan." This specificity transforms opaque rejections into actionable guidance. Similarly, 
quantifying each factor's contribution to decisions—"location contributed 10%, transaction 
history 45%, digital footprint 35%, with 10% from other factors"—enables users to understand 
why decisions were made and effectively contest errors.

Preserving privacy while enabling learning presents a fundamental tension in AI-driven financial 
inclusion: alternative data improves credit scoring but raises surveillance concerns. Privacy-
preserving techniques like federated learning resolve this tension by keeping sensitive data on 
users' phones or at local institutions—the AI model travels to where data resides, learns 
patterns locally, and only shares aggregated statistical updates rather than raw information. 
Multiple microfinance institutions can collaboratively improve credit models without ever 
sharing customer databases. Differential privacy adds carefully calibrated statistical noise 
ensuring no individual's information can be extracted from trained models while preserving 
overall accuracy.

25

---

<!-- PAGE 26 -->

Proactively identifying when models fail requires adversarial testing—systematically challenging 
AI systems with edge cases before deployment. Developers feed models applications from 
unusual occupations, transaction patterns from remote rural areas, and data combinations 
rarely seen during training. This stress-testing reveals failure modes where models make 
egregiously wrong decisions for specific subpopulations, allowing fixes before vulnerable users 
are harmed. For instance, adversarial testing might reveal that a credit model systematically 
underscores seasonal agricultural workers, prompting recalibration.

Regulatory frameworks must evolve beyond traditional financial regulation to address 
algorithmic accountability. Requirements might include mandatory algorithmic impact 
assessments before deployment, regular fairness audits testing for disparate impacts across 
demographic groups, explainability standards requiring comprehensible decision explanations, 
data governance frameworks limiting alternative data collection and use, and accessible appeals 
processes for algorithmic decisions. The challenge lies in crafting regulation that protects 
vulnerable populations without stifling beneficial innovation—adaptive governance rather than 
rigid control.

Institutional commitments ultimately determine whether AI serves inclusion or exploitation. 
Financial service providers must adopt fiduciary mindsets, designing products that genuinely 
serve client welfare rather than merely extracting fees. This requires performance metrics that 
measure actual improvements in client financial wellbeing—emergency savings accumulated, 
debts repaid, insurance claims paid, wealth built—not just transaction volumes or revenue 
generated. Participatory design processes should involve intended beneficiaries in product 
development rather than imposing technocratic solutions. Human oversight must complement 
automation, preserving agency and providing recourse when algorithms fail.

Cross-sector collaboration among technology providers, financial institutions, regulators, civil 
society organizations, and affected communities is essential to navigate the complex tradeoffs 
inherent in AI-driven financial inclusion. No single actor possesses sufficient expertise or 
perspective to ensure humane deployment. Multi-stakeholder governance mechanisms can 
facilitate ongoing dialogue, surfacing concerns and adapting practices as understanding evolves.

The evidence from Global South implementations—from M-Pesa's transformation of financial 
access in Kenya to challenges with digital savings platforms in Africa, from alternative credit 
scoring's expansion of lending across multiple markets to concerns about predatory practices—
demonstrates both AI's transformative potential and its capacity to create new forms of 
exclusion and exploitation when deployed without adequate safeguards. Success requires 
unwavering commitment to centering human dignity, social justice, and genuine inclusion rather 
than merely technological sophistication or financial efficiency.

5.  Conclusion

26

---

<!-- PAGE 27 -->

Artificial intelligence emerges as a transformative enabler of financial inclusion, operating 
powerfully across payments, savings, lending, insurance, and investments through innovative 
applications of supervised learning, unsupervised learning, reinforcement learning, natural 
language processing, computer vision, and generative AI. Real-world implementations across 
the Global South—from M-Pesa's AI-enhanced identity verification in Kenya to Nubank's 
automated investment services in Brazil, from Tala's alternative credit scoring across multiple 
African markets to BIMA's micro-insurance serving tens of millions, from India's UPI ecosystem's 
multilingual chatbots to Nigeria's AI-powered agricultural insurance—demonstrate AI's potential 
to democratize financial services at unprecedented scale. By integrating evidence from 
contemporary global research and practical deployments, this analysis illustrates how AI 
fundamentally transforms access, equity, and financial stability for populations previously 
marginalized from formal financial systems.

Credit invisibility represents  20% of the adult population in developed economies and even 
higher proportions in developing markets (Consumer Financial Protection Bureau, 2015). The 
technology's capacity to process alternative data, automate complex decisions, personalize 
services at scale, and operate efficiently in resource-constrained environments promises 
unprecedented opportunities for economic empowerment across diverse global populations. 
Research demonstrates that alternative data models achieve comparable or superior predictive 
power to traditional credit scores while dramatically expanding access—mobile payment data 
correlates with creditworthiness at 0.65-0.72, matching FICO score performance (Björkegren & 
Grissen, 2019). AI-driven microfinance reduces operational costs from 6-12% to under 2%, 
enabling profitable lending at scales previously impossible (Milana & Ashta, 2021). Alternative 
data scoring overwhelmingly relies on gradient boosted tree methods like XGBoost and 
LightGBM, which power 70-80% of production systems because they automatically detect non-
linear relationships and this can reduce costs by 6% to 25% of total losses (Khandani et al., 
2010).

However, realizing this transformative potential requires unwavering commitment to 
responsible deployment, robust ethical oversight, and sustained efforts to mitigate critical risks 
including algorithmic bias that perpetuates discrimination, privacy violations through invasive 
data collection, digital exclusion of populations lacking connectivity or devices, opaque decision-
making that prevents meaningful contestation of automated decisions, and predatory practices 
disguised as financial inclusion (Solon Barocas & Selbst, 2016; Kalluri, 2020). Alternative data can 
encode existing societal inequalities when machine learning trains on data reflecting historical 
discrimination, creating proxy discrimination even without explicitly using protected 
characteristics (Solon Barocas & Selbst, 2016). Mission drift represents a profound risk in 
microfinance, where algorithmic optimization of repayment prediction can gradually shift 
portfolios away from the poorest populations toward easier-to-serve segments, abandoning 
original social missions (A. Ashta & Hudon, 2012; Cull, Demirgüç-Kunt, & Morduch, 2011). The 
inclusion versus exploitation dilemma emerges in the interest rate paradox: AI enables lending 
to previously excluded populations, but often at 30-40% APR or higher: rates that enable access

27

---

<!-- PAGE 28 -->

while potentially trapping borrowers in debt spirals (Rona-Tas & Guseva, 2018).

Success demands that financial inclusion efforts prioritize human dignity over efficiency metrics, 
ensure transparent governance with meaningful accountability mechanisms, proactively address 
digital divides through investment in infrastructure and digital literacy, maintain accessible 
human oversight and appeals processes, and rigorously evaluate whether AI deployments 
genuinely improve financial wellbeing or merely extract value from vulnerable populations 
(Kalluri, 2020; Kroll et al., 2017). Cultural context must inform AI systems—recognizing that 
irregular income flows may reflect seasonal agriculture rather than financial instability, and that 
family financial support represents cultural values rather than poor financial discipline 
(Anderson et al., 2009; Clark, 1997). Financial behavior doesn't translate uniformly across 
cultures, and AI models trained on Western credit bureau data may see culturally appropriate 
patterns as high risk. Fairness constraints must balance predictive accuracy with equitable 
outcomes across demographic groups, accepting minor performance reductions to achieve 
demographic parity and prevent discriminatory impacts (S. Barocas et al., 2019). Regulatory 
frameworks increasingly recognize that algorithmic neutrality doesn't guarantee fair outcomes, 
requiring explainability, disparate impact testing, and fairness-aware machine learning 
approaches (Bracke et al., 2019; V. Bumacov et al., 2014).

Only through such conscientious approaches—informed by voices from affected communities, 
guided by ethical frameworks that center human rights and social justice, regulated by 
governance structures that hold technology providers accountable, and continuously evaluated 
against outcomes for the most marginalized—can AI genuinely advance financial inclusion while 
honoring principles of justice, respecting human dignity, and fostering sustainable, equitable 
development that genuinely serves historically underserved communities rather than creating 
new forms of technological exploitation or algorithmic exclusion (Bélanger et al., 2025; Kalluri, 
2020). The future of AI-driven financial inclusion depends not merely on technological 
sophistication, but on our collective commitment to deploying these powerful tools responsibly, 
ethically, and in genuine service to those who need them most. Ethical AI-driven financial 
inclusion requires preserving human agency, aligning objectives with borrower welfare, 
involving borrowers in design, auditing relentlessly for bias, respecting data dignity, and 
maintaining epistemic humility—recognizing that algorithms trained on thousands of loans 
know patterns while experienced loan officers know context, and both are valuable (Kalluri, 
2020).

References

28

---

<!-- PAGE 29 -->

Akanfe, O., Bhatt, P., & Lawong, D. A. (2025). Technology Advancements Shaping the Financial

Inclusion Landscape: Present Interventions, Emergence of Artificial Intelligence and 
Future Directions. Information Systems Frontiers. doi:10.1007/s10796-025-10597-z 
Anderson, S., Baland, J. M., & Moene, K. O. (2009). Enforcement in informal saving groups.

Journal of Development Economics, 90(1), 14-23. doi:10.1016/j.jdeveco.2008.08.004 
Ash, E., & Hansen, S. (2023). Text algorithms in economics. Annual Review of Economics, 15,

659-688. doi:10.1146/annurev-economics-012320-122921

Ashta, A. (2025). Building Humane Advances and Institutions: A Critical Look at Recent News 
about Artificial Intelligence. Available at SSRN: https://ssrn.com/abstract=5685682.  
Retrieved from https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5685682

Ashta, A., & Herrmann, H. (2021). Artificial intelligence and fintech: An overview of

opportunities and risks for banking, investments, and microfinance. Strategic Change, 
30(3), 211-222. doi:10.1002/jsc.2404

Ashta, A., & Hudon, M. (2012). The Compartamos microfinance IPO: Mission conflicts in hybrid

institutions with diverse shareholding. Strategic Change: Briefings in Entrepreneurial 
Finance, 21(7-8), 331-341.

Barocas, S., Hardt, M., & Narayanan, A. (2019). Fairness and machine learning: Limitations and

opportunities: MIT Press.

Barocas, S., & Selbst, A. D. (2016). Big Data's Disparate Impact. California Law Review, 104(3),

671-732. Retrieved from http://www.jstor.org/stable/24758720

Bélanger, C., Ashta, A., & Mason, G. (2025). Fintech, Banks and Mobile Operators: Interplays for

Increasing Financial Inclusion. In A. Zarifis & X. Cheng (Eds.), Fintech and the Emerging 
Ecosystems: Exploring Centralised and Decentralised Financial Technologies (pp. 409-
425): Springer Nature.

Berg, T., Burg, V., Gombović, A., & Puri, M. (2019). On the Rise of FinTechs: Credit Scoring Using

Digital Footprints. The Review of Financial Studies, 33(7), 2845-2897. 
doi:10.1093/rfs/hhz099

Binns, R. (2018). Fairness in Machine Learning: Lessons from Political Philosophy. Paper

presented at the Proceedings of the 1st Conference on Fairness, Accountability and 
Transparency, Proceedings of Machine Learning Research. 
https://proceedings.mlr.press/v81/binns18a.html

Björkegren, D., & Grissen, D. (2019). Behavior Revealed in Mobile Phone Usage Predicts Credit

Repayment. The World Bank Economic Review, 34(3), 618-634. 
doi:10.1093/wber/lhz006

Bracke, P., Datta, A., Jung, C., & Sen, S. (2019). Machine learning explainability in finance: An

application to default risk analysis. Retrieved from 
https://www.bankofengland.co.uk/working-paper/2019/machine-learning-
explainability-in-finance-an-application-to-default-risk-analysis

Bumacov, V., Ashta, A., & Singh, P. (2014). The Use of Credit Scoring in Microfinance Institutions 
and Their Outreach. Strategic Change: Briefings in Entrepreneurial Finance, 23(7-8), 401-
413.

Bumacov, V., Ashta, A., & Singh, P. (2017). Credit scoring: A historic recurrence in microfinance.

Strategic Change, 26(6), 543-554. doi:10.1002/jsc.2165

Burke, M., & Lobell, D. B. (2017). Satellite-based assessment of yield variation and its

determinants in smallholder African systems. Proceedings of the National Academy of 
Sciences, 114(9), 2189-2194. Retrieved from 
https://www.pnas.org/doi/pdf/10.1073/pnas.1616919114

29

---

<!-- PAGE 30 -->

Chu, M., Laranjeira, C., & Levindo, P. (2020). Nubank: Democratizing Financial Services. Harvard

Business School.

Citron, D. K., & Pasquale, F. (2014). The scored society: Due process for automated predictions.

Washington Law Review, 89, 1-33. Retrieved from 
https://scholarship.law.bu.edu/faculty_scholarship/618

Clark, G. (1997). Money-Go-Rounds: The Importance of Rotating Savings and Credit Associations

for Women. American Ethnologist, 24(3), 673-674. 
doi:https://doi.org/10.1525/ae.1997.24.3.673

Consumer Financial Protection Bureau. (2015). Data point: Credit invisibles. Retrieved from

https://www.consumerfinance.gov/data-research/research-reports/data-point-credit-
invisibles/

Cook, T., & McKay, C. (2015). How M-Shwari works: The story so far. Consultative group to assist

the poor (CGAP) and financial sector deepening (FSD).

Cull, R., Demirgüç-Kunt, A., & Morduch, J. (2011). Does regulatory supervision curtail

microfinance profitability and outreach? World Development, 39(6), 949-965.

Dietterich, T. G. (2000). Ensemble Methods in Machine Learning, Berlin, Heidelberg. 
Djeundje, V. B., Crook, J., Calabrese, R., & Hamid, M. (2021). Enhancing credit scoring with

alternative data. Expert Systems with Applications, 163, 113766. 
doi:https://doi.org/10.1016/j.eswa.2020.113766

Gambacorta, L., Huang, Y., Qiu, H., & Wang, J. (2019). How do machine learning and non-
traditional data affect credit scoring? New evidence from a Chinese fintech firm. 
Retrieved from https://www.bis.org/publ/work834.htm

Hayman, G. (2024). Pensions in the Age of Artificial Intelligence. CFA Institute (Thinking Ahead

Institute).

Hernandez, E., Goslinga, R., & Wang, V. (2018). Using satellite data to scale smallholder

agricultural insurance. Washington, DC: CGAP, August. https://www. cgap. 
org/research/publication/using-satellite-data-scale-smallholder-agricultural-insurance.

Hurley, M., & Adebayo, J. (2016). Credit scoring in the era of big data. Yale Journal of Law and

Technology, 18, 148-216. Retrieved from 
https://openyls.law.yale.edu/server/api/core/bitstreams/a8c7f4e3-ae53-4c43-b6cd-
1223a5703c32/content

Jagtiani, J., & Lemieux, C. (2019). The roles of alternative data and machine learning in fintech 
lending: Evidence from the LendingClub consumer platform. Financial Management, 
48(4), 1009-1029. doi:https://doi.org/10.1111/fima.12295

Jonnalagadda, A. K., & Babu, S. R. (2025). Enhancing Credit Scoring with Alternative Data and

Machine Learning for Financial Inclusion. South Eastern European Journal of Public 
Health, 511-518. doi:10.70135/seejph.vi.3584

Kalluri, P. (2020). Don't ask if artificial intelligence is good or fair, ask how it shifts power.

Nature, 583(7815), 169. doi:10.1038/d41586-020-02003-2

Khandani, A. E., Kim, A. J., & Lo, A. W. (2010). Consumer credit-risk models via machine-learning

algorithms. Journal of Banking & Finance, 34(11), 2767-2787. 
doi:https://doi.org/10.1016/j.jbankfin.2010.06.001

Krishnan, S., Ashta, A., & Babu, D. (2021). Business cycle prediction: Application of Markov chain 
to online crowdlending. Strategic Change, 30(4), 341-351. doi:10.1002/jsc.2428 
Kroll, J. A., Huey, J., Barocas, S., Felten, E. W., Reidenberg, J. R., Robinson, D. G., & Yu, H. (2017). 
Accountable algorithms. University of Pennsylvania Law Review, 165, 633-705. Retrieved 
from https://scholarship.law.upenn.edu/penn_law_review/vol165/iss3/3/

30

---

<!-- PAGE 31 -->

Kshetri, N. (2021). The Role of Artificial Intelligence in Promoting Financial Inclusion in

Developing Countries. Journal of Global Information Technology Management, 24(1), 1-
6. doi:10.1080/1097198X.2021.1871273

Kuraku, C., Gollangi, H. K., & Sunkara, J. R. (2020). Biometric Authentication In Digital Payments:

Utilizing AI And Big Data For Real-Time Security And Efficiency. Educational 
Administration: Theory and Practice, 26(4), 954-964.

Lobell, D. B., Thau, D., Seifert, C., Engle, E., & Little, B. (2015). A scalable satellite-based crop

yield mapper. Remote Sensing of Environment, 164, 324-333. 
doi:https://doi.org/10.1016/j.rse.2015.04.021

Makunda, L., & Matiko, C. (2023). Savings landscape and financial literacy in Kenya according to

FinAccess. Retrieved from https://www.fsdkenya.org/wp-
content/uploads/2023/06/Savings-landscape-and-financial-literacy-in-Kenya-according-
to-FinAccess.pdf

Manta, O., Vasile, V., & Rusu, E. (2025). Banking Transformation Through FinTech and the 
Integration of Artificial Intelligence in Payments. FinTech, 4(2), 13. Retrieved from 
https://www.mdpi.com/2674-1032/4/2/13

Mhlanga, D. (2020). Industry 4.0 in Finance: The Impact of Artificial Intelligence (AI) on Digital 
Financial Inclusion. International Journal of Financial Studies, 8(3), 45. Retrieved from 
https://www.mdpi.com/2227-7072/8/3/45

Milana, C., & Ashta, A. (2021). Artificial intelligence techniques in finance and financial markets:

A survey of the literature. Strategic Change, 30(3), 189-209. 
doi:https://doi.org/10.1002/jsc.2403

Nuka, T. F., & Ogunola, A. A. (2024). AI and machine learning as tools for financial inclusion: 
challenges and opportunities in credit scoring. International Journal of Science and 
Research Archive, 13(2), 1052-1067.

Olajide, B. T., Ekechi, C. C., Popoola, T. O., Adeshina, G. O., Ayittey, S., & Ozo-oguej, P. C. (2025). 
Machine learning for financial inclusion in agriculture: A study of AI-based credit scoring 
tools in rural Nigeria. World Journal of Advanced Research and Reviews, 27(2), 461-470. 
doi:https://doi.org/10.30574/wjarr.2025.27.2.2884

Rona-Tas, A., & Guseva, A. (2018). Consumer credit in comparative perspective. Annual Review

of Sociology, 44, 55-75.

Schwittay, A. (2014). Making poverty into a financial problem: From global poverty lines to

Kiva.org. Journal of International Development, 26(4), 508-519. doi:10.1002/jid.2969

Torre, D., & Xu, Q. (2020). Digital payments in China: adoption and interactions among

applications. Revue d'économie industrielle(172), 55-82.

Vuković, D. B., Dekpo-Adza, S., & Matović, S. (2025). AI integration in financial services: a

systematic review of trends and regulatory challenges. Humanities and Social Sciences 
Communications, 12(1), 562. doi:10.1057/s41599-025-04850-8

Waithaka, L., Kramer, B., Kivuva, B., & Cecchi, F. (2023). Improving agricultural productivity and

resilience with satellite and cellphone imagery to scale climate-smart crop insurance.

World Bank. (2021). The Global Findex Database 2021: Financial inclusion, digital payments, and

resilience in the age of COVID-19. Retrieved from 
https://www.worldbank.org/en/publication/globalfindex

Zuboff, S. (2019). The age of surveillance capitalism: The fight for a human future at the new

frontier of power, edn. PublicAffairs, New York.

31

---

<!-- PAGE 32 -->

Brief bio

Dr. Arvind Ashta is the founder of BHAI, a research consulting firm specializing in AI strategy, 
fintech, and development. He helps organizations articulate evidence-based strategies through 
research-informed writing, white papers, and strategic documentation.

With an h-index over 30 and recognition as a top 1% researcher worldwide (ScholarGPS; 
Stanford top 2% scientists list 2025), he brings 40+ years of experience spanning 17 years in 
corporate finance, 24 years as Professor at Burgundy School of Business, and current adjunct 
roles at Toulouse School of Management and Université Libre de Bruxelles.

His 100+ publications include highly cited research on AI in fintech, financial inclusion, and social 
entrepreneurship. His current work explores AI applications in agricultural technology and 
development finance. He accepts select consulting engagements for research writing, strategic 
advisory, and AI strategy documentation.

Portfolio: https://sites.google.com/view/arvindashta/assignments

For consulting inquiries: arvindashta@gmail.com , bhai2bhai08@gmail.com

Research: https://scholar.google.com/citations?user=zGpnCtUAAAAJ

32

<!-- MARKITDOWN CONVERSION -->

<!-- Full MarkItDown conversion for formatting fidelity. -->

Artificial Intelligence in Microfinance and Financial Inclusion:
Applications, Issues, and Future Directions
Dr. Arvind Ashta
Researcher/Consultant, BHAI: Building Humane Advances and Institutions
Adjunct faculty, Toulouse School of Management, Université Libre de Bruxelles
arvindashta@gmail.com
Abstract
Artificial intelligence (AI) is emerging as a transformative force in microfinance and financial
inclusion, addressing long-standing barriers such as credit invisibility, high operational costs, and
limited access to formal financial services. This paper systematically examines AI applications
across key financial domains (payments, savings, lending, insurance, investments) highlighting
how machine learning, natural language processing, and generative AI are enabling innovative
solutions tailored to the needs of marginalized populations. Drawing on contemporary research
and case studies from the Global South, the analysis demonstrates AI’s potential to democratize
financial services through alternative credit scoring, automated underwriting, and adaptive
tools.
However, the deployment of AI also presents significant challenges, including algorithmic bias,
proxy discrimination, privacy violations, and the risk of exacerbating digital divides. The paper
underscores the need for robust governance frameworks, ethical oversight, and inclusive
policies to mitigate these risks and ensure that AI-driven financial inclusion serves the most
vulnerable without creating new forms of exclusion. Future directions include advancing
fairness-aware AI, improving transparency, and fostering cross-sector collaboration to align
technological innovation with social justice and human dignity.
Keywords: Artificial Intelligence, Microfinance, Financial Inclusion, Machine Learning, Alternative
Credit Scoring, Algorithmic Bias, Digital Divide, Ethical AI, Global South
JEL: G21, G23, 016, O33, D81, I25, C45, C55
1

1. Introduction
Artificial intelligence (AI) comprises computer systems that can perform tasks typically requiring
human intelligence such as pattern recognition, decision-making, and language understanding.
It is rapidly emerging as a critical driver of financial inclusion by enabling access to essential
financial services for historically underserved populations. Financial inclusion represents one of
finance's greatest challenges, with two billion adults worldwide unable to access loans,
insurance, or banking services because they lack traditional credit histories ((World Bank, 2021).
Credit invisibility occurs when individuals have no footprint in conventional credit bureaus—no
credit cards, mortgages, or installment loans that demonstrate repayment behavior. Even those
with "thin files" face exclusion; traditional FICO scores require at least six months of credit
activity across multiple accounts (Consumer Financial Protection Bureau, 2015).
The integration of AI allows financial institutions to break through legacy barriers such as high
costs, lack of infrastructure, and information asymmetries, improving the reach, efficiency, and
personalization of offerings (Akanfe, Bhatt, & Lawong, 2025; Björkegren & Grissen, 2019;
Kshetri, 2021; Vuković, Dekpo-Adza, & Matović, 2025). AI leverages machine learning
(algorithms that improve automatically through experience), natural language processing
(NLP)—technology enabling computers to understand and generate human language—and
algorithmic analytics to empower payments, savings, lending, insurance and investments
(Mhlanga, 2020).
This paper systematically explores AI applications in each financial need area, highlighting
current research, real-world implementations from the Global South, and implications for
inclusive development.
2. Methodology
This study employs a critical review of academic and gray literature, combined with a targeted
analysis of multiple real-world case studies from the Global South.
The literature review draws on peer-reviewed articles, working papers, and reports from
international organizations (e.g., World Bank, CGAP, OECD) to explore the theoretical and
empirical landscape of AI in financial inclusion, with a focus on emerging trends, gaps, and
controversies.
The qualitative analysis examines multiple purposively selected case studies of AI-driven
financial services—including digital payment platforms (e.g., M-Pesa, GCash), micro-lending
apps (e.g., Tala, Branch), and insurtech solutions (e.g., BIMA, Pula)—to identify recurring
patterns, operational challenges, and humane dilemmas. For this analysis, the BHAI framework
is adopted (Arvind Ashta, 2025). The BHAI philosophy advocates for humane AI development
through multidimensional inclusion—political, economic, and social—alongside environmental
consciousness, calling for adaptive institutional oversight that guides how technologies are
applied rather than rigidly controlling innovation. It emphasizes context-sensitive governance
2

with transparent accountability to ensure AI advances benefit all people, especially marginalized
populations, while addressing interconnected technological, environmental, and societal
challenges through the lens of dignity, ethics, and social impact. The framework operationalizes
this vision through six core components—innovation assessment, human dignity and justice,
ethical oversight, inclusion and social impact, contextual sensitivity drawing on literary and
philosophical sources, and actionable reflection—using an interpretative-constructivist
approach that prioritizes context-rich, nuanced insights over universal generalizations to guide
humane and equitable AI development (Arvind Ashta, 2025).
By triangulating these sources, the paper offers a nuanced assessment of AI’s role in
microfinance, while acknowledging the limitations of a non-systematic review approach.
3. Findings
3.1 Payments
3.1.1 Digital Identity Verification & Onboarding
The adoption of AI-powered digital Know Your Customer (KYC) processes in payment platforms
has fundamentally transformed onboarding experiences for unbanked populations by
automating identity verification using biometric scans (fingerprints, facial recognition, iris scans),
document analytics powered by computer vision (AI systems that can 'see' and interpret
images), and liveness detection (technology that confirms a person is physically present rather
than using a photo or video) (Kuraku, Gollangi, & Sunkara, 2020). These systems typically
employ supervised learning—where algorithms are trained on labeled datasets of genuine
versus fraudulent documents—combined with deep learning neural networks (interconnected
layers of algorithms inspired by the human brain) for facial recognition.
Mobile money providers like M-Pesa1 in Kenya have pioneered AI-enhanced KYC that allows
users to register using basic mobile phones and biometric verification, reaching millions of
previously unbanked individuals. In India, the Aadhaar biometric identity system2, integrated
with payment platforms like Paytm and PhonePe, uses AI-powered iris and fingerprint matching
to onboard over 400 million digital payment users3. NuBank was able to reach millions of
unbanked people in Brazil through its online credit card which used automated KYC checks (Chu,
Laranjeira, & Levindo, 2020).
1 https://www.safaricom.co.ke/annualreport_2022/our-technology/
2 https://www.biometricupdate.com/202508/uidai-celebrates-2b-aadhaar-face-biometric-
authentications-milestone
3 https://www.indiatvnews.com/technology/news/google-pay-phonepe-and-paytm-users-now-use-your-
face-or-fingerprint-for-upi-payments-making-them-pin-free-2025-10-08-1011756
3

These innovations minimize manual errors, dramatically accelerate access to financial services
from weeks to minutes, and increase trust in digital payments for those previously excluded
from the formal financial sector while ensuring regulatory compliance and scalability even in
markets characterized by limited infrastructure.
3.1.2 Fraud Detection & Transaction Security
Machine learning models enable sophisticated real-time fraud detection in payment platforms,
identifying anomalies, fraudulent activities, and irregular behavioral patterns as transactions
occur across networks (Mhlanga, 2020). These systems predominantly use supervised learning
trained on historical fraud cases, combined with unsupervised learning (algorithms that find
hidden patterns in data without labeled examples) to detect novel fraud schemes not seen
before. Advanced implementations employ ensemble methods (combining multiple AI models
for better accuracy) that perform better than a single classifier (Dietterich, 2000). Anomaly
detection algorithms can flag deviations from normal transaction patterns.
Flutterwave, a Nigerian payment gateway processing transactions across Africa, uses AI-
powered fraud detection that analyzes multiple behavioral and transactional features in real-
time, reducing fraud losses while enabling cross-border payments for small businesses4. GCash
in the Philippines employs machine learning to monitor transactions of over 94 million users5,
detecting suspicious patterns like account takeovers or merchant fraud that would be
impossible for human analysts to identify at scale. Kenya's Safaricom uses AI to protect M-Pesa
transactions from SIM-swap fraud and account compromise, analyzing device fingerprints,
location patterns, and behavioral biometrics6.
By processing massive datasets with unprecedented speed and accuracy, these AI systems can
flag suspicious activity instantly, dynamically adapting risk thresholds and security protocols to
evolving user behavior patterns and emerging threat landscapes, which significantly improves
payment security while building customer confidence, especially critical for first-time users
entering the digital financial ecosystem.
3.1.3 Personalization & User Segmentation
AI enables payment systems to tailor services precisely to individual users through clustering
algorithms (unsupervised learning methods that group similar users together) and classification
models (supervised learning that predicts user categories) based on transactional patterns,
behavioral analytics, geographic data, and temporal usage trends. Recommendation systems,
similar to those used by e-commerce platforms, employ collaborative filtering (predicting user
preferences based on similar users' behavior) to suggest relevant payment features, cashback
offers, and financial products.
4 https://thepaymentsassociation.org/article/flutterwave-2024-report-highlights-record-growth-
expansion-and-innovation/
5 https://www.philstar.com/opinion/2024/11/12/2399421/gcash
6 https://kenyanwallstreet.com/how-safaricom-is-leveraging-ai-to-bolster-m-pesa-security-and-efficiency
4

WeChat Pay and Alipay in China pioneered AI-driven personalization in digital payments (Torre
& Xu, 2020), analyzing billions of transactions to offer customized merchant recommendations,
targeted promotions, and differentiated service tiers based on user behavior. India's PhonePe
employs AI to customize its interface and product recommendations for diverse user segments,
from urban professionals to rural farmers, ensuring relevance across literacy levels and use
cases7.
Platforms can offer customized payment options, personalized loyalty rewards, and
differentiated access mechanisms, rising above traditional one-size-fits-all approaches that often
fail to meet diverse user needs. This sophisticated personalization builds stronger user
engagement, encourages sustained participation in the financial ecosystem, and enables rapid
response to evolving customer needs, ensuring that financial services genuinely serve the
populations they aim to reach.
3.1.4 Embedded Finance & Cross-Platform Integration
AI-driven embedded payment solutions facilitate seamless integration with other essential daily
services including utility management, e-commerce platforms, public transportation systems, or
mobile wallet applications, substantially amplifying reach and user convenience (Bélanger,
Ashta, & Mason, 2025). These systems use API-based integration (application programming
interfaces that allow different software systems to communicate) enhanced with AI-powered
risk scoring and real-time fraud detection operating across platforms. Reinforcement learning
(algorithms that learn optimal strategies through trial and error with rewards for successful
outcomes) can optimize payment routing, fee structures, and approval rates across integrated
channels.
Grab in Southeast Asia embeds AI-enhanced payments within ride-hailing, food delivery, and
financial services, processing millions of micro-transactions daily across eight countries with
intelligent fraud prevention adapted to each use case8. Indonesia's Gojek similarly integrates
payments across transportation, food, logistics, and financial services using AI to detect
fraudulent merchants and protect users across ecosystem touchpoints9. In Africa, companies
like Jumia and Konga embed AI-powered payment scoring into e-commerce checkout, enabling
instant credit decisions for purchases. Jumia is driving its brand with AI-driven customer service
and product recommendation, while Konga is deploying predictive analytics and personalised
marketing10.
Real-time fraud detection capabilities and adaptive user authentication processes minimize
security risks while enabling service providers to deliver faster, more reliable payment
experiences across multiple touchpoints. By embedding financial services within familiar
contexts rather than requiring separate banking interactions, AI helps overcome psychological
7 https://brandwell.ai/blog/how-to-customize-phonepe-payment-solutions-with-ai-complete-guide/
8 https://bytebridge.medium.com/comprehensive-report-on-grab-holdings-daa9e7d3918f
9 https://techwireasia.com/2020/11/gojek-sees-profitability-ahead-after-a-decade-of-rapid-growth/
10 https://thenationonlineng.net/revealed-nigerian-brands-banking-on-robots-ai/
5

barriers to adoption and creates natural pathways for previously excluded populations to enter
the formal financial system. In one study, 70% reported that the use of artificial intelligence in
risk assessment and social impact evaluation improves decision making (Manta, Vasile, & Rusu,
2025).
3.1.5 Humane Considerations
While AI transforms payment accessibility, critical ethical concerns demand attention. Dignity
and justice require that biometric data collection respects privacy and obtains informed
consent, particularly from vulnerable populations who may not fully understand data
implications or have limited alternatives.
Cases of biometric data breaches in India's Aadhaar system and concerns about Chinese
payment platforms' data practices highlight risks of surveillance capitalism where user data
becomes a commodity (Zuboff, 2019).
Governance frameworks must ensure AI systems do not perpetuate discrimination through
biased algorithms that systematically disadvantage certain demographics—for instance, fraud
detection models trained predominantly on urban transaction patterns may incorrectly flag
legitimate rural transactions as suspicious, effectively excluding rural users (Solon Barocas &
Selbst, 2016).
Inclusion efforts must bridge digital divides by ensuring that AI-powered payment solutions
remain accessible to those with limited digital literacy, unreliable internet connectivity, or older
devices—many AI-enhanced payment apps require smartphones and stable internet, potentially
excluding the most marginalized (V. Bumacov, Ashta, & Singh, 2014; Hurley & Adebayo, 2016).
Transparency in algorithmic decision-making, particularly around why accounts are frozen or
transactions blocked, robust data protection measures that prevent unauthorized sharing of
financial data, and accessible recourse mechanisms when AI systems make errors are essential
to building trust. They ensure that AI-driven payment innovations genuinely empower rather
than exploit marginalized communities (Akanfe et al., 2025).
3.2 Savings & Pensions
3.2. 1 Behavioral Nudges & Automated Savings
AI's capacity for micro-segmentation and predictive analytics enables savings platforms to
create highly personalized savings mechanisms that adapt to individual users' unique
employment patterns, income volatility cycles, and financial goals. These systems employ
supervised learning models trained on historical savings behavior to predict optimal savings
amounts and timing, combined with reinforcement learning algorithms that continuously
optimize nudging strategies based on user responses. Behavioral economics principles are
operationalized through AI-powered interventions such as automated round-up features (saving
spare change from transactions), goal-based savings trackers, and timely motivational
6

messages(Cook & McKay, 2015; Makunda & Matiko, 2023). Table 1 shows some of the
behavioral finance features incorporated by digital savings accounts.
Table 1: Behavioural finance nudges in digital savings
Behavioural Principle Digital Savings Nudge Result
Present Bias Makes saving instant & Reduces procrastination.
frictionless.
Mental Accounting Creates a separate "Savings" Protects savings from daily
account. spending.
Loss Aversion Offers interest (a "gain"). Frames “not saving” as a loss.
Commitment Device "Lock Savings" feature. Enforces discipline by restricting
access.
Feedback Loop Links savings to loan eligibility. Rewards saving with a tangible,
valuable
Now, artificial intelligence can take this further. By analysing the payment patters based on bank
of mobile payments, AI can analyze transaction patterns and automatically suggest personalized
savings amounts based on predicted future income, enabling millions of informal workers to
build emergency funds. Savings and investement fintechs can use machine learning to create
customized automated savings plans that adapt to users' irregular income streams.
In India, micro-savings platforms like Jar use AI to invest small amounts automatically in digital
gold, with algorithms determining optimal purchase timing based on price patterns and user
affordability11. These AI-driven interventions motivate users to save regularly by aligning
financial products with their actual circumstances rather than imposing rigid structures,
improving client loyalty and helping close critical inclusion gaps in retirement planning and
emergency savings, ultimately contributing to more financially secure populations across diverse
socioeconomic contexts.
3.2.2 Pension Optimization & Retirement Planning
Generative AI and simulation models can forecast personalized retirement outcomes for
individual users, creating detailed scenario analyses showing how different savings strategies,
contribution levels, and investment allocations affect long-term financial security. These
systems use Monte Carlo simulations (running thousands of possible future scenarios with
11 https://www.forbesindia.com/article/leadership/jar-how-to-build-your-own-pot-of-gold/93180/1
7

different economic conditions) combined with supervised learning models that predict life
expectancy, healthcare costs, and inflation impacts based on individual characteristics. Time-
series forecasting algorithms (models specialized in predicting sequential data points) project
pension growth under various economic scenarios.
In Latin America, Mexico's CONSAR (pension regulator) has piloted AI tools that help informal
workers understand retirement needs through simplified projections based on irregular income
patterns. It has also used AI to detect potentially suspicious websites aimed at pension savers 12.
According to a CFA Institute report (Hayman, 2024), AI can be applied across the pension value
chain to enhance personalization, efficiency, and accuracy in addressing key retirement system
challenges. AI applications include improving member engagement through chatbots and
personalized communications, automating recordkeeping and fraud detection, streamlining
governance processes through document analysis and covenant assessments, enhancing
investment decision-making via predictive analytics and portfolio optimization, and supporting
better decumulation strategies in the payout phase. The technology can help pension funds
analyze large datasets to improve trustee decision-making, provide personalized retirement
planning tools tailored to individual member characteristics, reduce administrative burdens, and
enhance both DB and DC plan management through machine learning models that optimize
asset allocation and risk management.
South Africa's pension administrators are implementing AI-driven tools to project retirement
adequacy for workers transitioning between formal and informal employment. This adaptive
guidance significantly enhances financial understanding across literacy levels, increases
meaningful engagement with retirement planning, and empowers users to make confident,
informed decisions about their long-term financial stability. By translating complex financial
concepts into accessible scenarios and visualizations, AI strengthens the inclusive impact of
digital savings platforms, making sophisticated financial planning tools available to populations
that previously lacked access to professional financial advice.
3.2.3 Humane Considerations
AI-driven savings innovations must uphold human dignity by ensuring that automated nudging
systems do not exploit vulnerable savers through manipulative dark patterns (design choices
that trick users into actions against their interests) or opaque fee structures disguised as helpful
features. Governance mechanisms must prevent algorithmic manipulation that encourages
excessive risk-taking or inappropriate long-term lockups for users who may face emergencies
requiring liquidity—several African digital savings platforms have faced criticism for making
withdrawals difficult while aggressively pushing savings deposits.
Ethical frameworks should ensure that personalization respects cultural values around money,
family obligations, and retirement expectations rather than imposing Western financial planning
12 https://www.nortonrosefulbright.com/en-419/knowledge/publications/ba2b4dbd/pensions-regulator-
develops-ai-tool-to-detect-potentially-suspicious-pension-websites
8

models—in many cultures, supporting extended family takes precedence over individual
retirement savings, yet AI systems may penalize such transfers as 'poor savings discipline'
(Anderson, Baland, & Moene, 2009).
Inclusion requires addressing the reality that informal workers often face irregular income
streams, making rigid automated savings schedules counterproductive—AI systems should
accommodate rather than penalize income variability.
The CFA report (Hayman, 2024) emphasizes that while AI offers significant potential to improve
retirement outcomes and operational efficiency, successful implementation requires balancing
automation with human oversight, ensuring data privacy and security, maintaining transparency
and explainability in AI-driven decisions, and using technology to augment rather than replace
human judgment in fiduciary responsibilities. Transparent communication about investment
performance, accessible withdrawal options during genuine emergencies without excessive
penalties, protection against algorithmic errors that could devastate retirement security (such as
incorrect contribution calculations or failed transfers), and ensuring that predictive models don't
discriminate based on factors like gender or geography when projecting retirement needs are
fundamental requirements for ethical AI deployment in savings and pensions.
3.3 Lending & Credit
3.3.1 Alternative Credit Scoring & Data Analytics
A credit score is a number based on an analysis of a person's credit files, to represent the
creditworthiness of an individual. It has been used in developed countries for many decades but
was introduced more recently to microcredit (Vitalie Bumacov, Ashta, & Singh, 2017). Credit
invisibility occurs when individuals have no footprint in conventional credit bureaus: no credit
cards, mortgages, or installment loans that demonstrate repayment behavior. Traditional credit
scoring creates a paradox that locks out entire populations: you cannot get your first loan
without credit history, but you cannot build credit history without getting loans (World Bank,
2021).
In the United States alone, 45 million adults are either completely credit invisible or have credit
files too thin to generate reliable scores, representing 20% of the adult population,
disproportionately concentrated among minority communities and lower-income households
(Consumer Financial Protection Bureau, 2015).
Now, AI leverages alternative data sources (see Table 2) including mobile phone usage patterns,
e-commerce transaction histories, utility payment records, social network data, and smartphone
sensor data (like GPS patterns indicating stable employment) for sophisticated credit scoring
that addresses exclusion of populations with thin files or those without formal credit histories
(Björkegren & Grissen, 2019; Gambacorta, Huang, Qiu, & Wang, 2019; Nuka & Ogunola, 2024).
9

Research demonstrates that telecommunications payment data shows particularly strong
predictive power—studies across multiple markets find correlations of 0.65 to 0.72 between
mobile phone bill payment consistency and loan repayment rates, comparable to traditional
FICO scores (Björkegren & Grissen, 2019).
Table 2: Traditional versus Alternative Data
Data Type Traditional Data Alternative Data
Income Formal employment income Gig economy and freelance earnings
Payment History Credit card and loan Rental payments, utility bills
repayments
Spending Bank account transactions Mobile money and digital wallets
Patterns
Assets Property ownership Informal savings groups and investments
Demographics Age, marital status Social media and online activity
Credit History Bank credit reports Alternative lending platform histories
Behavioral Data N/A Psychometric testing, online behavior
analytics
Source: The first five rows (Nuka & Ogunola, 2024) and the last two rows added by author.
These systems employ supervised learning with classification algorithms such as gradient
boosting machines, random forests (ensemble methods that combine multiple decision trees),
and neural networks trained on historical repayment data to predict default probability
(Jonnalagadda & Babu, 2025). Alternative data scoring overwhelmingly relies on gradient
boosted tree methods, particularly XGBoost and LightGBM, which power 70-80% of production
systems at companies like Affirm, Upstart, and Kabbage because they automatically detect non-
linear relationships and handle the messy, incomplete nature of alternative data (Khandani, Kim,
& Lo, 2010).
Where traditional scoring uses 5-10 variables from credit bureaus, ML models might incorporate
500-5,000 features extracted from alternative sources and this reduces default rates (Berg,
Burg, Gombović, & Puri, 2019). Feature engineering (the process of selecting and transforming
raw data into useful predictors) identifies hundreds of behavioral indicators from alternative
10

data—call patterns, SMS metadata, app usage, mobile money transactions—that correlate with
creditworthiness (Gambacorta et al., 2019).
Kenya's Branch and Tala pioneered smartphone-based credit scoring analyzing over 10,000 data
points from users' phones to predict repayment likelihood, disbursing billions in microloans to
borrowers with no formal credit history. In India, companies like ZestMoney and KreditBee use
AI models incorporating e-commerce behavior, digital wallet usage, and education data to score
young borrowers entering credit markets. Nigeria's Carbon (formerly Paylater) analyzes bank
transaction data, mobile money flows, and social media presence to assess creditworthiness for
millions of borrowers (Olajide et al., 2025). China's Ant Financial developed Zhima Credit, which
scores over 1 billion users based on consumption behavior, money transfer networks, and
fulfillment of commitments13.
By recognizing reliability demonstrated through non-traditional channels, these AI-powered
alternative credit scoring systems fundamentally transform credit accessibility. They open
lending markets to billions previously deemed unscoreable or too risky based solely on absence
from traditional credit bureaus. This enables entrepreneurs, smallholder farmers, and gig
economy workers to access productive capital (Djeundje, Crook, Calabrese, & Hamid, 2021;
Jagtiani & Lemieux, 2019; Nuka & Ogunola, 2024).
3.3.2 Automated Credit Risk Assessment
Automated underwriting systems leverage ensemble machine learning methods combining
multiple supervised learning algorithms (logistic regression for baseline probability, gradient
boosting for complex patterns, and neural networks for non-linear relationships) for fast,
accurate risk evaluations in microfinance and small-to-medium enterprise lending (Milana &
Ashta, 2021). These systems process loan applications in real-time, analyzing hundreds of
variables simultaneously including alternative credit scores, cash flow patterns, business sector
risks, and macroeconomic indicators to generate risk ratings and recommend loan terms.
Natural language processing analyzes loan applications and business descriptions to assess
viability, while computer vision can evaluate collateral photos submitted via mobile apps.
India's Aye Finance uses AI underwriting to assess micro-enterprises' creditworthiness by
analyzing GST filings, bank statements, and business characteristics, approving loans within 72
hours for businesses traditional banks reject14. Kenya's Musoni uses machine learning models to
underwrite agricultural loans based on mobile money transaction history, farm size data from
satellite imagery, and weather patterns, serving smallholder farmers efficiently. Brazil's Creditas
employs AI to underwrite asset-backed loans for lower-income borrowers using alternative data
combined with vehicle and property valuations. Bangladesh's bKash integrates AI-powered
micro-lending directly into its mobile money platform, using transaction history to automatically
pre-approve small loans for merchants and users.
13 https://en.wikipedia.org/wiki/Zhima_Credit
14 https://www.ayefin.com/wp-content/uploads/2024/12/Aye-Finance-Limited-Industry-Report.pdf
11

By reducing decision-making costs from hundreds of dollars per loan to pennies, and processing
times from weeks to minutes, AI-powered underwriting makes credit accessible to borrowers
seeking smaller loan amounts that would be unprofitable under traditional manual underwriting
processes, enabling financial inclusion at unprecedented scale (Jagtiani & Lemieux, 2019).
3.3.3 Flexible Loan Products & Dynamic Pricing
AI enables lenders to create highly tailored lending products for diverse populations including
gig workers, self-employed individuals, seasonal laborers, and small entrepreneurs by using
reinforcement learning to continuously optimize loan terms, repayment schedules, and interest
rates based on borrower behavior and repayment success. Predictive models employing time-
series analysis forecast income volatility and optimal repayment timing for borrowers with
irregular cash flows. Dynamic pricing algorithms adjust interest rates based on individual risk
profiles, competitive market conditions, and the lender's liquidity needs, making credit more
accessible while maintaining profitability.
Argentina’s Ualá uses AI to offer flexible credit lines that adapt to users' spending and
repayment patterns, with personalized limits and interest rates reflecting individual behavior
rather than rigid categorical rules15. In Kenya, Apollo Agriculture combines AI credit scoring with
flexible repayment schedules aligned to harvest cycles, providing smallholder farmers with
inputs financing that accommodates seasonal income patterns16. Philippines-based Robocash
uses machine learning to dynamically adjust loan terms and pricing based on borrower
engagement and partial repayment behavior, reducing defaults while expanding access17. India's
KreditBee employs AI to offer flexible tenure options and personalized interest rates for young
professionals with variable income streams18.
This sophisticated segmentation moves beyond one-size-fits-all credit products that often fail to
serve non-traditional borrowers effectively, recognizing that different economic activities
require different financial structures. Personalized lending increases repayment success rates
while expanding access to populations whose income variability previously disqualified them
from credit, ultimately fostering entrepreneurship and economic development across diverse
economic sectors.
3.3.4 Humane Considerations
AI-powered lending raises profound ethical concerns around dignity and justice, particularly
regarding algorithmic bias that may perpetuate historical discrimination in credit access
(Djeundje et al., 2021). Alternative data can encode existing societal inequalities: low-income
15 https://www.bnamericas.com/en/news/argentinas-uala-working-on-integrating-2-banks-into-its-tech-
stack
16 https://nation.africa/kenya/news/gender/meet-the-don-teaching-machines-to-speak-africa-s-
languages-one-algorithm-at-a-time-5186224
17 https://juicyscore.ai/en/case-studies/robocash-reduces-high-risk-application-flow-by-75-with-
juicyscore
18 https://www.kreditbee.in/flexi-personal-loan
12

neighborhoods generate fewer digital footprints simply because residents have older phones,
less reliable internet, and lower e-commerce participation.
When machine learning trains on this data, it may learn that sparse digital activity predicts
default—not because sparse activity causes default, but because it correlates with poverty. This
creates proxy discrimination: the model never sees race, but zip code, device type, and app
usage patterns serve as proxies (Solon Barocas & Selbst, 2016). Studies have revealed that even
alternative credit scoring models can encode proxy discrimination—for instance, smartphone
models, app usage patterns, or social media behavior may correlate with protected
characteristics like race or ethnicity, leading to discriminatory outcomes despite not explicitly
using these variables.
Governance frameworks must ensure transparency in credit scoring algorithms, including model
explainability (the ability to understand why an AI system made a specific decision), allowing
borrowers to understand and effectively contest automated decisions affecting their economic
opportunities (Bracke, Datta, Jung, & Sen, 2019). Individuals should be granted an opportunity
to challenge adverse decisions based on artificial intelligence generated scores (Citron &
Pasquale, 2014).
Predatory lending practices can be amplified by AI systems that identify vulnerable populations
and target them with exploitative terms disguised as personalized offers. Debt creates an entire
industry profiting from exploitation (Rona-Tas & Guseva, 2018).
Inclusion requires that alternative data usage respects privacy boundaries—analyzing call logs,
SMS content, or social networks raises serious privacy concerns, especially when users aren't
fully informed about data usage (Citron & Pasquale, 2014).
Fair lending principles would require that AI systems do not punish poverty by charging
exponentially higher rates to those already economically marginalized: differential pricing
should reflect actual risk, not merely exploit price insensitivity among desperate borrowers.
Algorithmic credit expansion must not create debt traps through inappropriate loan approvals
or inflexible collection practices, but rather provide genuine pathways to economic
empowerment through responsible, affordable credit that borrowers can realistically repay (A.
Ashta & Hudon, 2012).
3.4 Insurance
3.4.1 Risk Profiling & Insurability Assessment
AI builds comprehensive insurability profiles by assessing digital footprints and alternative data
to evaluate risk levels when traditional actuarial data is limited or nonexistent, enabling insurers
to expand coverage into previously underserved markets (Vuković et al., 2025). These systems
employ supervised learning with classification models (typically ensemble methods like XGBoost
13

or neural networks) trained on claims history, lifestyle indicators extracted from mobile usage,
geographic risk factors from satellite imagery, and health proxies derived from activity patterns.
Computer vision analyzes submitted photos of homes, vehicles, or farms to assess insurability
and detect pre-existing damage, while satellite imagery and weather data inform agricultural
insurance risk models (Lobell, Thau, Seifert, Engle, & Little, 2015).
BIMA, operating across Africa and Asia, uses AI-powered micro-insurance assessment based on
mobile phone data and basic health questions to provide life and health insurance to over 45
million low-income customers who lack traditional medical records19. In India, Toffee Insurance
uses machine learning to offer bite-sized insurance products personalized to individual risk
profiles derived from smartphone data and payment histories20. Kenya's M-Pesa partners with
insurance providers to offer micro-insurance scored based on transaction patterns and mobile
usage, automatically enrolling users in appropriate coverage tiers.
By recognizing patterns that correlate with insurance claims experience across diverse data
sources, AI enables evidence-based risk pricing that makes insurance economically viable for
both providers and low-income customers. This innovation transforms insurance accessibility by
moving beyond stereotypes and limited data to data-driven individual risk assessment, opening
insurance markets to billions previously deemed too risky or expensive to serve profitably.
3.4.2 Automated Underwriting & Claims Processing
Machine learning automates complex insurance underwriting and accelerates claims processing
through computer vision for damage assessment, natural language processing for claims
documentation analysis, and predictive models for fraud detection. Supervised learning models
trained on historical claims data classify claim validity, estimate loss amounts, and detect
fraudulent patterns. Deep learning with convolutional neural networks (specialized
architectures for analyzing images) can assess crop damage, vehicle accidents, or property
destruction from photos submitted via mobile apps, providing near-instant loss estimates. In
parametric insurance (coverage that pays out automatically when specific measurable events
occur), AI monitors trigger conditions like rainfall levels, earthquake magnitude, or temperature
thresholds using IoT sensors and satellite data.
In Nigeria Pula uses AI-powered parametric insurance for smallholder farmers, automatically
triggering payouts based on satellite-derived vegetation health indices and weather station
data, eliminating lengthy manual claims processes (Hernandez, Goslinga, & Wang, 2018).
Kenya's Britam Insurance employs computer vision to assess vehicle damage from smartphone
photos, reducing claims processing time from weeks to hours21. India's Acko uses fully
19 https://www.cgap.org/about/people/bima
20 https://wishboxstudio.in/toffee-insurance-a-case-study/
21 https://thedailywhistle.co.ke/faster-claims-fewer-headaches-ai-is-transforming-kenyas-insurance-
industry/
14

automated claims processing with AI analyzing photos, policy terms, and repair cost databases
to approve and disburse claims within minutes for cyber insurance and product protection22.
By processing risk factors continuously and updating models with emerging data, AI enables
dynamic pricing that reflects actual risk rather than outdated assumptions, making innovative
insurance products financially sustainable and allowing insurers to offer coverage for climate-
related disasters, crop failures, and health emergencies that disproportionately affect poor
communities.
3.4.3 Micro-Insurance Products & Parametric Coverage
AI creates highly flexible micro-insurance products and specialized offerings like harvest-linked
agricultural insurance, weather-indexed coverage, and health micro-insurance tailored for
farmers, informal workers, and micro-entrepreneurs facing context-specific risks. Machine
learning models employing regression analysis (predicting continuous numerical outcomes) and
time-series forecasting assess correlations between observable parameters (rainfall,
temperature, vegetation indices) and actual losses, enabling parametric triggers that are
objective and verifiable (Burke & Lobell, 2017). Clustering algorithms segment users based on
occupation, location, and risk exposure to design targeted products.
Nigeria's Pula Advisors partners with mobile money platforms to offer index-based crop
insurance integrated directly into agricultural input purchases, with AI determining coverage
amounts and monitoring weather patterns to trigger automatic payouts via mobile money
without requiring manual claims (Hernandez et al., 2018). In Ghana, ACRE Africa uses machine
learning combined with satellite data and weather station networks to offer parametric
insurance covering drought and excess rainfall risks for smallholder farmers, with payouts
automatically triggered when rainfall deviates from optimal levels (Waithaka, Kramer, Kivuva, &
Cecchi, 2023). India's Skymet combines AI weather prediction models with blockchain-based
smart contracts to automate parametric insurance payouts for millions of farmers, reducing
administrative costs and preventing payout delays23. Kenya's Turaco offers device insurance, life
insurance, and health coverage bundled with mobile money services, using AI to price policies
dynamically based on risk profiles24.
This customization increases insurance value for policyholders while improving risk pools for
insurers, creating sustainable insurance markets that protect vulnerable populations from
shocks that could otherwise destroy livelihoods.
3.4.4 Humane Considerations
AI-driven insurance must respect dignity by avoiding discriminatory risk profiling that unfairly
penalizes vulnerable populations for factors beyond their control. Algorithmic redlining concerns
are particularly acute in insurance—AI systems trained on historical data may systematically
22 https://digiqt.com/blog/acko-insurance-automation/
23 https://www.skymetweather.com/corporate/cropinsurance.html
24 https://www.turaco.insure/about-us
15

deny coverage or charge prohibitive premiums to marginalized communities, perpetuating
rather than addressing inequality (Solon Barocas & Selbst, 2016). For instance, using geolocation
data may result in higher premiums for residents of informal settlements regardless of
individual risk factors, effectively excluding the poor. Governance mechanisms must prevent
proxy discrimination where AI uses variables like smartphone type, social network
characteristics, or consumption patterns that correlate with protected characteristics like race,
religion, or caste.
Justice would require that micro-insurance pricing remains genuinely affordable and that claims
processing does not become opaque or systematically deny legitimate claims through
algorithmic gatekeeping—some parametric insurance schemes have faced criticism for setting
triggers that rarely activate despite farmers experiencing losses. Commitment to expanding
genuine protection rather than simply extracting premiums from poor communities requires
that insurance products actually transfer meaningful risk and provide timely payouts when
losses occur, not just collect premiums while minimizing payouts through restrictive AI-
determined conditions.
Inclusion requires recognizing that alternative data usage for risk assessment must not become
invasive surveillance that commodifies poverty or exploits vulnerable populations by extracting
intimate behavioral data in exchange for basic insurance coverage (Zuboff, 2019).
Ethical deployment demands transparency about how AI determines insurability, with clear
explanations of why someone might be denied coverage or charged higher premiums (S.
Barocas, Hardt, & Narayanan, 2019). Accessible appeals processes for denied claims or disputed
risk ratings are essential, ensuring that algorithmic decisions can be challenged.
3.5 Investments
3.5.1 Automated Portfolio Management & Robo-Advisory
AI-powered robo-advisors (automated platforms providing financial planning and investment
management) democratize access to sophisticated portfolio management previously available
only through expensive human advisors (Kshetri, 2021). These systems employ supervised
learning algorithms for asset allocation (determining optimal distribution across stocks, bonds,
and other investments), regression models for return prediction, and optimization algorithms
(mathematical methods for finding the best solution under constraints) to build diversified
portfolios aligned with individual risk tolerance and goals. Reinforcement learning can
continuously adjust strategies based on market conditions and portfolio performance, learning
optimal rebalancing policies over time. Natural language processing enables conversational
interfaces that guide novice investors through onboarding and ongoing portfolio management in
accessible language.
16

Brazil's Nubank offers AI-driven investment products to over 120 million customers in Brazil,
Mexico, and Colombia, many first-time investors, with automated portfolio construction based
on individual risk profiles and goals25. Mexico's Flink uses robo-advisory with micro-investing
features, allowing users to start with as little as 30 pesos while AI builds diversified portfolios
adapted to Latin American markets26. Kenya's Ndovu provides automated investment
management accessible via mobile money integration, using AI to create portfolios suitable for
African market conditions and investor profiles ranging from urban professionals to rural
savers27. India's Groww platform use machine learning to recommend thematic investment
portfolios and mutual funds tailored to users' financial situations, education levels, and
investment horizons28.
By providing professional-grade portfolio management at fraction of traditional costs, AI enables
small-scale investors to participate in wealth-building opportunities historically reserved for the
affluent.
3.5.2 Risk-Based Asset Allocation & Market Intelligence
Machine learning systems comprehensively assess investor risk profiles and dynamically allocate
assets using portfolio optimization algorithms that balance expected returns against volatility.
These systems employ supervised learning for risk tolerance classification, time-series
forecasting models (LSTM neural networks—long short-term memory networks specialized for
sequential data—and ARIMA models) to predict market movements (Krishnan, Ashta, & Babu,
2021), and reinforcement learning to discover optimal long-term investment strategies that
adapt to changing market regimes. Sentiment analysis using natural language processing
extracts market signals from news articles, social media, and financial reports to inform
investment decisions. Volatility prediction models and correlation analysis ensure diversification
across assets with different risk characteristics.
Colombia's Tyba uses AI to assess users' risk profiles through behavioral questions and financial
data, automatically allocating investments across diverse assets while continuously rebalancing
based on market conditions and individual circumstances29. Chile's Fintual employs machine
learning to construct portfolios optimized for different life stages and goals, with AI-driven
rebalancing responding to market volatility while maintaining target risk levels30. In India, ET
Money uses AI to recommend mutual fund portfolios combining risk assessment with tax
optimization strategies, while continuously monitoring portfolio health and suggesting
25 https://international.nubank.com.br/company/with-122-million-customers-nubank-creates-products-
capable-of-gaining-global-scale/
26 https://www.latamfintech.co/articles/mexican-neobroker-flink-raised-57-m-in-a-series-b-round-to-
boost-financial-inclusion-in-latam
27 https://www.ndovu.co/about-ndovu-rw
28 https://yourstory.com/2019/11/groww-leverages-technology-eliminate-hassle
29 https://alpaca.markets/blog/tyba-creating-investment-access-in-latin-america/
30 https://www.hi.vc/insights/an-ai-tool-for-analyzing-investment-statements-fintuals-new-bet
17

adjustments31. Nigeria's Risevest allows diaspora and local investors to access global markets
through AI-curated portfolios that manage currency risk and optimize returns for naira-based
investors32.
For novice investors lacking sophisticated financial knowledge, automated risk management
provides professional-grade portfolio oversight, helping them build wealth over time while
avoiding common pitfalls like panic selling during downturns, excessive concentration in high-
risk assets, or overly conservative allocations that fail to generate real returns after inflation.
3.5.3 Humane Considerations
AI-powered investment platforms must uphold dignity by ensuring that democratized access
does not expose financially vulnerable populations to inappropriate risks through algorithmic
recommendations that prioritize platform profits over investor welfare. Governance frameworks
must prevent conflicts of interest where AI systems recommend high-fee products or
investments generating higher commissions for platforms rather than better returns for
investors—some robo-advisors have faced criticism for steering users toward proprietary funds
with higher fees. Ethical deployment demands that AI investment tools genuinely serve wealth-
building goals rather than extracting fees from novice investors through frequent trading or
complex products (Kalluri, 2020). Clear disclosure of conflicts of interest, commitment to
fiduciary responsibility (legal obligation to act in clients' best interests) in automated investment
advice, and protection against algorithmic failures that could cause significant portfolio losses
are essential.
Justice requires transparency in how algorithms allocate investments and assess suitability, with
clear explanations of automated decisions affecting people's financial futures. Model
explainability is crucial—investors should understand why they received specific
recommendations and what assumptions drive their portfolio allocation (Bracke et al., 2019).
Inclusion requires recognizing that investment literacy varies dramatically, necessitating
protective guardrails against algorithmic manipulation while preserving investor autonomy—
overly aggressive risk profiling might push unsophisticated investors into volatile assets they
don't understand, while overly conservative approaches might leave them unable to build
wealth.
Ensuring that robo-advisors account for local market conditions, currency risks, and tax
implications relevant to Global South investors—rather than simply adapting algorithms
designed for developed markets—is crucial for genuine financial inclusion in investment
services.
31 https://www.etmoney.com/tax-saving
32 https://risevest.com/why-rise
18

4. Discussion
This systematic examination of AI applications across five critical financial sectors reveals both
remarkable technological advances and persistent ethical challenges that must be addressed to
ensure truly inclusive and humane financial systems. The evidence demonstrates that AI is not
merely automating existing processes but fundamentally transforming how financial services
can reach and serve marginalized populations.
4.1 AI Technologies Across Financial Sectors
To understand the diverse AI applications described in this paper's findings, it is essential to first
grasp the foundational machine learning paradigms that underpin these systems. Machine
learning—the core technology driving AI-enabled financial inclusion—comprises three primary
learning approaches, each suited to different types of problems:
Supervised learning involves training algorithms on labeled datasets where the correct answer
is known (for example, historical loan data labeled as "repaid" or "defaulted"). The algorithm
learns patterns that map inputs to outputs, enabling it to make predictions on new, unseen
data. This approach powers most classification tasks (is this transaction fraudulent?) and
regression tasks (what return can be expected?).
Unsupervised learning discovers hidden patterns in data without pre-labeled examples. Rather
than predicting a known outcome, these algorithms identify natural groupings, detect
anomalies, or find underlying structures in data. This approach excels at segmentation (grouping
similar customers) and anomaly detection (finding unusual patterns that might indicate fraud).
Reinforcement learning takes a fundamentally different approach: algorithms learn optimal
strategies through trial and error, receiving rewards for successful actions and penalties for
unsuccessful ones. Over many iterations, the system discovers which decisions lead to the best
long-term outcomes. This paradigm is particularly powerful for sequential decision-making
problems like portfolio management or dynamic pricing.
Within each of these three paradigms, specific techniques and algorithms have proven
particularly effective for financial inclusion applications. Additionally, certain cross-cutting
technologies—natural language processing and computer vision—can employ any of these
learning paradigms depending on the specific task. Table 3 organizes all AI technologies
discussed in this paper's findings section according to these learning paradigms and shows
which techniques are deployed across the five financial sectors.
Table 3: AI Technologies by Financial Sector (Hierarchical Structure)
Learning Specific Payments Savings & Lending & Insurance Investment
Paradigm Technique/Application Pensions Credit s
19

SUPERVISED  Classification (fraud,  KYC  Savings  Credit  Risk  Risk
LEARNING  risk, default)  verification,  behavior  scoring,  classification,  tolerance
|     |     | fraud      | prediction  default  | claims validity  | classificatio |
| --- | --- | ---------- | -------------------- | ---------------- | ------------- |
|     |     | detection  | prediction           |                  | n             |

|     | Gradient Boosting  | -   | -  Alternative  | Risk profiling  | -   |
| --- | ------------------ | --- | --------------- | --------------- | --- |
(XGBoost/LightGBM)  credit
scoring (70-
80% of
systems)

|     | Neural Networks (CNNs  | Biometric     | -  -  | Damage       | -   |
| --- | ---------------------- | ------------- | ----- | ------------ | --- |
|     | for images)            | recognition   |       | assessment   |     |
|     |                        | (face, iris,  |       | from photos  |     |
fingerprint)

|     | Regression Models  | -   | -  -  | Parametric       | Return      |
| --- | ------------------ | --- | ----- | ---------------- | ----------- |
|     |                    |     |       | loss prediction  | prediction  |

|     | Time-Series Forecasting  | -   | Pension  Income          | -   | Market      |
| --- | ------------------------ | --- | ------------------------ | --- | ----------- |
|     | (labeled)                |     | projections  volatility  |     | prediction  |
|     |                          |     | (ARIMA)  prediction      |     | (LSTM,      |
ARIMA)
UNSUPERVISED  Anomaly Detection  Novel fraud  -  Novel fraud  -  -
| LEARNING  |     | pattern  | schemes  |     |     |
| --------- | --- | -------- | -------- | --- | --- |
detection

Clustering/Segmentatio User  -  Borrower  Risk-based  Investor
|     | n   | segmentation,  | segmentatio | groups  | profiling  |
| --- | --- | -------------- | ----------- | ------- | ---------- |
personalizatio n
n
REINFORCEMEN Strategy Optimization  Payment  Nudging  Dynamic  -  Portfolio
| T LEARNING  |     | routing, fee  | strategy  pricing  |     | strategy    |
| ----------- | --- | ------------- | ------------------ | --- | ----------- |
|             |     | optimization  | optimizatio        |     | optimizatio |
|             |     |               | n                  |     | n           |
CROSS-CUTTING  Natural Language  -  Chatbots  Application  Claims  Sentiment
TECHNIQUES  Processing  for  analysis  documentatio analysis,
|     |     |     | guidance  | n   | chatbots  |
| --- | --- | --- | --------- | --- | --------- |

|     | Computer Vision  | Document       | -  Collateral  | Satellite  | -   |
| --- | ---------------- | -------------- | -------------- | ---------- | --- |
|     |                  | verification,  | photos         | imagery,   |     |
|     |                  | liveness       |                | damage     |     |
|     |                  | detection      |                | photos     |     |
STATISTICAL  Monte Carlo Simulation  -  Retirement  -  -  Risk
| METHODS  |     |     | scenarios  |     | scenarios  |
| -------- | --- | --- | ---------- | --- | ---------- |

This hierarchical organization reveals several critical patterns about how AI technologies are
being deployed for financial inclusion:
20

First, supervised learning dominates across all five sectors, reflecting both its technical
maturity and the availability of labeled training data in financial services. Every sector employs
supervised classification or regression for core predictive tasks—fraud detection in payments,
credit scoring in lending, risk assessment in insurance, and return prediction in investments. This
prevalence indicates that financial institutions possess sufficient historical data (transactions,
defaults, claims, returns) to train supervised models effectively. The success of supervised
learning in financial inclusion stems from its ability to learn from past patterns and apply those
lessons to new cases at scale.
Second, gradient boosting methods—specifically XGBoost and LightGBM—have emerged as
the dominant technique for alternative credit scoring, powering 70-80% of production systems
in lending as documented in the findings. This near-universal adoption is not accidental. These
ensemble methods excel at handling the messy, incomplete, heterogeneous nature of
alternative data (mobile phone metadata, e-commerce transactions, utility payments) that
characterizes credit-invisible populations. Unlike simpler models that assume clean, structured
data, gradient boosting automatically detects complex non-linear relationships, handles missing
values gracefully, and combines insights from multiple decision trees to achieve robust
predictions. This technical advantage explains why virtually every successful alternative lending
platform—from Kenya's Tala and Branch to India's ZestMoney and KreditBee—relies on gradient
boosting as its core technology.
Third, deep learning neural networks find specific applications where they provide unique
capabilities, particularly in payments and insurance. Convolutional Neural Networks (CNNs)
power biometric authentication systems that enable digital identity verification for unbanked
populations—analyzing facial features, iris patterns, and fingerprints to confirm identity without
requiring traditional documentation. Similarly, CNNs assess damage from photographs in
insurance claims processing, extracting insights from visual data that traditional algorithms
cannot process. The pattern is clear: deep learning is deployed where the input data is
fundamentally unstructured (images, audio, video) rather than tabular, and where its superior
pattern recognition capabilities justify the higher computational costs and data requirements.
Fourth, unsupervised learning plays a more limited but critical role, primarily in fraud detection
and customer segmentation. Anomaly detection algorithms identify novel fraud patterns that
supervised models—trained only on historical fraud examples—would miss entirely. This
capability is essential because fraudsters constantly adapt their tactics; purely supervised
approaches would always lag behind. Similarly, clustering algorithms enable customer
segmentation without requiring pre-defined categories, allowing platforms to discover natural
groupings in their user bases and personalize services accordingly. The combination of
supervised learning (for known patterns) and unsupervised learning (for unknown patterns)
provides more comprehensive coverage than either approach alone.
Fifth, reinforcement learning remains relatively rare, appearing primarily in optimization
contexts—payment routing, automated savings nudging, dynamic loan pricing, and portfolio
21

management. This limited deployment reflects reinforcement learning's significant challenges: it
requires extensive trial-and-error learning (potentially costly if errors harm real customers),
demands careful reward function design (mis-specified rewards can lead to perverse outcomes),
and exhibits sample inefficiency (requiring many iterations to learn effective policies). Where
reinforcement learning does appear, it addresses sequential decision-making problems where
the optimal action depends on long-term consequences rather than immediate predictions, and
where simulation or safe experimentation is possible.
Sixth, cross-cutting technologies—Natural Language Processing and Computer Vision—bridge
multiple learning paradigms and extend AI's reach into previously inaccessible data modalities.
NLP enables conversational interfaces (chatbots providing pension guidance or investment
advice), analyzes unstructured text (loan applications, business descriptions, claims
documentation), and extracts market sentiment from news and social media. Computer Vision
processes identity documents, assesses collateral from photos, evaluates crop damage from
satellite imagery, and verifies physical presence through liveness detection. These technologies
transform unstructured human-generated content into structured data that supervised,
unsupervised, or reinforcement learning algorithms can then process.
Finally, the table reveals important sector-specific technological profiles. Payments
emphasizes real-time supervised classification (fraud detection) combined with biometric neural
networks and reinforcement learning for routing optimization—reflecting the sector's need for
instant decisions and continuous system optimization. Lending concentrates supervised learning
intensity, particularly gradient boosting for alternative credit scoring, reflecting the core
challenge of predicting creditworthiness from diverse data sources. Insurance uniquely
combines supervised classification with computer vision for damage assessment and regression
models for parametric triggers, reflecting its need to process both visual evidence and
quantifiable parameters. Investments employs the most diverse toolkit (supervised
classification, time-series forecasting, reinforcement learning, and NLP) reflecting the multi-
faceted challenges of asset allocation, market prediction, risk management, and investor
communication. Savings & Pensions occupies a middle ground, using supervised learning for
behavioral prediction and reinforcement learning for nudging optimization, but lacking the
visual or textual analysis needs that drive other sectors.
This systematic mapping reveals that AI-driven financial inclusion is not monolithic but rather
comprises a sophisticated ecosystem of complementary technologies, each addressing specific
challenges through appropriate learning paradigms. The dominance of supervised learning
reflects pragmatic choices based on data availability and problem structure, while the selective
deployment of unsupervised learning, reinforcement learning, and advanced techniques like
deep learning indicates thoughtful matching of tools to tasks. Understanding this technological
landscape is essential for evaluating both the opportunities and risks that AI presents for
financial inclusion, as different techniques carry distinct implications for fairness, transparency,
and accountability: issues we turn to next in examining humane considerations.
22

4.2 Humane Challenges Across Financial Sectors
While AI's technical capabilities are impressive, Table 4 reveals that each sector confronts
profound ethical challenges that threaten to undermine financial inclusion goals if not
adequately addressed.

Table 4: Humane Considerations by Financial Sector
Humane  Payments  Savings & Pensions  Lending & Credit  Insurance  Investments
Challenge
Algorithmic Bias  Fraud models flag rural  Gender/geography  Proxy  Discriminatory  Biased risk
&  transactions as suspicious  discrimination in  discrimination  risk profiling,  assessment
Discrimination  projections  through alternative  algorithmic
|          |                           |                   | data, historical bias  | redlining  |     |
| -------- | ------------------------- | ----------------- | ---------------------- | ---------- | --- |
|          |                           |                   | perpetuation           |            |     |
| Privacy  | Biometric data breaches,  | Data privacy and  | Invasive alternative   | Invasive   |     |
Violations  surveillance capitalism  security concerns  data collection (call  behavioral
|     |     |     | logs, SMS, social  | surveillance  |     |
| --- | --- | --- | ------------------ | ------------- | --- |
networks)
Digital Divide &  Smartphone/internet  Irregular income  Sparse digital  Geolocation- Limited access for
Exclusion  requirements exclude  penalized by rigid  footprints from  based premium  low digital literacy
marginalized groups  systems  poverty misread as  increases  populations
risk
Lack of  Opaque account  Opaque fee structures,  Non-explainable  Unclear denial  Conflicts of
Transparency  freezing/transaction  withdrawal difficulties  credit decisions,  reasons, opaque  interest,
blocking  black-box scoring  claims processing  algorithm opacity
Manipulative    Dark patterns,  Predatory lending  Restrictive  Fee optimization
Practices  excessive risk  targeting vulnerable  parametric  over returns,
|                |     | encouragement      | populations  | triggers, premium  | inappropriate risk  |
| -------------- | --- | ------------------ | ------------ | ------------------ | ------------------- |
|                |     |                    |              | extraction         | pushing             |
| Cultural       |     | Western financial  |              |                    | One-size-fits-all   |
| Insensitivity  |     | models imposed,    |              |                    | approaches          |
family obligations
penalized
Inadequate  No contestation  Liquidity lockups  No ability to  Denied claims  Algorithmic
Recourse  mechanisms for  during emergencies  challenge adverse  without  failures without
|     | automated decisions  |     | decisions  | explanation  | accountability  |
| --- | -------------------- | --- | ---------- | ------------ | --------------- |
Governance  Insufficient data  Insufficient human  Insufficient fairness  Inadequate  Weak fiduciary
Gaps  protection, weak  oversight in fiduciary  auditing, weak  disparate impact  enforcement
|     | oversight  | decisions  | explainability  | testing  |     |
| --- | ---------- | ---------- | --------------- | -------- | --- |
requirements

The systematic analysis reveals recurring themes across sectors. Algorithmic bias and proxy
discrimination emerge as perhaps the most pervasive challenge. Even when protected
characteristics like race, ethnicity, or gender are explicitly excluded from models, AI systems
learn to use proxy variables—zip code, device type, app usage patterns, social network
characteristics—that correlate with these protected attributes, thereby perpetuating historical
discrimination under the guise of objective assessment. This is particularly pernicious because it
23

operates invisibly: the model never explicitly considers race, yet systematically disadvantages
racial minorities.
Privacy violations constitute another cross-cutting concern. The alternative data powering AI-
driven financial inclusion—mobile phone metadata, social media activity, e-commerce behavior,
location patterns—represents intimate behavioral surveillance that most users neither fully
understand nor meaningfully consent to. The Aadhaar biometric breaches in India and concerns
about Chinese payment platform data practices illustrate how financial inclusion can become a
pathway to surveillance capitalism, where user data becomes a commodity extracted in
exchange for financial access.
The digital divide paradoxically threatens to make AI-driven financial inclusion exclusionary.
Many AI-enhanced services require smartphones, stable internet connectivity, and digital
literacy—prerequisites that exclude the most marginalized populations who need financial
inclusion most urgently. When fraud detection systems are trained predominantly on urban
digital transaction patterns, they may incorrectly flag legitimate rural transactions as suspicious,
effectively excluding rural users. Similarly, sparse digital footprints generated by poverty—older
phones, limited internet, low e-commerce participation—get misread by AI as risk indicators,
creating a vicious cycle where poverty itself becomes a disqualifying factor.
Lack of transparency and explainability undermines user agency and prevents meaningful
contestation of automated decisions. When an AI system denies credit, freezes an account, or
increases insurance premiums, users rarely receive comprehensible explanations of why the
decision was made or how they might improve their situation. This opacity violates principles of
due process and prevents users from effectively challenging erroneous automated decisions
that can have devastating consequences for their economic opportunities.
Manipulative practices disguised as personalization represent a particularly insidious risk. AI
systems can identify vulnerable populations and target them with exploitative terms—predatory
loans at usurious rates, insurance products with restrictive triggers unlikely to activate,
investment products generating high fees with poor returns—all optimized through machine
learning to maximize provider profits while minimizing payouts. Behavioral nudging can cross
the line into manipulation when it encourages excessive risk-taking by vulnerable savers or locks
users into illiquid products they cannot access during emergencies.
Cultural insensitivity reflects how AI models trained predominantly on Western financial
behaviors may misinterpret culturally appropriate patterns as risk indicators. In many cultures,
supporting extended family takes precedence over individual savings, yet AI systems may
penalize such transfers as "poor financial discipline." Irregular income reflecting seasonal
agriculture gets flagged as "income instability" rather than recognized as normal for smallholder
farmers. These cultural blind spots can make ostensibly inclusive AI systems systematically
disadvantage non-Western populations.
24

4.3 The Inclusion Paradox
Perhaps the most troubling finding is what might be termed the "inclusion paradox": AI enables
access to financial services for previously excluded populations, but often at exploitative terms.
Alternative credit scoring allows lending to the credit invisible, but frequently at 30-40% APR or
higher—rates that provide access while potentially trapping borrowers in debt spirals. Micro-
insurance reaches poor populations, but with parametric triggers set to rarely activate despite
farmers experiencing losses. Automated investment platforms democratize wealth
management, but may steer novice investors into high-fee proprietary products.
This paradox raises fundamental questions about whether AI-driven expansion of financial
access should be celebrated as inclusion or critiqued as exploitation. The answer likely depends
on implementation details—interest rates, fee structures, transparency, recourse mechanisms,
and genuine commitment to serving rather than extracting from marginalized communities.
Technology alone is neutral; the ethical valence depends entirely on how it is deployed and
governed.
4.4 Toward Humane AI-Driven Financial Inclusion
Achieving genuinely humane and inclusive AI-driven financial services requires multifaceted
interventions across technical, regulatory, and institutional domains:
Technical interventions can address fairness, transparency, and privacy challenges through
several approaches that make AI systems more accountable.
Making algorithms transparent rather than black-box requires explainability techniques. Often,
when AI denies credit or increases insurance premiums, users receive little explanation.
Counterfactual explanations flip this paradigm by showing exactly what would need to change:
"If your mobile payment consistency increased from 60% to 80%, you would qualify for this
loan." This specificity transforms opaque rejections into actionable guidance. Similarly,
quantifying each factor's contribution to decisions—"location contributed 10%, transaction
history 45%, digital footprint 35%, with 10% from other factors"—enables users to understand
why decisions were made and effectively contest errors.
Preserving privacy while enabling learning presents a fundamental tension in AI-driven financial
inclusion: alternative data improves credit scoring but raises surveillance concerns. Privacy-
preserving techniques like federated learning resolve this tension by keeping sensitive data on
users' phones or at local institutions—the AI model travels to where data resides, learns
patterns locally, and only shares aggregated statistical updates rather than raw information.
Multiple microfinance institutions can collaboratively improve credit models without ever
sharing customer databases. Differential privacy adds carefully calibrated statistical noise
ensuring no individual's information can be extracted from trained models while preserving
overall accuracy.
25

Proactively identifying when models fail requires adversarial testing—systematically challenging
AI systems with edge cases before deployment. Developers feed models applications from
unusual occupations, transaction patterns from remote rural areas, and data combinations
rarely seen during training. This stress-testing reveals failure modes where models make
egregiously wrong decisions for specific subpopulations, allowing fixes before vulnerable users
are harmed. For instance, adversarial testing might reveal that a credit model systematically
underscores seasonal agricultural workers, prompting recalibration.
Regulatory frameworks must evolve beyond traditional financial regulation to address
algorithmic accountability. Requirements might include mandatory algorithmic impact
assessments before deployment, regular fairness audits testing for disparate impacts across
demographic groups, explainability standards requiring comprehensible decision explanations,
data governance frameworks limiting alternative data collection and use, and accessible appeals
processes for algorithmic decisions. The challenge lies in crafting regulation that protects
vulnerable populations without stifling beneficial innovation—adaptive governance rather than
rigid control.
Institutional commitments ultimately determine whether AI serves inclusion or exploitation.
Financial service providers must adopt fiduciary mindsets, designing products that genuinely
serve client welfare rather than merely extracting fees. This requires performance metrics that
measure actual improvements in client financial wellbeing—emergency savings accumulated,
debts repaid, insurance claims paid, wealth built—not just transaction volumes or revenue
generated. Participatory design processes should involve intended beneficiaries in product
development rather than imposing technocratic solutions. Human oversight must complement
automation, preserving agency and providing recourse when algorithms fail.
Cross-sector collaboration among technology providers, financial institutions, regulators, civil
society organizations, and affected communities is essential to navigate the complex tradeoffs
inherent in AI-driven financial inclusion. No single actor possesses sufficient expertise or
perspective to ensure humane deployment. Multi-stakeholder governance mechanisms can
facilitate ongoing dialogue, surfacing concerns and adapting practices as understanding evolves.
The evidence from Global South implementations—from M-Pesa's transformation of financial
access in Kenya to challenges with digital savings platforms in Africa, from alternative credit
scoring's expansion of lending across multiple markets to concerns about predatory practices—
demonstrates both AI's transformative potential and its capacity to create new forms of
exclusion and exploitation when deployed without adequate safeguards. Success requires
unwavering commitment to centering human dignity, social justice, and genuine inclusion rather
than merely technological sophistication or financial efficiency.
5. Conclusion
26

Artificial intelligence emerges as a transformative enabler of financial inclusion, operating
powerfully across payments, savings, lending, insurance, and investments through innovative
applications of supervised learning, unsupervised learning, reinforcement learning, natural
language processing, computer vision, and generative AI. Real-world implementations across
the Global South—from M-Pesa's AI-enhanced identity verification in Kenya to Nubank's
automated investment services in Brazil, from Tala's alternative credit scoring across multiple
African markets to BIMA's micro-insurance serving tens of millions, from India's UPI ecosystem's
multilingual chatbots to Nigeria's AI-powered agricultural insurance—demonstrate AI's potential
to democratize financial services at unprecedented scale. By integrating evidence from
contemporary global research and practical deployments, this analysis illustrates how AI
fundamentally transforms access, equity, and financial stability for populations previously
marginalized from formal financial systems.
Credit invisibility represents 20% of the adult population in developed economies and even
higher proportions in developing markets (Consumer Financial Protection Bureau, 2015). The
technology's capacity to process alternative data, automate complex decisions, personalize
services at scale, and operate efficiently in resource-constrained environments promises
unprecedented opportunities for economic empowerment across diverse global populations.
Research demonstrates that alternative data models achieve comparable or superior predictive
power to traditional credit scores while dramatically expanding access—mobile payment data
correlates with creditworthiness at 0.65-0.72, matching FICO score performance (Björkegren &
Grissen, 2019). AI-driven microfinance reduces operational costs from 6-12% to under 2%,
enabling profitable lending at scales previously impossible (Milana & Ashta, 2021). Alternative
data scoring overwhelmingly relies on gradient boosted tree methods like XGBoost and
LightGBM, which power 70-80% of production systems because they automatically detect non-
linear relationships and this can reduce costs by 6% to 25% of total losses (Khandani et al.,
2010).
However, realizing this transformative potential requires unwavering commitment to
responsible deployment, robust ethical oversight, and sustained efforts to mitigate critical risks
including algorithmic bias that perpetuates discrimination, privacy violations through invasive
data collection, digital exclusion of populations lacking connectivity or devices, opaque decision-
making that prevents meaningful contestation of automated decisions, and predatory practices
disguised as financial inclusion (Solon Barocas & Selbst, 2016; Kalluri, 2020). Alternative data can
encode existing societal inequalities when machine learning trains on data reflecting historical
discrimination, creating proxy discrimination even without explicitly using protected
characteristics (Solon Barocas & Selbst, 2016). Mission drift represents a profound risk in
microfinance, where algorithmic optimization of repayment prediction can gradually shift
portfolios away from the poorest populations toward easier-to-serve segments, abandoning
original social missions (A. Ashta & Hudon, 2012; Cull, Demirgüç-Kunt, & Morduch, 2011). The
inclusion versus exploitation dilemma emerges in the interest rate paradox: AI enables lending
to previously excluded populations, but often at 30-40% APR or higher: rates that enable access
27

while potentially trapping borrowers in debt spirals (Rona-Tas & Guseva, 2018).
Success demands that financial inclusion efforts prioritize human dignity over efficiency metrics,
ensure transparent governance with meaningful accountability mechanisms, proactively address
digital divides through investment in infrastructure and digital literacy, maintain accessible
human oversight and appeals processes, and rigorously evaluate whether AI deployments
genuinely improve financial wellbeing or merely extract value from vulnerable populations
(Kalluri, 2020; Kroll et al., 2017). Cultural context must inform AI systems—recognizing that
irregular income flows may reflect seasonal agriculture rather than financial instability, and that
family financial support represents cultural values rather than poor financial discipline
(Anderson et al., 2009; Clark, 1997). Financial behavior doesn't translate uniformly across
cultures, and AI models trained on Western credit bureau data may see culturally appropriate
patterns as high risk. Fairness constraints must balance predictive accuracy with equitable
outcomes across demographic groups, accepting minor performance reductions to achieve
demographic parity and prevent discriminatory impacts (S. Barocas et al., 2019). Regulatory
frameworks increasingly recognize that algorithmic neutrality doesn't guarantee fair outcomes,
requiring explainability, disparate impact testing, and fairness-aware machine learning
approaches (Bracke et al., 2019; V. Bumacov et al., 2014).
Only through such conscientious approaches—informed by voices from affected communities,
guided by ethical frameworks that center human rights and social justice, regulated by
governance structures that hold technology providers accountable, and continuously evaluated
against outcomes for the most marginalized—can AI genuinely advance financial inclusion while
honoring principles of justice, respecting human dignity, and fostering sustainable, equitable
development that genuinely serves historically underserved communities rather than creating
new forms of technological exploitation or algorithmic exclusion (Bélanger et al., 2025; Kalluri,
2020). The future of AI-driven financial inclusion depends not merely on technological
sophistication, but on our collective commitment to deploying these powerful tools responsibly,
ethically, and in genuine service to those who need them most. Ethical AI-driven financial
inclusion requires preserving human agency, aligning objectives with borrower welfare,
involving borrowers in design, auditing relentlessly for bias, respecting data dignity, and
maintaining epistemic humility—recognizing that algorithms trained on thousands of loans
know patterns while experienced loan officers know context, and both are valuable (Kalluri,
2020).
References
28

Akanfe, O., Bhatt, P., & Lawong, D. A. (2025). Technology Advancements Shaping the Financial
Inclusion Landscape: Present Interventions, Emergence of Artificial Intelligence and
Future Directions. Information Systems Frontiers. doi:10.1007/s10796-025-10597-z
Anderson, S., Baland, J. M., & Moene, K. O. (2009). Enforcement in informal saving groups.
Journal of Development Economics, 90(1), 14-23. doi:10.1016/j.jdeveco.2008.08.004
Ash, E., & Hansen, S. (2023). Text algorithms in economics. Annual Review of Economics, 15,
659-688. doi:10.1146/annurev-economics-012320-122921
Ashta, A. (2025). Building Humane Advances and Institutions: A Critical Look at Recent News
about Artificial Intelligence. Available at SSRN: https://ssrn.com/abstract=5685682.
Retrieved from https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5685682
Ashta, A., & Herrmann, H. (2021). Artificial intelligence and fintech: An overview of
opportunities and risks for banking, investments, and microfinance. Strategic Change,
30(3), 211-222. doi:10.1002/jsc.2404
Ashta, A., & Hudon, M. (2012). The Compartamos microfinance IPO: Mission conflicts in hybrid
institutions with diverse shareholding. Strategic Change: Briefings in Entrepreneurial
Finance, 21(7-8), 331-341.
Barocas, S., Hardt, M., & Narayanan, A. (2019). Fairness and machine learning: Limitations and
opportunities: MIT Press.
Barocas, S., & Selbst, A. D. (2016). Big Data's Disparate Impact. California Law Review, 104(3),
671-732. Retrieved from http://www.jstor.org/stable/24758720
Bélanger, C., Ashta, A., & Mason, G. (2025). Fintech, Banks and Mobile Operators: Interplays for
Increasing Financial Inclusion. In A. Zarifis & X. Cheng (Eds.), Fintech and the Emerging
Ecosystems: Exploring Centralised and Decentralised Financial Technologies (pp. 409-
425): Springer Nature.
Berg, T., Burg, V., Gombović, A., & Puri, M. (2019). On the Rise of FinTechs: Credit Scoring Using
Digital Footprints. The Review of Financial Studies, 33(7), 2845-2897.
doi:10.1093/rfs/hhz099
Binns, R. (2018). Fairness in Machine Learning: Lessons from Political Philosophy. Paper
presented at the Proceedings of the 1st Conference on Fairness, Accountability and
Transparency, Proceedings of Machine Learning Research.
https://proceedings.mlr.press/v81/binns18a.html
Björkegren, D., & Grissen, D. (2019). Behavior Revealed in Mobile Phone Usage Predicts Credit
Repayment. The World Bank Economic Review, 34(3), 618-634.
doi:10.1093/wber/lhz006
Bracke, P., Datta, A., Jung, C., & Sen, S. (2019). Machine learning explainability in finance: An
application to default risk analysis. Retrieved from
https://www.bankofengland.co.uk/working-paper/2019/machine-learning-
explainability-in-finance-an-application-to-default-risk-analysis
Bumacov, V., Ashta, A., & Singh, P. (2014). The Use of Credit Scoring in Microfinance Institutions
and Their Outreach. Strategic Change: Briefings in Entrepreneurial Finance, 23(7-8), 401-
413.
Bumacov, V., Ashta, A., & Singh, P. (2017). Credit scoring: A historic recurrence in microfinance.
Strategic Change, 26(6), 543-554. doi:10.1002/jsc.2165
Burke, M., & Lobell, D. B. (2017). Satellite-based assessment of yield variation and its
determinants in smallholder African systems. Proceedings of the National Academy of
Sciences, 114(9), 2189-2194. Retrieved from
https://www.pnas.org/doi/pdf/10.1073/pnas.1616919114
29

Chu, M., Laranjeira, C., & Levindo, P. (2020). Nubank: Democratizing Financial Services. Harvard
Business School.
Citron, D. K., & Pasquale, F. (2014). The scored society: Due process for automated predictions.
Washington Law Review, 89, 1-33. Retrieved from
https://scholarship.law.bu.edu/faculty_scholarship/618
Clark, G. (1997). Money-Go-Rounds: The Importance of Rotating Savings and Credit Associations
for Women. American Ethnologist, 24(3), 673-674.
doi:https://doi.org/10.1525/ae.1997.24.3.673
Consumer Financial Protection Bureau. (2015). Data point: Credit invisibles. Retrieved from
https://www.consumerfinance.gov/data-research/research-reports/data-point-credit-
invisibles/
Cook, T., & McKay, C. (2015). How M-Shwari works: The story so far. Consultative group to assist
the poor (CGAP) and financial sector deepening (FSD).
Cull, R., Demirgüç-Kunt, A., & Morduch, J. (2011). Does regulatory supervision curtail
microfinance profitability and outreach? World Development, 39(6), 949-965.
Dietterich, T. G. (2000). Ensemble Methods in Machine Learning, Berlin, Heidelberg.
Djeundje, V. B., Crook, J., Calabrese, R., & Hamid, M. (2021). Enhancing credit scoring with
alternative data. Expert Systems with Applications, 163, 113766.
doi:https://doi.org/10.1016/j.eswa.2020.113766
Gambacorta, L., Huang, Y., Qiu, H., & Wang, J. (2019). How do machine learning and non-
traditional data affect credit scoring? New evidence from a Chinese fintech firm.
Retrieved from https://www.bis.org/publ/work834.htm
Hayman, G. (2024). Pensions in the Age of Artificial Intelligence. CFA Institute (Thinking Ahead
Institute).
Hernandez, E., Goslinga, R., & Wang, V. (2018). Using satellite data to scale smallholder
agricultural insurance. Washington, DC: CGAP, August. https://www. cgap.
org/research/publication/using-satellite-data-scale-smallholder-agricultural-insurance.
Hurley, M., & Adebayo, J. (2016). Credit scoring in the era of big data. Yale Journal of Law and
Technology, 18, 148-216. Retrieved from
https://openyls.law.yale.edu/server/api/core/bitstreams/a8c7f4e3-ae53-4c43-b6cd-
1223a5703c32/content
Jagtiani, J., & Lemieux, C. (2019). The roles of alternative data and machine learning in fintech
lending: Evidence from the LendingClub consumer platform. Financial Management,
48(4), 1009-1029. doi:https://doi.org/10.1111/fima.12295
Jonnalagadda, A. K., & Babu, S. R. (2025). Enhancing Credit Scoring with Alternative Data and
Machine Learning for Financial Inclusion. South Eastern European Journal of Public
Health, 511-518. doi:10.70135/seejph.vi.3584
Kalluri, P. (2020). Don't ask if artificial intelligence is good or fair, ask how it shifts power.
Nature, 583(7815), 169. doi:10.1038/d41586-020-02003-2
Khandani, A. E., Kim, A. J., & Lo, A. W. (2010). Consumer credit-risk models via machine-learning
algorithms. Journal of Banking & Finance, 34(11), 2767-2787.
doi:https://doi.org/10.1016/j.jbankfin.2010.06.001
Krishnan, S., Ashta, A., & Babu, D. (2021). Business cycle prediction: Application of Markov chain
to online crowdlending. Strategic Change, 30(4), 341-351. doi:10.1002/jsc.2428
Kroll, J. A., Huey, J., Barocas, S., Felten, E. W., Reidenberg, J. R., Robinson, D. G., & Yu, H. (2017).
Accountable algorithms. University of Pennsylvania Law Review, 165, 633-705. Retrieved
from https://scholarship.law.upenn.edu/penn_law_review/vol165/iss3/3/
30

Kshetri, N. (2021). The Role of Artificial Intelligence in Promoting Financial Inclusion in
Developing Countries. Journal of Global Information Technology Management, 24(1), 1-
6. doi:10.1080/1097198X.2021.1871273
Kuraku, C., Gollangi, H. K., & Sunkara, J. R. (2020). Biometric Authentication In Digital Payments:
Utilizing AI And Big Data For Real-Time Security And Efficiency. Educational
Administration: Theory and Practice, 26(4), 954-964.
Lobell, D. B., Thau, D., Seifert, C., Engle, E., & Little, B. (2015). A scalable satellite-based crop
yield mapper. Remote Sensing of Environment, 164, 324-333.
doi:https://doi.org/10.1016/j.rse.2015.04.021
Makunda, L., & Matiko, C. (2023). Savings landscape and financial literacy in Kenya according to
FinAccess. Retrieved from https://www.fsdkenya.org/wp-
content/uploads/2023/06/Savings-landscape-and-financial-literacy-in-Kenya-according-
to-FinAccess.pdf
Manta, O., Vasile, V., & Rusu, E. (2025). Banking Transformation Through FinTech and the
Integration of Artificial Intelligence in Payments. FinTech, 4(2), 13. Retrieved from
https://www.mdpi.com/2674-1032/4/2/13
Mhlanga, D. (2020). Industry 4.0 in Finance: The Impact of Artificial Intelligence (AI) on Digital
Financial Inclusion. International Journal of Financial Studies, 8(3), 45. Retrieved from
https://www.mdpi.com/2227-7072/8/3/45
Milana, C., & Ashta, A. (2021). Artificial intelligence techniques in finance and financial markets:
A survey of the literature. Strategic Change, 30(3), 189-209.
doi:https://doi.org/10.1002/jsc.2403
Nuka, T. F., & Ogunola, A. A. (2024). AI and machine learning as tools for financial inclusion:
challenges and opportunities in credit scoring. International Journal of Science and
Research Archive, 13(2), 1052-1067.
Olajide, B. T., Ekechi, C. C., Popoola, T. O., Adeshina, G. O., Ayittey, S., & Ozo-oguej, P. C. (2025).
Machine learning for financial inclusion in agriculture: A study of AI-based credit scoring
tools in rural Nigeria. World Journal of Advanced Research and Reviews, 27(2), 461-470.
doi:https://doi.org/10.30574/wjarr.2025.27.2.2884
Rona-Tas, A., & Guseva, A. (2018). Consumer credit in comparative perspective. Annual Review
of Sociology, 44, 55-75.
Schwittay, A. (2014). Making poverty into a financial problem: From global poverty lines to
Kiva.org. Journal of International Development, 26(4), 508-519. doi:10.1002/jid.2969
Torre, D., & Xu, Q. (2020). Digital payments in China: adoption and interactions among
applications. Revue d'économie industrielle(172), 55-82.
Vuković, D. B., Dekpo-Adza, S., & Matović, S. (2025). AI integration in financial services: a
systematic review of trends and regulatory challenges. Humanities and Social Sciences
Communications, 12(1), 562. doi:10.1057/s41599-025-04850-8
Waithaka, L., Kramer, B., Kivuva, B., & Cecchi, F. (2023). Improving agricultural productivity and
resilience with satellite and cellphone imagery to scale climate-smart crop insurance.
World Bank. (2021). The Global Findex Database 2021: Financial inclusion, digital payments, and
resilience in the age of COVID-19. Retrieved from
https://www.worldbank.org/en/publication/globalfindex
Zuboff, S. (2019). The age of surveillance capitalism: The fight for a human future at the new
frontier of power, edn. PublicAffairs, New York.
31

Brief bio
Dr. Arvind Ashta is the founder of BHAI, a research consulting firm specializing in AI strategy,
fintech, and development. He helps organizations articulate evidence-based strategies through
research-informed writing, white papers, and strategic documentation.
With an h-index over 30 and recognition as a top 1% researcher worldwide (ScholarGPS;
Stanford top 2% scientists list 2025), he brings 40+ years of experience spanning 17 years in
corporate finance, 24 years as Professor at Burgundy School of Business, and current adjunct
roles at Toulouse School of Management and Université Libre de Bruxelles.
His 100+ publications include highly cited research on AI in fintech, financial inclusion, and social
entrepreneurship. His current work explores AI applications in agricultural technology and
development finance. He accepts select consulting engagements for research writing, strategic
advisory, and AI strategy documentation.
Portfolio: https://sites.google.com/view/arvindashta/assignments
For consulting inquiries: arvindashta@gmail.com , bhai2bhai08@gmail.com
Research: https://scholar.google.com/citations?user=zGpnCtUAAAAJ
32