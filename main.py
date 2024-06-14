# -*- coding: utf-8 -*-
"""
Updated on Sat Nov 25 11:34:59 2023

@author: thtam09
"""

    
def menu():
    print("1. Tinh diem TB mon trong 1 HK.")
    print("2. Tinh diem TB ca nam.")
    print("3. Thoát")
    
    select = input("Hay chon 1 trong 2 de thuc hien (vui long nhap so): ")
    if select == "1":
        tinh_tb_tx()
    elif select == "2":
        tb_ca_nam()
    elif select == "3":
        raise KeyboardInterrupt("Program stopped by USER") from None
    elif select == "":
        print("Vui long chon 1 trong 3 de thuc hien !")
        menu()
    else:
        print("Vui long nhap dung so da cho")
        menu()
        

        
def tinh_tb_tx():
    global so_cot_diem_tx
    global tb_tx
    so_cot_diem_tx = input("Hay nhap so cot diem thuong xuyen ban co: ")
    so_cot_md = 1
    tb_tx = 0
    

    try:
        while so_cot_md <= int(so_cot_diem_tx): # Tạo vòng lập nhập cột điểm tx khi số cột mđ <= số cột điểm tx user có
            print("Hay nhap cot diem tx so", so_cot_md,": ")
            try:
                tb_tx += float(input())# dùng float vì điểm kt có thể là số thập phân (nằm trong tập hợp số thực)
                so_cot_md += 1
            except:
                print("Vui long nhap dung thong tin de chuong trinh xu ly !") 
    except:
        print("Vui long nhap dung thong tin de chuong trinh xu ly !") 
        tinh_tb_tx()
    
    tinh_diem_tb_mon()
    
     
def tinh_diem_tb_mon():
    diem_ghk = 0
    diem_chk = 0
    print("Hay nhap diem thi giua HK1: ")
    diem_ghk = input()
    print("Hay nhap diem thi cuoi HK1: ")
    diem_chk = input()
    
        
        
    try:    
        diem_tb_mon_hk = (float(tb_tx) + 2.0 * float(diem_ghk) + 3.0 * float(diem_chk)) / (int(so_cot_diem_tx) + 5)
        print("Diem trung binh mon cua ban la: ", diem_tb_mon_hk)
    except:
        print("Vui long nhap dung thong tin de chuong trinh xu ly !") # Check user đã nhập chx
        tinh_diem_tb_mon() # In test


    

    

def tb_ca_nam():
    print("Diem trung binh mon hoc ki 1 cua ban la: ")
    tb_mon_hk1 = input()
    print("Diem trung binh mon hoc ki 2 cua ban la: ")
    tb_mon_hk2 = input()
    
    try:
        tb_mon_ca_nam = float(tb_mon_hk1) + (float(tb_mon_hk2) * 2.0)
        
        tb_mon_ca_nam /= 3.0
        print("Diem trung binh mon ca nam cua ban la: ", round(float(tb_mon_ca_nam), 2))
    except:
        print("Vui long nhap dung thong tin de chuong trinh xu ly !")
        tb_ca_nam()
    

menu()
