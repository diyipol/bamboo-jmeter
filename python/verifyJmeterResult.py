import pandas as pd
import sys

print("Summary of jmeter execution")

jmeterResult = pd.read_csv("./jmeter-result.jtl")

okExecutions = jmeterResult[jmeterResult["success"] == True]["success"].count()

print("There are [", okExecutions, "] success executions in jmeter result")

koExecutions = jmeterResult[jmeterResult["success"] == False]["success"].count()

print("There are [", koExecutions, "] error executions in jmeter result")

print("The average response time is [", jmeterResult["elapsed"].mean(), "]")

slowerExecutions = jmeterResult[jmeterResult["elapsed"] > 300]["elapsed"].count()

print("There are [", slowerExecutions, "] slower executions in jmeter result")

if koExecutions > 0 or slowerExecutions > 0 :
    sys.exit(-1)

sys.exit(0)
