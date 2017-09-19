import welcome as start
import login
import file
from collections import Counter

foods=dict()
foodbill=0
drinksbill=0
drinks=dict()


def food() :
	global foods
	foods={'1':'Chicken strips',
		'2':'French Fries',
		'3':'Hamburger',
		'4':'Hotdogs',
		'5':'Caeser Salad',
		'6':'Potato smileys',
		'7':'Chocolate Lava Cake',
		'8':'Cheese Beef Steak',
		'9':'Chicken Wings'}
	print  '_______________________The menu for food is______________________________\n'
	print '''\t1.\tChicken Strips- \t Rs.60 \n
	2.\tFrench Fries-\t\t Rs.40\n
	3.\tHamburger-\t\t Rs.55\n
	4.\tHotdogs-\t\t Rs.60\n
	5.\tCaesar Salad-\t\t Rs.60\n
	6.\tPotato Smileys-\t\t Rs.40\n
	7.\tChocolate Lava Cake-\t Rs.50\n
	8.\tCheese Beef Steak-\t Rs.60\n
	9.\tChicken Wings-\t\t Rs.70\n
        \n---------------**-----------------------**-------------------------**-----------\n'''
	order(foods,1)

	
def order(dictn,ids):
	items=list()
	global drinksbill,foodbill

	dchoice =raw_input("Enter your order\n")
	print 'your order is as follows\n'
	for key,value in dictn.iteritems():
		for i in dchoice:
			if int(key)==int(i):
				items.append(value)	
	counter=Counter(items)
	for key,value in counter.iteritems():
		print value,"\t",key,"\n"
			
	'''x=list(set(items))
	print " \n".join(str(i) for i in x)'''
	dictnid=ids			
	bill(dchoice,dictnid)

def tb():
	 
	print"\t\t_______________BILL_______________\n"
	print 'Total amount payable for food:\t\t',foodbill
	print '\nTotal amount payable for drinks:\t',drinksbill
	tot=foodbill+drinksbill
	ser=.10*(foodbill+drinksbill)
	tax=.14*(tot+ser)
	print '\nService tax Payable:\t\t\t',ser
	print '\nVAT payable:\t\t\t\t',tax
	print '\nNet amount payable:\t\t\t',(tot+ser+tax)

def bill(choice,ids):
	global foodbill,drinksbill
	d=0
	f=0
	if(ids==1):
		tb=0

		for i in choice:

			if int(i)==1:

				tb=tb+30  

			elif int(i)==2:

				tb=tb+20

			elif int(i)==3:	

				tb=tb+50

			elif int(i)==4:

				tb=tb+30

			elif int(i)==5:	

				tb=tb+40

			elif int(i)==6:
				tb=tb+40

			elif int(i)==7:	

				tb=tb+30
			elif int(i)==8:
				tb=tb+20
			elif int(i)==9:	

				tb=tb+50
		f=tb
	else: 	
		tb=0
		for i in choice:
			if int(i)==1:
				tb=tb+60  
			elif int(i)==2:
				tb=tb+40
			elif int(i)==3:	
				tb=tb+55
			elif int(i)==4:
				tb=tb+60
			elif int(i)==5:	
				tb=tb+60
			elif int(i)==6:
				tb=tb+40
			elif int(i)==7:	
				tb=tb+50
			elif int(i)==8:
				tb=tb+60
			elif int(i)==9:	
				tb=tb+70
		d=tb
	foodbill=foodbill+f	
	drinksbill=drinksbill+d
					
	
def drink():
	global drinks
	drinks={'1':'Apple Juice',
		'2':'Lemonade',
		'3':'Milkshake',
		'4':'Coca Cola',
		'5':'Hot Chocolate',
		'6':'Fruit Punch',
		'7':'Orange Juice',
		'8':'Tea',
		'9':'Cold Coffee'}
	print  '____________________________The Menu for Drinks_______________________________'
	print '''\t1:Apple Juice:\t\t Rs.30\n
	2.Lemonade:\t\t Rs.20\n
	3.Milkshake:\t\t Rs.50\n
	4.Coca Cola:\t\t Rs.30\n
	5.Hot Chocolate:\tRs.40\n
	6.Fruit Punch:\t\tRs.40\n
	7.Orange Juice:\t\tRs.30\n
	8.Tea:\t\t\tRs.20\n
	9.Cold Coffee:\t\tRs.50\n
\n-----------------------------------------***------------------------------------\n'''
	order(drinks,2)
	
start.welcome()	
flag1=0
while flag1==0:
	yes1=raw_input("Do you have a reservation?\nY/N\n")
	yes=yes1.lower()
	if yes=='n':
		file.res()
		flag1=login.log()

	else : 
		flag1=login.log()
	
while True:		
	if flag1==1:
		print '\nEnter the choice of food\n','\t1.Food\t2.Drinks\t3.Exit\n'
		choice=raw_input()
		if int(choice)==1:	
			food()
		elif int(choice)==2:
			drink()
		else: break
	else : 
		print "login failed\n"
		login.log()

	
tb()
start.end()
