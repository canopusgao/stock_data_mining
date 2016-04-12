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
    "Get specific data from ISM Manufacturing Production Index from Quandl. Monthly updated data, time format: XXXX(YEAR)-XX(MONTH)-01"
    ret = Quandl.get("FRED/NAPMPI", authtoken= tokenName)
    return ret. loc[time, "VALUE"]

#ISM Manufacturing: Prices Index
def get_quandl_ism_m_pri_monthly(time):
    "Get specific data from ISM Manufacturing Prices Index from Quandl. Monthly updated data, time format: XXXX(YEAR)-XX(MONTH)-01"
    ret = Quandl.get("FRED/NAPMPRI", authtoken= tokenName)
    return ret. loc[time, "VALUE"]

#ISM Manufacturing: Imports Index
def get_quandl_ism_m_imi_monthly(time):
    "Get specific data from ISM Manufacturing Imports Index from Quandl. Monthly updated data, time format: XXXX(YEAR)-XX(MONTH)-01"
    ret = Quandl.get("FRED/NAPMIMP", authtoken= tokenName)
    return ret. loc[time, "VALUE"]

#ISM Manufacturing: PMI Composite Index
def get_quandl_ism_m_pmici_monthly(time):
    "Get specific data from ISM Manufacturing PMI Composite Index from Quandl. Monthly updated data, time format: XXXX(YEAR)-XX(MONTH)-01"
    ret = Quandl.get("FRED/NAPM", authtoken= tokenName)
    return ret. loc[time, "VALUE"]

#ISM Manufacturing: New Orders Index
def get_quandl_ism_m_noi_monthly(time):
    "Get specific data from ISM Manufacturing New Orders Index from Quandl. Monthly updated data, time format: XXXX(YEAR)-XX(MONTH)-01"
    ret = Quandl.get("FRED/NAPMNOI", authtoken= tokenName)
    return ret. loc[time, "VALUE"]

#ISM Manufacturing: Supplier Deliveries Index
def get_quandl_ism_m_sdi_monthly(time):
    "Get specific data from ISM Manufacturing Supplier Deliveries Index from Quandl. Monthly updated data, time format: XXXX(YEAR)-XX(MONTH)-01"
    ret = Quandl.get("FRED/NAPMSDI", authtoken= tokenName)
    return ret. loc[time, "VALUE"]

#ISM Manufacturing: Customer Inventories Index
def get_quandl_ism_m_cii_monthly(time):
    "Get specific data from ISM Manufacturing Customer Inventories Index Index from Quandl. Monthly updated data, time format: XXXX(YEAR)-XX(MONTH)-01"
    ret = Quandl.get("FRED/NAPMCI", authtoken= tokenName)
    return ret. loc[time, "VALUE"]

#ISM Manufacturing: Backlog of Orders Index
def get_quandl_ism_m_boi_monthly(time):
    "Get specific data from ISM Manufacturing Backlog of Orders Index from Quandl. Monthly updated data, time format: XXXX(YEAR)-XX(MONTH)-01"
    ret = Quandl.get("FRED/NAPMBI", authtoken= tokenName)
    return ret. loc[time, "VALUE"]

#ISM Manufacturing: New Export Orders Index
def get_quandl_ism_m_neoi_monthly(time):
    "Get specific data from ISM Manufacturing New Export Orders Index from Quandl. Monthly updated data, time format: XXXX(YEAR)-XX(MONTH)-01"
    ret = Quandl.get("FRED/NAPMEXI", authtoken= tokenName)
    return ret. loc[time, "VALUE"]

#ISM Manufacturing ends

#ISM Non-manufacturing starts
#ISM Non-manufacturing: Employment Index
def get_quandl_ism_nm_emi_monthly(time):
    "Get specific data from ISM Non-Manufacturing Employment Index from Quandl. Monthly updated data, time format: XXXX(YEAR)-XX(MONTH)-01"
    ret = Quandl.get("FRED/NMFEI", authtoken= tokenName)
    return ret. loc[time, "VALUE"]

