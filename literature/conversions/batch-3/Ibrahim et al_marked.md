---
conversion_metadata:
  converted_at: "2026-07-21T13:34:29Z"
  converter_tool: "markitdown"
  converter_version: "0.1.6"
  source_pdf: "Ibrahim et al.pdf"
  source_pdf_sha256: "7ea9cc38c76f1aa6681ec9089b094c3b2a5b7e607a5671adb0ec63c299b0f6fe"
  page_count: 16
  markdown_char_count: 171019
---

<!-- PAGE-AWARE EXTRACTION (via pdfminer.six) -->

<!-- PAGE 1 -->

www.nature.com/scientificreports

An equity aware recommender 
system for university admissions 
balancing operational constraints 
and strategic objectives

Ahmed Ibrahim1, Ala Alarood2 & Eesa Alsolami3

Institutions of higher education must balance multiple, often conflicting objectives when setting 
admission targets for their academic programs. In this paper, we introduce a recommendation system 
that integrates Constraint Satisfaction Problem (CSP) techniques, goal programming, and Equity 
Theory to optimize student assignments. Our model strictly enforces hard constraints—such as faculty-
hour limits and classroom capacities—while accommodating soft constraints—such as government 
quotas and institutional preferences—through adjustable penalty functions. Evaluations against 
static and heuristic benchmarks show that our approach maintains enrollment at 85–90% of total 
capacity, markedly reducing both the frequency and severity of constraint violations. Furthermore, an 
average Gini coefficient of 0.067 demonstrates a fairer distribution of seats across programs. Over five 
simulated admission cycles, institutions employing this recommender achieve substantial compliance 
improvements within four years, striking an effective balance between rapid constraint adherence and 
stable enrollment figures. These results confirm that our system offers a practical, data-driven solution 
for flexible and equitable enrollment management in resource-limited higher-education settings.

Keywords  Recommender systems, Higher education admissions, Constraints satisfaction problem, Goal 
programming

Universities have long faced the difficult task of matching incoming student numbers to the limitations of their 
teaching staff, classroom capacity, and budgets1,2. In Saudi Arabia, the free-education system makes this challenge 
even harder to manage, since there are no consequences for students who fail to graduate as planned (e.g. they 
continue to occupy seats at no extra cost). Although this system opens doors for more learners, it also intensifies 
competition for spots in the most sought-after programs. Moreover, sudden events—such as unexpected staff 
cuts or the introduction of new government quotas—can throw even the most carefully planned enrollment 
figures  off  course3.  Institutions,  therefore,  need  flexible  methods  that  can  rapidly  adjust  admission  numbers 
whenever policies shift or resources change.

This  challenge  is  not  merely  theoretical;  it  manifests  in  significant  operational  inefficiencies  that  static 
planning methods struggle to resolve. For instance, it is common for internal university reports to reveal that 
high-demand programs consistently operate well beyond their intended faculty capacity, sometimes by as much 
as 15–20%, leading to overworked staff and potential compromises in educational quality4,5. Concurrently, other 
academic programs may remain significantly under-enrolled, utilizing only 60–70% of their available classroom 
and laboratory space6. This persistent misalignment between student demand and available resources highlights 
the critical failure of seat-planning methods that cannot adapt to shifting enrollment trends or sudden changes 
in capacity, such as unexpected staff departures. The resulting imbalance not only strains institutional resources 
but also creates inequities in access and educational experience across different fields of study

Many universities attempt to address these complexities by instituting two types of guidelines: strict limits on 
resources (e.g., maximum student–faculty ratios) and more flexible, policy-oriented goals7,8. While traditional 
methods such as goal programming effectively uphold these boundaries, they often struggle when immediate 
adjustments  become  necessary9,10.  Meanwhile,  machine  learning  and  predictive  analytics  provide  valuable 
insights into enrollment trends11,12, but rarely incorporate mechanisms to dynamically reassign seats once the

1Department  of  Computer  Science  and  Artificial  Intelligence,  College  of  Computer  Science  and  Engineering, 
University of Jeddah,  Jeddah, Saudi Arabia. 2Department of Information Technology, College of Computer Science 
and Engineering, University of Jeddah,  Jeddah, Saudi Arabia. 3Department of Cybersecurity, College of Computer 
Science and Engineering, University of Jeddah,  Jeddah, Saudi Arabia. email: amabrahem6@uj.edu.sa

Scientific Reports |        (2025) 15:39756

| https://doi.org/10.1038/s41598-025-23116-6

1

---

<!-- PAGE 2 -->

www.nature.com/scientificreports/

initial  plan  becomes  suboptimal.  Approaches  based  on  constraint  satisfaction  problems  (CSP)  and  heuristic 
algorithms can adapt seat allocations more flexibly, yet they frequently disregard equity concerns, risking the 
exclusion of borderline-compliant programs or underuse of institutional resources13,14.

In this paper, we introduce a dynamic recommender system that categorizes institutional requirements into 
hard constraints (e.g., faculty-to-student ratios, physical space) and soft constraints (e.g., academic performance 
targets,  policy-driven  objectives),  managing  them  within  an  iterative,  penalty-based  framework.  Rather  than 
depending on a single enrollment plan that quickly becomes outdated, our method recalculates seat allocations 
each cycle, revising penalty scores for programs that either exceed capacity limits or improve their compliance. 
Grounded in Equity Theory, the system ensures partially compliant programs remain partially enrolled, thus 
avoiding the idle capacity that might result from excluding them outright.

To  evaluate  the  performance  and  robustness  of  our  recommender  system,  we  conduct  a  comprehensive 
experimental study simulating multiple admission cycles under diverse institutional conditions. Across these 
multi-year simulations, the approach consistently demonstrates higher resource utilization, fewer violations, and 
more balanced seat distributions compared to both static and heuristic baselines. By adjusting recommended 
allocations  after  each  cycle,  the  framework  dynamically  responds  to  newly  surfaced  violations  or  emergent 
opportunities  for  strategic  growth—such  as  sudden  faculty  departures  or  shifts  in  government  policy.  This 
setup not only enables direct benchmarking against simpler allocation methods and heuristic alternatives but 
also  clarifies  how  each  approach  deals  with  complex,  real-time  demands.  The  following  sections  detail  our 
experimental design, data sources, and evaluation metrics, illustrating how the proposed framework maintains 
equitable seat distribution and high utilization across multiple academic cycles.

To conclude, our contribution is threefold:

•  Poses the admissions allocation problem as a dynamic CSP, thereby detecting and rectifying capacity viola-

tions in real time.

•  Incorporates Equity Theory into a penalty-based algorithm, ensuring that near-compliant programs remain

partially enrolled while fully compliant programs retain priority.

•  Demonstrates through multi-year simulations that the system achieves better resource usage, lower violation

rates, and fairer seat allocations compared to common static or heuristic strategies.

The  remainder  of  this  paper  is  organized  as  follows.  Section  Related  Work  surveys  relevant  literature 
on  enrollment  planning  and  CSP  models,  while  Section  Method  describes  our  penalty-based  approach. 
Section Experimentation outlines the experimental design and data sources as well as presents the key findings 
and Section Discussion discusses limitations, implications, and potential avenues for future research. Finally, 
Section Conclusion concludes our work by summarizing key insights and outlining potential directions.

Related work
Deciding how many students to admit each year is a widely considered challenge for universities. On one hand, 
institutions  must  make  the  most  of  their  available  classrooms,  faculty,  and  budgets;  on  the  other,  they  want 
to  meet  the  needs  of  eager  applicants  while  maintaining  quality.  Early  efforts  tackled  this  by  studying  past 
enrollment patterns and plugging the data into models—think simple linear regression or time-series forecasts—
to  get  a  sense  of  how  many  students  each  program  might  attract15,16.  Nowadays,  universities  are  leaning  on 
machine learning to take their forecasts to the next level. By feeding models not just past enrollment numbers 
but also factors like student demographics and evolving admission policies, they can uncover hidden patterns 
that simpler methods might miss11,12. By plugging your data into a neural network or a decision-tree model, you 
can tease out the key patterns that point to next year’s class size. For large universities, this level of precision is 
a game-changer, helping them juggle dozens of programs while serving a wide-ranging applicant pool17. But 
because these models are tuned for forecast accuracy rather than quick tweaks, they can stumble when you need 
to adjust constraints on the fly.

Goal programming has been extensively utilized in addressing resource allocation problems in education, 
including determining the optimal number of admissions. Think of goal programming as linear programming’s 
multitasking cousin: instead of chasing a single target, it can juggle several goals at once. That makes it ideal 
for universities juggling “must-haves” and “nice-to-haves”18,19 — from setting class sizes and spreading faculty 
workloads to squeezing every bit of value from scarce resources, all while keeping strategic priorities in view20,21. 
In the admissions office, you’ll see it in action when assigning students to programs by weighing factors like 
who’s available to teach and how much classroom space you have, ensuring you meet both your own policies and 
any outside rules22,23. However, goal programming models are typically static and struggle to adapt to real-time 
updates in constraints or priorities.

Constraint  Satisfaction  Problems  (CSPs)  offer  a  flexible  approach  to  solving  allocation  and  optimization 
challenges  in  education.  CSPs  are  used  in  scheduling,  resource  allocation,  and  admissions  to  dynamically 
balance competing constraints24. Algorithms such as backtracking, forward-checking, and Min-Conflicts have 
been widely applied to resolve CSPs in educational domains13,25. The Min-Conflicts algorithm, in particular, is 
known for its efficiency in solving large-scale CSPs by heuristically minimizing violations13. CSPs have been used 
to  optimize  course  scheduling,  allocate  resources  among  academic  departments,  and  balance  class  sizes26,27. 
However, while CSPs excel in handling hard constraints, they often require integration with other frameworks 
to address soft constraints effectively.

Beyond  classical  CSP  heuristics,  recent  advancements  in  recurrent  neural  networks  and  neural  dynamics 
have  introduced  powerful  methods  for  solving  time-varying  optimization  problems  with  guaranteed 
convergence28.  These  models  offer  robust,  noise-tolerant  frameworks  for  handling  dynamic  constraints29, 
making  them  theoretically  relevant  for  iteratively  recalculating  admission  targets  as  policies  and  resources

Scientific Reports |        (2025) 15:39756

| https://doi.org/10.1038/s41598-025-23116-6

2

---

<!-- PAGE 3 -->

www.nature.com/scientificreports/

shift. For instance, unified frameworks for time-varying quadratic optimization provide tools for guaranteed 
finite-time convergence30, while other research has focused on designing novel error functions to accelerate this 
process31 or developing specific discretization strategies for efficient implementation32. Such neural-dynamics 
approaches  offer  strong  theoretical  guarantees  for  stability  and  optimality  that  are  complementary  to  the 
heuristic, penalty-based adjustments proposed in our work. While our method prioritizes interpretability and 
ease  of  implementation  for  university  administrators,  these  state-of-the-art  optimization  techniques  provide 
a  valuable  theoretical  foundation  and  suggest  promising  avenues  for  future  extensions  involving  provably 
convergent models.

Equity  theory,  first  proposed  by  John  Stacey  Adams,  posits  that  individuals  gauge  fairness  by  comparing 
the ratio of their inputs (e.g., effort, skill) to the outcomes (e.g., rewards, opportunities) they receive relative to 
others. Although initially explored within organizational and social psychology33, equity theory has since found 
applications  in  technology-driven  contexts,  where  automated  decision-making  and  resource  allocation  can 
magnify perceptions of inequity. Scholars now embed fairness criteria directly into recommendation engines to 
prevent any demographic from being sidelined34,35. In educational technology, developers apply equity theory 
when creating adaptive learning platforms and enrollment-management systems, ensuring each student cohort 
receives an appropriate share of resources36. Embedding equity checks at every stage of development ensures that 
resources are distributed fairly. It also fosters genuine confidence among students, educators, and administrators 
that the system operates impartially—an assurance as vital to its success as the allocation itself.

Recommender  systems  have  increasingly  been  applied  to  higher  education  to  address  complex  allocation 
problems. Traditionally used in e-commerce and entertainment, recommender systems are now used to optimize 
course  selection,  match  students  to  programs,  and  allocate  admissions37.  While  content-  and  collaboration-
driven recommenders still form the backbone of most systems, knowledge-driven models—particularly those 
built  on  constraint-satisfaction  frameworks—are  increasingly  embraced  for  their  capacity  to  enforce  precise, 
domain-specific  rules38.  At  the  university  level,  these  recommendation  engines  guide  each  student  along 
a  tailored  curriculum  by  matching  courses  to  their  past  performance  and  individual  interests39,40.  However, 
when it comes to juggling firm requirements—such as credit limits or departmental quotas—alongside more 
flexible preferences in real time, most systems struggle, which makes them less effective for tasks like managing 
admissions10,41.

Our work combines the strengths of goal programming, CSP-based modeling, and equity theory, framing 
the  admissions  problem  as  a  flexible  yet  robust  constraint  satisfaction  challenge  within  a  knowledge-based 
recommender system. The decision to integrate these methods arises from their complementary capabilities: 
goal programming offers a sound structure for balancing competing institutional objectives, CSPs provide the 
capacity to dynamically handle both strict and adaptable constraints, and the incorporation of equity theory 
preserves fairness by ensuring that no group is systematically advantaged or disadvantaged18,37. Our approach 
brings  together  real-world  constraints  and  program-lifecycle  adjustments  so  that  student  allocations  both 
respect capacity limits and adapt as courses and resources change over time. In doing so, it fills a key gap in 
existing research and gives universities a practical, scalable tool for meeting the evolving challenges of today’s 
enrollment management8,12,42.

Method
Determining  the  optimal  number  of  students  for  each  academic  program  requires  careful  modeling  of 
institutional constraints. We split those into hard and soft categories. Hard constraints, such as infrastructure 
readiness and total available faculty teaching hours, constitute strict, non-negotiable limits that programs must 
observe. By contrast, soft constraints include factors like academic performance metrics or resource allocation 
preferences—criteria  that  allow  for  some  degree  of  flexibility  or  adjustment  under  specific  circumstances.  In 
this section, we detail how these constraints are formulated to recommend student admissions across diverse 
programs. Our modeling process leverages concepts from constraint satisfaction problems (CSP) and includes 
penalty-based adjustments inspired by Equity Theory (ET), enabling controlled deviations from soft constraints 
while preserving institutional priorities. In practical terms, the system calculates a combined compliance score 
for  each  program  based  on  both  strict  capacities  and  adjustable  performance  benchmarks,  thus  respecting 
critical operational thresholds while maintaining a level of flexibility. Ultimately, hard constraints serve as the 
groundwork for ensuring basic feasibility, whereas soft constraints function as tunable parameters that guide and 
optimize final admissions recommendations. (Sections Faculty capacity across multiple departments and Soft 
constraints).

Hard constraints
Hard constraints define the non-negotiable limits that govern how many students a program can admit, ensuring 
enrollment  never  exceeds  the  institution’s  physical  infrastructure  or  faculty  teaching  capacity.  In  this  paper, 
we focus on two key hard constraints—infrastructure readiness and faculty teaching capacity—and model both 
mathematically to highlight their critical roles in the decision-making process. Each of these constraints imposes 
a non-negotiable threshold; exceeding it would violate fundamental requirements necessary for a functional and 
high-quality learning environment.

Infrastructure capacity
Infrastructure capacity ensures that the number of admitted students does not exceed the university’s resources. 
To determine the maximum infrastructure capactity, we consider several factors. Each room i has a room capacity 
Ri (the maximum number of students it can seat) and a section capacity Si (the maximum number of students 
per  lecture  section).  We  also  track  the  number  of  available  timeslots  Ti,  indicating  how  many  instructional 
blocks the room can accommodate in a given period (e.g., per day or per week). Additionally, each course p has

Scientific Reports |        (2025) 15:39756

| https://doi.org/10.1038/s41598-025-23116-6

3

---

<!-- PAGE 4 -->

www.nature.com/scientificreports/

a timeslot requirement τp, often based on credit hours or whether the course is theoretical or practical, as well as 
a course type factor γp to adjust capacities for specialized classes (e.g., γp < 1 for lab-based courses).

An  important  consideration  is  the  scheduling  block,  namely  a  contiguous  set  of  timeslots  during  which 
courses can be scheduled without overlap. For example, a lab might occupy a two-hour block and preclude other 
classes in the same room, regardless of seating capacity. Integrating these elements, we use the following model 
to compute the maximum number of students that can be allocated to program p:

n

Cp =

min(Ri, Si)

i=1 (
∑

α(i, p)

,

×

)

where Cp is the overall infrastructure-based capacity for program p, and

α(i, p) =

γp,

Ti
τp ×
0,

