import pandas as pd
import json 


def getGroups():
	ept = pd.read_csv('ept.csv', low_memory = False)
	ept_count = ept[['Plaza Managing code','Dec-22']]
	total_count = 0
	total_pmc = 0
	for index,row in ept_count.iterrows():
		total_pmc = total_pmc+1
		total_count += row['Dec-22']

	average_count_per_job = total_count/5
	print(total_count,average_count_per_job)

	jobs = [None] * 5
	pointer = 0

	for index,row in ept_count.iterrows():
		if(jobs[pointer] == None):
			jobs[pointer] = {
				"pmc":[],
				"count":0,
				"length":0
			}
		if(jobs[pointer]["count"] < average_count_per_job):
			jobs[pointer]["pmc"].append(row["Plaza Managing code"])
			jobs[pointer]["count"] = jobs[pointer]["count"] + row["Dec-22"]
			jobs[pointer]["length"] = jobs[pointer]["length"] + 1
		else:
			if(pointer + 1 < 5):
				pointer = pointer + 1

			if(jobs[pointer] == None):
				jobs[pointer] = {
					"pmc":[],
					"count":0,
					"length":0
				}

			jobs[pointer]["pmc"].append(row["Plaza Managing code"])
			jobs[pointer]["count"] = jobs[pointer]["count"] + row["Dec-22"]
			jobs[pointer]["length"] = jobs[pointer]["length"] + 1



	json_object = json.dumps(jobs, indent = 4) 
	print(json_object)


getGroups()