#!/usr/bin/env python3

import yaml
from collections import UserList
import matplotlib.pyplot as plt

class Payslip:
    def __init__(self, payslip):
         self.period = str(payslip["period"]["year"]) +"-"+ str(payslip["period"]["month"])
         self.kind = payslip["kind"]
         self.payment_items = payslip["payment"]["items"]
         self.payment_total = payslip["payment"]["total"]
         self.deduction_items = payslip["deduction"]["items"] 
         self.deduction_total = payslip["deduction"]["total"] 
         self.netpayment = payslip["netpayment"]

    def payment_check(self):
        payment_item_sum = 0
        for v in self.payment["items"]:
            payment_item_sum += int(v["amount"])
        print(self.period, "payment check   :",end="")
        if(payment_item_sum == int(self.payment["total"])):
            print("OK")
        else:
            print("NG")
            print("payment_item_sum:", payment_item_sum)
            print("payment[\"total\"]:", self.payment["total"])

    def deduction_check(self):
        deduction_item_sum = 0
        for v in self.dedction["items"]:
            dedction_item_sum += int(v["amount"])
        print(self.period, "dedction check   : ",end="")
        if(dedction_item_sum == int(self.dedction["total"])):
            print("OK")
        else:
            print("NG")
            print("dedction_item_sum:", dedction_item_sum)
            print("dedction[\"total\"]:", self.dedction["total"])

    def netpayment_check(self):
        netpayment_item_sum = 0
        for v in self.netpayment["items"]:
            netpayment_item_sum += int(v["amount"])
        print(self.period, "payment check   : ",end="")
        if(netpayment_item_sum == int(self.payment["total"]) - int(self.deduction["total"])):
            print("OK")
        else:
            print("NG")
            print("payment[\"total\"]  :", self.payment["total"])
            print("deduction[\"total\"]:", self.payment["total"])
            print("netpayment[\"total\"]:", self.netpayment["total"])


class Payslip_monthly(Payslip):
    def __init__(self,payslip):
        super().__init__(payslip)
        self.overtime = payslip["overtime"]



input_file = open('salary.yaml')
list_payslip_monthly = []
list_payslip_bonus = []
for data in yaml.load_all(input_file, Loader=yaml.SafeLoader):
    if(data["kind"] == "monthly"):
        payslip = Payslip_monthly(data)
        list_payslip_monthly.append(payslip)
    elif(data["kind"] == "bonus"):
        payslip = Payslip(data)
        list_payslip_bonus.append(payslip)
    else:
        continue



# plot test
date = []
overtime = []
for payslip in list_payslip_monthly:
    print(payslip.period, payslip.overtime)
    date.append(payslip.period)
    overtime.append(payslip.overtime)

fig, ax = plt.subplots()
fig.autofmt_xdate()
ax.grid(visible="True",axis="y",linestyle='--')
ax.plot(date, overtime, label="overtime")
ax.set(xlabel="month", ylabel="overtime")
ax.set_title('monthly overtime')
plt.show()
