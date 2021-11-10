import pandas as pd

rdf=pd.read_csv("rs.csv")
mdf=pd.read_csv("split_final_merged.csv")

for ri, rr in rdf.iterrows():
	df=mdf[(mdf.name==rr["name"])&(mdf.year==2019)]
	for index, row in df.iterrows():
		mdf.loc[index,"State"]=rr["State"]
		mdf.loc[index,"party"]=rr["party"]
		mdf.loc[index,"gender"]=rr["gender"]
		mdf.loc[index,"house"]=rr["house"]

mdf.to_csv("TCPD_Indian_Cabinet_1990_2021.csv")