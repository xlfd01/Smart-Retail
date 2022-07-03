# 示例代码 #
import os,sys
import win32print
printer_name = win32print.GetDefaultPrinter ()
top='\t\t\t\t----------------小票----------------\n'
persons='陈晓锋'
shop = ['苹果','草莓','香蕉']
num = [1,2,3]
money = [5,6,7]
moneyAll = 0
shopprint=''
raw_data =top+"\n\t\t\t\t商品\t\t\t\t数量\t\t\t\t价格\n"
for i in range(0,3):
    shopName = "\n\t\t\t\t" + shop[i]
    shopNum = "\t\t\t\t" + str(num[i])
    shopMoney = "\t\t\t\t" + str(money[i]) +"\t\t\t\t\n"
    moneyAll += money[i]
    shopprint+=shopName+shopNum+shopMoney
printer = "\n\n\t\t\t\t付款人："+ persons + "\t\t\t\t\t总价："+str(moneyAll)
print(raw_data+shopprint+printer)

# 示例代码 #
# import os,sys
# import win32print
# printer_name = win32print.GetDefaultPrinter ()
# if sys.version_info >= (3,):
#     raw_data =bytes ("\n\n\n\n\n\n\n\n 测试数据\n\n\n\n\n\n\n\n", "gbk")
# else:
#     raw_data = "test"
# hPrinter = win32print.OpenPrinter (printer_name)
# try:
#     hJob = win32print.StartDocPrinter (hPrinter, 1, ("test of raw data",
# None, "RAW"))
#     try:
#         win32print.StartPagePrinter (hPrinter)
#         win32print.WritePrinter (hPrinter, raw_data)
#         win32print.EndPagePrinter (hPrinter)
#     finally:
#         win32print.EndDocPrinter (hPrinter)
# finally:
#     win32print.ClosePrinter (hPrinter)