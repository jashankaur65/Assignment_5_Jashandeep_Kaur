# Intermediate Software Development Automated Teller Project
This project will be developed over the course of several assignments.
 Each assignment will build on the work done in the previous assignment(s).
 Ultimately, an entire system will be created to manage bank transactions
  for clients who have one or more bank accounts.

## Author
Jashandeep Kaur

## Assignment
Assignment 1: Indicate the Classes, Encapsulation and Unit Test Planning.
Assignment 2: Indicate the Abstraction, Inheritance and Polymorphism.
Assignment 3: This is assignment 3 which indicates the Design Patterns
such as observer pattern.
Assignment 4: Event-Driven Windows Application with PySide6 – 
Develop a responsive Windows app using PySide6, focusing on event handling,
inheritance, and data management.
Assignment 5: This project uses algorithms to make the code run better
and more efficiently.


## Encapsulation
Encapsulation in the BankAccount class is achieved by using private attributes
and providing controlled access to them through getter methods.

## Polymorphism
Polymorphism allows different account types to share a common structure 
while having their own behaviors. ChequingAccount, SavingsAccount,
and InvestmentAccount inherit from BankAccount and override methods like 
calculate_interest() and apply_fees(). 

## Strategy Pattern
The Strategy Pattern is used to make fee calculations flexible
and interchangeable. Different strategies like ManagementFeeStrategy,
MinimumBalanceStrategy, OverdraftStrategy, and ServiceChargeStrategy are
implemented as separate classes. This improves flexibility,
 maintainability, and extensibility.

## Observer Patteren
The Observer Pattern is used to notify multiple entities when a bank account
changes. ChequingAccount, SavingsAccount, and InvestmentAccount act as subjects, 
while AccountHolder, BankManager, and FraudDetectionSystem are observers.
When an event like a large withdrawal occurs, the account notifies its observers
—for example, sending an alert to the account holder and flagging
the transaction for fraud review. This design keeps the system flexible,
allowing new observers to be added without modifying account classes.

## Event-Driven Programming Paradigm
This app uses an event-driven style, meaning it waits for user actions
 (like clicks) to do things.
It uses PySide6’s signal-slot system, where a signal (an event) triggers
 a slot (a function) to respond.

## Filtering
The filtering algorithm is built to show only the rows that
match specific conditions. If a row meets the condition,
it stays visible—otherwise, it gets hidden from view.