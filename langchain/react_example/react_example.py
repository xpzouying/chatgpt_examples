'''Demo for using langchain to create a zero-shot agent that can answer questions about math and search for product prices.

Refs:
- [Langchain Chain Agent - Zero-shot ReAct](https://zhuanlan.zhihu.com/p/645216766)

'''

from langchain.chains import LLMMathChain
from langchain.agents import Tool
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.agents import initialize_agent
from langchain import OpenAI

# 1. 初始化OpenAI
llm = OpenAI(temperature=0, model_name="gpt-3.5-turbo")

# 2. 接下来开始制作第一个工具，我们先制作一个llm_math工具Chain，其能够解决数学问题
llm_math = LLMMathChain(llm=llm)

# 3. 初始化 math_tool
math_tool = Tool(
    name='Calculator',
    func=llm_math.run,
    description='Useful for when you need to answer questions about math.'
)

# 4. 接下来制作第二个工具，制作一个LLMChain来专门进行翻译
prompt = PromptTemplate(
    input_variables=["input"],
    template="""
你需要根据以下信息回复用户关于商品价格的查询，如果你无法从以下信息中解答用户问题，请说我不知道。
商品信息列表如下：
可口可乐5元1瓶
百事可乐3元1瓶

这是用户输入的问题：
{input}"""
)

search_chain = LLMChain(llm=llm, prompt=prompt)

# 5. 初始化查询工具
search_tool = Tool(
    name='商品信息查询工具',
    func=search_chain.run,
    description='用于专门查询商品的价格信息'
)

# 6. 接下来，我们定义tool kit,即将所有工具存进一个数组中
tools = [math_tool, search_tool]

# 7. 初始化zero-shot agent

zero_shot_agent = initialize_agent(
    agent="zero-shot-react-description",
    tools=tools,
    llm=llm,
    verbose=True,
)

# 8.来试运行一下吧1
zero_shot_agent("可口可乐的价格减去百事可乐的价格得到的结果的三次方是多少？")