{

τp,

if Ti

≥
otherwise.

(1)

(2)

The term min(Ri, Si) enforces whichever limit is stricter between room and section capacities, while α(i, p) 
indicates how many sections can practically run in room i given its timeslots and any special course requirements. 
In cases where a course needs two timeslots (τp = 2), these might be split across multiple rooms, depending on 
scheduling rules.

Some courses require special consideration. When γp = 1, the course has no additional capacity adjustments 
beyond the usual theoretical/practical requirements. If γp < 1, it may represent a specialized course (e.g., small-
group labs) that permits only a fraction of the normal section size. Likewise, if Ti < τp for a particular room, 
that room alone cannot host the course; it might, however, combine with another room’s timeslot to satisfy the 
requirement.

Example  of  Capacity  Calculation.  Suppose  a  specialized  course  (γp = 0.3)  requires  τp = 2  timeslots.

Consider one room i with Ri = 60, Si = 30, and Ti = 2. Because Ti

τp, we have

≥

α(i, p) =

Ti
τp ×

γp =

2
2 ×

0.3 = 0.3, min(Ri, Si) = 30, Cp = 30

0.3 = 9.

×

(3)

Thus, the room can accommodate 9 students for this specialized course. If Ti were only 1, then α(i, p) would be 
zero, indicating that this single room could not individually fulfill the two-timeslot requirement.

Utilization Factor. To measure how effectively resources are used, define

U =

Achieved Seat-Hours
Available Seat-Hours ×

100,

(4)

where Achieved Seat-Hours is the total number of scheduled students multiplied by their occupied timeslots, 
and  Available  Seat-Hours  is  the  product  of  a  room’s  capacity  and  all  assigned  timeslots  (including  relevant 
adjustments). Continuing the previous example, if we actually schedule 9 students in a room with Ri = 60 for 
2 timeslots, then

Achieved Seat-Hours = 9
×
Available Seat-Hours = 60
18
120 ×

U =

×

2 = 18,
2 = 120,

100 = 15%.

(5)

Although  15%  utilization  reflects  the  specialized  nature  of  the  course,  additional  classes  might  boost  overall 
seat-hour  usage  in  the  same  room.  By  considering  section  sizes,  timeslot  requirements,  and  course-specific 
adjustments, this approach maintains realistic scheduling constraints in institutional settings.

Faculty capacity across multiple departments
In many universities, a single program can draw courses from multiple departments, each of which has its own 
pool of faculty resources. Consequently, even if one department has surplus teaching capacity, a program may 
be forced to limit enrollment if another department that contributes courses is already at or near its faculty-
workload limit. This section describes how to compute a program’s maximum feasible enrollment in light of 
these  department-based  teaching  constraints,  without  multiplying  course  credit  hours  in  the  section-count 
calculation.

Department-Level Teaching Pools. Let 
D
the university’s programs. Each department d
(or load) they can collectively provide is

∈ D

be the set of all academic departments involved in teaching any of 
d, and the total teaching hours

has a set of faculty members

F

A course assigned to department d draws its entire teaching load from Tfaculty,d.

Tfaculty,d =

Wf .

f
∈Fd
∑

Scientific Reports |        (2025) 15:39756

| https://doi.org/10.1038/s41598-025-23116-6

(6)

4

---

<!-- PAGE 5 -->

www.nature.com/scientificreports/

∈ C

Programs and Course Assignments. Consider an academic program p that requires a set of courses 
C

p. Each 
p is administered by a single department, denoted dept(i). For each course i, let Si be the section 
course i
capacity, i.e., the maximum number of students per section; let Hi be the total faculty hours needed to deliver 
one section of course i per week (e.g., 3–6 hours, depending on the academic plan). Some institutions derive Hi 
by multiplying the course’s credit hours by a weekly contact-hour factor (e.g., 3 credits 
 2 hour/credit = 6 total 
hours). However, in this paper Hi encapsulates the total teaching load for one section, regardless of its credit or 
contact hours components.

×

Number of Sections. If X students enroll in Program p, then each course i

p requires

∈ C

Nsec(i) =

X
Si ⌉

⌈

(7)

X/Si

Hi

⌉ ×

sections, ensuring that no section exceeds its capacity Si. Hence, department dept(i) must provide 
⌈
hours for course i.

Departmental  Faculty  Constraints.  All  faculty  hours  for  course  i  must  come  from  dept(i).  Hence,  each

department d must satisfy

X
Si

Hi

×

(⌈

⌉

)

∑i
∈ C
dept(i) = d

p

Tfaculty,d,

≤

(8)

where Nsec(i) =
department) must hold simultaneously for an admission size X to be feasible.

. Because Program p may involve multiple departments, all such inequalities (one per 
⌉

X/Si

⌈

Program’s Maximum Feasible Enrollment. The maximum number of students X that can be admitted under 
departmental faculty constraints is the largest integer X for which (8) is satisfied across every department whose 
courses appear in

p. Formally,

C

max X such that

d

∀

∈ {

dept(i)

i

|

p
∈ C

}

:

X
Si

∑i: dept(i)=d(⌈

⌉

Hi

×

≤

Tfaculty,d.

(9)

)

Because  a  program’s  courses  may  span  multiple  departments,  all  such  constraints  must  hold  to  admit  X 
students.  For  instance,  suppose  program  p  draws  upon  Department  1  and  Department  2.  Let  Department  1 
have  Tfaculty,1 = 60  hours  available,  with  two  courses:  Course  A  (dept(A) = 1,  SA = 30,  HA = 3)  and 
Course B (dept(B) = 1, SB = 20, HB = 4). Let Department 2 have Tfaculty,2 = 36 hours and offer Course 
C (dept(C) = 2, SC = 40, HC = 6). For X students, we need 
 sections 
 sections of A and 
⌉
⌉
X/40
  sections  of  C  in  Department  2.  The  total  load  in  Department  1  is 
of  B  in  Department  1,  and 
⌉
⌈
X/30
6, 
3 +
⌈
capped at 36. If X = 40, then 
×
4=8  hours),  for  a  total  of  6 + 8 = 14  hours  in  Department  1,  which  is  feasible  since  14
60.  Department  2 
≤
36. Thus, X = 40 is within capacity; one 
runs 
can increment X further until either department’s limit is exceeded, thereby finding the program’s maximum 
feasible enrollment.

4,  which  must  not  exceed  60,  while  the  load  in  Department  2  is

6=6 hours), also feasible since 6

