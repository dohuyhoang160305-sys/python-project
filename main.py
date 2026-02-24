from product_manager import *
def menu():
    print("==== POLY_LAP ====")
    print("1. Hiển thị sản phẩm")
    print("2. Thêm sản phẩm")
    print("3. Cập nhật sản phẩm")
    print("4. Xóa sản phẩm")
    print("5. Tìm kiếm sản phẩm")
    print("6. Thoát")
def main():
    products = load_data()
    
    while True:
        menu()
        choice = input("Mời bạn chọn chức năng : ")
        if choice == "1":
            display_all_products(products)
            
        elif choice == "2":
            products = add_product(products)
            
        elif choice == "3":
            update_product(products)
        
        elif choice == "4":
            delete_product(products)
            
        elif choice == "5":
            search_all_product_by_name(products)
        elif choice == "6":
            save_data(products)
            print("Sản phẩm đã lưu . Chào tạm biệt ")
            break
        else:
            print("Lựa chọn không hợp lệ")
if __name__ == "__main__":
    main()