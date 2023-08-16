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

company_df.drop(labels="John", inplace=True)

company_df["Replaced_by_AI"] = "No"

company_df.loc["Rober","Replaced_by_AI"] = "Yes"

print(company_df.loc[["Carol", "Ivo", "Nuno","Rui"]])
print(f"\n\nThe company has {company_df.shape[0]} workers")
print(f"There are {len(company_df[company_df.Seniority >= 5])} workers that have been in the company for 5 or more years\n\n")

company_df.reset_index(inplace=True)
company_df.rename(columns={"index": "Name"}, inplace=True)
print(company_df)