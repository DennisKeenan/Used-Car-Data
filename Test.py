import pickle 
import pandas as pd
import numpy as np

with open("Car Price AI", 'rb') as file:
    pipe=pickle.load(file)
result=pipe.predict((pd.DataFrame(columns=['name', 'company', 'year', 'kms_driven', 'fuel_type'],
                           data=np.array(['Maruti Suzuki Alto','Maruti',2015,30000,'Petrol']).reshape(1,5))))
print(result)
