from binance.client import Client
from binance.enums import *
import time
from datetime import datetime
from binance.enums import *
import math
import calendar

api_key ='jRbf0dNViSFiiaXB0172IkzXgyIaXaOIzxMDGzIQAdHCAmUUfajL96XM9j7le5iR'
api_secret ='5O8Nn5EcBMpDutTSebqN7ybkwK5SpgdPcWdekZGVJwxspicH0mDEItz4KKrBgaMf'

client = Client(api_key, api_secret)
#o = client.get_exchange_info()
#print(o)
def run():
    while 1:
        try:
            initialize_arb()
        except Exception as e: print(e)
    pass
global q
global cant1,cant2,cant3
global rate1,rate2,rate3
global pre_tax1,pre_tax2,pre_tax3
global tax1,tax2,tax3
global i
global price1,price2,price3
def initialize_arb():
    print("start")
    print("\n")
    d = datetime.utcnow()
    unixtime = calendar.timegm(d.utctimetuple())
    print(unixtime)
    list_of_symbols2 = ['BNBBTC', 'ADABNB', 'ADABTC']
    list_of_symbols3 = ['BNBBTC', 'ADXBNB', 'ADXBTC']
    list_of_symbols4 = ['BNBBTC', 'AEBNB', 'AEBTC']
    list_of_symbols5 = ['BNBBTC', 'AGIBNB', 'AGIBTC']
    list_of_symbols6 = ['BNBBTC', 'AIONBNB', 'AIONBTC']
    list_of_symbols7 = ['BNBBTC', 'AMBBNB', 'AMBBTC']
    list_of_symbols8 = ['BNBBTC', 'APPCBNB', 'APPCBTC']
    list_of_symbols9 = ['BNBBTC', 'ARDRBNB', 'ARDRBTC']
    list_of_symbols10 = ['BNBBTC', 'BATBNB', 'BATBTC']
    list_of_symbols12 = ['BNBBTC', 'BCPTBNB', 'BCPTBTC']
    list_of_symbols13 = ['BNBBTC', 'BLZBNB', 'BLZBTC']
    list_of_symbols14 = ['BNBBTC', 'BRDBNB', 'BRDBTC']
    list_of_symbols15 = ['BNBBTC', 'BTSBNB', 'BTSBTC']
    list_of_symbols16 = ['BNBBTC', 'CMTBNB', 'CMTBTC']
    list_of_symbols17 = ['BNBBTC', 'CNDBNB', 'CNDBTC']
    list_of_symbols18 = ['BNBBTC', 'CVCBNB', 'CVCBTC']
    list_of_symbols19 = ['BNBBTC', 'DLTBNB', 'DLTBTC']
    list_of_symbols20 = ['BNBBTC', 'ENJBNB', 'ENJBTC']
    list_of_symbols21 = ['BNBBTC', 'EOSBNB', 'EOSBTC']
    list_of_symbols22 = ['BNBBTC', 'ETCBNB', 'ETCBTC']
    list_of_symbols23 = ['BNBBTC', 'GNTBNB', 'GNTBTC']
    list_of_symbols24 = ['BNBBTC', 'GTOBNB', 'GTOBTC']
    list_of_symbols25 = ['BNBBTC', 'ICXBNB', 'ICXBTC']
    list_of_symbols26 = ['BNBBTC', 'IOTABNB', 'IOTABTC']
    list_of_symbols27 = ['BNBBTC', 'LOOMBNB', 'LOOMBTC']
    list_of_symbols28 = ['BNBBTC', 'LSKBNB', 'LSKBTC']
    list_of_symbols29 = ['BNBBTC', 'LTCBNB', 'LTCBTC']
    list_of_symbols30 = ['BNBBTC', 'MCOBNB', 'MCOBTC']
    list_of_symbols31 = ['BNBBTC', 'MFTBNB', 'MFTBTC']
    list_of_symbols32 = ['BNBBTC', 'NANOBNB', 'NANOBTC']
    list_of_symbols33 = ['BNBBTC', 'NASBNB', 'NASBTC']
    list_of_symbols34 = ['BNBBTC', 'NAVBNB', 'NAVBTC']
    list_of_symbols35 = ['BNBBTC', 'NCASHBNB', 'NCASHBTC']
    list_of_symbols36 = ['BNBBTC', 'NEBLBNB', 'NEBLBTC']
    list_of_symbols37 = ['BNBBTC', 'NEOBNB', 'NEOBTC']
    list_of_symbols38 = ['BNBBTC', 'NULSBNB', 'NULSBTC']
    list_of_symbols39 = ['BNBBTC', 'NXSBNB', 'NXSBTC']
    list_of_symbols40 = ['BNBBTC', 'ONTBNB', 'ONTBTC']
    list_of_symbols41 = ['BNBBTC', 'OSTBNB', 'OSTBTC']
    list_of_arb_sym = [list_of_symbols2,list_of_symbols3,list_of_symbols4,list_of_symbols5,list_of_symbols6
        ,list_of_symbols7,list_of_symbols8,list_of_symbols9,list_of_symbols10,list_of_symbols12
        ,list_of_symbols13,list_of_symbols14,list_of_symbols15,list_of_symbols16,list_of_symbols17,list_of_symbols18
        ,list_of_symbols19,list_of_symbols20,list_of_symbols21,list_of_symbols22,list_of_symbols23,list_of_symbols24
        ,list_of_symbols25,list_of_symbols26,list_of_symbols27,list_of_symbols28,list_of_symbols29,list_of_symbols30
        ,list_of_symbols31,list_of_symbols32,list_of_symbols33,list_of_symbols34,list_of_symbols35,list_of_symbols36
        ,list_of_symbols37,list_of_symbols38,list_of_symbols39,list_of_symbols40,list_of_symbols41]
    rup = balanta("BTC")
    q = float(rup['free'][:10])
    c=0
    while 1:
        for arb_market in list_of_arb_sym:
            i=0
            for sym in arb_market:
                timp=[]
                depth = client.get_order_book(symbol=sym)
                if i % 3 == 0:
                    price1 = float(depth['bids'][0][0])
                    #vzt[c]=1
                    c+= 1
                    print(sym)
                    print("Exchange rate: " + str(price1))
                if i % 3 == 1:
                    price2 =  float(depth['bids'][0][0])
                    #vzt[c]=1
                    c+= 1
                    print(sym)
                    print("Exchange rate: " + str(price2))
                if i % 3 == 2:
                    price3 = float(depth['asks'][0][0])
                    #vzt[c]=1
                    c+= 1
                    print(sym)
                    print("Exchange rate: " + str(price3))
                    print('\n')
                i +=1
            if (i-1) % 3 ==2:
                rate1  = float(price1/price3)
                rate2 =  float(price1/price2)
                rate3 =  float(price2/price3)
                if  rate1 > price2 or price1 < rate3 or rate2 > price3:
                    ceva = float(arbitrage_bin(float(q),price1,price2,price3))
                    if ceva > q:
                        q = ceva
                        c1 = arb_market[0]
                        c1_1 = c1[3:]
                        real_cant1 = balanta(c1_1)
                        #vzt[c]=1
                        c+= 1
                        real_cant1_final = float(real_cant1['free'][:10])
                        quant1 = round(float(real_cant1_final / price1),5)
                        print(real_cant1_final)
                        print(quant1)
                        order_buy(arb_market[0],price1,quant1)
                        c+= 1
                        c2 = arb_market[1]
                        c2_2 = c2[3:]
                        real_cant2 = balanta(c2_2)
                        c+= 1
                        real_cant2_final = float(real_cant2['free'][:10])
                        quant2 = round((real_cant2_final / price2),5)
                        quant2_ceil = math.ceil(quant2)
                        print(real_cant2_final)
                        order_buy(arb_market[1],price2,quant2)
                        c+= 1
                        c3 = arb_market[2]
                        c3_3 = c3[3:]
                        real_cant3 = balanta(c3_3)
                        #vzt[c]=1
                        c+= 1
                        real_cant3_final = float(real_cant3['free'][:10])
                        quant = round(float(real_cant3_final * price3),5)
                        print(real_cant3_final)
                        order_sell(arb_market[2],price3,quant)
                        c+= 1
                        profit = real_cant1_final - initial
                        print("Balanta este:" , balanta(c1_1))
                    else:
                        print("Nu se poate sef")
                        y = datetime.utcnow()
                        unixtime2 = calendar.timegm(y.utctimetuple())
                        if(c/(unixtime2-unixtime)<=30):
                            print("Am facut: " + str(c) + " operatii in " + str(unixtime2-unixtime) + " secunde  si fac: " + str(c/(unixtime2-unixtime)) + " operatii in 1 secunda")
                        print("\n")
