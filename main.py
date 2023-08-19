# v1.0 -- The core of the program
# Using with GNU GENERAL PUBLIC LICENSE




def main(): # Hàm main

    def chon_mon():
        print("1. Mon Toan")
        print("2. Mon Ngu Van")
        print("3. Mon Tieng Anh")
        print("4. Thoat")


    def chon_hk(mon):
        print("1. Tinh diem TB mon " + mon + " HK1.")
        print("2. Tinh diem TB mon " + mon + " HK2.")
        print("3. Tính diem TB mon " + mon + " ca nam (HK1 va HK2).")
        print("4. Quay tro lai")




    def xep_loai(mon , tbm): # Xếp loại
        gioi = "Chuc mung, ban duoc xep vao loai gioi trong mon " + mon + " !"
        kha = "Ban chi can co gang them chut nua thoi, ban se duoc den dap."
        trb = "Ban can phai co gang them nua, chi can cham chi hoc hanh, ban se duoc den dap."
        yeu = "Ban chi can cham chi hoc hanh la se co tien bo ngay thoi, dung ham choi nua !"
        if int(tbm) >= 8:
            print(gioi)
        elif int(tbm) << 8 and int(tbm) >> 5:
            print(kha)
        elif int(tbm) == 5:
            print(trb)
        elif int(tbm) << 5:
            print(yeu)
        

    def mon_toan(): # Toán
        mon = "Toan"
        chon_hk(mon=mon)
        def check_user_input_hk():
            input_hk = input("Hay nhap so tuong ung: ")
            if int(input_hk) == 1:
                hk1_math()
            elif int(input_hk) == 2:
                hk2_math()
            elif int(input_hk) == 3:
                tinh_tb_nam(mon=mon)  
            elif int(input_hk) == 4:
                main()
            else:
                print("Vui long nhap so tuong ung 1 hoac 2.")
                reset_input_math()
        def reset_input_math():

            check_user_input_hk()

        check_user_input_hk()




    def hk1_math():
        mon = "Toan"
        hk = " HK1"
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

        # Tính điểm GK
        diem_gk = input("Nhap diem giua ki cua ban: ")

        # Tính diểm CHK
        diem_chk = input("Nhap diem cuoi ki cua ban: ")

        # Tính tổng để chia
        tong_bai = x_tx + 2
        chia_tb = x_tx + tong_bai

        # Tính điểm TBC 
        tbc = tong_tx + 2 * float(diem_gk) + 3 * float(diem_chk)
        tbm = tbc / chia_tb
        print("Điểm trung binh cong mon " + mon + " trong" + hk + " cua ban là: " + str(tbm))
        xep_loai(mon=mon, tbm=tbm)
        print("")
        mon_toan()




    def hk2_math():
        mon = "Toan"
        hk = " HK2"
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

        # Tính điểm GK
        diem_gk = input("Nhap diem giua ki cua ban: ")

        # Tính diểm CHK
        diem_chk = input("Nhap diem cuoi ki cua ban: ")

        # Tính tổng để chia
        tong_bai = x_tx + 2
        chia_tb = x_tx + tong_bai

        # Tính điểm TBC 
        tbc = tong_tx + 2 * float(diem_gk) + 3 * float(diem_chk)
        tbm = tbc / chia_tb
        print("Điểm trung binh cong mon " + mon + " trong" + hk + " cua ban là: " + str(tbm))
        xep_loai(mon=mon, tbm=tbm)
        print("")
        mon_toan()

    def tinh_tb_nam(mon): 
        hk1_tb = input("Ban hay nhap diem TB mon " + str(mon) + " trong HK1 cua ban: ")
        hk2_tb = input("Ban hay nhap diem TB mon " + str(mon) + " trong HK2 cua ban: ")

        hk_2_tb_tinh = float(hk2_tb) * 2
        tb_ca_nam_cong = float(hk1_tb) + float(hk_2_tb_tinh)
        tb_ca_nam_chia = float(tb_ca_nam_cong) / 3
        tb_ca_nam = tb_ca_nam_chia
        print("Diem TB mon ca nam mon " + str(mon) +  " cua ban la: " + str(tb_ca_nam))


    def mon_van(): # Toán
        mon = "Ngu Van"
        chon_hk(mon=mon)
        def check_user_input_hk():
            input_hk = input("Hay nhap so tuong ung: ")
            if int(input_hk) == 1:
                hk1_vie()
            elif int(input_hk) == 2:
                hk2_vie()
            elif int(input_hk) == 3:
                tinh_tb_nam(mon=mon)
            elif int(input_hk) == 4:
                main()
            else:
                print("Vui long nhap so tuong ung 1 hoac 2.")
                reset_input_vie()
        def reset_input_vie():

            check_user_input_hk()

        check_user_input_hk()




    def hk1_vie():
        mon = "Ngu Van"
        hk = " HK1"
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

        # Tính điểm GK
        diem_gk = input("Nhap diem giua ki cua ban: ")

        # Tính diểm CHK
        diem_chk = input("Nhap diem cuoi ki cua ban: ")

        # Tính tổng để chia
        tong_bai = x_tx + 2
        chia_tb = x_tx + tong_bai

        # Tính điểm TBC 
        tbc = tong_tx + 2 * float(diem_gk) + 3 * float(diem_chk)
        tbm = tbc / chia_tb
        print("Điểm trung binh cong mon " + mon + " trong" + hk + " cua ban là: " + str(tbm))
        xep_loai(mon=mon, tbm=tbm)
        print("")
        mon_van()



    def hk2_vie():
        mon = "Ngu Van"
        hk = " HK2"
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

        # Tính điểm GK
        diem_gk = input("Nhap diem giua ki cua ban: ")

        # Tính diểm CHK
        diem_chk = input("Nhap diem cuoi ki cua ban: ")

        # Tính tổng để chia
        tong_bai = x_tx + 2
        chia_tb = x_tx + tong_bai

        # Tính điểm TBC 
        tbc = tong_tx + 2 * float(diem_gk) + 3 * float(diem_chk)
        tbm = tbc / chia_tb
        print("Điểm trung binh cong mon " + mon + " trong" + hk + " cua ban là: " + str(tbm))
        xep_loai(mon=mon, tbm=tbm)
        print("")
        mon_van()


    def mon_anh(): # Toán
        mon = "Tieng Anh"
        chon_hk(mon=mon)
        def check_user_input_hk():
            input_hk = input("Hay nhap so tuong ung: ")
            if int(input_hk) == 1:
                hk1_english()
            elif int(input_hk) == 2:
                hk2_english()
            elif int(input_hk) == 3:
                tinh_tb_nam(mon=mon)
            elif int(input_hk) == 4:
                main()
            else:
                print("Vui long nhap so tuong ung 1 hoac 2.")
                reset_input_english()
        def reset_input_english():

            check_user_input_hk()

        check_user_input_hk()




    def hk1_english():
        mon = "Tieng Anh"
        hk = " HK1"
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

        # Tính điểm GK
        diem_gk = input("Nhap diem giua ki cua ban: ")

        # Tính diểm CHK
        diem_chk = input("Nhap diem cuoi ki cua ban: ")

        # Tính tổng để chia
        tong_bai = x_tx + 2
        chia_tb = x_tx + tong_bai

        # Tính điểm TBC 
        tbc = tong_tx + 2 * float(diem_gk) + 3 * float(diem_chk)
        tbm = tbc / chia_tb
        print("Điểm trung binh cong mon " + mon + " trong" + hk + " cua ban là: " + str(tbm))
        xep_loai(mon=mon, tbm=tbm)
        print("")
        mon_anh()



    def hk2_english():
        mon = "Tieng Anh"
        hk = " HK2"
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

        # Tính điểm GK
        diem_gk = input("Nhap diem giua ki cua ban: ")

        # Tính diểm CHK
        diem_chk = input("Nhap diem cuoi ki cua ban: ")

        # Tính tổng để chia
        tong_bai = x_tx + 2
        chia_tb = x_tx + tong_bai

        # Tính điểm TBC 
        tbc = tong_tx + 2 * float(diem_gk) + 3 * float(diem_chk)
        tbm = tbc / chia_tb
        print("Điểm trung binh cong mon " + mon + " trong" + hk + " cua ban là: " + str(tbm))
        xep_loai(mon=mon, tbm=tbm)
        print("")
        mon_anh()


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
    
    def reset_input_2(): # 

        exit_program()



    print("Vui long chon loai mon hoc:")
    chon_mon()
    user_input()



main()








