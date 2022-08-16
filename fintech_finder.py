# Cryptocurrency Wallet

################################################################################
# * Generates a new Ethereum account instance by using a mnemonic seed phrase.

# * Fetches and displays the account balance associated with the client's Ethereum account
# address.

# * Calculates the total value of an Ethereum transaction, including the gas
# estimate, that pays a Fintech Finder candidate for their work.

# * Digitally signs a transaction that pays a Fintech Finder candidate, and sends
# this transaction to the Ganache blockchain.

# * Reviews the transaction hash code associated with the validated blockchain transaction.

################################################################################
# Imports
import streamlit as st
from dataclasses import dataclass
from typing import Any, List
from web3 import Web3
w3 = Web3(Web3.HTTPProvider('HTTP://127.0.0.1:7545'))
################################################################################
################################################################################
# Custom Imports

from crypto_wallet import generate_account, get_balance, send_transaction

################################################################################
# Fintech Finder Candidate Information

# Database of Fintech Finder candidates including their name, digital address, rating and hourly cost per Ether.

candidate_database = {
    "Lane": ["Lane", "0xaC8eB8B2ed5C4a0fC41a84Ee4950F417f67029F0", "4.3", .20, "Images/lane.jpeg"],
    "Ash": ["Ash", "0x2422858F9C4480c2724A309D58Ffd7Ac8bF65396", "5.0", .33, "Images/ash.jpeg"],
    "Jo": ["Jo", "0x8fD00f170FDf3772C5ebdCD90bF257316c69BA45", "4.7", .19, "Images/jo.jpeg"],
    "Kendall": ["Kendall", "0x8fD00f170FDf3772C5ebdCD90bF257316c69BA45", "4.1", .16, "Images/kendall.jpeg"]
}

# A list of the FinTech Finder candidates first names
people = ["Lane", "Ash", "Jo", "Kendall"]

def get_people(w3):
    """Display the database of Fintech Finders candidate information."""
    db_list = list(candidate_database.values())

    for number in range(len(people)):
        st.header(db_list[number][0])
        st.image(db_list[number][4], width=200)
        st.write("**Name**:&nbsp;&nbsp; ", db_list[number][0])
        st.write("**Ethereum Wallet Address**:&nbsp;&nbsp;&nbsp;&nbsp; ", db_list[number][1])
        st.write("**FinTech Finder Rating**:&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ", db_list[number][2])
        st.write("**Hourly Rate per Ether**:&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ", str(db_list[number][3]), "ETH")
        st.text(" \n")

################################################################################
# Streamlit Code

# Streamlit application headings
st.markdown("# Fintech Finder!")
st.markdown("## Hire A Fintech Professional!")
st.text(" \n")

################################################################################
# Streamlit Sidebar Code - Start
st.sidebar.markdown('-'*10)
st.sidebar.markdown("## Connected Client Account Address")

##########################################
# Generating the Fintech Finder Customer's ethereum account wallet.  This is the
# ethereum account that will be used to transfer funds to the desired Fintech
# Professional.

account = generate_account()

##########################################

# Write the client's Ethereum account address to the sidebar
st.sidebar.write(account.address)

##########################################
# Display Balance of customer's account in ETH:

def display_customer_balance(w3,address):
    st.sidebar.write(f'### **Balance**: &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;{str(get_balance(w3,address))} ETH')
display_customer_balance(w3,account.address)
st.sidebar.markdown('-'*10)
##########################################

# Create a select box to chose a FinTech Hire candidate
person = st.sidebar.selectbox('Select a Person', people)

# Create a input field to record the number of hours the candidate worked
hours = st.sidebar.number_input("Number of Hours")

st.sidebar.markdown("## Candidate Name, Hourly Rate, and Ethereum Address")

# Identify the FinTech Hire candidate
candidate = candidate_database[person][0]

# Write the Fintech Finder candidate's name to the sidebar
st.sidebar.write(candidate)

# Identify the FinTech Finder candidate's hourly rate
hourly_rate = candidate_database[person][3]

# Write the inTech Finder candidate's hourly rate to the sidebar
st.sidebar.write(hourly_rate)

# Identify the FinTech Finder candidate's Ethereum Address
candidate_address = candidate_database[person][1]

# Write the inTech Finder candidate's Ethereum Address to the sidebar
st.sidebar.write(candidate_address)

# Write the Fintech Finder candidate's wage to the sidebar

st.sidebar.markdown("## Total Wage in Ether")

################################################################################
# 1. Fintech Finder customers will select a fintech professional from the
# application interface’s drop-down menu, and then input the amount of time for
# which they’ll hire the worker. Once a customer completes these steps, the app-
# lication will calculate the amount that the worker will be paid in ether. 

##########################################
# * The equation that calculates the candidate’s wage. This equation
# should assess the candidate’s hourly rate from the candidate database
# (`candidate_database[person][3]`) and then multiply this hourly rate by
# the value of the `hours` variable. This calculation’s output is named as a
# variable `wage`.
# * The `wage` variable is written to the Streamlit sidebar by using `st.sidebar.write`.

wage = hourly_rate * hours

st.sidebar.write(f"**{wage} ETH**")

##########################################
# * The `send_transaction` function is called and is passed three user parameters:
    # - Your Ethereum `account` information. 
    #  From the `account` instance, the application will be able to access the
    #  `account.address` information that is needed to populate the `from` data
    # attribute in the raw transaction.
    #- The `candidate_address` (which will be created and identified in the
    # sidebar when a customer selects a candidate). This will populate the `to`
    # data attribute in the raw transaction.
    # - The `wage` value. This will be passed to the `toWei` function to
    # determine the wei value of the payment in the raw transaction.

# * Save the transaction hash that the `send_transaction` function returns as a
# variable named `transaction_hash`, and have it display on the application’s
# web interface.


if st.sidebar.button("Send Transaction"):

    # The `send_transaction` function is called and passed 3 user parameters:
    # Your `account`, the `candidate_address`, and the `wage` as parameters
    # Save the returned transaction hash as a variable named `transaction_hash`
    transaction_hash = send_transaction(w3, account, candidate_address, wage)

    # Markdown for the transaction hash
    st.sidebar.markdown("#### Validated Transaction Hash")

    # Write the returned transaction hash to the screen
    st.sidebar.write(transaction_hash)

    # Celebrate your successful payment
    st.balloons()

# The function that starts the Streamlit application
# Writes FinTech Finder candidates to the Streamlit page
get_people(w3)

################################################################################
# Inspect the Transaction

# Send a test transaction by using the application’s web interface, and then
# look up the resulting transaction hash in Ganache.

# Complete the following steps:

# 1. From your terminal, navigate to the project folder that contains
# your `.env` file and the `fintech_finder.py` and `crypto_wallet.py` files.
# Be sure to activate your Conda `dev` environment if it is not already active.

# 2. To launch the Streamlit application,
# type `streamlit run fintech_finder.py`.

# 3. On the resulting webpage, select a candidate that you would like to hire
# from the appropriate drop-down menu. Then, enter the number of hours that you
# would like to hire them for. (Remember, you do not have a lot of ether in
# your account, so you cannot hire them for long!)

# 4 Click the Send Transaction button to sign and send the transaction with
# your Ethereum account information. If the transaction is successfully
# communicated to Ganache, validated, and added to a block,
# a resulting transaction hash code will be written to the Streamlit
# application sidebar.

# 5. Navigate to the Ganache accounts tab and locate your account (index 0).
    # * Take a note of the address, balance, and transaction (TX) count.

# 6. Navigate to the Ganache transactions tab and locate the transaction.
    # * Click the transaction and take a note of it.
