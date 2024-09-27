# การจัดการระบบการสั่งอาหารในร้านอาหาร

# เก็บข้อมูลของเมนูอาหารแต่ละจาน
class MenuItem():
    def __init__(self,menu,price,in_stock):
        self.menu = menu
        self.price = price
        self.in_stock = in_stock
    
    def show_info(self):
        return (f"เมนู: {self.menu}\n"
                f"ราคา: {self.price}\n"
                f"ของในสต็อก: {self.in_stock}\n"
                f"------------------------"
            )
        
    def __str__(self):
        return self.show_info()
        
menu1 = MenuItem("ข้าวผัด",40,20)
menu2 = MenuItem("กะเพราหมูสับ",40,20)
menu3 = MenuItem("สุกี้",40,20)
menu4 = MenuItem("ผัดไทย",40,20)
menu5 = MenuItem("ต้มยำกุ้ง",60,20)
print(menu1)
print(menu2)
print(menu3)
print(menu4)
print(menu5)