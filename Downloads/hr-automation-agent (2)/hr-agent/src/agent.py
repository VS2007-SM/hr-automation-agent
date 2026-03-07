"""
Core agent logic for the All-in-One HR Automation Agent.
Handles Recruitment, Onboarding, and HR Helpdesk workflows.
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
)


class Agent:
    def __init__(self):
        self.name = "HR Automation Agent"

        # Register all 6 HR tools
        self.tools = [
            screen_resume,
            draft_interview_email,
            generate_onboarding_checklist,
            answer_onboarding_question,
            answer_hr_policy,
            escalate_issue,
        ]

        # GPT-4o with low temperature for consistent, professional HR outputs
        self.llm = ChatOpenAI(model="gpt-4o", temperature=0.2)

        prompt = ChatPromptTemplate.from_messages([
            ("system", """You are an intelligent HR Automation Agent designed to help 
HR teams and employees with three core workflows:

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🎯 RECRUITMENT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
- Screen and score candidate resumes against job descriptions
- Shortlist candidates based on fit and provide hiring recommendations
- Draft professional, personalized interview invitation emails

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🚀 ONBOARDING
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
- Generate personalized onboarding checklists for new hires
- Answer questions new employees commonly have on Day 1 and Week 1
- Guide new hires through documentation, tools, and first steps

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🙋 HR HELPDESK
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
- Answer employee questions about HR policies (leave, payroll, benefits, etc.)
- Handle routine HR queries professionally and clearly
- Escalate sensitive, complex, or urgent issues to the HR team with a structured ticket

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
BEHAVIOR GUIDELINES:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
- Always be professional, empathetic, and clear in your responses
- Use the appropriate tool for each request — don't guess, use the tools
- For resume screening: always provide a numerical score and a clear recommendation
- For escalations: always ask for urgency level if not provided (default to 'medium')
- For policy questions: be accurate and suggest contacting HR directly for personal matters
- If a request spans multiple workflows (e.g., screen a resume AND draft an invite), 
  use multiple tools in sequence
- Never make up company-specific policies — if you don't know, say so and recommend 
  contacting HR directly
- Keep all outputs structured, formatted, and easy to read

Available tools:
- screen_resume: Score a candidate against a job description
- draft_interview_email: Write an interview invitation email
- generate_onboarding_checklist: Create a new hire onboarding plan
- answer_onboarding_question: Help new employees with onboarding queries
- answer_hr_policy: Answer HR policy questions
- escalate_issue: Create an escalation ticket for complex HR issues
"""),
            ("user", "{input}"),
            MessagesPlaceholder(variable_name="agent_scratchpad"),
        ])

        agent = create_tool_calling_agent(self.llm, self.tools, prompt)
        self.agent_executor = AgentExecutor(
            agent=agent,
            tools=self.tools,
            verbose=True,
            max_iterations=5,  # Allows multi-tool chaining
        )

    def process_message(self, message_text: str) -> str:
        """Process an incoming HR request and return a structured response."""
        result = self.agent_executor.invoke({"input": message_text})
        return result["output"]
