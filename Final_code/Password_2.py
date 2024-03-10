import csv
def add(muser,service,username, password):
	with open("storage.csv", "a") as file2:
    	file2.write(muser+",")#change the krow to muser
	with open("storage.csv", "a") as file2:
    	file2.write(service+",")

    with open("storage.csv", "a") as file2:
        file2.write(username+",")
    with open("storage.csv", "ab") as file2:
        file2.write(password)
    with open("storage.csv", "a") as file2:
        file2.write("\n")

