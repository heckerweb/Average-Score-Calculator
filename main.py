# v1.0

# Môn chính
def main():
    def mon_chinh():
        print("Mon Ngu Van")
        print("Mon Toan")
        print("Mon Tieng Anh")


    def chon_mon():
        print("1. Mon chinh")
        print("2. Mon phu")
        print("Vui long nhap so tuong ung !")



    def liet_ke_mon_hoc():
        if user_chon_mon == "1": # Ghi chú / Input khi user nhập là str vì vậy nếu để if user_chon_mon == 1: thì không thể đúng !
            mon_chinh()
        elif user_chon_mon == "2":
            print(None)
        else:
            print("Nhap so 1 cho mon chinh, nhap so 2 cho mon phu !")
            main()








    print("Vui long chon loai mon hoc:")
    chon_mon()
    user_chon_mon = input("Nhap so tuong ung voi loai mon: ")
    liet_ke_mon_hoc()

main()








