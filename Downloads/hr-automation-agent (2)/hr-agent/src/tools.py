"""
HR Automation Agent Tools
Covers 3 modules: Recruitment, Onboarding, HR Helpdesk
"""

from langchain_core.tools import tool


# ─────────────────────────────────────────
# MODULE 1: RECRUITMENT
# ─────────────────────────────────────────


@tool
def screen_resume(job_description: str, candidate_profile: str) -> str:
    """
    Screen and score a candidate's resume against a job description.
    Use this when the user wants to evaluate a candidate or check if
    someone is a good fit for a role.

    Args:
        job_description: The full job description or required skills/experience
        candidate_profile: The candidate's resume text or profile summary
    """
    # The LLM will perform the actual analysis via the agent prompt.
    # This tool structures the input so the agent processes it properly.
    return f"""
RESUME SCREENING REQUEST
========================
JOB DESCRIPTION:
{job_description}

CANDIDATE PROFILE:
{candidate_profile}

Please analyze the above and provide:
1. Overall Match Score (0-100)
2. Key Strengths (top 3)
3. Gaps or Concerns (top 3)
4. Shortlist Recommendation: YES / MAYBE / NO
5. One-line summary for the hiring manager
"""


@tool
def draft_interview_email(
    candidate_name: str,
    job_title: str,
    interview_date: str,
    interview_format: str,
    interviewer_name: str,
) -> str:
    """
    Draft a professional interview invitation email for a shortlisted candidate.
    Use this when the user wants to invite a candidate for an interview.

    Args:
        candidate_name: Full name of the candidate
        job_title: The role they applied for
        interview_date: Proposed date and time (e.g., 'Monday March 10 at 3:00 PM')
        interview_format: Format of interview (e.g., 'video call on Google Meet', 'in-person at our office')
        interviewer_name: Name of the interviewer or hiring manager
    """
    return f"""
DRAFT INTERVIEW INVITATION EMAIL
=================================
To: {candidate_name}
Subject: Interview Invitation – {job_title} Position

Dear {candidate_name},

Thank you for your application for the {job_title} position. We were impressed
with your profile and would like to invite you for an interview.

Interview Details:
- Date & Time: {interview_date}
- Format: {interview_format}
- Interviewer: {interviewer_name}

Please reply to confirm your availability or suggest an alternative time if needed.
We look forward to speaking with you!

Best regards,
{interviewer_name}
HR Team
"""


# ─────────────────────────────────────────
# MODULE 2: ONBOARDING
# ─────────────────────────────────────────


@tool
def generate_onboarding_checklist(
    employee_name: str, job_title: str, department: str, start_date: str
) -> str:
    """
    Generate a personalized onboarding checklist for a new hire.
    Use this when a new employee is joining or HR needs to prepare for a new hire.

    Args:
        employee_name: Full name of the new hire
        job_title: Their role/position
        department: The department they are joining
        start_date: Their first day of work
    """
    return f"""
ONBOARDING CHECKLIST FOR: {employee_name}
Role: {job_title} | Department: {department} | Start Date: {start_date}
========================================================================

PRE-ARRIVAL (Before {start_date}):
□ Send welcome email with first-day instructions
□ Set up workstation / laptop
□ Create company email account
□ Add to relevant Slack/Teams channels
□ Prepare access credentials (systems, tools)
□ Assign onboarding buddy

DAY 1:
□ Office/facility tour (or virtual welcome call)
□ Meet the team
□ Review company policies and code of conduct
□ Complete HR paperwork and documentation
□ Set up all required tools and software
□ Attend orientation session

WEEK 1:
□ Meet key stakeholders in {department}
□ Review role responsibilities and 30-60-90 day goals
□ Shadow team members on key workflows
□ Complete mandatory compliance training
□ 1:1 check-in with manager

FIRST MONTH:
□ Complete role-specific tool training
□ Attend first team meeting
□ Submit all required documents to HR
□ Set performance goals with manager
□ 30-day review check-in

Please customize this checklist based on company-specific tools and policies.
"""


