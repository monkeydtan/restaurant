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
    
    # quantity จะมีค่าเท่ากับจำนวนจานที่ลูกค้าสั่งไป    
    def reduce_stock(self,quantity):
        if quantity < self.in_stock:
            self.in_stock -= quantity
            return f"สั่งเมนู {self.menu} จำนวน {quantity} จาน"
        else:
            return f"ของในสต็อกไม่เพียงพอต่อการเสิร์ฟ"
        
    def __str__(self):
        return self.show_info()

# ข้อมูลลูกค้า
class Customer:
    def __init__(self,name,budget):
        self.name = name
        self.budget = budget # งบตอนแรก
        self.budget_pay = budget # งบที่เหลือ
    
    # การสั่งอาหาร    
    def order_food(self,menu_item,quantity):
        total_food_cost = menu_item.price * quantity # ยอดรวม = ราคา * จำนวนจาน
        if total_food_cost > self.budget:
            print (f"ไม่สามารถสั่งได้ เนื่องจากรายการที่สั่งเกินราคา")
        else:
            self.budget_pay = self.budget - total_food_cost # งบหลังคำนวณ = งบตอนแรก - ยอดที่สั่ง
            if menu_item.reduce_stock(quantity):
                print (f"{self.name} สั่ง {menu_item.menu} จำนวน {quantity} จาน\n"
                        f"ยอดรวม {total_food_cost} บาท\n"
                        f"จ่ายมา {self.budget} บาท เงินคงเหลือ {self.budget_pay} บาท"
                    )
            else:
                print ("ไม่สามารถสั่งได้")

    def __str__(self):
        return f"ลูกค้า: {self.name} | เงินคงเหลือ: {self.budget_pay} บาท"


########## สร้าง object เมนูอาหาร ##########        
menu1 = MenuItem("ข้าวผัด",40,20)
menu2 = MenuItem("กะเพราหมูสับ",40,20)
menu3 = MenuItem("สุกี้",40,20)
menu4 = MenuItem("ผัดไทย",40,20)
menu5 = MenuItem("ต้มยำกุ้ง",60,20)

# แสดงผลเมนูอาหาร

########## สร้าง object ลูกค้า ##########  
customer1 = Customer("ตาล",200)

# ลูกค้าสั่งอาหาร
customer1.order_food(menu1,3)
customer1.order_food(menu2,1)
print(customer1) # แสดงผลลัพธ์ของการสั่งอาหาร