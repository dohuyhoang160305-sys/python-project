def add_product(product):
    print("===Thêm Sản Phẩm===")
    ma = input("Nhập mã sản phẩm:")
    ten = input("Nhập tên sản phẩm:")
    thuong_hieu = input("Nhập tên thương hiệu:")
    gia = int(input("Nhập giá:"))
    so_luong = int(input("Nhập số lượng:"))
    product = {"mã",ma,"tên",ten,"thương hiệu",thuong_hieu,"giá",gia,"số lượng",so_luong}
    product.append(product)
    print("Thêm sản phẩm thành công")
def show_product(product):
    print("===Danh Sách Sản Phẩm===")
    if product == []:
        print("Chưa có sản phẩm nào")
    for product in product:
        print("-----------------")
        print("Mã sản phẩm:",product["mã"])
        print("Tên sản phẩm:",product["tên"])
        print("Tên thương hiệu:",product["thương hiệu"])
        # một nháy được-sai
        print("Giá:",product["giá"])
        print("Số lượng:",product["số lượng"])
import json

FILE_NAME = "products.json"
# load dữ liệu từ file
def load_data():
    try:
        with open(FILE_NAME,"r",encoding= "utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return[]
# lưu dữ liệu vào file
def save_data(products):
    with open(FILE_NAME,"w",encoding= "utf-8") as f:
        json.dump(products,f,indent=4,ensure_ascii=False)
# thêm sản phẩm
def add_product(products):
    new_id = f"LT{len(products)+1:02d}"
    name = input("Nhập tên sản phẩm : ")
    brand = input("Nhập tên thương hiệu : ")
    prince = input("Nhập giá : ")
    quantily = int(input("Nhập số lượng : "))
    new_product = {
        "id":new_id,
        "name":name,
        "brand":brand,
        "prince":prince,
        "quantily":quantily 
    }
    products.append(new_product)
    print("Thêm sản phẩm thành công")
    return products
# cập nhật sản phẩm
def update_product(products):
        
    product_id = input("Nhập id cần cập nhật : ")
    
    for product in products:
        if product["id"] == product_id:
           product["Tên"] = input("Tên sản phẩm : ")
           product["Thương hiệu"] = input("Tên thương hiệu : ")
           product["Giá"] = input("Giá : ")
           product["Số lượng"] = input("Số lượng : ")
           print("Cập nhật thành công")
           return
    print("Không tìm thấy sản phẩm")
# xóa sản phẩm
def delete_product(products):
    product_id = input("Nhập id cần xóa : ")
    
    for product in products:
        if product["id"] == product_id:
            products.remove(product)
            print("Đã xóa sản phẩm")
            return
# tìm kiếm theo tên 
def search_all_product_by_name(products):
    keyword = input("Nhập từ khóa tìm kiếm : ").lower()
    
    for product in products:
        if keyword in product["name"].lower():
            print(product)
# hiển thị tất cả
def display_all_products(products):
    if not products:
        print("Kho hàng trống")
        return
    for product in products:
        print("------------------------")
        print("id : ",product["id"])
        print("Tên : ",product["name"])
        print("Thương hiệu : ",product["brand"])
        print("Giá : ",product["prince"])
        print("Số lượng : ",product["quantily"])
        
