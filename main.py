# v1.0
# Using with GNU GENERAL PUBLIC LICENSE

# Made with PASSION from Dao Thanh Tam

def main(): # Hàm main

    def chon_mon():
        print("1. Mon Toan")
        print("2. Mon Ngu Van")
        print("3. Mon Tieng Anh")
        print("4. Thoat")

    def xep_loai(mon , tb): # Xếp loại
        gioi = "Chuc mung, ban duoc xep vao loai gioi trong mon " + mon + " !"
        kha = "Ban chi can co gang them chut nua thoi, ban se duoc den dap."
        trb = "Ban can phai co gang them nua, chi can cham chi hoc hanh, ban se duoc den dap."
        yeu = "Ban chi can cham chi hoc hanh la se co tien bo ngay thoi, dung ham choi nua !"
        if int(tb) >= 8:
            print(gioi)
        elif int(tb) << 8 and int(tb) >> 5:
            print(kha)
        elif int(tb) == 5:
            print(trb)
        elif int(tb) << 5:
            print(yeu)
        

    def mon_toan(): # Toán
        mon = "Toan"
        # Tính điểm TX
        x_tx = 1
        tong_tx = 0
        so_cot_tx = input("Nhap so cot diem thuong xuyen ban co: ")

        while x_tx < int(so_cot_tx):
            input_cot_tx = input("Cot diem mieng so " + str(x_tx) + " cua ban là: ")
            if int(input_cot_tx) >> 10:
                print("Diem kiem tra khong the lon hon 10.")
                main()
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
        tbc = tong_tx + 2.0 * float(diem_gk) + 3.0 * float(diem_chk)
        tb = tbc / chia_tb
        print("Điểm trung binh cong mon " + mon + " cua ban là: " + str(tb))
        xep_loai(mon=mon, tb=tb)
        print("")
        main()



    def mon_van(): # Ngữ văn
        mon = "Ngu Van"
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
        tbc = tong_tx + 2.0 * float(diem_gk) + 3.0 * float(diem_chk)
        tb = tbc / chia_tb
        print("Điểm trung binh cong mon " + mon + " cua ban là: " + str(tb))
        xep_loai(mon=mon, tb=tb)
        print("")
        main()

    def mon_anh():
        mon = "Tieng Anh"
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
        tbc = tong_tx + 2.0 * float(diem_gk) + 3.0 * float(diem_chk)
        tb = tbc / chia_tb
        print("Điểm trung binh cong mon " + mon + " cua ban là: " + str(tb))
        xep_loai(mon=mon, tb=tb)
        print("")
        main()


    def exit_program():
        input_thoat = input("Ban co chac chan muon thoat ? [y/n]: ")
        if input_thoat == "y":
            exit()
        elif input_thoat == "n":
            main()
        else:
            print("Vui long nhan y (tuong ung voi co) hoac n (tuong ung voi khong).")
            reset_input_2()



    # Ghi chú / Input khi user nhập là str vì vậy nếu để if user_chon_mon == 1: thì không thể đúng !
    def user_input():
        user_chon_mon = input("Nhap so tuong ung voi loai mon: ")
        if int(user_chon_mon) == 1: 
            mon_toan()
        elif int(user_chon_mon) == 2:
            mon_van()
        elif int(user_chon_mon) == 3:
            mon_anh()
        elif int(user_chon_mon) == 4:
            exit_program()

        else:
            print("Hay nhap so tuong ung voi tung mon hoc !")
            reset_input_1()

    
    def reset_input_1(): # Hàm dùng để reset về user_input khi nhập sai số
            
        user_input()
    
    def reset_input_2(): # RESET 

        exit_program()






    print("Vui long chon loai mon hoc:")
    chon_mon()
    user_input()







main()








