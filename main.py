# -*- coding: utf-8 -*-
"""
Updated on Sun Jun 16 9:57:08 2024

@author: thtam09
"""

def print_menu():
    print("1. Tinh diem TB mon trong 1 HK.")
    print("2. Tinh diem TB ca nam.")
    print("3. Thoát")

def get_user_choice():
    while True:
        select = input("Hay chon 1 trong 2 de thuc hien (vui long nhap so): ")
        if select in ["1", "2", "3"]:
            return select
        elif select == "":
            print("Vui long chon 1 trong 3 de thuc hien !")
        else:
            print("Vui long nhap dung so da cho")

def tinh_tb_tx():
    while True:
        try:
            so_cot_diem_tx = int(input("Hay nhap so cot diem thuong xuyen ban co: "))
            break
        except ValueError:
            print("Vui long nhap dung thong tin de chuong trinh xu ly !")

    tb_tx = 0
    for so_cot_md in range(1, so_cot_diem_tx + 1):
        while True:
            try:
                tb_tx += float(input(f"Hay nhap cot diem tx so {so_cot_md}: "))
                break
            except ValueError:
                print("Vui long nhap dung thong tin de chuong trinh xu ly !")

    tinh_diem_tb_mon(so_cot_diem_tx, tb_tx)

def tinh_diem_tb_mon(so_cot_diem_tx, tb_tx):
    while True:
        try:
            diem_ghk = float(input("Hay nhap diem thi giua HK1: "))
            diem_chk = float(input("Hay nhap diem thi cuoi HK1: "))
            break
        except ValueError:
            print("Vui long nhap dung thong tin de chuong trinh xu ly !")

    diem_tb_mon_hk = (tb_tx + 2.0 * diem_ghk + 3.0 * diem_chk) / (so_cot_diem_tx + 5)
    print("Diem trung binh mon cua ban la: ", diem_tb_mon_hk)

def tb_ca_nam():
    while True:
        try:
            tb_mon_hk1 = float(input("Diem trung binh mon hoc ki 1 cua ban la: "))
            tb_mon_hk2 = float(input("Diem trung binh mon hoc ki 2 cua ban la: "))
            break
        except ValueError:
            print("Vui long nhap dung thong tin de chuong trinh xu ly !")

    tb_mon_ca_nam = (tb_mon_hk1 + tb_mon_hk2 * 2.0) / 3.0
    print("Diem trung binh mon ca nam cua ban la: ", round(tb_mon_ca_nam, 2))

def main():
    while True:
        print_menu()
        select = get_user_choice()
        if select == "1":
            tinh_tb_tx()
        elif select == "2":
            tb_ca_nam()
        elif select == "3":
            print("Program stopped by USER")
            break

if __name__ == "__main__":
    main()
