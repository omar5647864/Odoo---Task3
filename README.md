# Odoo---Task3

- Create a new Module called "Allowed Discount"

In res. partner, add new field "allowed discount". >> type = float, not mandatory

In module accounting >> settings, add a new tab called " customer discount "
below this tab add :-
- Allowed discount account >> mandatory - many to one field ( account.account)

- allowed discount product >>  mandatory - many to one field. ( product. product) , domain : Product type = service 


In sales order >> so line
Select the customer, and if " allowed discount > 0 " 
 
so line will be create with the data 
1- unit price = field "allowed discount" from this partner form * (-1)
2- product account = Allowed discount account from " accounting settings " to be in invoice line 
3-  product = allowed discount product From " accounting settings "  
4- the quantity of the product will be one.  


Journal Entry :-

Then, journal entry generated from invoice, its should contains discount line 
Debit and credit should be equal after the discount
