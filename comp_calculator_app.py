from compound_interest_calculator import CompoundCalculator
import streamlit as st

def main():

    st.set_page_config(layout="wide")
    with open('style.css') as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

    st.markdown("## Compound Interest Calculator", unsafe_allow_html=True)
    col1, col2 = st.columns([1,2])

    with col1:
        with st.form(key='my_form'):
            st.markdown("<h6>Please Enter the initial investment amount (£): </h6>", unsafe_allow_html=True)
            initial_investment = st.number_input(label = "hide", label_visibility= "hidden", min_value=0, max_value=100000)
            
            st.markdown("<h6>Please Enter the annual interest rate please: </h6>", unsafe_allow_html=True)
            annual_interest = st.slider(label = "hide", label_visibility= "hidden", min_value=0, max_value=50)
            
            st.markdown("<h6>Enter the number of years you plan to invest for: </h6>", unsafe_allow_html=True)
            num_years = st.slider(label = "hide", label_visibility= "hidden", min_value=1, max_value=35)
        
            st.markdown("<h6>How much money will you be investing annually (£)?: </h6>", unsafe_allow_html=True)
            annual_deposit = st.number_input(label = "hide", label_visibility= "hidden", min_value=0, max_value=10000)
            
            comp_calculator = CompoundCalculator(initial_investment, annual_interest, num_years, annual_deposit)
        
            if st.form_submit_button("Calculate"):
                comp_calculator = CompoundCalculator(initial_investment, annual_interest, num_years, annual_deposit)
                comp_calculator.calculate()
    with col2:
        st.image('di_caprio.gif', use_column_width=False)
if __name__ == '__main__':
    main()
