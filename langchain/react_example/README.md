# ReAct Demo

## Run

```bash
export OPENAI_API_KEY='sk-xxx'
python3 ./react_example.py
```

## Result

```
> Entering new  chain...
I need to find the price of Coca-Cola and Pepsi-Cola first before calculating the final answer.
Action: 商品信息查询工具
Action Input: 可口可乐, 百事可乐
Observation: 可口可乐的价格是5元1瓶，百事可乐的价格是3元1瓶。
Thought:Now that I have the prices of Coca-Cola and Pepsi-Cola, I can calculate the final answer.
Action: Calculator
Action Input: (5 - 3)^3
Observation: Answer: 8
Thought:I now know the final answer
Final Answer: 8

> Finished chain.
```
