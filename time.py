currentTimeStr = input("What is the current time (in hours 0-23)?")
waitTimeStr = input("How many hours do you want to wait:")                      #added missing parantheses

currentTimeInt = int(currentTimeStr)                                            #removed underscores
waitTimeInt = int(waitTimeStr)                                                  #removed underscores
finalTimeInt = currentTimeInt + waitTimeInt
print(finalTimeInt)                                                             #removed underscore
