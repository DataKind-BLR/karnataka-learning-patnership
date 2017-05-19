import pandas as pd

# Load data from Excel file
contestData = pd.ExcelFile("data/GP Contest Data Sample.xlsx")
data = contestData.parse('4th')
schoolwiseData= data[['Name of the school','Q1','Q2','Q3','Q4','Q5','Q6','Q7','Q8','Q9','Q10','Q11','Q12','Q13','Q14','Q15','Q16','Q17','Q18','Q19','Q20']].groupby(['Name of the school']).mean()
	
questionData = pd.DataFrame.from_csv('data/class4Blueprint.csv')


"""
This function gets the schoolwise total for all the schools. 
Mean of total with the schoolname is returned.
""" 
def getSchoolwiseTotal():
	schoolwiseData= data[['Name of the school','Total','Q1','Q2','Q3','Q4','Q5','Q6','Q6','Q7','Q8','Q9','Q10','Q11','Q12','Q13','Q14','Q15','Q16','Q17','Q18','Q19','Q20']].groupby(['Name of the school']).mean()
	records= {}
	for index, row in schoolwiseData.iterrows():
		records[index] =row['Total']
	return records

"""
This function gets the schoolwise mean of scores according to question type. 
Dictonary of schoolname: Questiontype:Mean of scores in that school.
""" 
def getSchoolwiseAccToQuestiontype():	
	typeOfQuestion= questionData['Type of question'].replace({'\n': ''}, regex=True).tolist()
	qtype_dict ={}
	qtype_mean ={}
	schoolwise_qtype={}
	for index, row in schoolwiseData.iterrows():
		for Qno in range(20):
			# print index, typeOfQuestion[Qno], row[Qno]
			try:
				qtype_dict[typeOfQuestion[Qno]].append(row[Qno])
			except KeyError:
				qtype_dict[typeOfQuestion[Qno]] = [row[Qno]]
		for key, value in qtype_dict.iteritems():
			# print key, value, index
			qtype_mean[key]= round(reduce(lambda x, y: x + y, value) / len(value),3)	
		schoolwise_qtype[index] = qtype_mean
		qtype_dict = {}
		qtype_mean ={}
	return schoolwise_qtype

# print getSchoolwiseTotal()
print getSchoolwiseAccToQuestiontype()
