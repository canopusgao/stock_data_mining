import Quandl

tokenName = "CVQWV6wLVWnrgjsVbc4g"

#ISM Manufacturing starts
#ISM Manufacturing: Inventories Index
def get_quandl_ism_m_ii_monthly(time):
    "Get specific data from ISM Manufacturing Inventories Index from Quandl. Monthly updated data, time format: XXXX(YEAR)-XX(MONTH)-01"
    ret = Quandl.get("FRED/NAPMII", authtoken= tokenName)
    return ret.loc[time,"VALUE"]
    

#ISM Manufacturing: Employment Index
def get_quandl_ism_m_ei_monthly(time):
    "Get specific data from ISM Manufacturing Employment Index from Quandl. Monthly updated data, time format: XXXX(YEAR)-XX(MONTH)-01"
    ret = Quandl.get("FRED/NAPMEI", authtoken= tokenName)
    return ret. loc[time, "VALUE"]


#ISM Manufacturing: Production Index
def get_quandl_ism_m_pi_monthly(time):
Quandl.get("FRED/NAPMPI", authtoken= tokenName)

#ISM Manufacturing: Prices Index
def get_quandl_ism_m_pri_monthly(time):
Quandl.get("FRED/NAPMPRI", authtoken= tokenName)

#ISM Manufacturing: Imports Index
def get_quandl_ism_m_imi_monthly(time):
Quandl.get("FRED/NAPMIMP", authtoken= tokenName)

#ISM Manufacturing: PMI Composite Index
def get_quandl_ism_m_pmici_monthly(time):
Quandl.get("FRED/NAPM", authtoken= tokenName)

#ISM Manufacturing: New Orders Index
def get_quandl_ism_m_noi_monthly(time):
Quandl.get("FRED/NAPMNOI", authtoken= tokenName)

#ISM Manufacturing: Supplier Deliveries Index
def get_quandl_ism_m_sdi_monthly(time):
Quandl.get("FRED/NAPMSDI", authtoken= tokenName)

#ISM Manufacturing: Customer Inventories Index
def get_quandl_ism_m_cii_monthly(time):
Quandl.get("FRED/NAPMCI", authtoken= tokenName)

#ISM Manufacturing: Backlog of Orders Index
def get_quandl_ism_m_boi_monthly(time):
Quandl.get("FRED/NAPMBI", authtoken= tokenName)

#ISM Manufacturing: New Export Orders Index
def get_quandl_ism_m_neoi_monthly(time):
Quandl.get("FRED/NAPMEXI", authtoken= tokenName)

#ISM Manufacturing ends

#ISM Non-manufacturing starts
#ISM Non-manufacturing: Employment Index
def get_quandl_ism_nm_emi_monthly(time):
Quandl.get("FRED/NMFEI", authtoken= tokenName)

#ISM Non-manufacturing: Prices Index
def get_quandl_ism_nm_pi_monthly(time):
Quandl.get("FRED/NMFPI", authtoken= tokenName)

#ISM Non-manufacturing: Inventory Index
def get_quandl_ism_nm_ini_monthly(time):
Quandl.get("FRED/NMFINI", authtoken= tokenName)

#ISM Non-manufacturing: Imports Index
def get_quandl_ism_nm_imi_monthly(time):
Quandl.get("FRED/NMFIMI", authtoken= tokenName)

#ISM Non-manufacturing: Business Activity Index
def get_quandl_ism_nm_bai_monthly(time):
Quandl.get("FRED/NMFBAI", authtoken= tokenName)

#ISM Non-manufacturing: New Orders Index
def get_quandl_ism_nm_noi_monthly(time):
Quandl.get("FRED/NMFNOI", authtoken= tokenName)

#ISM Non-manufacturing: Inventory Sentiment Index
def get_quandl_ism_nm_isi_monthly(time):
Quandl.get("FRED/NMFINSI", authtoken= tokenName)

#ISM Non-manufacturing: Supplier Deliveries Index
def get_quandl_ism_nm_sdi_monthly(time):
Quandl.get("FRED/NMFSDI", authtoken= tokenName)

#ISM Non-manufacturing: NMI Composite Index
def get_quandl_ism_nm_nmici_monthly(time):
Quandl.get("FRED/NMFCI", authtoken= tokenName)

#ISM Non-manufacturing: New Export Orders Index
def get_quandl_ism_nm_neoi_monthly(time):
Quandl.get("FRED/NMFEXI", authtoken= tokenName)

#ISM Non-manufacturing: Backlog of Orders Index
def get_quandl_ism_nm_boi_monthly(time):
Quandl.get("FRED/NMFBI", authtoken= tokenName)
#ISM Non-manufacturing ends