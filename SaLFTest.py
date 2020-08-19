# COMP 301 Final Test
# Param Vir S. Sandhu


def main():
    print("Welcome to COMP 301 Future Value Calculator!!!")
    print("---------------------------------------------------")
    principal = eval(input("Enter the initial principal: "))
    print("--------------------------------------------------------")
    apr = eval(input("Enter the annual interest rate: "))
    print("----------------------------------------------------------")
    yr = eval(input("Enter the number of years: "))

    for i in range(yr):
        Final = principal * (1 + (apr * yr))

    print("The value in", yr, "years is $""{0:.2f}".format(Final))
    print("----------------------------------------------------------")

    print("Thanks for using COMP 301 Future Value Calculator.")
    print("---------------------------------------------------------")
    print("Bye for Now")


main()
