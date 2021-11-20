from kivy.app import App
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.label import Label
import csv

lastID = 2



class invenProduct():
    #TO DO: reordenar los campos para hacerlos consistentes
    prodID = 0
    name = ''
    desc = ''
    quan = 0.0
    qUnit = ''
    prot = 0.0
    carb = 0.0
    fat = 0.0
    cal = 0.0


    def __init__(self, prodID: int, name: str, desc: str, quan: float, 
                qUnit: str, prot: float, carb: float, fat: float, cal: float):
        self.prodID = prodID
        self.name = name
        self.desc = desc
        self.quan = quan
        self.qUnit = qUnit
        self.prot = prot
        self.carb = carb
        self.fat = fat
        self.cal = cal
    pass

class listaProds():
    #Gestor de la lista de productos
    freeID = 0
    prods = []
    def __init__(self):
        "self.freeID = max(self.prods, key=attrgetter('prodID')) + 1"
    def add(self, item: invenProduct):
        self.prods.append(item)
        self.freeID = self.freeID + 1
    def remove(self, prodID: int):
        for i in prods[i]:
            if i.prodID == prodID:
                self.prods.remove(i)
    def read(self):
        with open('inventory.txt', 'r') as prodFile:
            reader = csv.reader(prodFile, delimiter=',')
            firstLine = True
            for row in reader:
                if firstLine:
                    firstLine = False
                else:
                    print(row)
                    if int(row[0])>=self.freeID:
                        self.freeID = int(row[0]) + 1
                    item = invenProduct(int(row[0]), str(row[1]), str(row[2]), float(row[3]), str(row[4]), float(row[6]), float(row[7]), float(row[8]), float(row[5]))
                    self.prods.append(item)
        pass
    def write(self):
        with open('inventory.txt', 'w', newline='') as prodFile:
            prodFile.truncate()
            writer = csv.writer(prodFile, delimiter=',')
            writer.writerow(['id','name','desc','quan','qunit','cal','prot','carb','fat'])
            for item in self.prods:
                writer.writerow([str(item.prodID), item.name, item.desc, str(item.quan), item.qUnit, str(item.cal), str(item.prot), str(item.carb), str(item.fat)])
        pass

class addItemWindow(GridLayout):
    def generateItem(self):
        if self.quan.text != '':
            quan = float(self.quan.text)
        else:
            quan = 0.0
        if self.prot.text != '':
            prot = float(self.prot.text)
        else:
            prot = 0.0
        if self.carbs.text != '':
            carbs = float(self.carbs.text)
        else:
            carbs = 0.0
        if self.fat.text != '':
            fat = float(self.fat.text)
        else:
            fat = 0.0
        if self.cal.text != '':
            cal = float(self.cal.text)
        else:
            cal = 0.0
        item = invenProduct(0, self.name.text, self.desc.text, quan, self.unit.text, prot, carbs, fat, cal)
        return item
    pass

class productWindow(GridLayout):
    # comentario
    pass

class productItem(RelativeLayout):
    updateMenu = False
    prodID = 0
    def __init__(self, item: invenProduct, **kwargs):
        super(productItem, self).__init__(**kwargs)
        self.prodID = item.prodID
        self.add_widget(Label(text = str(self.prodID)))
        print(item.prodID)
        print(self.prodID)
        self.name.text = item.name
        self.quan.text = str(item.quan)
        self.unit.text = item.qUnit
    pass

class productInfo(GridLayout):
    def __init__(self, item: invenProduct, **kwargs):
        super(productInfo, self).__init__(**kwargs)
        self.name.text = item.name
        self.desc.text = item.desc
        self.quan.text = str(item.quan)
        self.unit.text = item.qUnit
        self.fat.text = str(item.fat)
        self.carbs.text = str(item.carb)
        self.prot.text = str(item.prot)
        self.cal.text = str(item.cal)
    pass


class InventoryWindow(RelativeLayout):
    item = invenProduct(0, 'pito', '', 0.0, 'kg', 0.0, 0.0, 0.0, 0.0)
    lista = listaProds()
    def __init__(self, **kwargs):
        self.lista.read()
        super(InventoryWindow, self).__init__(**kwargs)
        self.addIt = addItemWindow
        self.updateDisplay()

    def updateDisplay(self):
        self.inv_scroll.clear_widgets()
        for it in self.lista.prods:
            self.inv_scroll.add_widget(productItem(it))

    def newProd(self):
        self.addIt = addItemWindow()
        self.add_widget(self.addIt, index=0)
        self.addBut.disabled = True
    
    def closeInfo(self):
        self.remove_widget(self.prodIn)
        self.updateDisplay()
        self.addBut.disabled = False

    def prodInfo(self, prodID: int):
        item = self.item
        for x in self.lista.prods:
            if x.prodID == prodID:
                item = x
        self.prodIn = productInfo(item)
        self.add_widget(self.prodIn, index=0)
        self.addBut.disabled = True

    def addProd(self):
        self.item = self.addIt.generateItem()
        self.item.prodID = self.lista.freeID
        self.lista.add(self.item)
        self.remove_widget(self.addIt)
        self.updateDisplay()
        self.addBut.disabled = False
        self.lista.write()

    def cancelNew(self):
        self.remove_widget(self.addIt)
        self.updateDisplay()
        self.addBut.disabled = False
    pass

class inventoryApp(App):
    def build(self):
        return InventoryWindow()

if __name__=="__main__":
    lista = listaProds()
    lista.read()
    inapp = inventoryApp()
    inapp.run()
    lista.write()