import pandas as pd

# mpr_all = pd.read_csv('mpr_all.csv', low_memory = False)

# mpr_all = mpr_all[(mpr_all['status'] == 1) | (mpr_all['status'] == 11)]
# mpr_true = mpr_all[mpr_all['isEcom'] == True]
# mpr_false = mpr_all[mpr_all['isEcom'] != True]


# print(len(mpr_all), len(mpr_true), len(mpr_false))
# print(mpr_all.groupby(['isEcom', 'status'])['id'].count())
# print(mpr_true.groupby(['isEcom', 'status'])['id'].count())
# print(mpr_false.groupby(['isEcom', 'status'])['id'].count())

# mpr_true.to_csv('mpr_true.csv', index = False)


def diffRecords():
	mpr_true = pd.read_csv('mpr_true.csv', low_memory = False)
	ecom = pd.read_csv('ecom.csv', low_memory = False)

	concat_df = pd.concat([mpr_true,ecom])
	concat_df = concat_df.drop_duplicates(keep=False)
	
	concat_df.to_csv('diff.csv', index = False)

def tcsReports():
	tcs = pd.read_csv('tcs.csv', low_memory = False)
	tcs_201352 = tcs[tcs['mid'] == 201352]
	tcs_201352.to_csv('tcs_201352.csv',index = False)

def bbpsReports():
	bbps = pd.read_csv('bbps1.csv', low_memory = False)
	bbps_cod = bbps[(bbps['cod_payable'] != None) & (bbps['cod_payable'] >= 0)]
	bbps_cod_col = bbps_cod[['order_item_id','payout_id','merchant_id','cod_payable']]
	bbps_cod_col.to_csv('bbps_cod1.csv',index = False)

# diffRecords()
# tcsReports()
# bbpsReports()

def getSettlement():
	f1 = pd.read_csv('f1.csv', low_memory = False)
	f2 = pd.read_csv('f2.csv', low_memory = False)
	f3 = pd.read_csv('f3.csv', low_memory = False)
	f4 = pd.read_csv('f4.csv', low_memory = False)
	f5 = pd.read_csv('f5.csv', low_memory = False)

	f1_data = f1[(f1['merchant_id'] == 1151279)]
	f1_col = f1_data[['order_item_id']]
	f1_col.to_csv('f1_col.csv',index = False)
	
	f2_data = f2[(f2['merchant_id'] == 1151279)]
	f2_col = f2_data[['order_item_id']]
	f2_col.to_csv('f2_col.csv',index = False)

	f3_data = f3[(f3['merchant_id'] == 1151279)]
	f3_col = f3_data[['order_item_id']]
	f3_col.to_csv('f3_col.csv',index = False)

	f4_data = f4[(f4['merchant_id'] == 1151279)]
	f4_col = f4_data[['order_item_id']]
	f4_col.to_csv('f4_col.csv',index = False)

	f5_data = f5[(f5['merchant_id'] == 1151279)]
	f5_col = f5_data[['order_item_id']]
	f5_col.to_csv('f5_col.csv',index = False)


getSettlement()
