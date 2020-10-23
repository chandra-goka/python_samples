
if __name__ == '__main__':

    def calculate_simple_interest(p,t=1,r=10):
        # simple interest = (p * t * r) / 100
        # Where,
        # p is the principal amount
        # t is the time in years and
        # r is the rate of interest

        # taking default interest rate, years as default parameters - 10,1 respectively
        return p * t * r / 100

    # function call with default parameter values
    interest = calculate_simple_interest(100000)
    print("Interest with default values ",interest)

    # function call with overridden parameter values
    interest = calculate_simple_interest(100000,2,4)
    print("Interest overridden parameters ",interest)