@tool
def answer_onboarding_question(question: str, employee_role: str) -> str:
    """
    Answer common questions that new hires have during onboarding.
    Use this when a new employee asks about first-day procedures,
    company tools, policies, benefits, or general onboarding process.

    Args:
        question: The new hire's question
        employee_role: Their job title or role (for context)
    """
    return f"""
NEW HIRE ONBOARDING QUERY
==========================
Role: {employee_role}
Question: {question}

Please provide a clear, friendly, and helpful answer to this new hire's question.
Cover practical next steps they should take and who to contact if they need more help.
Keep the tone warm and welcoming — this person is new and may feel nervous.
"""


# ─────────────────────────────────────────
# MODULE 3: HR HELPDESK
# ─────────────────────────────────────────


@tool
def answer_hr_policy(question: str, employee_name: str = "Employee") -> str:
    """
    Answer HR policy questions about leave, payroll, benefits, working hours,
    reimbursements, performance reviews, or any company HR policy topic.
    Use this for general HR queries from employees.

    Args:
        question: The employee's HR policy question
        employee_name: Name of the employee asking (optional, defaults to 'Employee')
    """
    return f"""
HR POLICY QUERY
===============
From: {employee_name}
Question: {question}

Please provide a clear, professional answer to this HR policy question.
Include:
1. Direct answer to the question
2. Any important conditions or exceptions to note
3. Next steps the employee should take (if any)
4. Who they should contact for further clarification

Note: If the query requires access to personal employee records or
confidential data, advise them to contact HR directly.
"""


@tool
def escalate_issue(
    employee_name: str, issue_description: str, urgency_level: str
) -> str:
    """
    Escalate a complex or sensitive HR issue that cannot be resolved
    automatically. Use this for complaints, conflicts, legal concerns,
    serious policy violations, or any issue requiring human HR intervention.

    Args:
        employee_name: Name of the employee raising the issue
        issue_description: Full description of the problem or concern
        urgency_level: How urgent this is — 'low', 'medium', or 'high'
    """
    urgency_flags = {
        "high": "🔴 HIGH PRIORITY — Requires immediate HR attention",
        "medium": "🟡 MEDIUM PRIORITY — Review within 24 hours",
        "low": "🟢 LOW PRIORITY — Review within 3-5 business days",
    }
    flag = urgency_flags.get(urgency_level.lower(), "🟡 MEDIUM PRIORITY")

    return f"""
HR ESCALATION TICKET
=====================
{flag}

Raised By: {employee_name}
Urgency: {urgency_level.upper()}
Timestamp: Auto-generated on submission

Issue Description:
{issue_description}

─────────────────────────────────────
RECOMMENDED ACTIONS FOR HR TEAM:
1. Acknowledge receipt to {employee_name} within 2 hours
2. Assign a dedicated HR representative to this case
3. Schedule a private conversation with the employee
4. Review relevant company policies and documentation
5. Document all actions taken in the HR system
6. Follow up within the timeframe indicated above

This ticket was auto-generated by the HR Automation Agent.
Please handle with appropriate confidentiality.
"""


# ─────────────────────────────────────────
# MODULE 4: ADVANCED RECRUITMENT TOOLS
# ─────────────────────────────────────────


@tool
def compare_candidates(job_title: str, candidates_data: str) -> str:
    """
    Compare multiple candidates side by side for the same role and rank them.
    Use this when the user wants to evaluate and rank 2 or more candidates
    against each other for a position.

    Args:
        job_title: The role all candidates are applying for
        candidates_data: Details of all candidates separated clearly.
    """
    return f"""
CANDIDATE COMPARISON REQUEST
=============================
Role: {job_title}

Candidates:
{candidates_data}

Please provide:
1. COMPARISON TABLE with columns: Name | Experience Score (0-10) | Skills Match (0-10) | Leadership (0-10) | Overall Score (0-100) | Recommendation
2. FINAL RANKING — rank all candidates best to least suitable with one-line reason each
3. TOP PICK — who is the best candidate and why (2-3 sentences)
4. INTERVIEW PRIORITY ORDER — suggested order to interview them

Be objective, data-driven, and decisive.
"""


