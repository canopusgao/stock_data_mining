import Quandl
#from networkx.utils.decorators import open_file

tokenName = "CVQWV6wLVWnrgjsVbc4g"

#ISM Manufacturing starts
#ISM Manufacturing: Inventories Index
def get_quandl_ism_m_ii_monthly(time):
    "Get specific data from ISM Manufacturing Inventories Index from Quandl. Monthly updated data, time format: XXXX(YEAR)-XX(MONTH)-01"
    ret = Quandl.get("FRED/NAPMII", authtoken= tokenName)
    if time in ret.index:
        return ret.loc[time,"VALUE"]
    else :
        return -1
    

#ISM Manufacturing: Employment Index
def get_quandl_ism_m_ei_monthly(time):
    "Get specific data from ISM Manufacturing Employment Index from Quandl. Monthly updated data, time format: XXXX(YEAR)-XX(MONTH)-01"
    ret = Quandl.get("FRED/NAPMEI", authtoken= tokenName)
    if time in ret.index:
        return ret.loc[time,"VALUE"]
    else :
        return -1


#ISM Manufacturing: Production Index
def get_quandl_ism_m_pi_monthly(time):
    "Get specific data from ISM Manufacturing Production Index from Quandl. Monthly updated data, time format: XXXX(YEAR)-XX(MONTH)-01"
    ret = Quandl.get("FRED/NAPMPI", authtoken= tokenName)
    if time in ret.index:
        return ret.loc[time,"VALUE"]
    else :
        return -1

#ISM Manufacturing: Prices Index
def get_quandl_ism_m_pri_monthly(time):
    "Get specific data from ISM Manufacturing Prices Index from Quandl. Monthly updated data, time format: XXXX(YEAR)-XX(MONTH)-01"
    ret = Quandl.get("FRED/NAPMPRI", authtoken= tokenName)
    if time in ret.index:
        return ret.loc[time,"VALUE"]
    else :
        return -1

#ISM Manufacturing: Imports Index
def get_quandl_ism_m_imi_monthly(time):
    "Get specific data from ISM Manufacturing Imports Index from Quandl. Monthly updated data, time format: XXXX(YEAR)-XX(MONTH)-01"
    ret = Quandl.get("FRED/NAPMIMP", authtoken= tokenName)
    if time in ret.index:
        return ret.loc[time,"VALUE"]
    else :
        return -1

#ISM Manufacturing: PMI Composite Index
def get_quandl_ism_m_pmici_monthly(time):
    "Get specific data from ISM Manufacturing PMI Composite Index from Quandl. Monthly updated data, time format: XXXX(YEAR)-XX(MONTH)-01"
    ret = Quandl.get("FRED/NAPM", authtoken= tokenName)
    if time in ret.index:
        return ret.loc[time,"VALUE"]
    else :
        return -1

#ISM Manufacturing: New Orders Index
def get_quandl_ism_m_noi_monthly(time):
    "Get specific data from ISM Manufacturing New Orders Index from Quandl. Monthly updated data, time format: XXXX(YEAR)-XX(MONTH)-01"
    ret = Quandl.get("FRED/NAPMNOI", authtoken= tokenName)
    if time in ret.index:
        return ret.loc[time,"VALUE"]
    else :
        return -1

#ISM Manufacturing: Supplier Deliveries Index
def get_quandl_ism_m_sdi_monthly(time):
    "Get specific data from ISM Manufacturing Supplier Deliveries Index from Quandl. Monthly updated data, time format: XXXX(YEAR)-XX(MONTH)-01"
    ret = Quandl.get("FRED/NAPMSDI", authtoken= tokenName)
    if time in ret.index:
        return ret.loc[time,"VALUE"]
    else :
        return -1

#ISM Manufacturing: Customer Inventories Index
def get_quandl_ism_m_cii_monthly(time):
    "Get specific data from ISM Manufacturing Customer Inventories Index Index from Quandl. Monthly updated data, time format: XXXX(YEAR)-XX(MONTH)-01"
    ret = Quandl.get("FRED/NAPMCI", authtoken= tokenName)
    if time in ret.index:
        return ret.loc[time,"VALUE"]
    else :
        return -1

#ISM Manufacturing: Backlog of Orders Index
def get_quandl_ism_m_boi_monthly(time):
    "Get specific data from ISM Manufacturing Backlog of Orders Index from Quandl. Monthly updated data, time format: XXXX(YEAR)-XX(MONTH)-01"
    ret = Quandl.get("FRED/NAPMBI", authtoken= tokenName)
    if time in ret.index:
        return ret.loc[time,"VALUE"]
    else :
        return -1

