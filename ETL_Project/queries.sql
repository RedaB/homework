Select 
	dataSet1.first_name, 
	dataSet1.last_name, 
	dataSet2.marital_s, 
	dataSet2.occupation,
	dataSet2.annual_income
FROM 
	dataSet1
JOIN 
	dataSet2
ON dataSet1.id = dataSet2.user_id;