def arbitrage_bin(quant,price1,price2,price3):
    fees = 0.001
    cant2 = 0
    cant3 = 0
    pre_tax2= float(float(quant*fees) / price1)
    #tax2 = float(float(fees) * pre_tax2)
    #cant2 = float(pre_tax2 - tax2)
    pre_tax3= float (cant2*fees / price2)
    #tax3 = float(float(fees) * pre_tax3)
    #cant3 = float(pre_tax3 - tax3)
    pre_tax1 = float(price3 * cant3 * fees)
    #tax1 = float(float(fees) * pre_tax1)
    #cant1 = float(pre_tax1- tax1)
    if float(pre_tax1 > float(quant)) :
        ok=1
    else :
        ok=0
    if(ok==1):
        return quant
    else:
        return quant
def order_buy(sym,price,cant):
    order = client.create_order (symbol=sym,
                        side=SIDE_BUY,
                        type=ORDER_TYPE_LIMIT,
                        quantity=cant,
                        price=price,
                        timeInForce=TIME_IN_FORCE_GTC)
def order_sell(sym,price,cant):
    order = client.create_order (symbol=sym,
                        side=SIDE_SELL,
                        type=ORDER_TYPE_LIMIT,
                        quantity=cant,
                        price=price,
                        timeInForce=TIME_IN_FORCE_GTC)
def balanta(sym):
    cat = client.get_asset_balance(sym)
    return cat
if __name__ == "__main__":
    run()