#ISM Manufacturing: New Export Orders Index
def get_quandl_ism_m_neoi_monthly(time):
    "Get specific data from ISM Manufacturing New Export Orders Index from Quandl. Monthly updated data, time format: XXXX(YEAR)-XX(MONTH)-01"
    ret = Quandl.get("FRED/NAPMEXI", authtoken= tokenName)
    if time in ret.index:
        return ret.loc[time,"VALUE"]
    else :
        return -1

#ISM Manufacturing ends

#ISM Non-manufacturing starts
#ISM Non-manufacturing: Employment Index
def get_quandl_ism_nm_emi_monthly(time):
    "Get specific data from ISM Non-Manufacturing Employment Index from Quandl. Monthly updated data, time format: XXXX(YEAR)-XX(MONTH)-01"
    ret = Quandl.get("FRED/NMFEI", authtoken= tokenName)
    if time in ret.index:
        return ret.loc[time,"VALUE"]
    else :
        return -1

#ISM Non-manufacturing: Prices Index
def get_quandl_ism_nm_pi_monthly(time):
    "Get specific data from ISM Non-Manufacturing Prices Index from Quandl. Monthly updated data, time format: XXXX(YEAR)-XX(MONTH)-01"
    ret = Quandl.get("FRED/NMFPI", authtoken= tokenName)
    if time in ret.index:
        return ret.loc[time,"VALUE"]
    else :
        return -1

#ISM Non-manufacturing: Inventory Index
def get_quandl_ism_nm_ini_monthly(time):
    "Get specific data from ISM Non-Manufacturing Inventory Index from Quandl. Monthly updated data, time format: XXXX(YEAR)-XX(MONTH)-01"
    ret = Quandl.get("FRED/NMFINI", authtoken= tokenName)
    if time in ret.index:
        return ret.loc[time,"VALUE"]
    else :
        return -1

#ISM Non-manufacturing: Imports Index
def get_quandl_ism_nm_imi_monthly(time):
    "Get specific data from ISM Non-Manufacturing Imports Index from Quandl. Monthly updated data, time format: XXXX(YEAR)-XX(MONTH)-01"
    ret = Quandl.get("FRED/NMFIMI", authtoken= tokenName)
    if time in ret.index:
        return ret.loc[time,"VALUE"]
    else :
        return -1

#ISM Non-manufacturing: Business Activity Index
def get_quandl_ism_nm_bai_monthly(time):
    "Get specific data from ISM Non-Manufacturing Business Activity Index from Quandl. Monthly updated data, time format: XXXX(YEAR)-XX(MONTH)-01"
    ret = Quandl.get("FRED/NMFBAI", authtoken= tokenName)
    if time in ret.index:
        return ret.loc[time,"VALUE"]
    else :
        return -1

#ISM Non-manufacturing: New Orders Index
def get_quandl_ism_nm_noi_monthly(time):
    "Get specific data from ISM Non-Manufacturing New Orders Index from Quandl. Monthly updated data, time format: XXXX(YEAR)-XX(MONTH)-01"
    ret = Quandl.get("FRED/NMFNOI", authtoken= tokenName)
    if time in ret.index:
        return ret.loc[time,"VALUE"]
    else :
        return -1

#ISM Non-manufacturing: Inventory Sentiment Index
def get_quandl_ism_nm_isi_monthly(time):
    "Get specific data from ISM Non-Manufacturing Inventory Sentiment Index from Quandl. Monthly updated data, time format: XXXX(YEAR)-XX(MONTH)-01"
    ret = Quandl.get("FRED/NMFINSI", authtoken= tokenName)
    if time in ret.index:
        return ret.loc[time,"VALUE"]
    else :
        return -1

#ISM Non-manufacturing: Supplier Deliveries Index
def get_quandl_ism_nm_sdi_monthly(time):
    "Get specific data from ISM Non-Manufacturing Supplier Deliveries Index from Quandl. Monthly updated data, time format: XXXX(YEAR)-XX(MONTH)-01"
    ret = Quandl.get("FRED/NMFSDI", authtoken= tokenName)
    if time in ret.index:
        return ret.loc[time,"VALUE"]
    else :
        return -1

#ISM Non-manufacturing: NMI Composite Index
def get_quandl_ism_nm_nmici_monthly(time):
    "Get specific data from ISM Non-Manufacturing NMI Composite Index from Quandl. Monthly updated data, time format: XXXX(YEAR)-XX(MONTH)-01"
    ret = Quandl.get("FRED/NMFCI", authtoken= tokenName)
    if time in ret.index:
        return ret.loc[time,"VALUE"]
    else :
        return -1

