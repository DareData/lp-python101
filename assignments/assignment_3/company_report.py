import pandas as pd

company_df = pd.DataFrame(index=["Carol","Ivo","Nuno","Rui","Lucie","Maria","John","Rita","Rober","Sam","Ana"],
                          columns=["Role","Salary (in pasteis de nata/month)", "Age", "Seniority"],
                          data=[["Partner and COO", 31, 30, 7],
                                ["Partner and Proffessional Meeting Attender", 31, 35, 7],
                                ["Partner", 40, 40, 10],
                                ["Partner", 31, 34, 5],
                                ["Admin Sup", 25, 35, 6],
                                ["Data Scientist", 30, 30, 3],
                                ["ChatGPT enjoyer", 23, 24, 2],
                                ["Senior Data Scientist", 31, 32, 10],
                                ["Does things", 28, 30, 1],
                                ["MLOps Master", 35, 40, 10],
                                ["Data Engineer", 30, 25, 1]])

print(company_df)