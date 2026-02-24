from product_manager import *

def main():
    products_list = load_data()
    
    while True:
        print("\n" + "*"*10 + " QUẢN LÝ KHO HÀNG LAPTOP " + "*"*10)
        print("1. Xem danh sách sản phẩm")
        print("2. Thêm sản phẩm mới")
        print("3. Cập nhật sản phẩm")
        print("4. Xóa sản phẩm")
        print("5. Tìm kiếm theo tên")
        print("6. Lưu và Thoát")
        
        choice = input("Lựa chọn của bạn (1-6): ")

        if choice == '1':
            display_all_products(products_list)
        elif choice == '2':
            products_list = add_product(products_list)
        elif choice == '3':
            products_list = update_product(products_list)
        elif choice == '4':
            products_list = delete_product(products_list)
        elif choice == '5':
            search_product_by_name(products_list)
        elif choice == '6':
            save_data(products_list)
            print("Hệ thống đã đóng. Tạm biệt!")
            break
        else:
            print("Lựa chọn không hợp lệ, vui lòng nhập lại.")

if __name__ == "__main__":
    main()