#ISM Non-manufacturing: New Export Orders Index
def get_quandl_ism_nm_neoi_monthly(time):
    "Get specific data from ISM Non-Manufacturing New Export Orders Index from Quandl. Monthly updated data, time format: XXXX(YEAR)-XX(MONTH)-01"
    ret = Quandl.get("FRED/NMFEXI", authtoken= tokenName)
    if time in ret.index:
        return ret.loc[time,"VALUE"]
    else :
        return -1

#ISM Non-manufacturing: Backlog of Orders Index
def get_quandl_ism_nm_boi_monthly(time):
    "Get specific data from ISM Non-Manufacturing Backlog of Orders Index from Quandl. Monthly updated data, time format: XXXX(YEAR)-XX(MONTH)-01"
    ret = Quandl.get("FRED/NMFBI", authtoken= tokenName)
    if time in ret.index:
        return ret.loc[time,"VALUE"]
    else :
        return -1
#ISM Non-manufacturing ends


#S&P 500 index
def get_quandl_sp500idx_monthly(time):
    "Get specific data of s&p 500 index from Quandl. Daily updated monthly average data, time format: XXXX(YEAR)-XX(MONTH)"
    ret = Quandl.get("YAHOO/INDEX_GSPC", authtoken= tokenName)
#    print ret
    if time in ret.index:
        ret_temp = ret.loc[time,'Close']
        num1=0
        numCnt = 0
        for iter0 in ret_temp.index:
            numCnt = numCnt + 1
            num1 = num1 + ret_temp.loc[iter0]
    
        return num1/numCnt
    
    else:
        return -1

lista = []
file1 = open('1.txt','w')

for yearN in range(2005,2006):
    for Month in range(1,13):
        if yearN == 2016 and Month == 5:
            break
        if Month<=9:
            timeq = str(yearN)+'-0'+str(Month)+'-01'
            timeq_sp = str(yearN)+'-0'+str(Month)
        else:
            timeq = str(yearN)+'-'+str(Month)+'-01'
            timeq_sp = str(yearN)+'-'+str(Month)
            
        file1 = open(str(timeq_sp)+'.txt','w')        
        print timeq
        print timeq_sp
        lista.append(get_quandl_ism_m_ii_monthly(timeq))
        print lista
        lista.append(get_quandl_ism_m_ei_monthly(timeq))
        print lista
#        lista.append(get_quandl_ism_m_pi_monthly(timeq))
#        print lista
#        lista.append(get_quandl_ism_m_pri_monthly(timeq))
#        print lista
#        lista.append(get_quandl_ism_m_imi_monthly(timeq))
#        print lista
#        lista.append(get_quandl_ism_m_pmici_monthly(timeq))
#        print lista
#        lista.append(get_quandl_ism_m_sdi_monthly(timeq))
#        print lista
#        lista.append(get_quandl_ism_m_cii_monthly(timeq))
#        print lista
#        lista.append(get_quandl_ism_m_boi_monthly(timeq))
#        print lista
#        lista.append(get_quandl_ism_m_neoi_monthly(timeq))
#        print lista
#        lista.append(get_quandl_ism_m_noi_monthly(timeq))
#        print lista
#        lista.append(get_quandl_ism_nm_emi_monthly(timeq))
#        print lista
#        lista.append(get_quandl_ism_nm_pi_monthly(timeq))
#        print lista
#        lista.append(get_quandl_ism_nm_ini_monthly(timeq))
#        print lista
#        lista.append(get_quandl_ism_nm_imi_monthly(timeq))
#        print lista
#        lista.append(get_quandl_ism_nm_bai_monthly(timeq))
#        print lista
#        lista.append(get_quandl_ism_nm_noi_monthly(timeq))
#        print lista
#        lista.append(get_quandl_ism_nm_isi_monthly(timeq))
#        print lista
#        lista.append(get_quandl_ism_nm_sdi_monthly(timeq))
#        print lista
#        lista.append(get_quandl_ism_nm_nmici_monthly(timeq))
#        print lista
#        lista.append(get_quandl_ism_nm_neoi_monthly(timeq))
#        print lista
#        lista.append(get_quandl_ism_nm_boi_monthly(timeq))
#        print lista
#        lista.append(get_quandl_sp500idx_monthly(timeq_sp))
        
        print lista
        
        print len(lista)
        for i in range (len(lista)):
            print lista[i]
            file1.write(str(lista[i]))
            file1.write('\t')
        file1.write('\n')
        file1.close()  
        
        del lista[:]