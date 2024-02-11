from autogen import AssistantAgent, UserProxyAgent, config_list_from_json

# Load LLM inference endpoints from an env variable or a file
# See https://microsoft.github.io/autogen/docs/FAQ#set-your-api-endpoints
# and OAI_CONFIG_LIST_sample

# config_list = config_list_from_json(env_or_file="OAI_CONFIG_LIST")
config_list = [
    {'model': 'gpt-4',
     'api_key': ''},
]

# You can also set config_list directly as a list, for example, config_list = [{'model': 'gpt-4', 'api_key': '<your OpenAI API key here>'},]

custom_agent_prmpt = "Give company names, find which company has higher employee count as of dec 2022."

assistant = AssistantAgent(name="assistant"
                           , system_message=custom_agent_prmpt
                           , llm_config={"config_list": config_list})

user_proxy = UserProxyAgent("user_proxy", code_execution_config=
{"work_dir": "Code",
 "use_docker": False}
                            )
# IMPORTANT: set to True to run code in docker, recommended

user_proxy.initiate_chat(assistant, message="Google or Microsft, which is better?")
# This initiates an automated chat between the two agents to solve the task
