"""
Build a compound calculator class that takes in the following inputs:
- initial investment (£) Float
- Annual interest (%) Float
- Number of Years INT
- Annual Deposit Amount (£)

Output:
- Final Investment (£)

"""
from decimal import Decimal, getcontext
import streamlit as st

class CompoundCalculator:
    getcontext().prec = 10
    def __init__(self, initial_investment_amount, annual_interest, num_years, annual_deposit_amount):
        self.initial_investment_amount =  Decimal(initial_investment_amount)
        self.annual_interest =  Decimal(annual_interest)/100
        self.num_years = int(num_years)
        self.annual_deposit_amount =  Decimal(annual_deposit_amount)

    def calculate(self):
        initial_return = Decimal(self.initial_investment_amount * ((1 + self.annual_interest) ** self.num_years))
        if self.annual_interest == 0:
            invest_return = self.annual_deposit_amount * self.num_years
        else:
            invest_return = self.annual_deposit_amount * ((1 + self.annual_interest) ** self.num_years - 1) / self.annual_interest

        total = initial_return + invest_return
        return st.success((f"The total amount after {self.num_years} years will be £{total:,.2f}"))
