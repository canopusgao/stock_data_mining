import Quandl

tokenName = "CVQWV6wLVWnrgjsVbc4g"

#ISM Manufacturing starts
#ISM Manufacturing: Inventories Index
def get_quandl_ISM_M_II_Monthly(time):
    "Get specific data from ISM Manufacturing Inventories Index from Quandl. Monthly updated data, time format: XXXX(YEAR)-XX(MONTH)-01"
    ret = Quandl.get("FRED/NAPMII", authtoken= tokenName)
    return ret.loc[time,"VALUE"]
    

#ISM Manufacturing: Employment Index
Quandl.get("FRED/NAPMEI", authtoken="CVQWV6wLVWnrgjsVbc4g")

#ISM Manufacturing: Production Index
Quandl.get("FRED/NAPMPI", authtoken="CVQWV6wLVWnrgjsVbc4g")

#ISM Manufacturing: Prices Index
Quandl.get("FRED/NAPMPRI", authtoken="CVQWV6wLVWnrgjsVbc4g")

#ISM Manufacturing: Imports Index
Quandl.get("FRED/NAPMIMP", authtoken="CVQWV6wLVWnrgjsVbc4g")

#ISM Manufacturing: PMI Composite Index
Quandl.get("FRED/NAPM", authtoken="CVQWV6wLVWnrgjsVbc4g")

#ISM Manufacturing: New Orders Index
Quandl.get("FRED/NAPMNOI", authtoken="CVQWV6wLVWnrgjsVbc4g")

#ISM Manufacturing: Supplier Deliveries Index
Quandl.get("FRED/NAPMSDI", authtoken="CVQWV6wLVWnrgjsVbc4g")

#ISM Manufacturing: Customer Inventories Index
Quandl.get("FRED/NAPMCI", authtoken="CVQWV6wLVWnrgjsVbc4g")

#ISM Manufacturing: Backlog of Orders Index
Quandl.get("FRED/NAPMBI", authtoken="CVQWV6wLVWnrgjsVbc4g")

#ISM Manufacturing: New Export Orders Index
Quandl.get("FRED/NAPMEXI", authtoken="CVQWV6wLVWnrgjsVbc4g")

#ISM Manufacturing ends

#ISM Non-manufacturing starts
#ISM Non-manufacturing: Employment Index
Quandl.get("FRED/NMFEI", authtoken="CVQWV6wLVWnrgjsVbc4g")

#ISM Non-manufacturing: Prices Index
Quandl.get("FRED/NMFPI", authtoken="CVQWV6wLVWnrgjsVbc4g")

#ISM Non-manufacturing: Inventory Index
Quandl.get("FRED/NMFINI", authtoken="CVQWV6wLVWnrgjsVbc4g")

#ISM Non-manufacturing: Imports Index
Quandl.get("FRED/NMFIMI", authtoken="CVQWV6wLVWnrgjsVbc4g")

#ISM Non-manufacturing: Business Activity Index
Quandl.get("FRED/NMFBAI", authtoken="CVQWV6wLVWnrgjsVbc4g")

#ISM Non-manufacturing: New Orders Index
Quandl.get("FRED/NMFNOI", authtoken="CVQWV6wLVWnrgjsVbc4g")

#ISM Non-manufacturing: Inventory Sentiment Index
Quandl.get("FRED/NMFINSI", authtoken="CVQWV6wLVWnrgjsVbc4g")

#ISM Non-manufacturing: Supplier Deliveries Index
Quandl.get("FRED/NMFSDI", authtoken="CVQWV6wLVWnrgjsVbc4g")

#ISM Non-manufacturing: NMI Composite Index
Quandl.get("FRED/NMFCI", authtoken="CVQWV6wLVWnrgjsVbc4g")

#ISM Non-manufacturing: New Export Orders Index
Quandl.get("FRED/NMFEXI", authtoken="CVQWV6wLVWnrgjsVbc4g")

#ISM Non-manufacturing: Backlog of Orders Index
Quandl.get("FRED/NMFBI", authtoken="CVQWV6wLVWnrgjsVbc4g")
#ISM Non-manufacturing ends