#ISM Non-manufacturing: Prices Index
def get_quandl_ism_nm_pi_monthly(time):
    "Get specific data from ISM Non-Manufacturing Prices Index from Quandl. Monthly updated data, time format: XXXX(YEAR)-XX(MONTH)-01"
    ret = Quandl.get("FRED/NMFPI", authtoken= tokenName)
    return ret. loc[time, "VALUE"]

#ISM Non-manufacturing: Inventory Index
def get_quandl_ism_nm_ini_monthly(time):
    "Get specific data from ISM Non-Manufacturing Inventory Index from Quandl. Monthly updated data, time format: XXXX(YEAR)-XX(MONTH)-01"
    ret = Quandl.get("FRED/NMFINI", authtoken= tokenName)
    return ret. loc[time, "VALUE"]

#ISM Non-manufacturing: Imports Index
def get_quandl_ism_nm_imi_monthly(time):
    "Get specific data from ISM Non-Manufacturing Imports Index from Quandl. Monthly updated data, time format: XXXX(YEAR)-XX(MONTH)-01"
    ret = Quandl.get("FRED/NMFIMI", authtoken= tokenName)
    return ret. loc[time, "VALUE"]

#ISM Non-manufacturing: Business Activity Index
def get_quandl_ism_nm_bai_monthly(time):
    "Get specific data from ISM Non-Manufacturing Business Activity Index from Quandl. Monthly updated data, time format: XXXX(YEAR)-XX(MONTH)-01"
    ret = Quandl.get("FRED/NMFBAI", authtoken= tokenName)
    return ret. loc[time, "VALUE"]

#ISM Non-manufacturing: New Orders Index
def get_quandl_ism_nm_noi_monthly(time):
    "Get specific data from ISM Non-Manufacturing New Orders Index from Quandl. Monthly updated data, time format: XXXX(YEAR)-XX(MONTH)-01"
    ret = Quandl.get("FRED/NMFNOI", authtoken= tokenName)
    return ret. loc[time, "VALUE"]

#ISM Non-manufacturing: Inventory Sentiment Index
def get_quandl_ism_nm_isi_monthly(time):
    "Get specific data from ISM Non-Manufacturing Inventory Sentiment Index from Quandl. Monthly updated data, time format: XXXX(YEAR)-XX(MONTH)-01"
    ret = Quandl.get("FRED/NMFINSI", authtoken= tokenName)
    return ret. loc[time, "VALUE"]

#ISM Non-manufacturing: Supplier Deliveries Index
def get_quandl_ism_nm_sdi_monthly(time):
    "Get specific data from ISM Non-Manufacturing Supplier Deliveries Index from Quandl. Monthly updated data, time format: XXXX(YEAR)-XX(MONTH)-01"
    ret = Quandl.get("FRED/NMFSDI", authtoken= tokenName)
    return ret. loc[time, "VALUE"]

#ISM Non-manufacturing: NMI Composite Index
def get_quandl_ism_nm_nmici_monthly(time):
    "Get specific data from ISM Non-Manufacturing NMI Composite Index from Quandl. Monthly updated data, time format: XXXX(YEAR)-XX(MONTH)-01"
    ret = Quandl.get("FRED/NMFCI", authtoken= tokenName)
    return ret. loc[time, "VALUE"]

#ISM Non-manufacturing: New Export Orders Index
def get_quandl_ism_nm_neoi_monthly(time):
    "Get specific data from ISM Non-Manufacturing New Export Orders Index from Quandl. Monthly updated data, time format: XXXX(YEAR)-XX(MONTH)-01"
    ret = Quandl.get("FRED/NMFEXI", authtoken= tokenName)
    return ret. loc[time, "VALUE"]

#ISM Non-manufacturing: Backlog of Orders Index
def get_quandl_ism_nm_boi_monthly(time):
    "Get specific data from ISM Non-Manufacturing Backlog of Orders Index from Quandl. Monthly updated data, time format: XXXX(YEAR)-XX(MONTH)-01"
    ret = Quandl.get("FRED/NMFBI", authtoken= tokenName)
    return ret. loc[time, "VALUE"]
#ISM Non-manufacturing ends


ret = Quandl.get("YAHOO/INDEX_GSPC", authtoken="CVQWV6wLVWnrgjsVbc4g")
print ret.head(5)