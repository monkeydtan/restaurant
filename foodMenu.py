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
        if quantity <= self.in_stock:
            self.in_stock -= quantity
            return True
        else:
            return False
        
    def __str__(self):
        return self.show_info()

# ข้อมูลลูกค้า
class Customer:
    def __init__(self,name,budget):
        self.name = name
        self.budget = budget # งบตอนแรก
        self.budget_pay = budget # งบที่เหลือ
        self.total_spent = 0 # ยอดรวมการสั่ง ... บาท
        self.order_items = [] # รายการอาหารที่สั่ง
    
    # การสั่งอาหาร    
    def order_food(self,menu_item,quantity):
        total_food_cost = menu_item.price * quantity # ยอดรวม = ราคา * จำนวนจาน
        
        if total_food_cost > self.budget:
            return (f"ไม่สามารถสั่งได้ เนื่องจากรายการที่สั่งเกินราคา")
        else:
            if menu_item.reduce_stock(quantity):
                self.total_spent += total_food_cost # ยอดรวม += รายการอาหารที่สั่งทั้งหมด
                self.budget_pay -= total_food_cost # เงินคงเหลือ...บาท -= ยอดที่สั่ง
                self.order_items.append(f"{menu_item.menu} จำนวน {quantity} จาน จานละ {menu_item.price} บาท")  # เพิ่มเมนูที่สั่งเข้าไปในรายการ
                return f"สั่ง {menu_item.menu} จำนวน {quantity} จานสำเร็จ"
            else:
                return ("ไม่สามารถสั่งได้")

    def __str__(self):
        order_details = "\n".join(self.order_items)
        return (f"----------------------------------\n"
            f"รายการของ {self.name}\n"
            f"{order_details}\n"
            f"ยอดรวม : {self.total_spent} บาท\n"
            f"จ่ายมา {self.budget} บาท เงินคงเหลือ {self.budget_pay} บาท\n"
            f"----------------------------------\n"
        )
        
# รายการเมนูอาหาร
class Restaurant:
    def __init__(self):
        self.menus_food = [] # รายการเมนูอาหาร เก็บไว้ในลิสต์
        
    # เอาไว้เพิ่มเมนูในร้าน
    def add_menu_item(self,menu_item):
        self.menus_food.append(menu_item)
    
    # แสดงเมนูทั้งหมดที่มีในร้าน  
    def show_menu(self):
        menu_details = "\n".join(str(menu) for menu in self.menus_food)
        return f"เมนูอาหารในร้าน:\n{menu_details}"

    # ลูกค้าสั่งอาหาร
    def place_order(self,customer,menu_item,quantity):
        return customer.order_food(menu_item, quantity)

########## สร้าง object เมนูอาหาร ##########        
menu1 = MenuItem("ข้าวผัด",40,20)
menu2 = MenuItem("กะเพราหมูสับ",40,20)
menu3 = MenuItem("สุกี้",40,20)
menu4 = MenuItem("ผัดไทย",40,20)
menu5 = MenuItem("ต้มยำกุ้ง",60,20)

########## สร้าง object ลูกค้า ##########  
customer1 = Customer("ตาล",200)

########## สร้าง object ร้านอาหารและเพิ่มเมนู ##########
restaurant = Restaurant()

# -------- เพิ่มเมนูอาหาร --------- #
restaurant.add_menu_item(menu1)
restaurant.add_menu_item(menu2)
restaurant.add_menu_item(menu3)

# -------- แสดงเมนูในร้าน --------- #
print(restaurant.show_menu()) ### แสดงเมนูทั้งหมดในร้าน OK

# ลูกค้าสั่งอาหาร
order_response = restaurant.place_order(customer1, menu1, 3)  # สั่งข้าวผัด 3 จาน
print(order_response)  # แสดงผลการสั่งอาหาร
order_response = restaurant.place_order(customer1, menu2, 1)  # สั่งกะเพราหมูสับ 1 จาน
print(order_response)  # แสดงผลการสั่งอาหาร

# แสดงรายละเอียดการสั่งอาหารของลูกค้า
print(customer1) # แสดงผลลัพธ์ของการสั่งอาหารทั้งหมดของ customer1