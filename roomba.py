def checkGoHome(blackboard):
	if blackboard["BATTERY_LEVEL"] < 30:
		goHome(blackboard)
	else: 
		return


def checkBatteryLow(blackboard):
	if blackboard["BATTERY_LEVEL"] < 30:
		return True
	else:
		return False


def goHome(blackboard):
	home = blackboard["HOME_PATH"]
	print "FIND HOME SUCCEEDED"
	print "GO HOME SUCCEEDED"
	print "DOCK SUCCEEDED"


def checkSpot(blackboard):
	if blackboard["SPOT"] == True:
		cleanSpot(20)
		blackboard["SPOT"] = False
	else:
		return


def cleanSpot(time):
	if (time == 0):
		print("CLEAN SPOT SUCCEEDED")
		return
	print "CLEAN SPOT RUNNING", time
	cleanSpot(time - 1)


def checkDustySpot(blackboard):
	if blackboard["DUSTY_SPOT"] == True:
		cleanSpot(35)
	else:
		cleanSpot(1)


def checkGeneral(blackboard):
	if blackboard["GENERAL"] == True:
		if checkBatteryLow(blackboard) == True:
			print "battery too low - cant complete general tasks"
			return

		while checkBatteryLow(blackboard) == False:
			blackboard["BATTERY_LEVEL"] -= 10
			print(blackboard["BATTERY_LEVEL"]) 
			checkDustySpot(blackboard)
		blackboard["GENERAL"] = False


def doNothing(blackboard):
	print("DO NOTHING SUCCEEDED")
	return


def main():
	num_runs = 5
	blackboard = {"BATTERY_LEVEL":50, "SPOT":True, "GENERAL":True, "DUSTY_SPOT":True,"HOME_PATH":""}

	# BATTERY_LEVEL = input ("Enter battery level: ") 
	# print(BATTERY_LEVEL) 
	# SPOT = input("Enter spot boolean: ") 
	# print(SPOT) 
	# GENERAL = input("Enter general boolean: ") 
	# print(GENERAL)
	# DUSTY_SPOT = input("Enter dusty spot boolean: ") 
	# print(DUSTY_SPOT)
	# HOME_PATH = raw_input("Enter home path: ") 
	# print(HOME_PATH)
	# num_runs = input("Enter number of runs: ")

	while num_runs != 0:
		checkGoHome(blackboard)
		checkSpot(blackboard)
		checkGeneral(blackboard)
		doNothing(blackboard)
		num_runs -= 1


if __name__== "__main__":
	main()