import requests
from bs4 import BeautifulSoup
import re

class tsectc:
    link1="http://members.tsetmc.com/tsev2/data/MarketWatchPlus.aspx?d=0&format=0"
    listall = []
    goodlist = []
    def __int__(self):
        self.link1=""


    def getDuplicatesWithInfo(self,listOfElems):
        dictOfElems = dict()
        index = 0
        for elem in listOfElems:
            if elem in dictOfElems:
                dictOfElems[elem][0] += 1
                dictOfElems[elem][1].append(index)
            else:
                dictOfElems[elem] = [1, [index]]
            index += 1
        dictOfElems = {key: value for key, value in dictOfElems.items() if value[0] > 1}
        return dictOfElems

    def getfirstdata(self):
        html = requests.get(
            "http://members.tsetmc.com/tsev2/data/MarketWatchPlus.aspx?d=0&format=0")  # اطلاعات لحظه ای 23 موردی در دیده بان بازار
        soup = BeautifulSoup(html.text, 'lxml')
        text = soup.text
        newtext = text.split("@")
        alltext = newtext[2]
        alltext = alltext.split(";")
        for i in range(0, len(alltext), 1):
            self.listall.append(alltext[i].split(","))
        return self.listall

    def urlmaker(self,id):
        return "http://www.tsetmc.com/tsev2/data/TradeDetail.aspx?i=" + str(id)

    def checking(self,qty, time, x):
        for key, value in qty.items():
            if (value[0] > 5 and int(key) > 5001):
                repeattime = []
                for j in range(0, len(value[1]) - 1, 1):
                    repeattime.append(time[value[1][j]])
                newdic = self.getDuplicatesWithInfo(repeattime)
                for kt, vt in newdic.items():
                    if (vt[0] > 4):
                        print(
                            "کد به کد در زمان :" + repeattime[vt[1][0]] + "و حجم : " + key + "دفعات تکرار" + str(vt[0]))
                        percent = round(
                            ((float(self.listall[x][7]) - float(self.listall[x][13])) / (float(self.listall[x][13]))) * 100, 2)
                        self.goodlist.append([self.listall[x][2], vt[0], key, repeattime[vt[1][0]], percent])
                        if (True): #percent < -4
                            self.goodlist.append([self.listall[x][2],vt[0],key,repeattime[vt[1][0]],percent])
                            #print("##")
        return self.goodlist

    def check(self):
        self.getfirstdata()
        for ii in range(0, len(self.listall), 1):
            #print(str(self.listall[ii][2]))
            html2 = requests.get(self.urlmaker(self.listall[ii][0]))
            x = re.findall(r"<cell>([\(.|:)\d]*)</cell>", html2.text)  # re.findall(r"hEven..([\.\d]*),",txt)
            listalldetail = []
            qty = []
            time = []
            for j in range(0, len(x), 4):
                listalldetail.append([x[j], x[j + 1], x[j + 2], x[j + 3]])
                qty.append(x[j + 2])
                time.append(x[j + 1])
            # print(listalldetail)
            # print(len(listalldetail))
            if ((len(listalldetail) > 100) and ((bool(re.search(r'\d', self.listall[ii][2])) == False))):
                # check code to code
                dict_qty = self.getDuplicatesWithInfo(qty)
                # print(qty)
                self.checking(dict_qty, time, ii)
                print(str(self.listall[ii][2]))
                print("******* Checked ********")
        return self.goodlist