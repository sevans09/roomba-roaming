import time
import sys

def checkGoHome(blackboard):
	if blackboard["BATTERY_LEVEL"] < 30:
		goHome(blackboard)
	else: 
		return

def checkBatteryLow(blackboard):
	if blackboard["BATTERY_LEVEL"] < 30:
		print "BATTERY LOW"
		return True
	else:
		return False

def checkBatteryDead(blackboard):
	if (blackboard["BATTERY_LEVEL"] <= 0):
		return True
	else:
		return False

def goHome(blackboard):
	home = blackboard["HOME_PATH"]
	print "DOCK SUCCEEDED, RECHARGING"
	blackboard["BATTERY_LEVEL"] += 30

	if blackboard["BATTERY_LEVEL"] >= 100:
		blackboard["BATTERY_LEVEL"] = 100

	time.sleep(10)
	print "RECHARGED, BATTERY LEVEL IS ", blackboard["BATTERY_LEVEL"]

def checkSpot(blackboard):
	if blackboard["SPOT"] == True:
		print "CLEAN SPOT RUNNING"
		for x in range(20):
			if x % 5 == 0:
				blackboard["BATTERY_LEVEL"] -= 5
			time.sleep(1)
		blackboard["SPOT"] = False
		print "CLEAN SPOT SUCCEEDED"

def checkDustySpot(blackboard):
	if blackboard["DUSTY_SPOT"] == True:
		print "CLEAN DUSTY SPOT RUNNING"
		for x in range(35):
			if x % 5 == 0:
				blackboard["BATTERY_LEVEL"] -= 5
				print"Battery level decrementing: ", blackboard["BATTERY_LEVEL"]
			time.sleep(1)
		blackboard["DUSTY_SPOT"] = False
		print "CLEAN DUSTY SPOT SUCCEEDED"

def checkGeneral(blackboard):
	if blackboard["GENERAL"] == True:
		if checkBatteryLow(blackboard) == True:
			return

		while checkBatteryLow(blackboard) == False:
			blackboard["BATTERY_LEVEL"] -= 10
			print"In general, battery level ", blackboard["BATTERY_LEVEL"]
			checkDustySpot(blackboard)
		blackboard["GENERAL"] = False

def doNothing(blackboard):
	blackboard["BATTERY_LEVEL"] -= 1
	print "In do nothing, battery level is ", blackboard["BATTERY_LEVEL"]
	time.sleep(1)
	return

def run(blackboard, num_runs):
	while num_runs != 0:
		if (checkBatteryDead(blackboard) == True):
			sys.exit("Battery has died.")
		if blackboard["DUSTY_SPOT"] == False and blackboard["SPOT"] == False and blackboard["GENERAL"] == False:
			print "Floor is clean, idling"
			blackboard["BATTERY_LEVEL"] -= 1
			time.sleep(1)

		checkGoHome(blackboard)
		checkSpot(blackboard)
		checkGeneral(blackboard)
		doNothing(blackboard)
		num_runs -= 1

def main():
	num_runs = 5
	blackboard = {"BATTERY_LEVEL":35, "SPOT":True, "GENERAL":True, "DUSTY_SPOT":True,"HOME_PATH":""}

	BATTERY_LEVEL = input ("Enter battery level: ") 
	print(BATTERY_LEVEL) 
	SPOT = input("Enter spot boolean: ") 
	print(SPOT) 
	GENERAL = input("Enter general boolean: ") 
	print(GENERAL)
	DUSTY_SPOT = input("Enter dusty spot boolean: ") 
	print(DUSTY_SPOT)
	HOME_PATH = raw_input("Enter home path: ") 
	print(HOME_PATH)
	num_runs = input("Enter number of runs: ")

	keep_running = True

	while keep_running:
		run(blackboard, num_runs)
		userInput = raw_input("Do you want to keep cleaning? Enter Y for yes and N for no: ")
		if userInput == "N":
			keep_running = False
		if userInput == "Y":
			num_runs = 5
			blackboard["SPOT"] = input("Do we need a spot clean? Enter True or False: ") 
			blackboard["DUSTY_SPOT"] = input("Is there a dusty spot? Enter True or False: ") 
			blackboard["GENERAL"] = input("Do we need a general cleaning? Enter True or False: ") 

if __name__== "__main__":
	main()
