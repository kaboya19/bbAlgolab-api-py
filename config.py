# USER INFO
MY_API_KEY='API-Tgw3D8GhB8GoPk0kVkXp4S1Ot+OkcYrSvBg852LE0vA=' #API Key'inizi Buraya Giriniz
MY_USERNAME = "25447086950" #TC veya Denizbank Kullanıcı Adınızı Buraya Giriniz
MY_PASSWORD = "238523" #Denizbank İnternet Bankacılığı Şifrenizi Buraya Giriniz

# URLS
hostname = "www.algolab.com.tr"
api_hostname = f"https://{hostname}"
api_url = api_hostname + "/api"
socket_url = f"wss://{hostname}/api/ws"

# ORDER STATUS
ORDER_STATUS = {0: "Bekleyen",
1: "Teslim Edildi",
2: "Gerçekleşti",
3: "Kısmi Gerçekleşti",
4: "İptal Edildi",
5: "Değiştirildi",
6: "Askıya Alındı",
7: "Süresi Doldu",
8: "Hata"}

# ENDPOINTS
URL_LOGIN_USER = "/api/LoginUser"
URL_LOGIN_CONTROL = "/api/LoginUserControl"
URL_GETEQUITYINFO = "/api/GetEquityInfo"
URL_GETSUBACCOUNTS = "/api/GetSubAccounts"
URL_INSTANTPOSITION = "/api/InstantPosition"
URL_TODAYTRANSACTION = "/api/TodaysTransaction"
URL_VIOPCUSTOMEROVERALL = "/api/ViopCustomerOverall"
URL_VIOPCUSTOMERTRANSACTIONS = "/api/ViopCustomerTransactions"
URL_SENDORDER = "/api/SendOrder"
URL_MODIFYORDER = "/api/ModifyOrder"
URL_DELETEORDER = "/api/DeleteOrder"
URL_DELETEORDERVIOP = "/api/DeleteOrderViop"
URL_SESSIONREFRESH = "/api/SessionRefresh"
URL_GETCANDLEDATA = "/api/GetCandleData"
URL_VIOPCOLLETERALINFO = "/api/ViopCollateralInfo"
URL_RISKSIMULATION = "/api/RiskSimulation"
URL_GETEQUITYORDERHISTORY = "/api/GetEquityOrderHistory"
URL_GETVIOPORDERHISTORY = "/api/GetViopOrderHistory"
URL_CASHFLOW = "/api/CashFlow"
URL_ACCOUNTEXTRE = "/api/AccountExtre"
