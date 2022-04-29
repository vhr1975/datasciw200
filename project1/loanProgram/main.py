
import utilities
import random
from random import randint

def generate_account_number():
    ''' method that generates a 16 digit random ID number '''
    
    accountNum = ''
    
    for i in range(16):
        accountNum = accountNum + str(randint(0,9))
        
    return accountNum

# main method
def main ():

    bFlag = False
    applicantID = generate_account_number()
    
    print('Welcome to the car loan program')
    print('Will this be a personal or commercial loan?')
        
    while bFlag == False:
        
        loanType = input('Please enter p = personal or c = commercial: or q = quit ')
        
        if loanType == 'p':

            name = input('Please enter the persons name: ')
            address = input('Please enter the persons address: ')
            license = input('Please enter the persons drivers license: ')
            phone = input('Please enter the persons phone: ')
            email = input('Please enter the persons email: ')
            ssn = input('Please enter the persons ssn: ')
            age = input('Please enter the persons age: ')
            creditScore = input('Please enter the persons credit score: ')
            downPayment = input('Please enter the persons down payment: ')            
            bFlag = True  
            
            # type cast into integer
            creditScore = int(creditScore)
                      
            applicant = utilities.Person(applicantID, name, address, phone, email, ssn, age, license, creditScore)
            print('Application for:', applicant.name, 'has been entered.')
            
        elif loanType == 'c':
            
            name = input('Please enter the company\'s name: ')
            address = input('Please enter the company\'s address: ')
            website = input('Please enter the company\'s website: ')            
            collateralType = input('Please enter the company\'s collateral type: ')
            collateralValue = input('Please enter the company\'s collateral value: ')            
            companyID = generate_account_number()
            
            # type cast into integer
            collateralValue = int(collateralValue)
            
            applicant = utilities.Company(companyID, name, address, website)
            
            bFlag = True                   
            collateralID = generate_account_number()
            collateral = utilities.Company(collateralID, collateralType, collateralValue, website)
            
            # TODO move to a method        
            if collateralValue > 50000.:
                # print('Excellent')
                # new 3.31% used 3.97%
                applicant.creditScore = 800
            elif 4999 <= collateralValue >= 3000:
                # print('Good')
                # new 4.19% used 5.60%
                applicant.creditScore = 700
            elif 2999 <= collateralValue >= 10000:
                # print('Fair')
                # new 7.15% used 9.97%
                applicant.creditScore = 630
            elif 9999 <= collateralValue >= 1000:
                # print('Poor')
                # new 11.52% used 15.77%
                applicant.creditScore = 550
            elif 999 <= collateralValue:
                # print('Very Poor')
                # new 14.04% used 19.61%
                applicant.creditScore = 450
            
        elif loanType == 'q':
            
            print('Goodbye')
            bFlag = True
            quit()
    
    car_eligible = False
        
    while car_eligible == False:
        
        # enter car information
        year = input('Please enter the car\'s year: ')
        make = input('Please enter the car\'s make: ')
        model = input('Please enter the car\'s model: ')
        mileage = input('Please enter the car\'s mileage: ')        
        price = input('Please enter the car\'s sticker price: ')
        apr = input('Please enter the car\'s loan interest: ')
        # years = input('Please enter the car\'s loan year length: ')
        years = 5
        carID = generate_account_number()
        
        # type cast into integer
        year = int(year)
        mileage = int(mileage)
        price = int(price)
        apr = float(apr)
        
        car = utilities.Car(carID, applicantID, year, make, model, mileage, price)
        
        print('Car information is being processed.')
        car_eligible = car.eligibility()
        
        if car_eligible == True:
            # car is eligiable
            car_eligible = True
            print('Car is eligible for financing.')
        else:
            # car is not eligiable
            car_eligible = False
            print('Vehicles older than 10 years, with more than 100,000 miles, priced less than $5,000 do not qualify for financing.')
    
    ########################################################################################################
    
    # set values based on entered info    
    loan = utilities.CarLoan(apr, car.price, years)
    car_payment = loan.process(applicant, car)

    ########################################################################################################  
    
    if loan.approved == True:
        
        # print('Annual car payment amout:', round(car_payment, 2))
        banks = ['Bank of America', 'Wells Fargo', 'Chase Bank', 'Patelco Credit Union']    
        bank_name = random.choice(banks)
        bank_number = generate_account_number()
        
        bank = utilities.Bank(bank_number, bank_name)
        
        print('Congratulations', bank.name, 'has approved your loan.')
        print('Please see your loan schedule below: ')
        # print loan schedule table
        loan.printTable(loan, car_payment)
    
    else:
        
        print('Unfortunately your loan cannot be approved at this time.')
        print('Please try increasing your credit score or increaseing your down payment amount.')
        
    
# set main entry point to main
if __name__ == '__main__':
    main()
    