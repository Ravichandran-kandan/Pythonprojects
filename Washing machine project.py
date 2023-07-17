import time

def auto_mode():
    try:
        print("Auto mode selected.")
        running_mode = input("Enter the washing cycle (Normal, Delicate, or Heavy): ")
        if running_mode.lower() == "normal":
            print("Total 70 mins")
            print("Fill two cups of detergent....")
            print("__________________Machine is running please wait for 3sec__________________")
            time.sleep(3)
            print("Water has been filled successfully")
            print("__________________Machine is running please wait for 5sec__________________")
            time.sleep(5)
            print("Washing the clothes....")
            print("__________________Machine is running please wait for 30sec__________________")
            time.sleep(30)
            print("Rinse process has started....")
            print("__________________Machine is running please wait for 20sec__________________")
            time.sleep(20)
            print("Spin cycle has started....")
            print("__________________Machine is running please wait for 10sec__________________")
            time.sleep(10)
            print("Washing process ended....")
        elif running_mode.lower() == "delicate":
            print("Total 110 mins")
            print("Fill two cups of detergent.")
            print("__________________Machine is running please wait for 3sec__________________")
            time.sleep(3)
            print("Water is filling...")
            print("__________________Machine is running please wait for 5sec__________________")
            time.sleep(5)
            print("Washing the clothes.")
            print("__________________Machine is running please wait 60sec__________________")
            time.sleep(60)
            print("Rinse process has started.")
            print("__________________Machine is running please wait for 25sec__________________")
            time.sleep(25)
            print("Spin cycle has started.")
            print("__________________Machine is running please wait for 15sec__________________")
            time.sleep(15)
            print("Washing process ended.")
        elif running_mode.lower() == "heavy":
            print("Total 80 mins")
            print("Fill two cups of detergent.")
            print("__________________Machine is running please wait for 3sec__________________")
            time.sleep(3)
            print("Water is filling...")
            print("__________________Machine is running please wait for 5sec__________________")
            time.sleep(5)
            print("Washing the clothes.")
            print("__________________Machine is running please wait for 40sec__________________")
            time.sleep(40)
            print("Rinse process has started.")
            print("__________________Machine is running please wait 250sec__________________")
            time.sleep(250)
            print("Spin cycle has started.")
            print("__________________Machine is running please wait 15sec__________________")
            time.sleep(15)
            print("Washing process ended.")
        else:
            print("Invalid running mode.")

    except NameError as e:
        print("NameError occured:",e)
    except ValueError as e:
        print("ValueError occured:",e)
    except TypeError as e:
        print("TypeError occured:", e)
    else:
        print("....The washing machine has ended.....")