⌉ ×
⌈
= 2 sections of B (2

= 2 sections of A (2

= 1 section of C (1

3=6 hours) plus

40/30
⌉

40/40

40/20

X/30

X/20

X/20

X/40

⌉ ×

⌉ ×

×

×

≤

⌈

⌈

⌈

⌈

⌈

⌉

⌈

⌉

Utilization Metric. To measure how effectively each department’s teaching resources are used, define

Ufaculty,d =

Total Hours Used in Dept. d
Tfaculty,d

×

100%.

(10)

A  high  Ufaculty,d  (close  to  or  above  100%)  indicates  potential  overload  of  department  d,  while  a  low  value 
suggests that the department might be underutilized or could accommodate more students. By enforcing

∑i
∈ C
dept(i) = d

p

⌈

(

X/Si

Hi

⌉ ×

≤

)

Tfaculty,d

for every involved department d,

(11)

the institution ensures that no department is inadvertently overloaded by cross-departmental demands. This 
multi-department  approach,  unlike  simpler  models  that  compute  capacity  for  each  program  in  isolation 
[e.g6],  prevents  one  heavily  demanded  department  from  becoming  a  hidden  bottleneck,  while  also  revealing 
underutilized  areas  that  might  expand  enrollment.  Such  a  holistic  perspective  allows  decision-makers  to  set 
accurate, equitable admission targets that reflect the true distribution of faculty resources.

Soft constraints
In contrast to hard constraints—which enforce non-negotiable limits based on physical resources or operational 
capacities—soft constraints provide a flexible mechanism for integrating a wide range of institutional objectives 
and  policy-driven  goals  into  the  admissions  process.  The  proposed  framework  is  designed  to  accommodate 
not  only  the  common  constraints  discussed  below  (e.g.,  academic  performance  metrics,  resource  allocation 
preferences, and government-imposed policies) but also additional criteria as needed. For instance, institutions

Scientific Reports |        (2025) 15:39756

| https://doi.org/10.1038/s41598-025-23116-6

5

---

<!-- PAGE 6 -->

www.nature.com/scientificreports/

may incorporate measures such as student satisfaction, retention rates, extracurricular balance, demographic 
equity, or regional representation. In what follows, we detail the general formulation for the soft constraints and 
their integration.

General formulation and examples
We encode each soft constraint by introducing a penalty score that grows with the gap between actual outcomes 
and the desired targets. During optimization, these penalty score steer the solution toward institutional priorities 
and equity goals — without ever overriding the immutable hard constraints. Formally, each soft constraint is 
represented by a penalty function:

Pi(p) = ωi

×

f

target(p), actual(p)

,

(12)

(

)

where Pi(p) is the penalty from constraint i for program p, ωi is a weighting factor reflecting that constraint’s 
relative importance, and f (
) is a function measuring how far the program’s actual performance deviates from 
its  target.  Typically,  f   takes  the  form  of  a  max
  expression  to  ensure  no  penalty  is  incurred  when  a 
}
program meets or exceeds the target. In what follows, we detail three representative soft constraints commonly 
encountered in higher education admissions planning.

0, . . .

{

·

·

,

Example 1: Academic Performance (Graduation Rates) Academic performance metrics, such as graduation 
rates, exemplify this framework. Let Tgrad(p) be the target graduation rate for program p, and Agrad(p) the 
actual rate. Using a deviation function,

Pperformance(p) = α

max

{

×

0, Tgrad(p)

Agrad(p)

,

}

−

(13)

we  impose  a  penalty  only  when  the  actual  graduation  rate  falls  short  of  the  target.  The  weighting  factor  α 
determines how heavily to penalize shortfalls.

Example 2: Government-Imposed Policies Many institutions must comply with labor-market mandates or 
government  directives.  Let  Rj(p)  be  the  target  metric  (e.g.,  an  employment-rate  threshold)  and  Mj(p)  the 
measured or projected value. Summing over all such restrictions j = 1, . . . , J:

Ppolicy(p) =

J

j=1
∑

γj

max

{

×

0, Rj(p)

Mj(p)

. 
}

−

(14)

Programs falling below any required threshold incur a penalty, scaled by γj.

Example 3: Resource Allocation Preferences Finally, some institutions prefer to keep enrollments balanced 
across programs. Suppose each program p admits Sp students, and  ¯S is the average across all programs. One can 
penalize large deviations via

Presource(p) = β

Sp

−

¯S

.

×

(15)

Sp

High 
−
encourages rebalancing.

|

|

¯S

means the program is either over- or under-subscribed, triggering an institutional penalty that

(cid:31)
(cid:31)

(cid:31)
(cid:31)

Aggregate soft constraint penalty
The overall soft constraint penalty for each program p is obtained by aggregating the penalties associated with 
all individual soft constraints. Let 
 be the index set for all soft constraints incorporated into the model (e.g., 
academic performance, resource allocation, government-imposed policies, and any additional criteria). Then, 
the aggregate soft penalty is defined as:

I

Psoft(p) =

Pi(p).

(16)

i
∑
∈I
For example, if the model includes three soft constraints—graduation rates Pperformance(p), resource allocation 
preferences Presource(p), and government-imposed policies Ppolicy(p)—the aggregate penalty becomes:

Psoft(p) = Pperformance(p) + Presource(p) + Ppolicy(p).

(17)

This formulation is inherently flexible and can easily be extended to incorporate additional soft constraints (such 
as student retention rates or demographic balance) by adding corresponding penalty terms to the summation. 
Minimizing  Psoft(p)  across  all  programs  thus  ensures  that  the  optimization  process  effectively  balances 
deviations from institutional targets, market needs, and other quality indicators.

Integration of hard and soft constraints
Our goal is to recommend an optimal admission number for each program that balances operational feasibility 
(hard constraints) with strategic quality and market objectives (soft constraints). Specifically, we adjust the current 
(baseline)  admissions  continuously  according  to  each  program’s  degree  of  compliance  with  soft  constraints. 
Programs with low penalty scores (full compliance) are permitted to approach their maximum feasible number, 
whereas those with high penalty scores are subject to reduction.

Scientific Reports |        (2025) 15:39756

| https://doi.org/10.1038/s41598-025-23116-6

6

---

<!-- PAGE 7 -->

www.nature.com/scientificreports/

Let S0

p represent the current or baseline admission number for program p, as dictated by the program’s actual 
usage of available hard resources. The maximum feasible admission number based exclusively on these hard 
constraints is denoted by Smax

. The ratio

p

δp =

S0
p

Smax
p −
S0
p

(18)

then expresses the relative increase possible. For instance, if a program is currently operating at 80% of its hard-
capacity limit, that is S0
p = 0.8 Smax
, the term δp evaluates to 0.25, which indicates admissions may be raised by 
up to 25% of the current count before reaching full capacity.

p

We further define Psoft(p) in equation 16 as the program’s aggregate penalty for soft constraints. Normalizing

this penalty by a constant Pmax (for example, the largest observed penalty) yields

xp =

Psoft(p)
Pmax

,

(19)

ensuring  xp
closer to 1 are regarded as highly non-compliant and may see sharper reductions in admissions.

[0, 1].  Programs  with  low  xp  have  minimal  soft-constraint  penalties,  whereas  those  with  xp

∈

Next,  we  define  a  continuous  adjustment  function,  g(xp) = 1 + δp(1

2xp),  that  maps  the  normalized 
penalty xp onto a multiplicative factor. The choice of this linear form is deliberate. Its primary advantage lies 
in its simplicity and interpretability: it creates a direct, proportional relationship between a program’s non-
compliance penalty and its recommended admission adjustment. This straightforward mapping ensures that a 
program halfway to the maximum penalty (xp = 0.5) receives no change, while those at the extremes (xp = 0 
or xp = 1) receive the maximum possible increase or decrease, respectively. While other non-linear functions 
could  be  employed—such  as  a  sigmoid  function  for  smoother  transitions  or  a  concave  function  to  penalize 
minor deviations more heavily—the linear model provides a balanced and easily understandable baseline for 
iterative adjustments.

−

Accordingly, the recommended admission number for program p is given by:

p = S0
Srec
p ·

g(xp) = S0
p

1 + δp

1

[

(

2

−

Psoft(p)
Pmax ))]

.

(

(20)

This formulation yields three key outcomes depending on the value of xp. First, when xp = 0 (i.e., the program 
is fully compliant), we have

p = S0
Srec
p

1 + δp

= Smax
p

,

(21)

which  means  the  program  can  safely  increase  its  admissions  to  reach  its  hard-capacity  limit.  Second,  if 
xp = 0.5 (moderate non-compliance), then

[

]

p = S0
Srec
p

1 + δp(1

1)

= S0
p,

−

(22)

implying there is no recommended change from the baseline. Finally, with xp = 1 (maximum non-compliance), 
the system imposes

[

]

p = S0
Srec
p

1 + δp(1

2)

= S0

p(1

δp),

−

−

(23)

thus reducing admissions below the current level to penalize severe deviations from soft-constraint objectives.

[

]

It is worth noting that the framework operates much like a warm-start optimization. Each cycle begins from 
the baseline allocation Sp
0 , which reflects the current admissions state, and then makes proportional adjustments 
using penalty scores. In this way, recommendations build on earlier solutions rather than being recalculated in 
full, which helps improve computational efficiency and makes the process easier for administrators to follow. 
In practice, this mechanism enables institutions to track incremental changes transparently while retaining the 
efficiency benefits of warm-start optimization techniques.

p > Smax

Also, it is crucial to note how the framework handles programs that are already operating beyond their hard 
capacity limits. In a scenario where the current admission number exceeds the maximum feasible limit (i.e., 
S0
p) becomes negative. Consequently, the adjustment formula will inherently 
recommend a reduction in admissions regardless of the program’s soft constraint performance, guiding it back 
towards its non-negotiable capacity threshold. This ensures the system’s primary objective—adherence to hard 
constraints—is always prioritized.

), the term (Smax

p −

S0

p

Thus, the final recommended admissions for each program is first calculated as:

p = S0
Srec
p

1 +

[

(

S0
p

Smax
p −
S0
p

2

1

−

Psoft(p)
Pmax ))]

.

(

) (

(24)

Finally,  this  recommended  number  is  adjusted  to  enforce  a  minimum  admission  quota,  M ,  ensuring  that 
no  program  falls  below  a  baseline  institutional  threshold,  such  that  Srec
p ). This  continuous 
adjustment mechanism ensures that the recommendation is dynamically aligned with the program’s compliance

max(M, Srec

p ←

Scientific Reports |        (2025) 15:39756

| https://doi.org/10.1038/s41598-025-23116-6

7

---

<!-- PAGE 8 -->

www.nature.com/scientificreports/

with soft constraints—rewarding those that are well-aligned and penalizing those that are less aligned, while 
always remaining within the bounds set by the hard constraints.

To facilitate prioritization, we define a program’s compliance score as:

compliancep = 1

xp.

−

(25)

Consequently, programs can be ranked in descending order of their compliance scores. A higher score indicates 
better adherence to soft constraint objectives and justifies a higher recommended admission number (subject to 
the hard resource limits). This ranking provides a quantitative basis for strategic admissions planning.

Algorithm 1.  Two-phase admissions Algorithm: Hard constraints and penalty-based scaling.

Experimentation
We evaluated our admissions framework using a simulated dataset composed of 14 academic programs serving 
a combined total of 29,100 students. The dataset was designed to capture both the variety and complexity of 
constraints typically encountered in higher education. Next, we detail the setup and results of our experimentation.

Experimental setup
In generating the simulation, we began by distributing the 29,100 students unevenly across the 14 programs, 
replicating real-world imbalances in popularity and resource usage. Each program was assigned a unique blend 
of  requirements,  reflecting  differences  in  credit  hours,  lab  or  lecture  format,  and  baseline  compliance  with 
institutional  standards.  To  model  capacity  constraints,  we  sampled  faculty  loads  and  room  availability  from 
realistic ranges, ensuring that some programs were already near (or over) their limits while others had significant 
spare capacity.

Beyond hard constraints, we introduced three soft penalties (corresponding to the three soft constraints; we 
simulate the target values according to actual statistics from the ministry of education and labor in Saudi Arabia) 
by assigning each program specific performance targets (e.g., graduation rates), policy requirements (e.g., labor-
market alignment), and enrollment balance goals (e.g., deviation from the average). Some programs thus started 
with negligible penalty scores, while others faced large penalties for underperforming across multiple criteria. 
This mixture guaranteed a meaningful test of the system’s ability to reallocate enrollments effectively.

All approaches were implemented in Python 3.9, using standard libraries (NumPy, pandas, PuLP) for data 
handling, matrix operations, and constraint satisfaction. Random seeds were fixed to ensure reproducibility of 
the simulated data.

To benchmark our results, we compared our method against two baselines: (1) a Greedy approach43 that ranks 
programs by a single performance metric (e.g., quality or priority) and allocates seats in descending order until 
capacities are filled, and (2) Simulated Annealing44,45, a well-known metaheuristic widely used for combinatorial 
optimization  and  Constraint  Satisfaction  Problems  (CSPs).  The  Greedy  method  serves  as  a  straightforward 
baseline  for  seat  allocation,  while  Simulated  Annealing  probabilistically  explores  seat  distributions,  allowing 
occasional  “uphill”  moves  to  escape  local  minima.  We  evaluated  each  method  on  (a)  the  number  of  hard-
constraint violations, (b) an overall penalty score capturing the severity of any violated constraints, and (c) the 
fairness of seat distribution across programs, measured by an equity metric, namely the Gini coefficient46.

These  metrics  enabled  us  to  comprehensively  assess  each  method’s  adherence  to  capacity  and  staffing 
constraints, its penalty for violating institutional and policy-driven preferences, and the fairness of its allocations.

Scientific Reports |        (2025) 15:39756

| https://doi.org/10.1038/s41598-025-23116-6

8

---

<!-- PAGE 9 -->

www.nature.com/scientificreports/

In the following sections, we present and discuss our solution’s performance relative to these baseline and state-
of-the-art  techniques,  highlighting  both  quantitative  gains  and  practical  insights  for  institutional  planning. 
While the results are presented for one representative simulated environment to ensure clarity, the fixed random 
seeds  guarantee  reproducibility.  Furthermore,  the  statistical  tests  presented  in  the  following  sections  (e.g., 
bootstrapping  and  ANOVA)  provide  confidence  in  the  stability  of  our  findings,  which  were  consistent  with 
patterns observed across several preliminary generative runs.

Results
We begin by presenting the outcomes of our proposed approach, focusing on two key metrics: penalty score 
(where a lower value indicates better compliance) and recommended changes in admission numbers to achieve 
optimal  allocation.  Table  1  summarizes  the  performance  of  our  approach  across  the  14  academic  programs, 
detailing how constraints influence the allocation process. As shown in the table, programs with zero penalty 
scores receive an increase in the number of admitted students, ensuring that resources are fully utilized while 
prioritizing compliant programs. However, these increases are bounded by the hard constraints cap for each 
program, preventing overallocation beyond infrastructural and faculty limits.

To promote fairness and a gradual transition to compliance, our approach does not enforce abrupt reductions 
for  non-compliant  programs  but  adjusts  student  numbers  proportionally  based  on  penalty  severity.  Colleges 
with lower penalty scores receive slight increases in admissions, reinforcing equity by rewarding near-compliant 
institutions.  Conversely,  programs  with  high  penalty  scores  experience  gradual  reductions,  ensuring  that 
resource allocation shifts do not disrupt the institutional ecosystem. By distributing reductions proportionally 
rather  than  uniformly,  the  approach  allows  severely  non-compliant  programs  to  progressively  adjust  while 
maintaining an equitable growth trajectory for those closer to full compliance. Figure 1(a) illustrates the actual 
number of students recommended for the next year, reflecting the combined effect of graduation adjustments 
and new admissions allocations.

In  contrast,  the  Simulated  Annealing  (SA)  method  centers  on  minimizing  the  overall  penalty  score, 
sometimes to the detriment of locally equitable student allocations. As depicted in Figure 1(b), SA can produce 
sizeable  increases  in  certain  programs—notably  Medicine,  Applied  Medical  Sciences,  and  Sports  Science—
while simultaneously enforcing substantial cuts in others, such as Computer Science, Law, and Education. This 
pattern  arises  because  SA,  through  exploring  a  wide  range  of  potential  seat  distributions,  prioritizes  global 
penalty  reduction  over  proportional  adjustments  that  reflect  each  program’s  individual  level  of  compliance. 
Consequently,  even  fully  compliant  programs  may  not  see  enrollment  rises  commensurate  with  their  strong 
performance  if  doing  so  fails  to  reduce  the  system-wide  penalty,  whereas  other  programs  may  receive  large 
enrollment boosts despite minimal or moderate violations.

The  third  algorithm  in  our  comparison  is  the  Greedy  approach  (Fig.  1  (c)),  which  focuses  on  a  single 
constraint  at  a  time  rather  than  weighing  all  constraints  holistically.  As  a  result,  locally  optimal  choices  can 
lead to suboptimal outcomes once the remaining constraints are considered. For instance, the Greedy method 
allocates more students to Computer Science and Social Science because they appear compliant with the specific 
constraint it evaluates initially, even though both programs violate several other constraints under a broader 
assessment. In contrast, programs that are compliant across most measures may receive large cuts under Greedy, 
simply because the available “quota” was already consumed by programs flagged as non-violative for the single 
constraint in focus, thereby overlooking their broader compliance record.

To  assess  the  equity  of  enrollment  recommendations  across  the  three  methods,  we  calculated  the  Gini

coefficient using the standard formula:

G =

n
i=1 i xi
n
i=1 xi −

2
n
∑
∑

n + 1
n

,

Program

Penalty Score Change in Admission (%)

Status

Applied Medical Science

Engineering

Computer Science

Business

Social Sciences

Law

Languages

Education

Sciences

Design and Arts

Applied Studies

Humanities

Medicine

Sports Science

25

25

10

25

10

25

30

25

25

25

25

10

0

0

−2.18%

−2.16%

2.64%

−3.48%

2.08%

−1.78%

−5.88%

−1.29%

−2.55%

−2.86%

−3.18%

2.35%

22.50%

53.12%

Violated

Violated

Violated

Violated

Violated

Violated

Violated

Violated

Violated

Violated

Violated

Violated

Committed

Committed

Table 1.  Summary of our method’s performance across programs.

Scientific Reports |        (2025) 15:39756

| https://doi.org/10.1038/s41598-025-23116-6

9

---

<!-- PAGE 10 -->

www.nature.com/scientificreports/

Fig. 1.  Comparison of student allocations across different approaches.

Fig. 2.  Comparison of Gini Coefficients Across Methods. A lower coefficient indicates a more equitable 
distribution of the recommended enrollments. Our method exhibits the smallest Gini value (0.067), signifying 
superior fairness compared to the Simulated Annealing and Greedy algorithms (0.293 and 0.387, respectively).

where  x1, x2, . . . , xn  are  the  sorted  enrollment  allocations  and  n = 14  is  the  number  of  programs.  Our 
recommender system achieved the lowest Gini coefficient, 0.067, indicating the most equitable distribution of 
students. By contrast, Simulated Annealing and Greedy resulted in substantially higher coefficients of 0.293 and 
0.387, respectively. Using a bootstrap resampling approach with 10,000 iterations, we found that the differences 
between our method’s Gini coefficient and those of the other two approaches were statistically significant at the 
p < 0.01 level. As illustrated in Fig. 2, these results suggest that our recommender not only meets key constraints

Scientific Reports |        (2025) 15:39756

| https://doi.org/10.1038/s41598-025-23116-6

10

---

<!-- PAGE 11 -->

www.nature.com/scientificreports/

Fig. 3.  Average Utilization of Hard Constraints Across Five Iterative Admission Cycles. Our recommender 
method prevents resource underutilization more effectively than Simulated Annealing or Greedy, reflecting a 
superior balance between compliance and capacity usage.

Method

Avg. Time to Full Compliance (Yrs) Notes

Our Recommender

Simulated Annealing

Greedy

4.2

6.2

7.6

Balances gradual reduction and avoids new violations.

Minimizes penalties each year but reintroduces local infractions.

Slowest due to its sequential, single-constraint approach.

Table 2.  Average Time (Years) to Eliminate Violations Over Five Admission Cycles.

but also more uniformly distributes enrollments across programs, thereby facilitating fairer and more informed 
decisions for the upcoming academic year.

Convergence over time
While rapid violation reduction can seem beneficial, highly aggressive cuts risk underutilizing essential resources 
(e.g., classrooms, faculty). In contrast, our recommender advocates moderate, incremental changes that preserve 
near-optimal usage of available capacity. To evaluate how each method balances compliance with efficient use of 
institutional resources, we conducted a multi-year simulation in which each algorithm’s recommendations for 
one year inform the next year’s baseline. Concretely, we first run the algorithm to determine the optimal number 
of students for the upcoming academic cycle. Once these recommendations are set, we use them as the starting 
point for the following year, repeating the same procedure. Through this iterative process, we capture the long-
term trajectory each approach induces.

Figure 3 shows how effectively the three methods preserve hard constraints (e.g., classroom capacity, faculty 
workload) across five consecutive admission cycles. Our recommender consistently achieves utilization levels of 
85–90% of the maximum capacity, thus avoiding both over-allocation and chronic underutilization. By contrast, 
≈
Simulated Annealing (SA) ranges between 50% and 75%, reflecting its focus on overall penalty minimization, 
which can lead to substantial under-allocation in certain programs. The Greedy algorithm remains closer to 60% 
utilization, indicating that it often discards capacity prematurely in favor of locally optimal steps.

An ANOVA test (F=9.72, p<0.01) on the average utilization rates confirms statistically significant differences 
among the methods. Post-hoc Tukey tests reveal that our recommender maintains a distinctly higher (p<0.01) 
utilization  rate  compared  to  both  SA  and  Greedy.  Hence,  although  other  methods  may  appear  to  reduce 
violations more quickly in certain cycles, they risk admitting too few students, thereby leaving valuable university 
resources idle. In contrast, our recommender systematically ensures each program is sufficiently filled without 
exceeding capacity, allowing institutions to fully leverage their infrastructure and faculty while still advancing 
toward compliance targets.

We also conducted a ten-year simulation to examine how quickly each approach eliminates penalties across 
all programs, assuming no new violations occur. As shown in Table 2, our recommender achieves full compliance 
in  an  average  of  4.2  years,  balancing  steady  penalty  reductions  with  minimal  new  infractions.  By  contrast, 
Simulated Annealing (SA) attains notably low penalties each year, but its strong focus on global minimization 
reintroduces local violations in previously near-compliant programs, preventing a zero-violation state across the 
system. Meanwhile, the Greedy method proves slowest overall: its sequential, single-constraint emphasis causes 
it to address additional penalties only once the dominant constraint has been satisfied, taking longer than five 
years in some scenarios.

The  findings  presented  across  all  experiments  underscore  the  strengths  of  our  recommender  system, 
particularly in balancing the need for prompt violation reduction with efficient resource utilization and long-
term  stability.  While  Simulated  Annealing  and  Greedy  each  show  certain  advantages—for  instance,  rapidly 
diminishing penalties in isolated cycles or meeting a single dominant constraint—they fail to maintain sustainable 
compliance or avoid undue underutilization of university capacity. By contrast, our recommender consistently 
achieves a robust blend of fairness, capacity preservation, and effective multi-year violation management. In the

Scientific Reports |        (2025) 15:39756

| https://doi.org/10.1038/s41598-025-23116-6

11

---

<!-- PAGE 12 -->

www.nature.com/scientificreports/

following section, we further contextualize these outcomes, highlighting the practical implications for higher 
education institutions and potential avenues for improvement and future research.

Discussion
In admissions planning, universities have often turned to goal programming and static linear models to manage 
competing  objectives. These  methods  are  rigorous;  however,  each  time  the  constraints  shift  the  problem  has 
to be solved again from scratch. That makes them less useful in settings where quotas, staffing, or facilities can 
shift quickly. Our equity-aware recommender takes a different approach. It introduces incremental, year-to-year 
adjustments through compliance penalties, much like a warm-start process. This approach cuts down on repeated 
computation while still preserving a high level of compliance and fairness. As shown in our simulations, the 
framework consistently sustains 85–90% utilization of available capacity and reduces violations more steadily 
over time than static goal programming or heuristic baselines such as Greedy and Simulated Annealing.

We  acknowledge  that  traditional  optimization  methods,  such  as  goal  programming,  can  be  adapted  to 
dynamic  environments  by  re-solving  the  problem  with  updated  constraints  or  by  adding  regularization 
terms  to  penalize  drastic  changes  in  enrollment  plans.  However,  our  iterative,  penalty-based  framework 
offers complementary advantages. It is often more intuitive for institutional administrators to interpret, as the 
adjustments are directly tied to transparent performance metrics. Furthermore, it can be computationally lighter 
than re-solving a complex optimization model from scratch each cycle, offering a practical and agile solution for 
real-time decision support.

Equity considerations feature prominently in our allocation logic, ensuring no department or program is 
permanently excluded from admissions. Rather than shutting out partially compliant departments, the system 
provides  them  with  controlled  enrollments  once  fully  compliant  programs  reach  their  limits.  This  strategy 
resonates  with  equity  theory,  which  emphasizes  distributing  resources  in  a  manner  that  prevents  any  single 
group from facing prolonged disadvantage. Empirically, our calculations (including low Gini coefficients) verify 
that allocations generated by our approach are more evenly distributed than those of SA or Greedy. Simulated 
Annealing, though adept at cutting global penalties, can repeatedly induce local infractions in programs that 
were close to compliance, while Greedy addresses pressing constraints in isolation, leaving other programs to 
lag behind.

It is worth noting that our SA implementation serves as a standard benchmark for penalty minimization in 
CSPs. We concede that a more direct comparison could be achieved by modifying the SA objective function 
to explicitly incorporate fairness and stability goals, and we consider the development of such a custom-tuned 
baseline a valuable direction for future comparative work. In contexts like Saudi Arabia—where government-
funded, tuition-free education adds further complexity to balancing capacity and access, where the ability to 
include  partially  compliant  programs  without  idling  vacant  seats  is  particularly  advantageous2,3.  By  allowing 
modest enrollment for these programs, the framework fosters incremental improvement while making full use 
of institutional resources. This measured yet inclusive approach promotes long-term institutional development, 
as it permits a broad range of programs to move steadily toward higher compliance.

Our framework introduces fairness by drawing on equity theory and using proportional seat adjustments, so 
that no program is left consistently disadvantaged. This stands in contrast to stable matching approaches, which 
focus on incentive compatibility—ensuring that no stakeholder wants to deviate from the outcome. Stability is 
a strong guarantee when individual preferences drive markets, but public university admissions often give more 
weight to meeting capacity limits and policy requirements than to alternative choice. In practice, stable matching 
can also impose rigid rules that make it harder to admit programs that nearly meet the criteria, leading to unused 
resources. For this reason, we adopt equity-based fairness as a more practical tool for dynamic seat planning. At 
the same time, stable matching offers a useful perspective, and adapting ideas such as deferred acceptance could 
improve robustness in the long run.

An important advantage of our equity-based algorithm is that its recommendations implicitly account for 
natural enrollment dynamics, including the gradual graduation of students. As shown in Fig. 1, other methods 
often  pursue  minimum  penalties  by  advising  drastic  reductions  for  programs  with  high  violation  scores; 
however, this can be impractical since universities remain responsible for students already enrolled. Abruptly 
halving or eliminating seats in the next academic cycle could negatively impact ongoing cohorts, conflicting 
with  institutional  policies  and  realistic  planning  horizons.  In  contrast,  our  framework’s  partial  allowance  for 
underperforming  or  partially  compliant  programs  moderates  such  steep  declines,  resulting  in  more  feasible 
recommendations that better reflect day-to-day operational constraints. Rather than advocating overly aggressive 
targets, the equity-aware model facilitates gradual, stepwise adjustments over multiple years. This approach not 
only curtails disruption for existing students and faculty but also provides administrators with a structured path 
to align enrollments with institutional goals without sacrificing educational continuity.

A deeper look at short-term gains versus enduring stability reveals the importance of a tempered approach. 
While  Simulated  Annealing  can  achieve  low  aggregate  penalties  quickly,  its  stochastic  reassignments  often 
cause previously near-compliant programs to oscillate back into violation. To analyze the robustness of our own 
approach, we conducted a one-factor-at-a-time (OFAT) sensitivity analysis on the annual reduction rate, with 
the results shown in Table 3. The analysis confirms that moderate annual reductions of 10%−20% significantly 
improve  both  hard  and  soft  constraint  adherence  without  spawning  unforeseen  violations  elsewhere.  This 
balanced  trajectory  is  vital  in  real  academic  environments,  where  precipitous  cuts  in  admissions  can  disrupt 
departmental planning and budgeting. Accordingly, our approach’s stable readjustment paradigm seems better 
suited to sustained institutional health.

We use the Gini coefficient as the main fairness indicator because it is easy to interpret, widely applied in 
inequality studies, and allows direct comparisons across programs. Fairness, however, has many dimensions. 
Other indices—such as entropy, Hoover, or Theil—highlight different kinds of distributional imbalance. In some

Scientific Reports |        (2025) 15:39756

| https://doi.org/10.1038/s41598-025-23116-6

12

---

<!-- PAGE 13 -->

www.nature.com/scientificreports/

Reduction (%/Yr) Hard Compliance (%)

Soft Compliance (%) Total Improvement (%)

5%

10%

15%

20%

25%

10

20

35

50

70

5

15

25

35

50

7.5

17.5

30

42.5

60

Table 3.  Sensitivity analysis of admission reductions.

Strategy

Min Time (Yrs) Max Time (Yrs) Avg Time (Yrs)

Large Reduction

1.4

Gradual Reduction 2

5.2

6.2

3.3

4.2

Table 4.  Reduction strategy. Min Time (Yrs): Minimum time required for compliance. Max Time (Yrs): 
Maximum time required for compliance. Avg Time (Yrs): Average time required for compliance.

early  experiments  (not  included  here),  these  alternative  measures  showed  patterns  similar  to  the  Gini-based 
results, which gives us confidence in our findings. Even so, a fuller evaluation across multiple indices could bring 
out trade-offs between competing notions of equity. We therefore acknowledge that while Gini provides a clear 
starting point, future work should adopt a broader suite of fairness measures to strengthen robustness.

Observing  multi-year  simulations  further  highlights  divergent  strategies  for  tackling  ongoing  constraints. 
SA may look attractive due to its capacity to minimize penalties early in each cycle, but it frequently under-
enrolls  certain  programs  and  allows  fresh  infractions  to  arise  over  time.  Greedy’s  single-constraint  approach 
resolves dominant issues but lags in addressing secondary or tertiary constraints, dragging out the timeline to 
full compliance. By contrast, our recommender continually updates program capacities and reassigns students 
methodically,  yielding  a  consistent  pattern  of  improvement.  When  dealing  with  severely  non-compliant 
departments,  more  decisive  “Large  Reduction”  tactics  can  achieve  compliance  within  seven  years,  though  at 
the  cost  of  immediate  operational  shifts.  Alternatively,  the  “Gradual  Reduction”  strategy  extends  the  process 
to a decade yet eases the transition for programs unprepared for sudden changes (Table 4). This flexibility to 
accelerate or decelerate the pace of reform aligns closely with the reality that universities vary in their tolerance for 
enrollment swings and resource reallocation. Thus, the algorithm provides a practical toolkit for administrators 
who must weigh the benefits of swift compliance against potential disruptions to staffing and budgets.

Our simulations show that the system typically converges to full compliance within about four admission 
cycles  when  moderate  adjustment  strategies  are  used.  This  outcome  gives  practical  evidence  of  stability 
and  robustness.  At  the  same  time,  there  is  scope  for  deeper  theoretical  grounding.  Recent  work  in  dynamic 
optimization  and  neural  dynamics  (e.g47–49])  has  established  finite-time  convergence  and  stability  for  time-
varying quadratic programs. Our current penalty-based approach was designed to keep the process clear and 
straightforward for administrators. Future work could make use of more advanced models. These would build 
on the stability we already observe in practice and, at the same time, provide stronger theoretical guarantees of 
optimality as institutional constraints evolve.

Notwithstanding  these  gains,  certain  limitations  merit  attention.  Our  experiments  rely  on  simulated  data 
designed  to  mimic  real-world  enrollment  trends,  but  genuine  institutional  environments  are  often  more 
complex.  While  this  simulation-driven  approach  is  instructive,  large-scale  field  trials  would  offer  a  stronger 
measure of how the algorithm handles the fine-grained distinctions that emerge between different departments 
or  campuses17.  Another  concern  is  that  our  penalty-based  soft  constraints  presume  relatively  stable  policy 
objectives, yet external mandates—such as new government directives or evolving accreditation criteria—can 
shift rapidly3. Incorporating adaptive or machine learning elements could enable near real-time recalibrations 
to the penalty structure, enhancing the algorithm’s resilience12. Additionally, the potential for multi-campus or 
cross-institutional applications remains largely untested; integrating resource-sharing mechanisms or parallel 
constraint-solvers  may  be  pivotal  for  scaling  up  in  large  or  distributed  university  networks10.  Despite  these 
limitations, the current results affirm that our solution offers both practical and theoretical benefits, positioning 
it as a viable option for institutions seeking a more nuanced admissions strategy.

In our sensitivity analysis, we looked at annual reduction ratios. The results showed that moderate cuts of 
about 10–20% improved compliance without upsetting the overall allocations. However, this one-factor-at-a-
time approach overlooks many other parameters that could impact robustness. Other factors—such as weighting 
coefficients in the penalty functions, the design of minimum admission quotas, and alternative formulations 
of  soft-constraint  penalties—could  also  significantly  affect  stability  and  fairness.  We  therefore  note  that  the 
present sensitivity analysis should be viewed as a baseline demonstration. Looking ahead, it will be beneficial to 
explore the parameter space in a more detailed and multi-factorial way. Doing so could give stronger evidence 
of robustness across different institutional settings.

Lastly,  this  study  underscores  the  potential  for  a  goal-oriented  recommender  system  that  balances 
infrastructural limits, academic quality metrics, and fairness principles. In settings like Saudi Arabia—where 
free tuition and centralized mandates require a careful mix of access and resource rationing—an algorithmic

Scientific Reports |        (2025) 15:39756

| https://doi.org/10.1038/s41598-025-23116-6

13

---

<!-- PAGE 14 -->

www.nature.com/scientificreports/

approach that aligns with these complex dynamics can greatly enhance admissions planning. Contrasting our 
method  with  Simulated  Annealing  and  Greedy  highlights  how  single-minded  emphasis  on  global  penalty 
reduction or stepwise constraint satisfaction risks leaving valuable resources unused or repeatedly reintroducing 
local  violations.  By  examining  all  constraints  in  tandem  and  providing  an  equitable  seat  distribution,  our 
framework maintains enough flexibility to adapt to institutional needs—whether that entails a quick convergence 
strategy or a protracted, more measured realignment process. Future developments should test these insights 
in actual campus environments, refine penalty structures based on machine learning predictions of program 
compliance,  and  consider  how  multi-institution  collaboration  might  further  optimize  resource  usage.  In  so 
doing, universities can ensure that a data-driven, policy-aware admissions tool continues to evolve in step with 
the rapidly changing landscape of higher education, enabling them to sustain fairness, efficiency, and academic 
excellence.

Conclusion
This  study  presented  a  recommender  system  for  student  admissions  that  integrates  hard  constraints  (e.g., 
classroom  capacity  and  faculty  loads)  and  soft  constraints  (such  as  academic  performance  targets,  policy 
requirements, and equity considerations) into a unified optimization framework. Through iterative refinements 
and  penalty-based  allocation,  the  system  maintains  near-complete  compliance  with  operational  thresholds 
while significantly reducing soft-constraint penalties, surpassing existing baselines by over 50%. In so doing, 
it  balances  capacity  utilization  against  equity  objectives,  offering  partially  compliant  programs  controlled 
admissions without unduly disadvantaging fully compliant ones.

A  multi-year  convergence  analysis  showed  that  institutions  can  achieve  full  compliance  in  approximately 
three  to  four  years,  particularly  when  combining  rapid  cuts  for  severe  infractions  with  more  incremental 
strategies  for  moderate  issues.  Sensitivity  tests  further  revealed  that  moderate  annual  enrollment  reductions 
(around 10%–20%) yield notable improvements in compliance while avoiding the instability often introduced by 
more aggressive plans. These findings affirm that the system is both robust and adaptable, allowing institutions 
to customize reduction levels in line with strategic, operational, or regulatory needs.

Despite these strengths, reliance on simulated data calls for additional real-world validation, especially in 
contexts where institutional constraints and policy shifts evolve dynamically. Future enhancements might include 
machine learning for predictive analytics and adaptive penalty weighting, further refining responsiveness and 
accuracy. Investigating applications in multi-campus networks or collaborative institutional settings would also 
broaden the framework’s utility.

Overall, the proposed system offers a flexible, equitable, and resource-efficient approach to higher education 
admissions. By reconciling institutional priorities with government directives in a single optimization process, 
it fosters sustainable long-term admissions planning that aligns educational quality standards with the principle 
of equitable access.

Data availability
Data is described within the manuscript.

Code availability
The complete source code, including data-generation scripts, will be made available by the corresponding 
author upon reasonable request following publication.

Received: 21 May 2025; Accepted: 3 October 2025

References
  1.  Altbach,  P.  G.,  Reisberg,  L.  &  Rumbley,  L.  E.  Trends  in  Global  Higher  Education:  Tracking  an  Academic  Revolution  (UNESCO,

2009). https://unesdoc.unesco.org/ark:/48223/pf0000183219

2.  UNESCO: The world needs almost 69 million new teachers to reach the 2030 education goals.  h t t p s : / / u n e s d o c . u n e s c o . o r g / a r k : / 4 8

2 2 3 / p f 0 0 0 0 2 4 6 1 2 4     (2016)

3.  McKinsey,  Company:  Reimagining  higher  education.   h t t p s :  / / w w w .  m c k i n s  e y . c o m  / i n d u  s t r i e s  / e d u c a  t i o n / o  u r - i n  s i g h t s  / r e i m a  g i n i n

g  - h i g h  e r - e d u  c a t i o n  - i n - t h  e - u n i t e d - s t a t e s # / (2020).

4.  DiBiase, D. The impact of increasing enrollment on faculty workload and student satisfaction over time. Journal of Asynchronous

Learning Networks 8(2), 45–60 (2004).

5.  Watts, J. & Robertson, N. Burnout in university teaching staff: A systematic literature review. Educational Research 53(1), 33–50

(2011).

6.  Beyrouthy, C. et al. Towards improving the utilization of university teaching space. Journal of the Operational Research Society

60(1), 130–143 (2009).

7.  Heller, D. E. The effects of tuition and state financial aid on public college enrollment. Review of Higher Education 23(1), 65–89

(2001).

8.  Brynjolfsson, E. & McAfee, A. The Second Machine Age: Work. Progress, and Prosperity in a Time of Brilliant Technologies. W.W.

Norton & Company. https://wwnorton.com/books/the-second-machine-age/ (2014).

9.  Pal, B. B., Kumar, M. & Sen, S. A priority-based goal programming method for solving academic personnel planning problems

with interval-valued resource goals in university management system. Int. J. Appl. Manag. Sci. 4 (3), 284–312 (2012).

10.  Ehlers, U.-D. Emerging Open-learning Cultures: Transforming Higher Education (Springer, 2013).  h t t p s :   /  / l i n  k . s p r i n g e  r . c   o m / c h  a p t  e

r   / 1 0 . 1   0 0 7  / 9   7 8 -  3 - 6 4 2 -  3 8 1 7 4 - 4

11.  Maulana, A. et al. Optimizing university admissions: a machine learning perspective. J. Educ. Manag. Learn. 1 (1), 1–7 (2023).
 12.  Shilbayeh,  S.  &  Abonamah,  A.  Predicting  student  enrollments  and  attrition  patterns  in  higher  educational  institutions  using

machine learning. Int. Arab J. Inf. Technol. 18 (4), 562–567 (2021).

13.  Minton, S., Johnston, M. D., Philips, A. B. & Laird, P. Minimizing conflicts: A heuristic repair method for constraint satisfaction

and scheduling problems. In: Artificial Intelligence Elsevier, (1992). https://doi.org/10.1016/0004-3702(92)90007-K.

Scientific Reports |        (2025) 15:39756

| https://doi.org/10.1038/s41598-025-23116-6

14

---

<!-- PAGE 15 -->

www.nature.com/scientificreports/

14.  Adams, J. S. Towards an understanding of inequity. The journal of abnormal and social psychology 67(5), 422 (1963).
 15.  Wilkinson,  R.,  Taylor,  J.  S.,  Peterson,  A.  &  Machado-Taylor,  M.  d.  L.  A  practical  guide  to  strategic  enrollment  management

planning. Online Submission (2007).

16.  Hossler, D. & Kalsbeek, D. Enrollment management and managing enrollments: Revisiting the context for institutional strategy

Strategic Enrollment Management Quarterly (2013).

17.  Maldonado, E. & Seehusen, V. Data mining student choices. J. Educ. Bus. 93 (5), 196–203 (2018).
 18.  Ignizio, J. P. Generalized goal programming an overview. Comput. Oper. Res. (1976)
 19.  Tamiz, M., Jones, D. F. & El-Darzi, E. A review of goal programming and its applications. Ann. Oper. Res. 58 (1), 39–53 (1995).
 20.  Chatterjee, S. & Bhattacharjee, K. K. Adoption of artificial intelligence in higher education. Educ. Inform. Technol. 25(5), 3443–

3463 (2020).

21.  Koksalan, M. & Wallenius, J. Multiple criteria decision making in resource allocation problems. Operations Research 59(5), 1302–

1308 (2011).

22.  Zeleny, M. Multiple criteria decision making. Operations Research 30(5), 1109–1110 (1982).
 23.  Wang,  J.,  Wang,  D.  &  Li,  A.  Goal  programming  and  its  variants.  In  Encyclopedia  of  Decision  Making  and  Decision  Support

Technologies 410–417 (2008)

24.  Dechter, R. Constraint Processing. Morgan Kaufmann. https://doi.org/10.5555/861293 (2003).
 25.  Russell, S. & Norvig, P. Artificial intelligence: A modern approach. Pearson (2020).
 26.  Garey, M. R. & Johnson, D. S. Computers and intractability: A guide to the theory of np-completeness (Freeman, 1979).
 27.  Haralick, R. M. & Elliott, G. L. Increasing tree search efficiency for constraint satisfaction problems. Artificial Intelligence 14(3),

263–313 (1980).

28.  Jin, L., Li, S., Liao, B. & Zhang, Z. Zeroing neural networks: A survey. Neurocomputing 267, 597–604 (2017).
 29.  Xiao, L. et al. Design and comprehensive analysis of a noise-tolerant znn model with limited-time convergence for time-dependent

nonlinear minimization. IEEE Transactions on Neural Networks and Learning Systems 31(12), 5339–5348 (2020).

30.  Xiao, L., Li, K. & Duan, M. Computing time-varying quadratic optimization with finite-time convergence and noise tolerance: 
A unified framework for zeroing neural network. IEEE transactions on neural networks and learning systems 30(11), 3360–3369 
(2019).

31.  Liao, B., Zhang, Y. & Jin, L. Taylor discretization of znn models for dynamic equality-constrained quadratic programming with

application to manipulators. IEEE transactions on neural networks and learning systems 27(2), 225–237 (2015).

32.  Xiao, L., Tan, H., Jia, L., Dai, J. & Zhang, Y. New error function designs for finite-time znn models with application to dynamic

matrix inversion. Neurocomputing 402, 395–408 (2020).

33.  Adams,  J.  S.  Inequity  in  social  exchange.  In  Advances  in  Experimental  Social  Psychology  Vol.  2  (ed.  Berkowitz,  L.)  267–299

(Academic Press, 1965).

34.  Burke, R. Multisided fairness for recommendation In: Proceedings of the Workshop on Responsible Recommendation at the 11th

ACM Conference on Recommender Systems (RecSys). ACM, New York, NY, USA, (2017).

35.  Li, Y. et al. Fairness in recommendation: Foundations, methods, and applications. ACM Transact. Intell. Syst. Technol. 14 (5), 1–48

(2023).

36.  Volery, T. & Lord, D. Critical success factors in online education. The International Journal of Educational Management 14(5),

216–223. https://doi.org/10.1108/09513540010344731 (2000).

37.  Ricci, F., Rokach, L. & Shapira. B.: Introduction to Recommender Systems Handbook. Springer ???  h t t p s : / / d o i . o r g / 1 0 . 1 0 0 7 / 9 7 8 - 0 - 3

8 7 - 8 5 8 2 0 - 3     (2011).

38.  Adomavicius, G. & Tuzhilin, A. Toward the next generation of recommender systems: A survey of the state-of-the-art and possible

extensions. IEEE Transactions on Knowledge and Data Engineering 17(6), 734–749 (2005).

39.  Drachsler,  H.  et  al.  Issues  and  considerations  regarding  sharable  data  sets  for  recommender  systems  in  technology  enhanced

learning. Proced. Comput. Sci. 1 (2), 2849–2858 (2010).

40.  Romero,  C.  &  Ventura,  S.  Educational  data  mining:  A  review  of  the  state  of  the  art.  IEEE  Transactions  on  Systems,  Man,  and

Cybernetics 40(6), 601–618 (2010).

41.  Deri, M. N., Singh, A., Zaazie, P. & Anandene, D. Leveraging artificial intelligence in higher educational institutions. Revista de

Educacion y Derecho (30) (2024).

42.  Jeddah, U. Internal Academic Admissions Reports. Confidential Data (2023). https://uj.edu.sa
 43.  Cormen, T. H., Leiserson, C. E., Rivest, R. L. & Stein, C. Introduction to Algorithms 3rd edn. (MIT Press, 2009).
 44.  Kirkpatrick, S., Gelatt, C. D. & Vecchi, M. P. Optimization by simulated annealing. Science 220(4598), 671–680.  h t t p s : / / d o i . o r g / 1 0

. 1 1 2 6 / s c i e n c e . 2 2 0 . 4 5 9 8 . 6 7 1     (1983).

45.  Černý, V. Thermodynamical approach to the traveling salesman problem: An efficient simulation algorithm. Journal of Optimization

Theory and Applications 45(1), 41–51. https://doi.org/10.1007/BF00940812 (1985).

46.  Allison, P. D. Measures of inequality. American Sociological Review 43(6), 865–880. https://doi.org/10.2307/2094626 (1978).
 47.  Zeng,  Y.,  Xiao,  L.,  Li,  K.,  Zuo,  Q.  &  Li,  K.  Solving  time-varying  linear  inequalities  by  finite-time  convergent  zeroing  neural

networks. Journal of the Franklin Institute 357(12), 8137–8155 (2020).

48.  Li, W., Xiao, L. & Liao, B. A finite-time convergent and noise-rejection recurrent neural network and its discretization for dynamic

nonlinear equations solving. IEEE Transactions on Cybernetics 50(7), 3195–3207 (2019).

49.  Xiao, L., Cao, Y., Dai, J., Jia, L. & Tan, H. Finite-time and predefined-time convergence design for zeroing neural network: Theorem,

method, and verification. IEEE Transactions on Industrial Informatics 17(7), 4724–4732 (2020).

Acknowledgements
The authors would like to express their sincere appreciation to the University of Jeddah and to His Excellency 
Prof. Adnan Humaidan, former President of the University, for his generous support and continuous guidance 
that greatly contributed to the successful completion of this research.

Author contributions
Dr Ahmed conceived the main idea, designed the research methodology, and wrote the initial draft of the man-
uscript. Dr Alaa contributed to data collection, experimental execution. Prof Eesa conducted further refinement 
of the methods and assisted with manuscript revisions. All authors reviewed and approved the final version of 
the manuscript.

Declarations

Competing interests
The authors declare no competing interests.

Scientific Reports |        (2025) 15:39756

| https://doi.org/10.1038/s41598-025-23116-6

15

---

<!-- PAGE 16 -->

www.nature.com/scientificreports/

Additional information
Correspondence and requests for materials should be addressed to A.I.

Reprints and permissions information is available at www.nature.com/reprints.

Publisher’s note  Springer Nature remains neutral with regard to jurisdictional claims in published maps and 
institutional affiliations.

Open Access   This article is licensed under a Creative Commons Attribution-NonCommercial-NoDerivatives 
4.0 International License, which permits any non-commercial use, sharing, distribution and reproduction in 
any medium or format, as long as you give appropriate credit to the original author(s) and the source, provide 
a link to the Creative Commons licence, and indicate if you modified the licensed material. You do not have 
permission under this licence to share adapted material derived from this article or parts of it. The images or 
other third party material in this article are included in the article’s Creative Commons licence, unless indicated 
otherwise in a credit line to the material. If material is not included in the article’s Creative Commons licence 
and your intended use is not permitted by statutory regulation or exceeds the permitted use, you will need to 
obtain permission directly from the copyright holder. To view a copy of this licence, visit  h t t p : / / c r e a t i v e c o m m o 
n s . o r g / l i c e n s e s / b y - n c - n d / 4 . 0 /     .

© The Author(s) 2025

Scientific Reports |        (2025) 15:39756

| https://doi.org/10.1038/s41598-025-23116-6

16

<!-- MARKITDOWN CONVERSION -->

<!-- Full MarkItDown conversion for formatting fidelity. -->

www.nature.com/scientificreports
OPEN An equity aware recommender
system for university admissions
balancing operational constraints
and strategic objectives
Ahmed Ibrahim1, Ala Alarood2 & Eesa Alsolami3
Institutions of higher education must balance multiple, often conflicting objectives when setting
admission targets for their academic programs. In this paper, we introduce a recommendation system
that integrates Constraint Satisfaction Problem (CSP) techniques, goal programming, and Equity
Theory to optimize student assignments. Our model strictly enforces hard constraints—such as faculty-
hour limits and classroom capacities—while accommodating soft constraints—such as government
quotas and institutional preferences—through adjustable penalty functions. Evaluations against
static and heuristic benchmarks show that our approach maintains enrollment at 85–90% of total
capacity, markedly reducing both the frequency and severity of constraint violations. Furthermore, an
average Gini coefficient of 0.067 demonstrates a fairer distribution of seats across programs. Over five
simulated admission cycles, institutions employing this recommender achieve substantial compliance
improvements within four years, striking an effective balance between rapid constraint adherence and
stable enrollment figures. These results confirm that our system offers a practical, data-driven solution
for flexible and equitable enrollment management in resource-limited higher-education settings.
Keywords Recommender systems, Higher education admissions, Constraints satisfaction problem, Goal
programming
Universities have long faced the difficult task of matching incoming student numbers to the limitations of their
teaching staff, classroom capacity, and budgets1,2. In Saudi Arabia, the free-education system makes this challenge
even harder to manage, since there are no consequences for students who fail to graduate as planned (e.g. they
continue to occupy seats at no extra cost). Although this system opens doors for more learners, it also intensifies
competition for spots in the most sought-after programs. Moreover, sudden events—such as unexpected staff
cuts or the introduction of new government quotas—can throw even the most carefully planned enrollment
figures off course3. Institutions, therefore, need flexible methods that can rapidly adjust admission numbers
whenever policies shift or resources change.
This challenge is not merely theoretical; it manifests in significant operational inefficiencies that static
planning methods struggle to resolve. For instance, it is common for internal university reports to reveal that
high-demand programs consistently operate well beyond their intended faculty capacity, sometimes by as much
as 15–20%, leading to overworked staff and potential compromises in educational quality4,5. Concurrently, other
academic programs may remain significantly under-enrolled, utilizing only 60–70% of their available classroom
and laboratory space6. This persistent misalignment between student demand and available resources highlights
the critical failure of seat-planning methods that cannot adapt to shifting enrollment trends or sudden changes
in capacity, such as unexpected staff departures. The resulting imbalance not only strains institutional resources
but also creates inequities in access and educational experience across different fields of study
Many universities attempt to address these complexities by instituting two types of guidelines: strict limits on
resources (e.g., maximum student–faculty ratios) and more flexible, policy-oriented goals7,8. While traditional
methods such as goal programming effectively uphold these boundaries, they often struggle when immediate
adjustments become necessary9,10. Meanwhile, machine learning and predictive analytics provide valuable
insights into enrollment trends11,12, but rarely incorporate mechanisms to dynamically reassign seats once the
1Department of Computer Science and Artificial Intelligence, College of Computer Science and Engineering,
University of Jeddah, Jeddah, Saudi Arabia. 2Department of Information Technology, College of Computer Science
and Engineering, University of Jeddah, Jeddah, Saudi Arabia. 3Department of Cybersecurity, College of Computer
Science and Engineering, University of Jeddah, Jeddah, Saudi Arabia. email: amabrahem6@uj.edu.sa
Scientific Reports | (2025) 15:39756 | https://doi.org/10.1038/s41598-025-23116-6 1

www.nature.com/scientificreports/
initial plan becomes suboptimal. Approaches based on constraint satisfaction problems (CSP) and heuristic
algorithms can adapt seat allocations more flexibly, yet they frequently disregard equity concerns, risking the
exclusion of borderline-compliant programs or underuse of institutional resources13,14.
In this paper, we introduce a dynamic recommender system that categorizes institutional requirements into
hard constraints (e.g., faculty-to-student ratios, physical space) and soft constraints (e.g., academic performance
targets, policy-driven objectives), managing them within an iterative, penalty-based framework. Rather than
depending on a single enrollment plan that quickly becomes outdated, our method recalculates seat allocations
each cycle, revising penalty scores for programs that either exceed capacity limits or improve their compliance.
Grounded in Equity Theory, the system ensures partially compliant programs remain partially enrolled, thus
avoiding the idle capacity that might result from excluding them outright.
To evaluate the performance and robustness of our recommender system, we conduct a comprehensive
experimental study simulating multiple admission cycles under diverse institutional conditions. Across these
multi-year simulations, the approach consistently demonstrates higher resource utilization, fewer violations, and
more balanced seat distributions compared to both static and heuristic baselines. By adjusting recommended
allocations after each cycle, the framework dynamically responds to newly surfaced violations or emergent
opportunities for strategic growth—such as sudden faculty departures or shifts in government policy. This
setup not only enables direct benchmarking against simpler allocation methods and heuristic alternatives but
also clarifies how each approach deals with complex, real-time demands. The following sections detail our
experimental design, data sources, and evaluation metrics, illustrating how the proposed framework maintains
equitable seat distribution and high utilization across multiple academic cycles.
To conclude, our contribution is threefold:
• Poses the admissions allocation problem as a dynamic CSP, thereby detecting and rectifying capacity viola-
tions in real time.
• Incorporates Equity Theory into a penalty-based algorithm, ensuring that near-compliant programs remain
partially enrolled while fully compliant programs retain priority.
• Demonstrates through multi-year simulations that the system achieves better resource usage, lower violation
rates, and fairer seat allocations compared to common static or heuristic strategies.
The remainder of this paper is organized as follows. Section Related Work surveys relevant literature
on enrollment planning and CSP models, while Section Method describes our penalty-based approach.
Section Experimentation outlines the experimental design and data sources as well as presents the key findings
and Section Discussion discusses limitations, implications, and potential avenues for future research. Finally,
Section Conclusion concludes our work by summarizing key insights and outlining potential directions.
Related work
Deciding how many students to admit each year is a widely considered challenge for universities. On one hand,
institutions must make the most of their available classrooms, faculty, and budgets; on the other, they want
to meet the needs of eager applicants while maintaining quality. Early efforts tackled this by studying past
enrollment patterns and plugging the data into models—think simple linear regression or time-series forecasts—
to get a sense of how many students each program might attract15,16. Nowadays, universities are leaning on
machine learning to take their forecasts to the next level. By feeding models not just past enrollment numbers
but also factors like student demographics and evolving admission policies, they can uncover hidden patterns
that simpler methods might miss11,12. By plugging your data into a neural network or a decision-tree model, you
can tease out the key patterns that point to next year’s class size. For large universities, this level of precision is
a game-changer, helping them juggle dozens of programs while serving a wide-ranging applicant pool17. But
because these models are tuned for forecast accuracy rather than quick tweaks, they can stumble when you need
to adjust constraints on the fly.
Goal programming has been extensively utilized in addressing resource allocation problems in education,
including determining the optimal number of admissions. Think of goal programming as linear programming’s
multitasking cousin: instead of chasing a single target, it can juggle several goals at once. That makes it ideal
for universities juggling “must-haves” and “nice-to-haves”18,19 — from setting class sizes and spreading faculty
workloads to squeezing every bit of value from scarce resources, all while keeping strategic priorities in view20,21.
In the admissions office, you’ll see it in action when assigning students to programs by weighing factors like
who’s available to teach and how much classroom space you have, ensuring you meet both your own policies and
any outside rules22,23. However, goal programming models are typically static and struggle to adapt to real-time
updates in constraints or priorities.
Constraint Satisfaction Problems (CSPs) offer a flexible approach to solving allocation and optimization
challenges in education. CSPs are used in scheduling, resource allocation, and admissions to dynamically
balance competing constraints24. Algorithms such as backtracking, forward-checking, and Min-Conflicts have
been widely applied to resolve CSPs in educational domains13,25. The Min-Conflicts algorithm, in particular, is
known for its efficiency in solving large-scale CSPs by heuristically minimizing violations13. CSPs have been used
to optimize course scheduling, allocate resources among academic departments, and balance class sizes26,27.
However, while CSPs excel in handling hard constraints, they often require integration with other frameworks
to address soft constraints effectively.
Beyond classical CSP heuristics, recent advancements in recurrent neural networks and neural dynamics
have introduced powerful methods for solving time-varying optimization problems with guaranteed
convergence28. These models offer robust, noise-tolerant frameworks for handling dynamic constraints29,
making them theoretically relevant for iteratively recalculating admission targets as policies and resources
Scientific Reports | (2025) 15:39756 | https://doi.org/10.1038/s41598-025-23116-6 2

www.nature.com/scientificreports/
shift. For instance, unified frameworks for time-varying quadratic optimization provide tools for guaranteed
finite-time convergence30, while other research has focused on designing novel error functions to accelerate this
process31 or developing specific discretization strategies for efficient implementation32. Such neural-dynamics
approaches offer strong theoretical guarantees for stability and optimality that are complementary to the
heuristic, penalty-based adjustments proposed in our work. While our method prioritizes interpretability and
ease of implementation for university administrators, these state-of-the-art optimization techniques provide
a valuable theoretical foundation and suggest promising avenues for future extensions involving provably
convergent models.
Equity theory, first proposed by John Stacey Adams, posits that individuals gauge fairness by comparing
the ratio of their inputs (e.g., effort, skill) to the outcomes (e.g., rewards, opportunities) they receive relative to
others. Although initially explored within organizational and social psychology33, equity theory has since found
applications in technology-driven contexts, where automated decision-making and resource allocation can
magnify perceptions of inequity. Scholars now embed fairness criteria directly into recommendation engines to
prevent any demographic from being sidelined34,35. In educational technology, developers apply equity theory
when creating adaptive learning platforms and enrollment-management systems, ensuring each student cohort
receives an appropriate share of resources36. Embedding equity checks at every stage of development ensures that
resources are distributed fairly. It also fosters genuine confidence among students, educators, and administrators
that the system operates impartially—an assurance as vital to its success as the allocation itself.
Recommender systems have increasingly been applied to higher education to address complex allocation
problems. Traditionally used in e-commerce and entertainment, recommender systems are now used to optimize
course selection, match students to programs, and allocate admissions37. While content- and collaboration-
driven recommenders still form the backbone of most systems, knowledge-driven models—particularly those
built on constraint-satisfaction frameworks—are increasingly embraced for their capacity to enforce precise,
domain-specific rules38. At the university level, these recommendation engines guide each student along
a tailored curriculum by matching courses to their past performance and individual interests39,40. However,
when it comes to juggling firm requirements—such as credit limits or departmental quotas—alongside more
flexible preferences in real time, most systems struggle, which makes them less effective for tasks like managing
admissions10,41.
Our work combines the strengths of goal programming, CSP-based modeling, and equity theory, framing
the admissions problem as a flexible yet robust constraint satisfaction challenge within a knowledge-based
recommender system. The decision to integrate these methods arises from their complementary capabilities:
goal programming offers a sound structure for balancing competing institutional objectives, CSPs provide the
capacity to dynamically handle both strict and adaptable constraints, and the incorporation of equity theory
preserves fairness by ensuring that no group is systematically advantaged or disadvantaged18,37. Our approach
brings together real-world constraints and program-lifecycle adjustments so that student allocations both
respect capacity limits and adapt as courses and resources change over time. In doing so, it fills a key gap in
existing research and gives universities a practical, scalable tool for meeting the evolving challenges of today’s
enrollment management8,12,42.
Method
Determining the optimal number of students for each academic program requires careful modeling of
institutional constraints. We split those into hard and soft categories. Hard constraints, such as infrastructure
readiness and total available faculty teaching hours, constitute strict, non-negotiable limits that programs must
observe. By contrast, soft constraints include factors like academic performance metrics or resource allocation
preferences—criteria that allow for some degree of flexibility or adjustment under specific circumstances. In
this section, we detail how these constraints are formulated to recommend student admissions across diverse
programs. Our modeling process leverages concepts from constraint satisfaction problems (CSP) and includes
penalty-based adjustments inspired by Equity Theory (ET), enabling controlled deviations from soft constraints
while preserving institutional priorities. In practical terms, the system calculates a combined compliance score
for each program based on both strict capacities and adjustable performance benchmarks, thus respecting
critical operational thresholds while maintaining a level of flexibility. Ultimately, hard constraints serve as the
groundwork for ensuring basic feasibility, whereas soft constraints function as tunable parameters that guide and
optimize final admissions recommendations. (Sections Faculty capacity across multiple departments and Soft
constraints).
Hard constraints
Hard constraints define the non-negotiable limits that govern how many students a program can admit, ensuring
enrollment never exceeds the institution’s physical infrastructure or faculty teaching capacity. In this paper,
we focus on two key hard constraints—infrastructure readiness and faculty teaching capacity—and model both
mathematically to highlight their critical roles in the decision-making process. Each of these constraints imposes
a non-negotiable threshold; exceeding it would violate fundamental requirements necessary for a functional and
high-quality learning environment.
Infrastructure capacity
Infrastructure capacity ensures that the number of admitted students does not exceed the university’s resources.
To determine the maximum infrastructure capactity, we consider several factors. Each room i has a room capacity
R i (the maximum number of students it can seat) and a section capacity S i (the maximum number of students
per lecture section). We also track the number of available timeslots T i, indicating how many instructional
blocks the room can accommodate in a given period (e.g., per day or per week). Additionally, each course p has
Scientific Reports | (2025) 15:39756 | https://doi.org/10.1038/s41598-025-23116-6 3

www.nature.com/scientificreports/
a timeslot requirement τ p, often based on credit hours or whether the course is theoretical or practical, as well as
a course type factor γ p to adjust capacities for specialized classes (e.g., γ <1 for lab-based courses).
p
An important consideration is the scheduling block, namely a contiguous set of timeslots during which
courses can be scheduled without overlap. For example, a lab might occupy a two-hour block and preclude other
classes in the same room, regardless of seating capacity. Integrating these elements, we use the following model
to compute the maximum number of students that can be allocated to program p:
n
|     |     |     | C   | =   | min(R | ,S i) | α(i,p) | ,   |     |
| --- | --- | --- | --- | --- | ----- | ----- | ------ | --- | --- |
|     |     |     |     | p   |       | i     |        |     | (1) |
×
|     |     |     |     | i=1( |     |     |     | )   |     |
| --- | --- | --- | --- | ---- | --- | --- | --- | --- | --- |
∑
where C p is the overall infrastructure-based capacity for program p, and
T
|     |     |     |         |     | i γ | , if | T τ | ,   |     |
| --- | --- | --- | ------- | --- | --- | ---- | --- | --- | --- |
|     |     |     | α(i,p)= |     | τ × | p    | i ≥ | p   | (2) |
p
|     |     |     |     |     | { 0, | otherwise. |     |     |     |
| --- | --- | --- | --- | --- | ---- | ---------- | --- | --- | --- |

The term min(R ,S i) enforces whichever limit is stricter between room and section capacities, while α(i,p)
i
indicates how many sections can practically run in room i given its timeslots and any special course requirements.
In cases where a course needs two timeslots (τ
p =2), these might be split across multiple rooms, depending on
scheduling rules.
Some courses require special consideration. When γ
p =1, the course has no additional capacity adjustments
beyond the usual theoretical/practical requirements. If γ <1, it may represent a specialized course (e.g., small-
p
| group labs) that permits only a fraction of the normal section size. Likewise, if T |     |     |     |     |     |     |     | <τ  |     |
| ----------------------------------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
i p for a particular room,
that room alone cannot host the course; it might, however, combine with another room’s timeslot to satisfy the
requirement.
| Example of Capacity Calculation. Suppose a specialized course (γ |     |     |     |     |     |     |     | =0.3) requires τ |     |
| ---------------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | ---------------- | --- |
p p =2 timeslots.
| Consider one room i with R |     |     | =60, S | =30, and T | =2. Because T |     |     | τ          |     |
| -------------------------- | --- | --- | ------ | ---------- | ------------- | --- | --- | ---------- | --- |
|                            |     |     | i      | i          | i             |     | i   | p, we have |     |
≥
|     |         | T i | 2     |          |       |     |        |               |     |
| --- | ------- | --- | ----- | -------- | ----- | --- | ------ | ------------- | --- |
|     | α(i,p)= |     | γ =   | 0.3=0.3, | min(R | ,S  | i)=30, | C =30 0.3=9.  | (3) |
|     |         | τ   | × p 2 | ×        |       | i   |        | p ×           |     |
|     |         | p   |       |          |       |     |        |               |     |
Thus, the room can accommodate 9 students for this specialized course. If T i were only 1, then α(i,p) would be
zero, indicating that this single room could not individually fulfill the two-timeslot requirement.
Utilization Factor. To measure how effectively resources are used, define
|     |     |     |     | Achieved  | Seat-Hours |     |       |     |     |
| --- | --- | --- | --- | --------- | ---------- | --- | ----- | --- | --- |
|     |     |     | U   | =         |            |     | 100,  |     | (4) |
|     |     |     |     | Available | Seat-Hours |     | ×     |     |     |
where Achieved Seat-Hours is the total number of scheduled students multiplied by their occupied timeslots,
and Available Seat-Hours is the product of a room’s capacity and all assigned timeslots (including relevant
adjustments). Continuing the previous example, if we actually schedule 9 students in a room with R i =60 for
2 timeslots, then
|     |     |     | Achieved | Seat-Hours=9 |     | 2=18, |     |     |     |
| --- | --- | --- | -------- | ------------ | --- | ----- | --- | --- | --- |
×
|     |     |     | Available | Seat-Hours=60 |     |     | 2=120, |     |     |
| --- | --- | --- | --------- | ------------- | --- | --- | ------ | --- | --- |
|     |     |     |           |               |     | ×   |        |     | (5) |
18
|     |     |     |     |     | U = |       | 100=15%. |     |     |
| --- | --- | --- | --- | --- | --- | ----- | -------- | --- | --- |
|     |     |     |     |     |     | 120 × |          |     |     |
Although 15% utilization reflects the specialized nature of the course, additional classes might boost overall
seat-hour usage in the same room. By considering section sizes, timeslot requirements, and course-specific
adjustments, this approach maintains realistic scheduling constraints in institutional settings.
Faculty capacity across multiple departments
In many universities, a single program can draw courses from multiple departments, each of which has its own
pool of faculty resources. Consequently, even if one department has surplus teaching capacity, a program may
be forced to limit enrollment if another department that contributes courses is already at or near its faculty-
workload limit. This section describes how to compute a program’s maximum feasible enrollment in light of
these department-based teaching constraints, without multiplying course credit hours in the section-count
calculation.
Department-Level Teaching Pools. Let   be the set of all academic departments involved in teaching any of
D
the university’s programs. Each department d  has a set of faculty members  d, and the total teaching hours
|     |     |     |     |     | ∈D  |     |     | F   |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
(or load) they can collectively provide is
|     |     |     |     | T   | =         | W   | .   |     |     |
| --- | --- | --- | --- | --- | --------- | --- | --- | --- | --- |
|     |     |     |     |     | faculty,d |     | f   |     | (6) |
|     |     |     |     |     |           | f   |     |     |     |
∑∈Fd
| A course assigned to department d draws its entire teaching load from T |     |     |     |     |     |     |     | faculty,d. |     |
| ----------------------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | ---------- | --- |
4
Scientific Reports |        (2025) 15:39756  | https://doi.org/10.1038/s41598-025-23116-6

www.nature.com/scientificreports/
Programs and Course Assignments. Consider an academic program p that requires a set of courses  p. Each
C
course i p is administered by a single department, denoted dept(i). For each course i, let S i be the section
∈C
capacity, i.e., the maximum number of students per section; let H i be the total faculty hours needed to deliver
one section of course i per week (e.g., 3–6 hours, depending on the academic plan). Some institutions derive H i
by multiplying the course’s credit hours by a weekly contact-hour factor (e.g., 3 credits   2 hour/credit = 6 total
×
hours). However, in this paper H i encapsulates the total teaching load for one section, regardless of its credit or
contact hours components.
| Number of Sections. If X students enroll in Program p, then each course i |     |     |     |     |     |     |     | p requires |     |     |     |
| ------------------------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | ---------- | --- | --- | --- |
∈C
X
|     |     |     |     | N sec (i) | =   |     |     |     |     |     | (7) |
| --- | --- | --- | --- | --------- | --- | --- | --- | --- | --- | --- | --- |
S i⌉
|     |     |     |     |     | ⌈   |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
sections, ensuring that no section exceeds its capacity S i. Hence, department dept(i) must provide  X/S H i
|     |     |     |     |     |     |     |     |     |     | ⌈   | i ⌉× |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---- |
hours for course i.
Departmental Faculty Constraints. All faculty hours for course i must come from dept(i). Hence, each
department d must satisfy
|     |     |     |        | X   | H   |     | T         | ,   |     |     |     |
| --- | --- | --- | ------ | --- | --- | --- | --------- | --- | --- | --- | --- |
|     |     |     |        | Si  | i   |     | faculty,d |     |     |     |     |
|     |     |     |        | ×   |     | ≤   |           |     |     |     |     |
|     |     | i   |        | (⌈  | )   |     |           |     |     |     | (8) |
|     |     |     | ∑∈ C p | ⌉   |     |     |           |     |     |     |     |
dept(i)=d

where N (i)= X/S . Because Program p may involve multiple departments, all such inequalities (one per
| sec                                                                          |     | i   |     |     |     |     |     |     |     |     |     |
| ---------------------------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| department) must hold simultaneously for an admission size X to be feasible. | ⌈   | ⌉   |     |     |     |     |     |     |     |     |     |
Program’s Maximum Feasible Enrollment. The maximum number of students X that can be admitted under
departmental faculty constraints is the largest integer X for which (8) is satisfied across every department whose
| courses appear in  | p. Formally, |     |     |     |     |     |     |     |     |     |     |
| ------------------ | ------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
C
X
| maxX | such | that d | dept(i) | i    | p :            |     |     | H i | T faculty,d | .   |     |
| ---- | ---- | ------ | ------- | ---- | -------------- | --- | --- | --- | ----------- | --- | --- |
|      |      | ∀      | ∈{      | | ∈C | }              |     | S i | ×   | ≤           |     | (9) |
|      |      |        |         |      | i:de∑pt(i)=d(⌈ |     | ⌉   | )   |             |     |     |
Because a program’s courses may span multiple departments, all such constraints must hold to admit X
students. For instance, suppose program p draws upon Department 1 and Department 2. Let Department 1
have T =60 hours available, with two courses: Course A (dept(A)=1, S =30, H =3) and
| faculty,1 |     |     |     |     |     |     |     |     | A   | A   |     |
| --------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Course B (dept(B)=1, S =20, H =4). Let Department 2 have T =36 hours and offer Course
|     |     | B   | B   |     |     |     | faculty,2 |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --------- | --- | --- | --- | --- |
C (dept(C)=2, S =40, H =6). For X students, we need  X/30 X/20
|     | C   | C    |     |     |     |     |  sections of A and  |     |     |     |  sections  |
| --- | --- | ---- | --- | --- | --- | --- | ------------------- | --- | --- | --- | ---------- |
|     |     | X/40 |     |     |     | ⌈   | ⌉                   |     |     | ⌈ ⌉ |            |
of B in Department 1, and   sections of C in Department 2. The total load in Department 1 is
X/30 3 + X/20 4, which must not exceed 60, while the load in Department 2 is  ⌈ ⌉ X/40 6,
⌈ capped at 36. If X ⌉× ⌈ =40, then  ⌉× 40/30 =2 sections of A (2 40/20 =2 sections of B (2 ⌈ ⌉×
3=6 hours) plus
4=8 hours), for a total of 6+8=14 hours in Department 1, which is feasible since 14 ⌈ ⌉ × ⌈ ⌉ ×
60. Department 2
| 40/40                                                                                                           | =1 section of C (1 |     |                                   |     |     |     | 36. Thus, X | =40 is within capacity; one  | ≤   |     |     |
| --------------------------------------------------------------------------------------------------------------- | ------------------ | --- | --------------------------------- | --- | --- | --- | ----------- | ---------------------------- | --- | --- | --- |
| runs                                                                                                            |                    |     | 6=6 hours), also feasible since 6 |     |     |     |             |                              |     |     |     |
| can increment X further until either department’s limit is exceeded, thereby finding the program’s maximum  ⌈ ⌉ |                    |     | ×                                 |     |     | ≤   |             |                              |     |     |     |
feasible enrollment.
Utilization Metric. To measure how effectively each department’s teaching resources are used, define
|     |     |           | Total | Hours     | Used in | Dept. | d   |        |     |     |      |
| --- | --- | --------- | ----- | --------- | ------- | ----- | --- | ------ | --- | --- | ---- |
|     |     | U         | =     |           |         |       |     | 100%.  |     |     | (10) |
|     |     | faculty,d |       | T         |         |       | ×   |        |     |     |      |
|     |     |           |       | faculty,d |         |       |     |        |     |     |      |
A high U faculty,d (close to or above 100%) indicates potential overload of department d, while a low value
suggests that the department might be underutilized or could accommodate more students. By enforcing
|     |       | X/S | i H i | T faculty,d | for | every | involved | department |     | d,  |      |
| --- | ----- | --- | ----- | ----------- | --- | ----- | -------- | ---------- | --- | --- | ---- |
|     |       | ⌈   | ⌉×    | ≤           |     |       |          |            |     |     |      |
| i   |       |     |       |             |     |       |          |            |     |     | (11) |
|     | ∑∈C p | (   |       | )           |     |       |          |            |     |     |      |
dept(i)=d

the institution ensures that no department is inadvertently overloaded by cross-departmental demands. This
multi-department approach, unlike simpler models that compute capacity for each program in isolation
[e.g6], prevents one heavily demanded department from becoming a hidden bottleneck, while also revealing
underutilized areas that might expand enrollment. Such a holistic perspective allows decision-makers to set
accurate, equitable admission targets that reflect the true distribution of faculty resources.
Soft constraints
In contrast to hard constraints—which enforce non-negotiable limits based on physical resources or operational
capacities—soft constraints provide a flexible mechanism for integrating a wide range of institutional objectives
and policy-driven goals into the admissions process. The proposed framework is designed to accommodate
not only the common constraints discussed below (e.g., academic performance metrics, resource allocation
preferences, and government-imposed policies) but also additional criteria as needed. For instance, institutions
5
Scientific Reports |        (2025) 15:39756  | https://doi.org/10.1038/s41598-025-23116-6

www.nature.com/scientificreports/
may incorporate measures such as student satisfaction, retention rates, extracurricular balance, demographic
equity, or regional representation. In what follows, we detail the general formulation for the soft constraints and
their integration.
General formulation and examples
We encode each soft constraint by introducing a penalty score that grows with the gap between actual outcomes
and the desired targets. During optimization, these penalty score steer the solution toward institutional priorities
and equity goals — without ever overriding the immutable hard constraints. Formally, each soft constraint is
represented by a penalty function:
|                                                                |     | P i(p) | = ω | i f | target(p),actual(p) |     | ,   |     | (12) |
| -------------------------------------------------------------- | --- | ------ | --- | --- | ------------------- | --- | --- | --- | ---- |
|                                                                |     |        |     | ×   |                     |     |     |     |      |
| where P i(p) is the penalty from constraint i for program p, ω |     |        |     | (   |                     |     | )   |     |      |
i is a weighting factor reflecting that constraint’s
relative importance, and f(, ) is a function measuring how far the program’s actual performance deviates from
| its target. Typically, f takes the form of a max |     | · · |     | 0,... |     |     |     |     |     |
| ------------------------------------------------ | --- | --- | --- | ----- | --- | --- | --- | --- | --- |
 expression to ensure no penalty is incurred when a
|     |     |     |     | {   | }   |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
program meets or exceeds the target. In what follows, we detail three representative soft constraints commonly
encountered in higher education admissions planning.
Example 1: Academic Performance (Graduation Rates) Academic performance metrics, such as graduation
rates, exemplify this framework. Let T (p) be the target graduation rate for program p, and A (p) the
|     |     |     | grad |     |     |     |     | grad |     |
| --- | --- | --- | ---- | --- | --- | --- | --- | ---- | --- |
actual rate. Using a deviation function,
|     | P           |     | (p) = | α max | 0,  | T (p) | A      | (p) ,  | (13) |
| --- | ----------- | --- | ----- | ----- | --- | ----- | ------ | ------ | ---- |
|     | performance |     |       | ×     | {   | grad  | − grad | }      |      |
we impose a penalty only when the actual graduation rate falls short of the target. The weighting factor α
determines how heavily to penalize shortfalls.
Example 2: Government-Imposed Policies Many institutions must comply with labor-market mandates or
government directives. Let R j(p) be the target metric (e.g., an employment-rate threshold) and M j(p) the
| measured or projected value. Summing over all such restrictions j |     |     |     |     |     | =1,...,J: |     |     |     |
| ----------------------------------------------------------------- | --- | --- | --- | --- | --- | --------- | --- | --- | --- |
J
|     |     | P policy (p) | =   | γ j | max 0, | R j(p) | M j(p) | .   | (14) |
| --- | --- | ------------ | --- | --- | ------ | ------ | ------ | --- | ---- |
|     |     |              |     | ×   | {      |        | −      | }   |      |
j=1
|                                                                            |     |     | ∑   |     |     |     |     |     |     |
| -------------------------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Programs falling below any required threshold incur a penalty, scaled by γ |     |     |     |     |     |     | j.  |     |     |
Example 3: Resource Allocation Preferences Finally, some institutions prefer to keep enrollments balanced
across programs. Suppose each program p admits S p students, and S¯ is the average across all programs. One can
penalize large deviations via
|                                                 |     |     | P        | (p) = | β   | S S¯     | .        |     | (15) |
| ----------------------------------------------- | --- | --- | -------- | ----- | --- | -------- | -------- | --- | ---- |
|                                                 |     |     | resource |       | ×   | p −      |          |     |      |
| S S¯ means the program is either over- or under |     |     |          |       |     | (cid:31) | (cid:31) |     |      |
High  p (cid:31)-subscrib (cid:31)ed, triggering an institutional penalty that
| | − | |     |     |     |     |     |     |     |     |     |
| ----- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
encourages rebalancing.
Aggregate soft constraint penalty
The overall soft constraint penalty for each program p is obtained by aggregating the penalties associated with
all individual soft constraints. Let   be the index set for all soft constraints incorporated into the model (e.g.,
I
academic performance, resource allocation, government-imposed policies, and any additional criteria). Then,
the aggregate soft penalty is defined as:
|     |     |     | P   | soft (p)= | P   | i(p). |     |     |      |
| --- | --- | --- | --- | --------- | --- | ----- | --- | --- | ---- |
|     |     |     |     |           |     |       |     |     | (16) |
|     |     |     |     |           | i   |       |     |     |      |
∑ ∈I
For example, if the model includes three soft constraints—graduation rates P (p), resource allocation
performance
preferences P (p), and government-imposed policies P (p)—the aggregate penalty becomes:
| resource |      |       |             |       |          | policy |        |       |      |
| -------- | ---- | ----- | ----------- | ----- | -------- | ------ | ------ | ----- | ---- |
|          | P    | (p)=P |             | (p)+P |          | (p)+P  |        | (p).  |      |
|          | soft |       | performance |       | resource |        | policy |       | (17) |
This formulation is inherently flexible and can easily be extended to incorporate additional soft constraints (such
as student retention rates or demographic balance) by adding corresponding penalty terms to the summation.
Minimizing P soft (p) across all programs thus ensures that the optimization process effectively balances
deviations from institutional targets, market needs, and other quality indicators.
Integration of hard and soft constraints
Our goal is to recommend an optimal admission number for each program that balances operational feasibility
(hard constraints) with strategic quality and market objectives (soft constraints). Specifically, we adjust the current
(baseline) admissions continuously according to each program’s degree of compliance with soft constraints.
Programs with low penalty scores (full compliance) are permitted to approach their maximum feasible number,
whereas those with high penalty scores are subject to reduction.
6
Scientific Reports |        (2025) 15:39756  | https://doi.org/10.1038/s41598-025-23116-6

www.nature.com/scientificreports/
Let S 0 represent the current or baseline admission number for program p, as dictated by the program’s actual
p
usage of available hard resources. The maximum feasible admission number based exclusively on these hard
| constraints is denoted by S |     | max. The ratio |     |     |     |     |     |     |     |
| --------------------------- | --- | -------------- | --- | --- | --- | --- | --- | --- | --- |
p
|     |     |     |     | Smax |     | S0  |     |     |      |
| --- | --- | --- | --- | ---- | --- | --- | --- | --- | ---- |
|     |     |     |     | δ =  | p − | p   |     |     | (18) |
|     |     |     |     | p    | S0  |     |     |     |      |
|     |     |     |     |      | p   |     |     |     |      |
then expresses the relative increase possible. For instance, if a program is currently operating at 80% of its hard-
0 max, the term δ
capacity limit, that is S p =0.8S p p evaluates to 0.25, which indicates admissions may be raised by
up to 25% of the current count before reaching full capacity.
We further define P soft (p) in equation 16 as the program’s aggregate penalty for soft constraints. Normalizing
| this penalty by a constant P |     | max (for example, the largest observed penalty) yields |     |     |     |     |     |     |     |
| ---------------------------- | --- | ------------------------------------------------------ | --- | --- | --- | --- | --- | --- | --- |
P (p)
|     |     |     |     | x = | so ft | ,   |     |     | (19) |
| --- | --- | --- | --- | --- | ----- | --- | --- | --- | ---- |
p
|     |     |     |     |     | P m ax |     |     |     |     |
| --- | --- | --- | --- | --- | ------ | --- | --- | --- | --- |
ensuring x [0,1]. Programs with low x p have minimal soft-constraint penalties, whereas those with x
p p
∈
closer to 1 are regarded as highly non-compliant and may see sharper reductions in admissions.
| Next, we define a continuous adjustment function, g(x |     |     |     |     |     | p)=1+δ |     | 2x                            |     |
| ----------------------------------------------------- | --- | --- | --- | --- | --- | ------ | --- | ----------------------------- | --- |
|                                                       |     |     |     |     |     |        | p(1 | p), that maps the normalized  |     |
| penalty x                                             |     |     |     |     |     |        | −   |                               |     |
p onto a multiplicative factor. The choice of this linear form is deliberate. Its primary advantage lies
in its simplicity and interpretability: it creates a direct, proportional relationship between a program’s non-
compliance penalty and its recommended admission adjustment. This straightforward mapping ensures that a
program halfway to the maximum penalty (x =0.5) receives no change, while those at the extremes (x
|     |     |     |     | p   |     |     |     |     | p =0  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ----- |
or x
p =1) receive the maximum possible increase or decrease, respectively. While other non-linear functions
could be employed—such as a sigmoid function for smoother transitions or a concave function to penalize
minor deviations more heavily—the linear model provides a balanced and easily understandable baseline for
iterative adjustments.
Accordingly, the recommended admission number for program p is given by:
P (p)
|     | S rec | =S 0 | g(x p)=S | 0 1+δ |     |     | soft  | .   |      |
| --- | ----- | ---- | -------- | ----- | --- | --- | ----- | --- | ---- |
|     | p     | p    |          | p     | p   | 1 2 |       |     | (20) |
|     |       |      | ·        |       |     | −   | P max |     |      |
|     |       |      |          | [     | (   | (   | ))]   |     |      |
This formulation yields three key outcomes depending on the value of x p. First, when x =0 (i.e., the program
p
is fully compliant), we have
|     |     |     | S rec | =S 0 | 1+δ | =S max,  |     |     | (21) |
| --- | --- | --- | ----- | ---- | --- | -------- | --- | --- | ---- |
|     |     |     | p     | p    | p   | p        |     |     |      |
|     |     |     |       | [    | ]   |          |     |     |      |
which means the program can safely increase its admissions to reach its hard-capacity limit. Second, if
x =0.5 (moderate non-compliance), then
p
|     |     |     | S rec =S | 0 1+δ | p(1 | 1) =S | 0,  |     | (22) |
| --- | --- | --- | -------- | ----- | --- | ----- | --- | --- | ---- |
|     |     |     | p        | p     | −   |       | p   |     |      |
|     |     |     |          | [     |     | ]     |     |     |      |
implying there is no recommended change from the baseline. Finally, with x p =1 (maximum non-compliance),
the system imposes
|     |     | S rec | =S 0 | 1+δ p(1 | 2)  | =S 0(1 | δ p),  |     |      |
| --- | --- | ----- | ---- | ------- | --- | ------ | ------ | --- | ---- |
|     |     | p     | p    |         |     | p      |        |     | (23) |
|     |     |       |      |         | −   |        | −      |     |      |
|     |     |       |      | [       | ]   |        |        |     |      |
thus reducing admissions below the current level to penalize severe deviations from soft-constraint objectives.
It is worth noting that the framework operates much like a warm-start optimization. Each cycle begins from
the baseline allocation Sp
, which reflects the current admissions state, and then makes proportional adjustments
0
using penalty scores. In this way, recommendations build on earlier solutions rather than being recalculated in
full, which helps improve computational efficiency and makes the process easier for administrators to follow.
In practice, this mechanism enables institutions to track incremental changes transparently while retaining the
efficiency benefits of warm-start optimization techniques.
Also, it is crucial to note how the framework handles programs that are already operating beyond their hard
capacity limits. In a scenario where the current admission number exceeds the maximum feasible limit (i.e.,
S 0 >S max), the term (S max S 0) becomes negative. Consequently, the adjustment formula will inherently
| p p | p   | −   | p   |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
recommend a reduction in admissions regardless of the program’s soft constraint performance, guiding it back
towards its non-negotiable capacity threshold. This ensures the system’s primary objective—adherence to hard
constraints—is always prioritized.
Thus, the final recommended admissions for each program is first calculated as:
|     |       |      |     | ma x | 0   |     |            |     |      |
| --- | ----- | ---- | --- | ---- | --- | --- | ---------- | --- | ---- |
|     |       |      |     | S p  | S p |     | P soft (p) |     |      |
|     | S rec | =S 0 | 1+  | −    |     | 1 2 |            | .   | (24) |
|     | p     | p    |     | S 0  |     | −   | P          |     |      |
|     |       |      | [ ( | p    | )(  | (   | max ))]    |     |      |
Finally, this recommended number is adjusted to enforce a minimum admission quota, M, ensuring that
|                                                                        |     |     |     |     |     |     | rec | rec). This continuous  |     |
| ---------------------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | ---------------------- | --- |
| no program falls below a baseline institutional threshold, such that S |     |     |     |     |     |     | p   | max(M,S p              |     |
←
adjustment mechanism ensures that the recommendation is dynamically aligned with the program’s compliance
7
Scientific Reports |        (2025) 15:39756  | https://doi.org/10.1038/s41598-025-23116-6

www.nature.com/scientificreports/
with soft constraints—rewarding those that are well-aligned and penalizing those that are less aligned, while
always remaining within the bounds set by the hard constraints.
To facilitate prioritization, we define a program’s compliance score as:
compliance p =1 − x p . (25)
Consequently, programs can be ranked in descending order of their compliance scores. A higher score indicates
better adherence to soft constraint objectives and justifies a higher recommended admission number (subject to
the hard resource limits). This ranking provides a quantitative basis for strategic admissions planning.
Algorithm 1. Two-phase admissions Algorithm: Hard constraints and penalty-based scaling.
Experimentation
We evaluated our admissions framework using a simulated dataset composed of 14 academic programs serving
a combined total of 29,100 students. The dataset was designed to capture both the variety and complexity of
constraints typically encountered in higher education. Next, we detail the setup and results of our experimentation.
Experimental setup
In generating the simulation, we began by distributing the 29,100 students unevenly across the 14 programs,
replicating real-world imbalances in popularity and resource usage. Each program was assigned a unique blend
of requirements, reflecting differences in credit hours, lab or lecture format, and baseline compliance with
institutional standards. To model capacity constraints, we sampled faculty loads and room availability from
realistic ranges, ensuring that some programs were already near (or over) their limits while others had significant
spare capacity.
Beyond hard constraints, we introduced three soft penalties (corresponding to the three soft constraints; we
simulate the target values according to actual statistics from the ministry of education and labor in Saudi Arabia)
by assigning each program specific performance targets (e.g., graduation rates), policy requirements (e.g., labor-
market alignment), and enrollment balance goals (e.g., deviation from the average). Some programs thus started
with negligible penalty scores, while others faced large penalties for underperforming across multiple criteria.
This mixture guaranteed a meaningful test of the system’s ability to reallocate enrollments effectively.
All approaches were implemented in Python 3.9, using standard libraries (NumPy, pandas, PuLP) for data
handling, matrix operations, and constraint satisfaction. Random seeds were fixed to ensure reproducibility of
the simulated data.
To benchmark our results, we compared our method against two baselines: (1) a Greedy approach43 that ranks
programs by a single performance metric (e.g., quality or priority) and allocates seats in descending order until
capacities are filled, and (2) Simulated Annealing44,45, a well-known metaheuristic widely used for combinatorial
optimization and Constraint Satisfaction Problems (CSPs). The Greedy method serves as a straightforward
baseline for seat allocation, while Simulated Annealing probabilistically explores seat distributions, allowing
occasional “uphill” moves to escape local minima. We evaluated each method on (a) the number of hard-
constraint violations, (b) an overall penalty score capturing the severity of any violated constraints, and (c) the
fairness of seat distribution across programs, measured by an equity metric, namely the Gini coefficient46.
These metrics enabled us to comprehensively assess each method’s adherence to capacity and staffing
constraints, its penalty for violating institutional and policy-driven preferences, and the fairness of its allocations.
Scientific Reports | (2025) 15:39756 | https://doi.org/10.1038/s41598-025-23116-6 8

www.nature.com/scientificreports/
In the following sections, we present and discuss our solution’s performance relative to these baseline and state-
of-the-art techniques, highlighting both quantitative gains and practical insights for institutional planning.
While the results are presented for one representative simulated environment to ensure clarity, the fixed random
seeds guarantee reproducibility. Furthermore, the statistical tests presented in the following sections (e.g.,
bootstrapping and ANOVA) provide confidence in the stability of our findings, which were consistent with
patterns observed across several preliminary generative runs.
Results
We begin by presenting the outcomes of our proposed approach, focusing on two key metrics: penalty score
(where a lower value indicates better compliance) and recommended changes in admission numbers to achieve
optimal allocation. Table 1 summarizes the performance of our approach across the 14 academic programs,
detailing how constraints influence the allocation process. As shown in the table, programs with zero penalty
scores receive an increase in the number of admitted students, ensuring that resources are fully utilized while
prioritizing compliant programs. However, these increases are bounded by the hard constraints cap for each
program, preventing overallocation beyond infrastructural and faculty limits.
To promote fairness and a gradual transition to compliance, our approach does not enforce abrupt reductions
for non-compliant programs but adjusts student numbers proportionally based on penalty severity. Colleges
with lower penalty scores receive slight increases in admissions, reinforcing equity by rewarding near-compliant
institutions. Conversely, programs with high penalty scores experience gradual reductions, ensuring that
resource allocation shifts do not disrupt the institutional ecosystem. By distributing reductions proportionally
rather than uniformly, the approach allows severely non-compliant programs to progressively adjust while
maintaining an equitable growth trajectory for those closer to full compliance. Figure 1(a) illustrates the actual
number of students recommended for the next year, reflecting the combined effect of graduation adjustments
and new admissions allocations.
In contrast, the Simulated Annealing (SA) method centers on minimizing the overall penalty score,
sometimes to the detriment of locally equitable student allocations. As depicted in Figure 1(b), SA can produce
sizeable increases in certain programs—notably Medicine, Applied Medical Sciences, and Sports Science—
while simultaneously enforcing substantial cuts in others, such as Computer Science, Law, and Education. This
pattern arises because SA, through exploring a wide range of potential seat distributions, prioritizes global
penalty reduction over proportional adjustments that reflect each program’s individual level of compliance.
Consequently, even fully compliant programs may not see enrollment rises commensurate with their strong
performance if doing so fails to reduce the system-wide penalty, whereas other programs may receive large
enrollment boosts despite minimal or moderate violations.
The third algorithm in our comparison is the Greedy approach (Fig. 1 (c)), which focuses on a single
constraint at a time rather than weighing all constraints holistically. As a result, locally optimal choices can
lead to suboptimal outcomes once the remaining constraints are considered. For instance, the Greedy method
allocates more students to Computer Science and Social Science because they appear compliant with the specific
constraint it evaluates initially, even though both programs violate several other constraints under a broader
assessment. In contrast, programs that are compliant across most measures may receive large cuts under Greedy,
simply because the available “quota” was already consumed by programs flagged as non-violative for the single
constraint in focus, thereby overlooking their broader compliance record.
To assess the equity of enrollment recommendations across the three methods, we calculated the Gini
coefficient using the standard formula:
n
2 ix i n+1
G= i=1 ,
n n x − n
|     | ∑i=1 | i   |
| --- | ---- | --- |
∑
 Program
|                         | Penalty Score Change in Admission (%) | Status    |
| ----------------------- | ------------------------------------- | --------- |
| Applied Medical Science | 25 −2.18%                             | Violated  |
| Engineering             | 25 −2.16%                             | Violated  |
| Computer Science        | 10 2.64%                              | Violated  |
| Business                | 25 −3.48%                             | Violated  |
| Social Sciences         | 10 2.08%                              | Violated  |
| Law                     | 25 −1.78%                             | Violated  |
| Languages               | 30 −5.88%                             | Violated  |
| Education               | 25 −1.29%                             | Violated  |
| Sciences                | 25 −2.55%                             | Violated  |
| Design and Arts         | 25 −2.86%                             | Violated  |
| Applied Studies         | 25 −3.18%                             | Violated  |
| Humanities              | 10 2.35%                              | Violated  |
| Medicine                | 0 22.50%                              | Committed |
| Sports Science          | 0 53.12%                              | Committed |
Table 1. Summary of our method’s performance across programs.
9
Scientific Reports |        (2025) 15:39756  | https://doi.org/10.1038/s41598-025-23116-6

www.nature.com/scientificreports/
Fig. 1. Comparison of student allocations across different approaches.
Fig. 2. Comparison of Gini Coefficients Across Methods. A lower coefficient indicates a more equitable
distribution of the recommended enrollments. Our method exhibits the smallest Gini value (0.067), signifying
superior fairness compared to the Simulated Annealing and Greedy algorithms (0.293 and 0.387, respectively).
where x 1 ,x 2 ,...,x n are the sorted enrollment allocations and n=14 is the number of programs. Our
recommender system achieved the lowest Gini coefficient, 0.067, indicating the most equitable distribution of
students. By contrast, Simulated Annealing and Greedy resulted in substantially higher coefficients of 0.293 and
0.387, respectively. Using a bootstrap resampling approach with 10,000 iterations, we found that the differences
between our method’s Gini coefficient and those of the other two approaches were statistically significant at the
p <0.01 level. As illustrated in Fig. 2, these results suggest that our recommender not only meets key constraints
Scientific Reports | (2025) 15:39756 | https://doi.org/10.1038/s41598-025-23116-6 10

www.nature.com/scientificreports/
Fig. 3. Average Utilization of Hard Constraints Across Five Iterative Admission Cycles. Our recommender
method prevents resource underutilization more effectively than Simulated Annealing or Greedy, reflecting a
superior balance between compliance and capacity usage.
Method Avg. Time to Full Compliance (Yrs) Notes
Our Recommender 4.2 Balances gradual reduction and avoids new violations.
Simulated Annealing 6.2 Minimizes penalties each year but reintroduces local infractions.
Greedy 7.6 Slowest due to its sequential, single-constraint approach.
Table 2. Average Time (Years) to Eliminate Violations Over Five Admission Cycles.
but also more uniformly distributes enrollments across programs, thereby facilitating fairer and more informed
decisions for the upcoming academic year.
Convergence over time
While rapid violation reduction can seem beneficial, highly aggressive cuts risk underutilizing essential resources
(e.g., classrooms, faculty). In contrast, our recommender advocates moderate, incremental changes that preserve
near-optimal usage of available capacity. To evaluate how each method balances compliance with efficient use of
institutional resources, we conducted a multi-year simulation in which each algorithm’s recommendations for
one year inform the next year’s baseline. Concretely, we first run the algorithm to determine the optimal number
of students for the upcoming academic cycle. Once these recommendations are set, we use them as the starting
point for the following year, repeating the same procedure. Through this iterative process, we capture the long-
term trajectory each approach induces.
Figure 3 shows how effectively the three methods preserve hard constraints (e.g., classroom capacity, faculty
workload) across five consecutive admission cycles. Our recommender consistently achieves utilization levels of
85–90% of the maximum capacity, thus avoiding both over-allocation and chronic underutilization. By contrast,
≈
Simulated Annealing (SA) ranges between 50% and 75%, reflecting its focus on overall penalty minimization,
which can lead to substantial under-allocation in certain programs. The Greedy algorithm remains closer to 60%
utilization, indicating that it often discards capacity prematurely in favor of locally optimal steps.
An ANOVA test (F=9.72, p<0.01) on the average utilization rates confirms statistically significant differences
among the methods. Post-hoc Tukey tests reveal that our recommender maintains a distinctly higher (p<0.01)
utilization rate compared to both SA and Greedy. Hence, although other methods may appear to reduce
violations more quickly in certain cycles, they risk admitting too few students, thereby leaving valuable university
resources idle. In contrast, our recommender systematically ensures each program is sufficiently filled without
exceeding capacity, allowing institutions to fully leverage their infrastructure and faculty while still advancing
toward compliance targets.
We also conducted a ten-year simulation to examine how quickly each approach eliminates penalties across
all programs, assuming no new violations occur. As shown in Table 2, our recommender achieves full compliance
in an average of 4.2 years, balancing steady penalty reductions with minimal new infractions. By contrast,
Simulated Annealing (SA) attains notably low penalties each year, but its strong focus on global minimization
reintroduces local violations in previously near-compliant programs, preventing a zero-violation state across the
system. Meanwhile, the Greedy method proves slowest overall: its sequential, single-constraint emphasis causes
it to address additional penalties only once the dominant constraint has been satisfied, taking longer than five
years in some scenarios.
The findings presented across all experiments underscore the strengths of our recommender system,
particularly in balancing the need for prompt violation reduction with efficient resource utilization and long-
term stability. While Simulated Annealing and Greedy each show certain advantages—for instance, rapidly
diminishing penalties in isolated cycles or meeting a single dominant constraint—they fail to maintain sustainable
compliance or avoid undue underutilization of university capacity. By contrast, our recommender consistently
achieves a robust blend of fairness, capacity preservation, and effective multi-year violation management. In the
Scientific Reports | (2025) 15:39756 | https://doi.org/10.1038/s41598-025-23116-6 11

www.nature.com/scientificreports/
following section, we further contextualize these outcomes, highlighting the practical implications for higher
education institutions and potential avenues for improvement and future research.
Discussion
In admissions planning, universities have often turned to goal programming and static linear models to manage
competing objectives. These methods are rigorous; however, each time the constraints shift the problem has
to be solved again from scratch. That makes them less useful in settings where quotas, staffing, or facilities can
shift quickly. Our equity-aware recommender takes a different approach. It introduces incremental, year-to-year
adjustments through compliance penalties, much like a warm-start process. This approach cuts down on repeated
computation while still preserving a high level of compliance and fairness. As shown in our simulations, the
framework consistently sustains 85–90% utilization of available capacity and reduces violations more steadily
over time than static goal programming or heuristic baselines such as Greedy and Simulated Annealing.
We acknowledge that traditional optimization methods, such as goal programming, can be adapted to
dynamic environments by re-solving the problem with updated constraints or by adding regularization
terms to penalize drastic changes in enrollment plans. However, our iterative, penalty-based framework
offers complementary advantages. It is often more intuitive for institutional administrators to interpret, as the
adjustments are directly tied to transparent performance metrics. Furthermore, it can be computationally lighter
than re-solving a complex optimization model from scratch each cycle, offering a practical and agile solution for
real-time decision support.
Equity considerations feature prominently in our allocation logic, ensuring no department or program is
permanently excluded from admissions. Rather than shutting out partially compliant departments, the system
provides them with controlled enrollments once fully compliant programs reach their limits. This strategy
resonates with equity theory, which emphasizes distributing resources in a manner that prevents any single
group from facing prolonged disadvantage. Empirically, our calculations (including low Gini coefficients) verify
that allocations generated by our approach are more evenly distributed than those of SA or Greedy. Simulated
Annealing, though adept at cutting global penalties, can repeatedly induce local infractions in programs that
were close to compliance, while Greedy addresses pressing constraints in isolation, leaving other programs to
lag behind.
It is worth noting that our SA implementation serves as a standard benchmark for penalty minimization in
CSPs. We concede that a more direct comparison could be achieved by modifying the SA objective function
to explicitly incorporate fairness and stability goals, and we consider the development of such a custom-tuned
baseline a valuable direction for future comparative work. In contexts like Saudi Arabia—where government-
funded, tuition-free education adds further complexity to balancing capacity and access, where the ability to
include partially compliant programs without idling vacant seats is particularly advantageous2,3. By allowing
modest enrollment for these programs, the framework fosters incremental improvement while making full use
of institutional resources. This measured yet inclusive approach promotes long-term institutional development,
as it permits a broad range of programs to move steadily toward higher compliance.
Our framework introduces fairness by drawing on equity theory and using proportional seat adjustments, so
that no program is left consistently disadvantaged. This stands in contrast to stable matching approaches, which
focus on incentive compatibility—ensuring that no stakeholder wants to deviate from the outcome. Stability is
a strong guarantee when individual preferences drive markets, but public university admissions often give more
weight to meeting capacity limits and policy requirements than to alternative choice. In practice, stable matching
can also impose rigid rules that make it harder to admit programs that nearly meet the criteria, leading to unused
resources. For this reason, we adopt equity-based fairness as a more practical tool for dynamic seat planning. At
the same time, stable matching offers a useful perspective, and adapting ideas such as deferred acceptance could
improve robustness in the long run.
An important advantage of our equity-based algorithm is that its recommendations implicitly account for
natural enrollment dynamics, including the gradual graduation of students. As shown in Fig. 1, other methods
often pursue minimum penalties by advising drastic reductions for programs with high violation scores;
however, this can be impractical since universities remain responsible for students already enrolled. Abruptly
halving or eliminating seats in the next academic cycle could negatively impact ongoing cohorts, conflicting
with institutional policies and realistic planning horizons. In contrast, our framework’s partial allowance for
underperforming or partially compliant programs moderates such steep declines, resulting in more feasible
recommendations that better reflect day-to-day operational constraints. Rather than advocating overly aggressive
targets, the equity-aware model facilitates gradual, stepwise adjustments over multiple years. This approach not
only curtails disruption for existing students and faculty but also provides administrators with a structured path
to align enrollments with institutional goals without sacrificing educational continuity.
A deeper look at short-term gains versus enduring stability reveals the importance of a tempered approach.
While Simulated Annealing can achieve low aggregate penalties quickly, its stochastic reassignments often
cause previously near-compliant programs to oscillate back into violation. To analyze the robustness of our own
approach, we conducted a one-factor-at-a-time (OFAT) sensitivity analysis on the annual reduction rate, with
the results shown in Table 3. The analysis confirms that moderate annual reductions of 10%−20% significantly
improve both hard and soft constraint adherence without spawning unforeseen violations elsewhere. This
balanced trajectory is vital in real academic environments, where precipitous cuts in admissions can disrupt
departmental planning and budgeting. Accordingly, our approach’s stable readjustment paradigm seems better
suited to sustained institutional health.
We use the Gini coefficient as the main fairness indicator because it is easy to interpret, widely applied in
inequality studies, and allows direct comparisons across programs. Fairness, however, has many dimensions.
Other indices—such as entropy, Hoover, or Theil—highlight different kinds of distributional imbalance. In some
Scientific Reports | (2025) 15:39756 | https://doi.org/10.1038/s41598-025-23116-6 12

www.nature.com/scientificreports/
Reduction (%/Yr) Hard Compliance (%) Soft Compliance (%) Total Improvement (%)
5% 10 5 7.5
10% 20 15 17.5
15% 35 25 30
20% 50 35 42.5
25% 70 50 60
Table 3. Sensitivity analysis of admission reductions.
Strategy Min Time (Yrs) Max Time (Yrs) Avg Time (Yrs)
Large Reduction 1.4 5.2 3.3
Gradual Reduction 2 6.2 4.2
Table 4. Reduction strategy. Min Time (Yrs): Minimum time required for compliance. Max Time (Yrs):
Maximum time required for compliance. Avg Time (Yrs): Average time required for compliance.
early experiments (not included here), these alternative measures showed patterns similar to the Gini-based
results, which gives us confidence in our findings. Even so, a fuller evaluation across multiple indices could bring
out trade-offs between competing notions of equity. We therefore acknowledge that while Gini provides a clear
starting point, future work should adopt a broader suite of fairness measures to strengthen robustness.
Observing multi-year simulations further highlights divergent strategies for tackling ongoing constraints.
SA may look attractive due to its capacity to minimize penalties early in each cycle, but it frequently under-
enrolls certain programs and allows fresh infractions to arise over time. Greedy’s single-constraint approach
resolves dominant issues but lags in addressing secondary or tertiary constraints, dragging out the timeline to
full compliance. By contrast, our recommender continually updates program capacities and reassigns students
methodically, yielding a consistent pattern of improvement. When dealing with severely non-compliant
departments, more decisive “Large Reduction” tactics can achieve compliance within seven years, though at
the cost of immediate operational shifts. Alternatively, the “Gradual Reduction” strategy extends the process
to a decade yet eases the transition for programs unprepared for sudden changes (Table 4). This flexibility to
accelerate or decelerate the pace of reform aligns closely with the reality that universities vary in their tolerance for
enrollment swings and resource reallocation. Thus, the algorithm provides a practical toolkit for administrators
who must weigh the benefits of swift compliance against potential disruptions to staffing and budgets.
Our simulations show that the system typically converges to full compliance within about four admission
cycles when moderate adjustment strategies are used. This outcome gives practical evidence of stability
and robustness. At the same time, there is scope for deeper theoretical grounding. Recent work in dynamic
optimization and neural dynamics (e.g47–49]) has established finite-time convergence and stability for time-
varying quadratic programs. Our current penalty-based approach was designed to keep the process clear and
straightforward for administrators. Future work could make use of more advanced models. These would build
on the stability we already observe in practice and, at the same time, provide stronger theoretical guarantees of
optimality as institutional constraints evolve.
Notwithstanding these gains, certain limitations merit attention. Our experiments rely on simulated data
designed to mimic real-world enrollment trends, but genuine institutional environments are often more
complex. While this simulation-driven approach is instructive, large-scale field trials would offer a stronger
measure of how the algorithm handles the fine-grained distinctions that emerge between different departments
or campuses17. Another concern is that our penalty-based soft constraints presume relatively stable policy
objectives, yet external mandates—such as new government directives or evolving accreditation criteria—can
shift rapidly3. Incorporating adaptive or machine learning elements could enable near real-time recalibrations
to the penalty structure, enhancing the algorithm’s resilience12. Additionally, the potential for multi-campus or
cross-institutional applications remains largely untested; integrating resource-sharing mechanisms or parallel
constraint-solvers may be pivotal for scaling up in large or distributed university networks10. Despite these
limitations, the current results affirm that our solution offers both practical and theoretical benefits, positioning
it as a viable option for institutions seeking a more nuanced admissions strategy.
In our sensitivity analysis, we looked at annual reduction ratios. The results showed that moderate cuts of
about 10–20% improved compliance without upsetting the overall allocations. However, this one-factor-at-a-
time approach overlooks many other parameters that could impact robustness. Other factors—such as weighting
coefficients in the penalty functions, the design of minimum admission quotas, and alternative formulations
of soft-constraint penalties—could also significantly affect stability and fairness. We therefore note that the
present sensitivity analysis should be viewed as a baseline demonstration. Looking ahead, it will be beneficial to
explore the parameter space in a more detailed and multi-factorial way. Doing so could give stronger evidence
of robustness across different institutional settings.
Lastly, this study underscores the potential for a goal-oriented recommender system that balances
infrastructural limits, academic quality metrics, and fairness principles. In settings like Saudi Arabia—where
free tuition and centralized mandates require a careful mix of access and resource rationing—an algorithmic
Scientific Reports | (2025) 15:39756 | https://doi.org/10.1038/s41598-025-23116-6 13

www.nature.com/scientificreports/
approach that aligns with these complex dynamics can greatly enhance admissions planning. Contrasting our
method with Simulated Annealing and Greedy highlights how single-minded emphasis on global penalty
reduction or stepwise constraint satisfaction risks leaving valuable resources unused or repeatedly reintroducing
local violations. By examining all constraints in tandem and providing an equitable seat distribution, our
framework maintains enough flexibility to adapt to institutional needs—whether that entails a quick convergence
strategy or a protracted, more measured realignment process. Future developments should test these insights
in actual campus environments, refine penalty structures based on machine learning predictions of program
compliance, and consider how multi-institution collaboration might further optimize resource usage. In so
doing, universities can ensure that a data-driven, policy-aware admissions tool continues to evolve in step with
the rapidly changing landscape of higher education, enabling them to sustain fairness, efficiency, and academic
excellence.
Conclusion
This study presented a recommender system for student admissions that integrates hard constraints (e.g.,
classroom capacity and faculty loads) and soft constraints (such as academic performance targets, policy
requirements, and equity considerations) into a unified optimization framework. Through iterative refinements
and penalty-based allocation, the system maintains near-complete compliance with operational thresholds
while significantly reducing soft-constraint penalties, surpassing existing baselines by over 50%. In so doing,
it balances capacity utilization against equity objectives, offering partially compliant programs controlled
admissions without unduly disadvantaging fully compliant ones.
A multi-year convergence analysis showed that institutions can achieve full compliance in approximately
three to four years, particularly when combining rapid cuts for severe infractions with more incremental
strategies for moderate issues. Sensitivity tests further revealed that moderate annual enrollment reductions
(around 10%–20%) yield notable improvements in compliance while avoiding the instability often introduced by
more aggressive plans. These findings affirm that the system is both robust and adaptable, allowing institutions
to customize reduction levels in line with strategic, operational, or regulatory needs.
Despite these strengths, reliance on simulated data calls for additional real-world validation, especially in
contexts where institutional constraints and policy shifts evolve dynamically. Future enhancements might include
machine learning for predictive analytics and adaptive penalty weighting, further refining responsiveness and
accuracy. Investigating applications in multi-campus networks or collaborative institutional settings would also
broaden the framework’s utility.
Overall, the proposed system offers a flexible, equitable, and resource-efficient approach to higher education
admissions. By reconciling institutional priorities with government directives in a single optimization process,
it fosters sustainable long-term admissions planning that aligns educational quality standards with the principle
of equitable access.
Data availability
Data is described within the manuscript.
Code availability
The complete source code, including data-generation scripts, will be made available by the corresponding
author upon reasonable request following publication.
Received: 21 May 2025; Accepted: 3 October 2025
References
1. Altbach, P. G., Reisberg, L. & Rumbley, L. E. Trends in Global Higher Education: Tracking an Academic Revolution (UNESCO,
2009). https://unesdoc.unesco.org/ark:/48223/pf0000183219
2. UNESCO: The world needs almost 69 million new teachers to reach the 2030 education goals. h t t p s : / / un e s d o c . u n es c o . o r g / a rk : / 4 8
2 2 3 / pf 0 0 0 0 2 4 6 1 24 (2016)
3. McKinsey, Company: Reimagining higher education. h t t p s : / / w w w . m c k i ns e y . c o m / in d u s t r i e s/ e d u c a t i o n / o u r - i n s i g h t s / r e i ma g i n i n
g - hi g h e r - e d uc a t i o n - i n - t h e - u n i t ed - s t a t e s # / (2020).
4. DiBiase, D. The impact of increasing enrollment on faculty workload and student satisfaction over time. Journal of Asynchronous
Learning Networks 8(2), 45–60 (2004).
5. Watts, J. & Robertson, N. Burnout in university teaching staff: A systematic literature review. Educational Research 53(1), 33–50
(2011).
6. Beyrouthy, C. et al. Towards improving the utilization of university teaching space. Journal of the Operational Research Society
60(1), 130–143 (2009).
7. Heller, D. E. The effects of tuition and state financial aid on public college enrollment. Review of Higher Education 23(1), 65–89
(2001).
8. Brynjolfsson, E. & McAfee, A. The Second Machine Age: Work. Progress, and Prosperity in a Time of Brilliant Technologies. W.W.
Norton & Company. https://wwnorton.com/books/the-second-machine-age/ (2014).
9. Pal, B. B., Kumar, M. & Sen, S. A priority-based goal programming method for solving academic personnel planning problems
with interval-valued resource goals in university management system. Int. J. Appl. Manag. Sci. 4 (3), 284–312 (2012).
10. Ehlers, U.-D. Emerging Open-learning Cultures: Transforming Higher Education (Springer, 2013). h t t ps : / / l i n k. s p r i n g e r . c o m / c h a pt e
r / 1 0 . 1 0 0 7 / 9 7 8 - 3 - 6 4 2 - 3 8 1 7 4 - 4
11. Maulana, A. et al. Optimizing university admissions: a machine learning perspective. J. Educ. Manag. Learn. 1 (1), 1–7 (2023).
12. Shilbayeh, S. & Abonamah, A. Predicting student enrollments and attrition patterns in higher educational institutions using
machine learning. Int. Arab J. Inf. Technol. 18 (4), 562–567 (2021).
13. Minton, S., Johnston, M. D., Philips, A. B. & Laird, P. Minimizing conflicts: A heuristic repair method for constraint satisfaction
and scheduling problems. In: Artificial Intelligence Elsevier, (1992). https://doi.org/10.1016/0004-3702(92)90007-K.
Scientific Reports | (2025) 15:39756 | https://doi.org/10.1038/s41598-025-23116-6 14

www.nature.com/scientificreports/
14. Adams, J. S. Towards an understanding of inequity. The journal of abnormal and social psychology 67(5), 422 (1963).
15. Wilkinson, R., Taylor, J. S., Peterson, A. & Machado-Taylor, M. d. L. A practical guide to strategic enrollment management
planning. Online Submission (2007).
16. Hossler, D. & Kalsbeek, D. Enrollment management and managing enrollments: Revisiting the context for institutional strategy
Strategic Enrollment Management Quarterly (2013).
17. Maldonado, E. & Seehusen, V. Data mining student choices. J. Educ. Bus. 93 (5), 196–203 (2018).
18. Ignizio, J. P. Generalized goal programming an overview. Comput. Oper. Res. (1976)
19. Tamiz, M., Jones, D. F. & El-Darzi, E. A review of goal programming and its applications. Ann. Oper. Res. 58 (1), 39–53 (1995).
20. Chatterjee, S. & Bhattacharjee, K. K. Adoption of artificial intelligence in higher education. Educ. Inform. Technol. 25(5), 3443–
3463 (2020).
21. Koksalan, M. & Wallenius, J. Multiple criteria decision making in resource allocation problems. Operations Research 59(5), 1302–
1308 (2011).
22. Zeleny, M. Multiple criteria decision making. Operations Research 30(5), 1109–1110 (1982).
23. Wang, J., Wang, D. & Li, A. Goal programming and its variants. In Encyclopedia of Decision Making and Decision Support
Technologies 410–417 (2008)
24. Dechter, R. Constraint Processing. Morgan Kaufmann. https://doi.org/10.5555/861293 (2003).
25. Russell, S. & Norvig, P. Artificial intelligence: A modern approach. Pearson (2020).
26. Garey, M. R. & Johnson, D. S. Computers and intractability: A guide to the theory of np-completeness (Freeman, 1979).
27. Haralick, R. M. & Elliott, G. L. Increasing tree search efficiency for constraint satisfaction problems. Artificial Intelligence 14(3),
263–313 (1980).
28. Jin, L., Li, S., Liao, B. & Zhang, Z. Zeroing neural networks: A survey. Neurocomputing 267, 597–604 (2017).
29. Xiao, L. et al. Design and comprehensive analysis of a noise-tolerant znn model with limited-time convergence for time-dependent
nonlinear minimization. IEEE Transactions on Neural Networks and Learning Systems 31(12), 5339–5348 (2020).
30. Xiao, L., Li, K. & Duan, M. Computing time-varying quadratic optimization with finite-time convergence and noise tolerance:
A unified framework for zeroing neural network. IEEE transactions on neural networks and learning systems 30(11), 3360–3369
(2019).
31. Liao, B., Zhang, Y. & Jin, L. Taylor discretization of znn models for dynamic equality-constrained quadratic programming with
application to manipulators. IEEE transactions on neural networks and learning systems 27(2), 225–237 (2015).
32. Xiao, L., Tan, H., Jia, L., Dai, J. & Zhang, Y. New error function designs for finite-time znn models with application to dynamic
matrix inversion. Neurocomputing 402, 395–408 (2020).
33. Adams, J. S. Inequity in social exchange. In Advances in Experimental Social Psychology Vol. 2 (ed. Berkowitz, L.) 267–299
(Academic Press, 1965).
34. Burke, R. Multisided fairness for recommendation In: Proceedings of the Workshop on Responsible Recommendation at the 11th
ACM Conference on Recommender Systems (RecSys). ACM, New York, NY, USA, (2017).
35. Li, Y. et al. Fairness in recommendation: Foundations, methods, and applications. ACM Transact. Intell. Syst. Technol. 14 (5), 1–48
(2023).
36. Volery, T. & Lord, D. Critical success factors in online education. The International Journal of Educational Management 14(5),
216–223. https://doi.org/10.1108/09513540010344731 (2000).
37. Ricci, F., Rokach, L. & Shapira. B.: Introduction to Recommender Systems Handbook. Springer ??? h t t p s :/ / d o i . o r g /1 0 . 1 0 0 7 / 9 78 - 0 - 3
8 7 - 8 58 2 0 - 3 (2011).
38. Adomavicius, G. & Tuzhilin, A. Toward the next generation of recommender systems: A survey of the state-of-the-art and possible
extensions. IEEE Transactions on Knowledge and Data Engineering 17(6), 734–749 (2005).
39. Drachsler, H. et al. Issues and considerations regarding sharable data sets for recommender systems in technology enhanced
learning. Proced. Comput. Sci. 1 (2), 2849–2858 (2010).
40. Romero, C. & Ventura, S. Educational data mining: A review of the state of the art. IEEE Transactions on Systems, Man, and
Cybernetics 40(6), 601–618 (2010).
41. Deri, M. N., Singh, A., Zaazie, P. & Anandene, D. Leveraging artificial intelligence in higher educational institutions. Revista de
Educacion y Derecho (30) (2024).
42. Jeddah, U. Internal Academic Admissions Reports. Confidential Data (2023). https://uj.edu.sa
43. Cormen, T. H., Leiserson, C. E., Rivest, R. L. & Stein, C. Introduction to Algorithms 3rd edn. (MIT Press, 2009).
44. Kirkpatrick, S., Gelatt, C. D. & Vecchi, M. P. Optimization by simulated annealing. Science 220(4598), 671–680. h t t p s :/ / d o i . o r g /1 0
. 1 1 2 6 / s ci e n c e . 2 2 0 .4 5 9 8 . 6 7 1 (1983).
45. Černý, V. Thermodynamical approach to the traveling salesman problem: An efficient simulation algorithm. Journal of Optimization
Theory and Applications 45(1), 41–51. https://doi.org/10.1007/BF00940812 (1985).
46. Allison, P. D. Measures of inequality. American Sociological Review 43(6), 865–880. https://doi.org/10.2307/2094626 (1978).
47. Zeng, Y., Xiao, L., Li, K., Zuo, Q. & Li, K. Solving time-varying linear inequalities by finite-time convergent zeroing neural
networks. Journal of the Franklin Institute 357(12), 8137–8155 (2020).
48. Li, W., Xiao, L. & Liao, B. A finite-time convergent and noise-rejection recurrent neural network and its discretization for dynamic
nonlinear equations solving. IEEE Transactions on Cybernetics 50(7), 3195–3207 (2019).
49. Xiao, L., Cao, Y., Dai, J., Jia, L. & Tan, H. Finite-time and predefined-time convergence design for zeroing neural network: Theorem,
method, and verification. IEEE Transactions on Industrial Informatics 17(7), 4724–4732 (2020).
Acknowledgements
The authors would like to express their sincere appreciation to the University of Jeddah and to His Excellency
Prof. Adnan Humaidan, former President of the University, for his generous support and continuous guidance
that greatly contributed to the successful completion of this research.
Author contributions
Dr Ahmed conceived the main idea, designed the research methodology, and wrote the initial draft of the man-
uscript. Dr Alaa contributed to data collection, experimental execution. Prof Eesa conducted further refinement
of the methods and assisted with manuscript revisions. All authors reviewed and approved the final version of
the manuscript.
Declarations
Competing interests
The authors declare no competing interests.
Scientific Reports | (2025) 15:39756 | https://doi.org/10.1038/s41598-025-23116-6 15

www.nature.com/scientificreports/
Additional information
Correspondence and requests for materials should be addressed to A.I.
Reprints and permissions information is available at www.nature.com/reprints.
Publisher’s note Springer Nature remains neutral with regard to jurisdictional claims in published maps and
institutional affiliations.
Open Access This article is licensed under a Creative Commons Attribution-NonCommercial-NoDerivatives
4.0 International License, which permits any non-commercial use, sharing, distribution and reproduction in
any medium or format, as long as you give appropriate credit to the original author(s) and the source, provide
a link to the Creative Commons licence, and indicate if you modified the licensed material. You do not have
permission under this licence to share adapted material derived from this article or parts of it. The images or
other third party material in this article are included in the article’s Creative Commons licence, unless indicated
otherwise in a credit line to the material. If material is not included in the article’s Creative Commons licence
and your intended use is not permitted by statutory regulation or exceeds the permitted use, you will need to
obtain permission directly from the copyright holder. To view a copy of this licence, visit h t t p : / / c re a t i v e c o m mo
n s . o r g / l ic e n s e s / b y -n c - n d / 4 . 0 / .
© The Author(s) 2025
Scientific Reports | (2025) 15:39756 | https://doi.org/10.1038/s41598-025-23116-6 16