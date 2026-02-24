import json
import os

FILENAME = "products.json"

def load_data():
    if os.path.exists(FILENAME):
        try:
            with open(FILENAME, 'r', encoding='utf-8') as f:
                data = json.load(f)
                if data: 
                    return data
        except (json.JSONDecodeError, FileNotFoundError):
            pass

    return [
        {"id": "LT01", "name": "Laptop Gaming Acer Nitro 5", "brand": "Acer", "price": 22000000, "stock": 10},
        {"id": "LT02", "name": "Macbook Air M2", "brand": "Apple", "price": 28000000, "stock": 5},
        {"id": "LT03", "name": "Dell XPS 13", "brand": "Dell", "price": 35000000, "stock": 3},
        {"id": "LT04", "name": "Asus Vivobook 15", "brand": "Asus", "price": 14500000, "stock": 15},
        {"id": "LT05", "name": "HP Pavilion 14", "brand": "HP", "price": 16000000, "stock": 8}
    ]

def save_data(products):
    """Ghi danh sách sản phẩm vào file JSON."""
    with open(FILENAME, 'w', encoding='utf-8') as f:
        json.dump(products, f, ensure_ascii=False, indent=4)
    print("\n[Hệ thống] Đã lưu dữ liệu thành công vào products.json!")

def add_product(products):
    print("\n--- THÊM SẢN PHẨM MỚI ---")
    new_id = f"LT{len(products) + 1:02d}"
    name = input("Nhập tên sản phẩm: ")
    brand = input("Nhập thương hiệu: ")
    try:
        price = int(input("Nhập giá: "))
        stock = int(input("Nhập số lượng tồn: "))
    except ValueError:
        print("Lỗi: Giá/Số lượng phải là số!")
        return products
    
    products.append({"id": new_id, "name": name, "brand": brand, "price": price, "stock": stock})
    print(f"Đã thêm sản phẩm {new_id}!")
    return products

def update_product(products):
    sid = input("Nhập mã ID : ").upper()
    for p in products:
        if p['id'] == sid:
            p['name'] = input(f"Tên mới ({p['name']}): ") or p['name']
            p['brand'] = input(f"Hãng mới ({p['brand']}): ") or p['brand']
            try:
                p['price'] = int(input(f"Giá mới ({p['price']}): ") or p['price'])
                p['stock'] = int(input(f"Tồn kho mới ({p['stock']}): ") or p['stock'])
            except ValueError: pass
            print("Đã cập nhật!")
            return products
    print("Không tìm thấy!")
    return products

def delete_product(products):
    sid = input("Nhập mã ID cần xóa: ").upper()
    for i, p in enumerate(products):
        if p['id'] == sid:
            products.pop(i)
            print("Đã xóa!")
            return products
    print("Không tìm thấy!")
    return products

def search_product_by_name(products):
    kw = input("Nhập từ khóa tìm kiếm: ").lower()
    results = [p for p in products if kw in p['name'].lower()]
    display_all_products(results)

def display_all_products(products):
    if not products:
        print("\n[!] Kho hàng trống.")
        return
    print("\n" + "="*75)
    print(f"{'ID':<6} | {'Tên Sản Phẩm':<30} | {'Hãng':<12} | {'Giá':<12} | {'Tồn'}")
    print("-" * 75)
    for p in products:
        print(f"{p['id']:<6} | {p['name']:<30} | {p['brand']:<12} | {p['price']:<12,} | {p['stock']}")
    print("="*75)