def manual_mode():
    try:
        print("Manual mode selected.")
        Running_mode = input("Select the washing cycle (Normal, Delicate, or Heavy):")

        if Running_mode.lower() == "normal":
            print("Add two cups of detergent….")

            def loop1():
                while True:
                    input1 = input("Two cups of detergent filled ? - Enter only Yes or No:")
                    if input1.lower() == "yes":
                        print("__________________Machine is running please wait for 2sec__________________")
                        time.sleep(2)
                        print("Detergent filled success fully")
                    elif input1.lower() == "no":
                        print("_______Detergent not filled_______")
                        break
                    else:
                        print("__________unexpected error occurred__________")
                        loop1()
                    break

            def loop2():
                while True:
                    input2 = input("Fill water ? - Enter only Yes or No:")
                    if input2.lower() == "yes":

                        def semi_loop1():
                            a = int(input("Enter the amount of time to wash the clothes: "))
                            while True:
                                if a > 3:
                                    print("Water will overflow, Enter the time below or equal to 3")
                                    semi_loop1()
                                elif a <= 3:
                                    print(f"_______Water filling is on process, please wait for",a,"sec_______")
                                    time.sleep(a)
                                    print("water filling completed successfully.")
                                break

                        semi_loop1()

                    elif input2.lower() == "no":
                        print("________Water is not filled________")
                        print("can't run washing machine without water")
                        loop2()
                        break
                    else:
                        print("__________unexpected error occurred__________")
                        loop2()
                    break

            def loop3():
                while True:
                    input3 = input("Shall the process to wash the clothes start ? - Enter only Yes or No:")
                    if input3.lower() == "yes":
                        a = int(input("enter the amount of time to wash the clothes: "))
                        print("__________________Machine is running please wait for",a,"sec__________________")
                        time.sleep(a)
                        print("Washing completed successfully.")
                    elif input3.lower() == "no":
                        print("Clothes are not yet washed.")
                        break
                    else:
                        print("__________unexpected error occurred__________")
                        loop3()
                    break

            def loop4():
                while True:
                    input4 = input("Shall the process to Rinse the clothes start ? - Enter only Yes or No: ")
                    if input4.lower() == "yes":
                        a = int(input("enter the amount of time to rinse the clothes: "))
                        print("__________________Machine is running please wait for",a,"sec__________________")
                        time.sleep(a)
                        print("Rinse process completed successfully.")
                    elif input4.lower() == "no":
                        print("rinse process not yet started")
                        break
                    else:
                        print("__________unexpected error occurred__________")
                        loop4()
                    break

            def loop5():
                while True:
                    input5 = input("Shall the spin process start ? - Enter only Yes or No: ")
                    if input5.lower() == "yes":
                        a = int(input("enter the amount of time for spinning process: "))
                        print("__________________Machine is running please wait for",a,"sec__________________")
                        time.sleep(a)
                        print("Spinning process completed successfully.")
                    elif input5.lower() == "no":
                        print("Spinning process not yet started")
                        break
                    else:
                        print("__________unexpected error occurred__________")
                        loop5()
                    break

            loop1()
            loop2()
            loop3()
            loop4()
            loop5()
            print("Washing machine completed washing clothes using normal mode...............")


        elif Running_mode.lower() == "delicate":
            print("Delicate mode use Cold water and low spinning speed")
            print("Add two cups of detergent….")

            def loop1():
                while True:
                    input1 = input("Two cups of detergent filled ? - Enter only Yes or No:")
                    if input1.lower() == "yes":
                        print("__________________Machine is running please wait for 2sec__________________")
                        time.sleep(2)
                        print("Detergent filled success fully")
                    elif input1.lower() == "no":
                        print("_______Detergent not filled_______")
                        break
                    else:
                        print("__________unexpected error occurred__________")
                        loop1()
                    break

            def loop2():
                while True:
                    input2 = input("Fill water ? - Enter only Yes or No:")
                    if input2.lower() == "yes":

                        def semi_loop2():
                            a = int(input("Enter the amount of time to wash the clothes (in seconds): "))
                            while True:
                                if a > 3:
                                    print("Water will overflow, Enter the time below or equal to 3")
                                    semi_loop2()
                                elif a <= 3:
                                    print("_________Water filling is on process, please wait for",a,"sec________")
                                    time.sleep(a)
                                    print("water filling completed successfully.")
                                break

                        semi_loop2()

                    elif input2.lower() == "no":
                        print("________Water is not filled________")
                        print("can't run washing machine without water")
                        loop2()
                        break
                    else:
                        print("__________unexpected error occurred__________")
                        loop2()
                    break

            def loop3():
                while True:
                    input3 = input("Shall the process to wash the clothes start ? - Enter only Yes or No:")
                    if input3.lower() == "yes":
                        a = int(input("enter the amount of time to wash the clothes: "))
                        print("__________________Machine is running please wait for",a,"sec__________________")
                        time.sleep(a)
                        print("Washing completed successfully.")
                    elif input3.lower() == "no":
                        print("Clothes are not yet washed.")
                        break
                    else:
                        print("__________unexpected error occurred__________")
                        loop3()
                    break

            def loop4():
                while True:
                    input4 = input("Shall the process to Rinse the clothes start ? - Enter only Yes or No: ")
                    if input4.lower() == "yes":
                        a = int(input("enter the amount of time to rinse the clothes: "))
                        print("__________________Machine is running please wait for",a,"sec__________________")
                        time.sleep(a)
                        print("Rinse process completed successfully.")
                    elif input4.lower() == "no":
                        print("rinse process not yet started")
                        break
                    else:
                        print("__________unexpected error occurred__________")
                        loop4()
                    break

            def loop5():
                while True:
                    input5 = input("Shall the spin process start ? - Enter only Yes or No: ")
                    if input5.lower() == "yes":
                        a = int(input("enter the amount of time for spinning process: "))
                        print("__________________Machine is running please wait for",a,"sec__________________")
                        time.sleep(a)
                        print("Spinning process at low speed completed successfully.")
                    elif input5.lower() == "no":
                        print("Spinning process not yet started")
                        break
                    else:
                        print("__________unexpected error occurred__________")
                        loop5()
                    break

            loop1()
            loop2()
            loop3()
            loop4()
            loop5()
            print("Washing machine completed washing clothes using Delicate mode...............")

        elif Running_mode.lower() == "heavy":
            print("Heavy mode use Hot water and High spinning speed than other mode.")
            print("Add two cups of detergent….")

            def loop1():
                while True:
                    input1 = input("Two cups of detergent filled ? - Enter only Yes or No:")
                    if input1.lower() == "yes":
                        print("__________________Machine is running please wait for 2 sec__________________")
                        time.sleep(2)
                        print("Detergent filled success fully")
                    elif input1.lower() == "no":
                        print("_______Detergent not filled_______")
                        break
                    else:
                        print("__________unexpected error occurred__________")
                        loop1()
                    break

            def loop2():
                while True:
                    input2 = input("Fill water ? - Enter only Yes or No:")
                    if input2.lower() == "yes":

                        def semi_loop3():
                            a = int(input("Enter the amount of time to wash the clothes (in seconds): "))
                            while True:
                                if a > 3:
                                    print("Water will overflow, Enter the time below or equal to 3")
                                    semi_loop3()
                                elif a <= 3:
                                    print(
                                        "________Water filling is on process, please wait for",a,"sec________")
                                    time.sleep(a)
                                    print("water filling completed successfully.")
                                break

                        semi_loop3()

                    elif input2.lower() == "no":
                        print("________Water is not filled________")
                        print("can't run washing machine without water")
                        loop2()
                        break
                    else:
                        print("__________unexpected error occurred__________")
                        loop2()
                    break

            def loop3():
                while True:
                    input3 = input("Shall the process to wash the clothes start ? - Enter only Yes or No:")
                    if input3.lower() == "yes":
                        a = int(input("enter the amount of time to wash the clothes: "))
                        print("__________________Machine is running please wait for",a,"sec__________________")
                        time.sleep(a)
                        print("Washing completed successfully.")
                    elif input3.lower() == "no":
                        print("Clothes are not yet washed.")
                        break
                    else:
                        print("__________unexpected error occurred__________")
                        loop3()
                    break

            def loop4():
                while True:
                    input4 = input("Shall the process to Rinse the clothes start ? - Enter only Yes or No: ")
                    if input4.lower() == "yes":
                        a = int(input("enter the amount of time to rinse the clothes: "))
                        print("__________________Machine is running please wait for",a,"sec__________________")
                        time.sleep(a)
                        print("Rinse process completed successfully.")
                    elif input4.lower() == "no":
                        print("rinse process not yet started")
                        break
                    else:
                        print("__________unexpected error occurred__________")
                        loop4()
                    break

            def loop5():
                while True:
                    input5 = input("Shall the high speed spin process start ? - Enter only Yes or No: ")
                    if input5.lower() == "yes":
                        a = int(input("enter the amount of time for spinning process: "))
                        print("__________________Machine is running please wait for",a,"sec__________________")
                        time.sleep(a)
                        print("Spinning process at high speed completed successfully.")
                    elif input5.lower() == "no":
                        print("Spinning process not yet started")
                        break
                    else:
                        print("__________unexpected error occurred__________")
                        loop5()
                    break

            loop1()
            loop2()
            loop3()
            loop4()
            loop5()
            print("Washing machine completed washing clothes using Heavy mode...............")

        else:
            print("Invalid running mode.")

    except NameError as h:
        print("NameError:", h)
    except ValueError as h:
        print("ValueError:",h)
    except TypeError as e:
        print("TypeError:", e)
    else:
        print("....The washing machine has ended.....")


mode = input("Enter the mode (Auto or Manual): ")
if mode.lower() == "auto":
    auto_mode()
elif mode.lower() == "manual":
    manual_mode()
else:
    print("Invalid mode.")