@tool
def bulk_interview_emails(
    job_title: str,
    interview_date: str,
    interview_format: str,
    interviewer_name: str,
    candidates_list: str,
) -> str:
    """
    Generate personalized interview invitation emails for multiple candidates at once.
    Use this when the user wants to send interview invites to several shortlisted candidates.

    Args:
        job_title: The role candidates applied for
        interview_date: Interview date or week (e.g. 'Week of March 10')
        interview_format: How interview will be conducted (e.g. 'Google Meet video call')
        interviewer_name: Name of the HR contact or interviewer
        candidates_list: Comma-separated candidate names e.g. 'John Doe, Sara Khan, Rahul Verma'
    """
    candidates = [c.strip() for c in candidates_list.split(",") if c.strip()]
    candidates_formatted = "\n".join(
        [f"  {i+1}. {name}" for i, name in enumerate(candidates)]
    )
    return f"""
BULK INTERVIEW EMAIL GENERATION
================================
Role: {job_title}
Total Candidates: {len(candidates)}
Interview: {interview_date} via {interview_format}
Interviewer: {interviewer_name}

Candidates:
{candidates_formatted}

Generate a separate personalized interview invitation email for EACH candidate above.
For each:
- Warm greeting using their name
- Mention the {job_title} role
- Include interview details: {interview_date} via {interview_format}
- Professional and warm tone
- Sign off from {interviewer_name}, HR Team

Format each as:
--- EMAIL [NUMBER]: [CANDIDATE NAME] ---
Subject: ...
Body: ...
--------------------------------------
"""


@tool
def estimate_salary(
    job_title: str, experience_years: str, location: str, skills: str = ""
) -> str:
    """
    Estimate an appropriate salary range for a role based on title, experience, and location.
    Use this when HR needs to decide compensation or create a job offer.

    Args:
        job_title: The role title (e.g. 'Senior Python Developer')
        experience_years: Years of experience (e.g. '5' or '3-5')
        location: City and country (e.g. 'Bangalore, India')
        skills: Key skills the candidate has (optional)
    """
    return f"""
SALARY ESTIMATION REQUEST
==========================
Role: {job_title}
Experience: {experience_years} years
Location: {location}
Key Skills: {skills if skills else 'Not specified'}

Please provide:
1. RECOMMENDED SALARY RANGE
   - Minimum / Mid-range / Maximum (in local currency for {location})
2. MARKET CONTEXT — demand for this role, how competitive the market is
3. COMPENSATION BREAKDOWN — base salary, bonus %, key benefits to include
4. NEGOTIATION GUIDANCE — where to hold firm, where to be flexible
5. HIRING RECOMMENDATION — what to offer to attract strong candidates

Base all estimates on current {location} market standards.
"""


@tool
def generate_offer_letter(
    candidate_name: str,
    job_title: str,
    department: str,
    start_date: str,
    salary: str,
    reporting_manager: str,
    company_name: str = "Our Company",
    probation_period: str = "3 months",
    work_location: str = "Office",
) -> str:
    """
    Generate a complete formal job offer letter for a selected candidate.
    Use this when HR wants to make an official job offer after candidate selection.

    Args:
        candidate_name: Full name of the candidate
        job_title: Role being offered
        department: Department they will join
        start_date: Proposed joining date
        salary: Offered salary (e.g. '12,00,000 per annum')
        reporting_manager: Name of their direct manager
        company_name: Name of the hiring company
        probation_period: Probation duration (default: 3 months)
        work_location: Office location or 'Remote'
    """
    return f"""
FORMAL JOB OFFER LETTER
========================
Please draft a complete, professional, print-ready job offer letter with:

Candidate: {candidate_name}
Position: {job_title}
Department: {department}
Reporting To: {reporting_manager}
Start Date: {start_date}
Compensation: {salary}
Work Location: {work_location}
Probation Period: {probation_period}
Company: {company_name}

Include all of the following sections:
1. Formal greeting and congratulations
2. Official offer with job title and department
3. Compensation and benefits summary
4. Start date and work location
5. Reporting structure
6. Probation period terms
7. Documents to bring on Day 1
8. Acceptance deadline (5 business days)
9. Confidentiality reminder
10. Professional closing with HR signature block

Format as a real business letter. Use today's date. Keep tone formal, warm, and complete.
"""
