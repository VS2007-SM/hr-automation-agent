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
    interviewer_name: str
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
    employee_name: str,
    job_title: str,
    department: str,
    start_date: str
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
    employee_name: str,
    issue_description: str,
    urgency_level: str
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
        "low": "🟢 LOW PRIORITY — Review within 3-5 business days"
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
