import workbook
def main():
    print("Wybierz ćwiczenia:\n [1] - Workbook\n [2] - Ćwiczenia pozajęciowe\n [3] - Prace domowe\n")
    user_choice = int(input("Wybór: "))
    if (user_choice==1):
        workbook.workbookmenu()
        main()
if __name__=="__main__":
    main()