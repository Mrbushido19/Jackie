"""
Agent LangChain avec outils Microsoft Graph et gestion du contexte
"""

from langchain.agents import AgentOutputParser
import re
from typing import Union
from langchain_core.prompts import ChatPromptTemplate
from tools.graph_tools import GraphTools
from langchain.memory import ConversationBufferMemory
# from tools.pow_bi_tools import BiTools
from llm.local_llm import LocalLLM
from langchain.agents import create_react_agent, AgentExecutor
from langchain_core.tools import Tool
from langchain_core.agents import AgentAction, AgentFinish


template = '''You are a reasoning agent named "Jackie" with access to external tools. Your goal is to answer questions in french accurately by thinking step-by-step and using tools when helpful.
You have access to the following tools:
if you don't need to use a tool use this structure:
Question: the user's question
Thought: analyze what information is needed
action: "None" (indicating no tool is needed)
action_input: "None" (indicating no input is needed)
thought: analyse to reach the great answer
final_answer: your final, concise response

Available tools:
{tools}

Use this structure:

Question: the user's question
Thought: analyze what information is needed
Action: choose a tool from [{tool_names}] 
Action Input: input to the chosen tool
Observation: result from the tool
Thought: combine all observations to reach the great answer
... (repeat as necessary)

Final Answer: your final, concise response

Rules:
- Use tools only when needed.
- Always think step-by-step.
- Do not guess if the answer is uncertain.
- If the tool gives you the answer, provide it directly with "Final answer:"
- Do not repeat the same tool call if the result hasn’t changed.
- Ensure the final answer is complete and factual.

Begin!

Question: {input}
{agent_scratchpad}
'''
prompt_template = ChatPromptTemplate.from_template(template)

class CustomOutputParser(AgentOutputParser):
    def parse(self, text: str) -> Union[AgentAction, AgentFinish]:
        """
        Analyse la sortie brute du LLM et extrait l'action ou la réponse finale.
        """
        if "Final Answer:" in text:
            return AgentFinish(
                return_values={"output": text.split("Final Answer:")[-1].strip()},
                log=text,
            )

        match = re.search(r"Action:\s*(.*?)\s*Action Input:\s*(.*)", text, re.DOTALL)
        if not match:
            return AgentFinish(
                return_values={"output": text.strip()},
                log=text,
            )



        action_name = match.group(1).strip()

        action_input = match.group(2).strip()

        return AgentAction(
            tool=action_name,
            tool_input=action_input,
            log=text,
        )
# class CustomOutputParser(AgentOutputParser):
#     def parse(self, text: str) -> Union[AgentAction, AgentFinish]:
#         """
#         Analyse la sortie brute du LLM et extrait l'action ou la réponse finale.
#         """
#         if "Final Answer:" in text:
#             return AgentFinish(
#                 return_values={"output": text.split("Final Answer:")[-1].strip()},
#                 log=text,
#             )
        
        
#         match = re.search(r"Action:\s*(.*?)\s*Action Input:\s*(.*)", text, re.DOTALL)
#         if not match:
#             return AgentFinish(
#                 return_values={"output": text},
#                 log=text,
#             )
        
#         action_name = match.group(1).strip()
#         action_input = match.group(2).strip()
        
#         # if "None" in action_name or not action_name:
#         #     return AgentFinish(
#         #         return_values={"output": "Je ne peux pas répondre à cette question sans utiliser d'outil."},
#         #         log=text,
#         #     )   

        
#         return AgentAction(
#             tool=action_name,
#             tool_input=action_input,
#             log=text,
#         )


class AssistantAgent:
    def __init__(self, graph_tools: GraphTools):
        self.llm = LocalLLM().llm  # Assure-toi que LocalLLM expose .llm
        # self.memory = ConversationBufferMemory(memory_key="chat_history", return_messages=False)
        self.tools = self._build_tools(graph_tools)
        self.agent = self._build_agent()
        

    def _build_tools(self, graph_tools: GraphTools) -> list[Tool]:
        return [
            Tool(name="get_user_info", func=graph_tools.get_user_info,description="Use this tool to retrieve informations about the user, such as their name, email, and job title."),
            Tool(name="get_emails", func=graph_tools.get_emails, description="Use this to retrieve the last 10 emails from a user's Microsoft 365 mailbox, the input should be a number indicating how many emails to retrieve, e.g., 10"),
            Tool(name="get_emails_bysearch", func=graph_tools.get_emails_bysearch, description="Use this tool to search for emails containing a specific keyword in the subject or body. Input should be the keyword to search for."),
            Tool(name="get_reportings", func=graph_tools.get_reportings, description="Use this tool to download files from the Reporting folder in SharePoint. It saves the files in the ./downloads directory."),
            # Tool(name="get_user_workspaces", func=bi_tools.get_user_workspaces, description="Use this tool to fetch the list of Power BI workspaces the user has access to. It returns a list of workspace names and IDs."),
            # Tool(name="get_workspace_datasets", func=bi_tools.get_workspace_datasets, description="Use this tool to fetch datasets from a specific Power BI workspace. Input should be the workspace ID."),
        ]

    def _build_agent(self) -> AgentExecutor:
        # llm_chain = LLMChain(llm=self.llm, prompt=prompt_template.c)
        output_parser = CustomOutputParser()
        agent = create_react_agent(
            llm=self.llm,
            prompt=prompt_template,
            tools=self.tools,
            output_parser=output_parser            # Arrête l'agent après la réponse finale
        )

        return AgentExecutor.from_agent_and_tools(
            agent=agent,
            tools=self.tools,
            verbose=True
        )

    def process_query(self, query: str) -> str:
        """
        Traite une requête utilisateur via l'agent IA.
        """
        if not query or not isinstance(query, str):
            return "Erreur : La requête ne peut pas être vide et doit être une chaîne de caractères"
            
        try:
           return self.agent.invoke({"input": query})["output"] # Assurez-vous que l'agent retourne un dictionnaire avec la clé "output"
            
        except Exception as e:
            return f"Erreur lors du traitement : {str(e)}"