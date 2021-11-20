class InvenProduct():
    #TO DO: reordenar los campos para hacerlos consistentes
    prodID = 0
    name = ''
    desc = ''
    quan = 0.0
    qUnit = ''
    cal = 0.0
    prot = 0.0
    carb = 0.0
    fat = 0.0

    def __init__(self, prodID: int, name: str, desc: str, quan: float, 
                qUnit: str, cal: float, prot: float, carb: float, fat: float):
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