# v1.0

# Môn chính
def main(): # Hàm main

    def chon_mon():
        print("1. Mon Toan")
        print("2. Mon Ngu Van")
        print("3. Mon Tieng Anh")

    def mon_toan():
        mon = "Toan"
        # Tính điểm TX
        x_tx = 1
        tong_tx = 0
        so_cot_tx = input("Nhap so cot diem thuong xuyen ban co: ")

        while x_tx < int(so_cot_tx):
            input_cot_tx = input("Cot diem mieng so " + str(x_tx) + " cua ban là: ")
            tong_tx = tong_tx + float(input_cot_tx)
            x_tx = x_tx + 1

        input_cot_tx = input("Cot diem mieng so " + str(x_tx) + " cua ban là: ")
        tong_tx = tong_tx + float(input_cot_tx)
        print(tong_tx)

        # Tính điểm GK
        diem_gk = input("Nhap diem giua ki cua ban: ")

        # Tính diểm CHK
        diem_chk = input("Nhap diem cuoi hoc ki cua ban: ")

        # Tính tổng để chia
        tong_bai = x_tx + 2
        chia_tb = x_tx + tong_bai

        # Tính điểm TBC 
        tbc = tong_tx + 2 * float(diem_gk) + 3 * float(diem_chk)
        tb = tbc / chia_tb
        print("Điểm trung binh cong mon " + mon + " cua ban là: " + str(tb))
        print(chia_tb)
        print(tong_bai)
        


    def user_input():
        user_chon_mon = input("Nhap so tuong ung voi loai mon: ")
        if int(user_chon_mon) == 1: # Ghi chú / Input khi user nhập là str vì vậy nếu để if user_chon_mon == 1: thì không thể đúng !
            mon_toan()
        elif int(user_chon_mon) == 2:
            print(None)
        elif int(user_chon_mon) == 3:
            print(None)
        else:
            print("Hay nhap so tuong ung voi tung mon hoc !")
            reset_input()

    
    def reset_input(): # Hàm dùng để reset về user_input khi nhập sai số
            
            user_input()






    print("Vui long chon loai mon hoc:")
    chon_mon()
    user_input()







main()








