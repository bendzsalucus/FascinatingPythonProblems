# **Bank Account Simulator Task Instructions**

Welcome to the **Bank Account Simulator Challenge**! This task is designed to evaluate the capabilities of AI-powered tools like GitHub CoPilot, Codium, and Tabnine for class creation, testing, and code refinement.

---

## **Project Overview**

The Bank Account Simulator consists of:
1. A **BankAccount** base class (deliberately overly complex for refactoring purposes).
2. A subclass, **ProspectComplimentsAccount**, implemented as an example.
3. `Main.py` to run the application and simulate accounts.
4. `Tests.py` to run unit tests for the `ProspectComplimentsAccount` class.

---

## **Bank Account Types and Features**

### **1. BankAccount (Base Class)**
This is the base class with basic functionality, including:
- Opening an account with a minimum deposit.
- Withdrawing funds.
- Depositing funds (cash or checks).
- Logging in via an app.
- Checking account status.
- Recording transactions.

The `BankAccount` class is intentionally written in a complex manner without documentation for you (or should we say the AI) to refactor.

### **2. ProspectComplimentsAccount**
- A simple subclass of `BankAccount`.
- Has no rewards or interest features.

### **3. KasasaCashAccount**
- Minimum opening deposit: $25.
- Tiered interest:
  - 2.5% on balances $0–15,000 if qualifications are met.
  - 0.25% on balances above $15,000.
- Rewards Qualifications:
  - At least one ACH debit or credit.
  - 12 debit card purchases.
  - Logged in via online banking.
- Rewards only apply if qualifications are met. Otherwise, no interest is earned.

### **4. KasasaPlayAccount**
- Minimum opening deposit: $25.
- Same qualifications as KasasaCashAccount.
- Additional reward: Up to $10 reimbursement for purchases made at Apple, Microsoft, Netflix, or Hulu.

### **5. KasasaCashBackAccount**
- Minimum opening deposit: $25.
- Rewards: 3% cashback on debit card purchases up to $9/month.
- Same qualifications as KasasaCashAccount.

---

## **Methods to Implement**

For all accounts, the following methods should be implemented or extended as needed:

1. **`__init__`**:
   - Initializes the account with necessary attributes.

2. **`make_purchase(amount, retailer_name, date)`**:
   - Records a debit card transaction.

3. **`withdraw(amount)`**:
   - Withdraws funds from the account.

4. **`deposit_check(amount)` / `deposit_cash(amount)`**:
   - Deposits funds into the account.

5. **`check_in_via_app()`**:
   - Logs a user login event.

6. **`calculate_rewards_due()`**:
   - Determines if the account qualifies for rewards and calculates them.

7. **`check_account_status()`**:
   - Returns the account’s status (e.g., open or closed).

---

## **Your Tasks**

### 1. **Extend the BankAccount Class**
Create subclasses for the following account types:
- **KasasaCashAccount**
- **KasasaPlayAccount**
- **KasasaCashBackAccount**

#### **How to Generate Classes Using AI**
1. **Provide the AI Tool with Information**:
   - Give the tool the details about the account type (minimum deposit, rewards, etc.).
   - Example for KasasaCashAccount:
     ```
     - Minimum opening deposit: $25
     - Tiered interest: 
       - 2.5% on balances $0–15,000 if qualifications are met.
       - 0.25% on balances above $15,000.
     - Rewards Qualifications:
       - At least one ACH debit or credit.
       - 12 debit card purchases.
       - Logged in via online banking.
     - Rewards only apply if qualifications are met. Otherwise, no interest is earned.
     ```
2. **Ask the AI Tool to Generate the Class**:
   - Provide the prompt: "Generate a Python class based on the information above that extends the BankAccount class."

3. **Review and Refine**:
   - Ensure the generated class meets the requirements.

---

### 2. **Generate Comprehensive Unit Tests**
For each account class, create detailed unit tests that cover all functionality, including edge cases.

#### **How to Generate Tests Using AI**
1. **Provide the AI Tool with Class Details**:
   - Share the generated class and its methods with the AI.
   - Example: "Write unit tests for the KasasaCashAccount class. Include edge cases like failing to meet qualifications or handling invalid input."

2. **Expand on Testing Scope**:
   - Ensure tests cover:
     - Successful and unsuccessful transactions.
     - Rewards eligibility based on various scenarios.
     - Edge cases, such as:
       - Transactions that exceed the balance.
       - Negative or zero inputs.

3. **Run and Validate**:
   - Add the tests to `Tests.py`.
   - Execute `python Tests.py` to ensure all tests pass.

---

### 3. **Refactor the BankAccount Class**
The `BankAccount` class is overly complex by design. Your task is to refactor it to improve readability, usability, and efficiency.

#### **How to Use AI for Refactoring**
1. **Provide the AI Tool with the Code**:
   - Share the entire `BankAccount` class.
   - Ask the AI: "Refactor this class to improve readability and usability. Simplify variable names and remove redundant logic."

2. **Validate the Refactor**:
   - Test the refactored class to ensure it remains compatible with existing subclasses.

---

### 4. **Generate Documentation**
Write detailed docstrings for:
- Each account class.
- Each method, including arguments, return values, and edge case behavior.

#### **How to Use AI for Documentation**
1. **Prompt the AI Tool**:
   - Example: "Generate docstrings for the KasasaCashAccount class and its methods. Include explanations of arguments, return values, and edge cases."

---

### 5. **Run and Validate**
1. Execute `python Main.py` to test the implementation interactively.
2. Execute `python Tests.py` to run all unit tests.

---

## **Submission Guidelines**
- Ensure all classes are implemented and tested.
- Include a refactored version of the `BankAccount` class.
- Provide updated documentation for the project.

---

Feel free to ask the AI tools for guidance, code snippets, or clarifications at any step. Good luck and happy coding! 🚀
"""
