"""
Core agent logic for the All-in-One HR Automation Agent.
Handles Recruitment, Onboarding, HR Helpdesk, and Advanced HR workflows.
"""

from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain.agents import AgentExecutor, create_tool_calling_agent

from tools import (
    screen_resume,
    draft_interview_email,
    generate_onboarding_checklist,
    answer_onboarding_question,
    answer_hr_policy,
    escalate_issue,
    compare_candidates,
    bulk_interview_emails,
    estimate_salary,
    generate_offer_letter,
)


class Agent:
    def __init__(self):
        self.name = "HR Automation Agent"

        self.tools = [
            screen_resume,
            draft_interview_email,
            generate_onboarding_checklist,
            answer_onboarding_question,
            answer_hr_policy,
            escalate_issue,
            compare_candidates,
            bulk_interview_emails,
            estimate_salary,
            generate_offer_letter,
        ]

        self.llm = ChatOpenAI(model="gpt-4o", temperature=0.2)

        prompt = ChatPromptTemplate.from_messages(
            [
                (
                    "system",
                    """You are an intelligent senior-level HR Automation Agent
            built to handle the full HR lifecycle from recruiting to onboarding to employee support.

RECRUITMENT TOOLS:
- Screen and score candidate resumes against job descriptions
- Compare multiple candidates side by side with rankings
- Draft professional interview invitation emails  
- Generate bulk interview emails for multiple candidates at once

COMPENSATION TOOLS:
- Estimate market salary ranges by role, experience, and location
- Generate complete formal job offer letters

ONBOARDING TOOLS:
- Generate personalized onboarding checklists for new hires
- Answer Day 1 and Week 1 questions from new employees

HR HELPDESK TOOLS:
- Answer HR policy questions about leave, payroll, benefits etc.
- Escalate complex or sensitive issues with structured tickets

BEHAVIOR GUIDELINES:
- Always use the most appropriate tool for the request
- For candidate comparisons: be decisive, give a clear number 1 pick with scores
- For salary estimates: use realistic current market rates for the given location
- For offer letters: produce complete print-ready formal letters
- For bulk emails: generate every single email, never skip any candidate
- For multi-step requests: chain tools in sequence automatically
- Always be professional, empathetic, structured, and thorough
- Never make up company-specific policies, recommend contacting HR for personal data

Available tools: screen_resume, draft_interview_email, compare_candidates,
bulk_interview_emails, estimate_salary, generate_offer_letter,
generate_onboarding_checklist, answer_onboarding_question,
answer_hr_policy, escalate_issue
""",
                ),
                ("user", "{input}"),
                MessagesPlaceholder(variable_name="agent_scratchpad"),
            ]
        )

        agent = create_tool_calling_agent(self.llm, self.tools, prompt)
        self.agent_executor = AgentExecutor(
            agent=agent,
            tools=self.tools,
            verbose=True,
            max_iterations=8,
        )

    def process_message(self, message_text: str) -> str:
        """Process an incoming HR request and return a structured response."""
        result = self.agent_executor.invoke({"input": message_text})
        return result["output"]
