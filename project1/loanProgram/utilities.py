import pandas as pd 
import numpy as np 
import numpy_financial 

class CarLoan():
    
    def __init__(self, apr = 0, bal = 0, years = 5):
        
        self.vechicleID = None
        self.customerID = None
        self.customer_Type = None
        self.accountNum = None
        self.intrestRate = apr
        self.balance = bal 
        self.loanYears = years
        self.approved = None        
        
    # getter method
    def get_intrestRate(self):
        return self.intrestRate
      
    # setter method
    def set_intrestRate(self, apr):
        self.intrestRate = apr
    
    def printTable(self, loan, car_payment):
        ''' prints the entire loan table schedule '''        
        
        # set rows and cols
        rows = 5
        cols = 6
        
        # DataFrame is a 2-dimensional labeled data structure with columns of potentially different types.
        # pre load using the numpy. zeros() function returns a new array of given shape and type, with zeros.
        loan_table = pd.DataFrame(np.zeros((loan.loanYears, cols)))
        loan_table.columns =['Year', 'Initial_Balance', 'Payments', 'Interest', 'Principal', 'Ending_Balance']
        
        # The iloc indexer for Pandas Dataframe is used for integer-location based indexing / selection by position.
        # prime the first row in the table
        # year
        loan_table.iloc[0,0] = 1   
        # loan beginning amout
        loan_table.iloc[0,1] = loan.balance
        # loan payment amount
        loan_table.iloc[0,2] = car_payment
        # loan intrest rate
        loan_table.iloc[0,3] = loan.balance * loan.intrestRate
        # principle amount - intrest amount
        loan_table.iloc[0,4] = car_payment - (loan.balance * loan.intrestRate)
        # loan endning amount
        loan_table.iloc[0,5] = loan.balance - (car_payment - (loan.balance * loan.intrestRate) )
        
        # The iloc indexer for Pandas Dataframe is used for integer-location based indexing / selection by position.
        # loop and load the entire table
        for i in range(1,loan.loanYears):
            loan_table.iloc[i,0] = i + 1
            loan_table.iloc[i,1] = loan_table.iloc[(i-1), rows]
            loan_table.iloc[i,2] = car_payment
            loan_table.iloc[i,3] = loan_table.iloc[i,1] * loan.intrestRate
            loan_table.iloc[i,4] = car_payment - (loan_table.iloc[i,1] * loan.intrestRate)
            loan_table.iloc[i,5] = loan_table.iloc[i,1] - (car_payment - (loan_table.iloc[i,1] * loan.intrestRate))
        
        # round all values to two decimal places
        loan_table = loan_table.round(2)
        
        # display the entire pandas dataframe
        with pd.option_context("display.max_rows",None,"display.max_columns", None):
            print(loan_table)
        
    def process(self, applicant, car):
        ''' process the car loan '''        
        
        print('Processing loan')
        # calculate loan intrest rate based on credit score
        credit_score = applicant.creditScore
        
        # TODO move to a method        
        if credit_score > 780:
            # print('Excellent')
            # new 3.31% used 3.97%
            self.set_intrestRate(0.0397)     
            self.approved = True       
        elif 780 <= credit_score >= 670:
            # print('Good')
            # new 4.19% used 5.60%
            self.set_intrestRate(0.0560)
            self.approved = True
        elif 670 <= credit_score >= 600:
            # print('Fair')
            # new 7.15% used 9.97%
            self.set_intrestRate(0.0997)
            self.approved = True
        elif 600 <= credit_score >= 500:
            # print('Poor')
            # new 11.52% used 15.77%
            self.set_intrestRate(0.1577)
            self.approved = True
        elif 500 <= credit_score:
            # print('Very Poor')
            # new 14.04% used 19.61%
            self.set_intrestRate(0.1961)
            self.approved = False
        
        if self.approved == True:
            # Numpy financial’s pmt() function to compute payment against loan principal plus interest.            
            # generate payments
            payment = numpy_financial.pmt(self.intrestRate, nper = self.loanYears, pv = -car.price)        
        else:
            # loan not approved
            payment = None
            
        return payment
        
class Car():
    
    def __init__(self, carID, ID, year, make, model, mileage, price):
        
        self.vechileID = carID
        self.customerID = ID
        self.customerType = None
        self.owner = None
        self.year = year
        self.make = make
        self.model = model
        self.mileage = mileage
        self.price = price
    
    def calculate_value(self):
        ''' calculates the car value '''
        pass
        
    # getter method
    def get_owner(self):
        return self.owner
      
    # setter method
    def set_owner(self, owner):
        self.owner = owner
        
    def eligibility(self):
        ''' method to check if the vechile is eligible for financing''' 
        
        bFlag = True        
        current_year = 2020        
        diff = current_year - self.year
        
        if diff > 10:
            # car year is too old
            bFlag = False
            
        elif self.mileage > 100000:
            # car milage is too high
            bFlag = False            
        
        if self.price < 5000:            
            # price too low
            bFlag = False      
            
        return bFlag
                
class Person():
    
    def __init__(self, ID, name, address, phone, email, ssn, age, license, creditScore):
        
        self.personID = ID
        self.name = name
        self.address = address
        self.phone = phone
        self.email = email
        self.ssn = ssn
        self.age = age
        self.driversLicense = license
        self.creditScore = creditScore
    
    # getter method        
    def get_creditScore(self):
        return self.creditScore

class Company():
    
    def __init__(self, ID, name, address, website, creditScore = 0):
        
        self.companyID = ID
        self.name = name
        self.address = address
        self.website = website
        self.creditScore = creditScore        
        
class Bank():
    
    def __init__(self, ID, name):
        
        self.bankID = ID
        self.name = name

class Collateral():
    
    def __init__(self, ID, type, value):
        
        self.collateralID = ID
        self.collateralType = type
        self.value = value
