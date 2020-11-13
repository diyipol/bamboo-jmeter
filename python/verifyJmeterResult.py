import pandas as pd
import sys

if len(sys.argv) < 3:
    print("Script has three args: jmeterResultFile, maxExecutionTimeAllowed and maxNumberSlowerExecutionsAllowed")
    sys.exit(-1)

jmeterResultFile = sys.argv[1]
maxExecutionTimeAllowed = int(sys.argv[2])
maxNumberSlowerExecutionsAllowed = int(sys.argv[3])

print("Verify jmeter tests result with jmeterResultFile [", 
    jmeterResultFile, "], maxExecutionTimeAllowed [", maxExecutionTimeAllowed, 
    "] and maxNumberSlowerExecutionsAllowed [", maxNumberSlowerExecutionsAllowed, "]")

jmeterResult = pd.read_csv(jmeterResultFile)

okExecutions = jmeterResult[jmeterResult["success"] == True]["success"].count()

print("There are [", okExecutions, "] success executions in jmeter result")

koExecutions = jmeterResult[jmeterResult["success"] == False]["success"].count()

print("There are [", koExecutions, "] error executions in jmeter result")

print("The average response time is [", jmeterResult["elapsed"].mean(), "]")

slowerExecutions = jmeterResult[jmeterResult["elapsed"] > maxExecutionTimeAllowed]["elapsed"].count()

print("There are [", slowerExecutions, "] slower executions in jmeter result")

if koExecutions > 0 or slowerExecutions > maxNumberSlowerExecutionsAllowed :
    sys.exit(-1)

sys.exit(0)
