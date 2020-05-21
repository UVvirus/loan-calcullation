def get_loan_info():
    loan={}
    loan['principal']=float(input("Enter the loan amount:"))
    loan['rate']=float(input("Enter the interest:"))/100
    loan['monthly payment']=float(input("Enter monthly payment:"))
    loan['money paid']=0
    return loan
def show_loan_info(loan,moths_passed):
    print("loan information after"+moths_passed)
    for key,value in loan.items():
        print(key+":"+str(value))

def collect_intrest(loan):
    loan['principal']=loan['principal']+loan['principal']*loan['rate']/12

def monthly_payment(loan):
    loan['principal']=loan['principal'] - loan['monthly payment']
    if loan['principal'] > 0:
      loan['money paid'] += loan['monthly payment']
    elif loan['principal'] < 0:
        loan['pr']
get_loan_info()

show_loan_info()