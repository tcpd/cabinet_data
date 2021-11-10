import re
import pandas as pd

df=pd.read_csv("ICOM_2019-2021.csv")
cols=df.columns.to_list()

data=[]

for index, row in df.iterrows():
	ports_st=row["Portfolio"]
	ports_st=re.sub(r"\; and",";",ports_st)
	ports_st=re.sub(r"\.","",ports_st)
	ports_st=re.sub(' +', ' ',ports_st)
	ports_st=re.sub(r'\s+$', '', ports_st)
	ports_st=re.sub(r"State in the","",ports_st)
	#ports_st=re.sub(r"(Independent Charge)","",ports_st)
	ports_st=re.sub(r"Minister of","",ports_st)
	ports_st=re.sub(' +', ' ',ports_st)
	ports_st=re.sub(r'\s+$', '', ports_st)
	ports_l=ports_st.split("; ")
	for x in ports_l:
		x_data={}
		for n in cols:
			if n!="Portfolio":
				x_data[n]=row[n]
			else:
				x_data[n]=x
		data.append(x_data)

new_df = pd.DataFrame(data)
#new_df["LD_ID"] = new_df["State_Name"].astype(str)+"_"+(new_df["Assembly_No"]).astype(str)+"_"+(new_df["Constituency_No"].astype(int)).astype(str)+"_"+(new_df["Poll_No"].astype(int)).astype(str)+"_1"
new_df=new_df.drop_duplicates(subset=["Ls_num","Name","Portfolio","Rank"],keep="first")

new_df.to_csv("split.csv")