from tkinter import*
import random
import time
import datetime

root=Tk()
root.geometry("1600x8000")
root.title("Restaurant Billing System")

Tops=Frame(root, width=1600,relief=SUNKEN)
Tops.pack(side=TOP)

f1=Frame(root,width=800,height=700,relief=SUNKEN)
f1.pack()

#TIME

localtime=time.asctime(time.localtime(time.time()))

lblInfo=Label(Tops,font=('Algerian',50,'bold'),text="H FOR HOTEL & RESTAURANT",fg="brown",bd=5,anchor='w')
lblInfo.grid(row=0,column=0)

lblInfo=Label(Tops,font=('Calibri',20,'bold'),text=localtime,fg="Grey",bd=5,anchor='w')
lblInfo.grid(row=1,column=0)

def Ref():
    x=random.randint(10908,500876)
    randomRef=str(x)
    rand.set(randomRef)

    if (RedPasta.get()==""):
        CoRedPasta=0
    else:
        CoRedPasta=float(RedPasta.get())


    
    if (WhitePasta.get()==""):
        CoWhitePasta=0
    else:
        CoWhitePasta=float(WhitePasta.get())



    if (VegBiryani.get()==""):
        CoVegBiryani=0
    else:
        CoVegBiryani=float(VegBiryani.get())



    if (Coffee.get()==""):
        CoCoffee=0
    else:
        CoCoffee=float(Coffee.get())

        
    if (Maggi.get()==""):
        CoMaggi=0
    else:
        CoMaggi=float(Maggi.get())

     
    if (Drinks.get()==""):
        CoD=0
    else:
        CoD=float(Drinks.get())

                   
    CostofRedPasta =CoRedPasta * 100
    CostofDrinks=CoD * 20
    CostofWhitePasta = CoWhitePasta* 100
    CostofVegBiryani = CoVegBiryani * 100
    CostCoffee = CoCoffee* 20
    CostMaggi=CoMaggi * 60

    CostofMeal= "Rs", str('%.2f' % (CostofRedPasta+CostofDrinks+CostofWhitePasta+CostofVegBiryani+CostCoffee+CostMaggi))

    PayTax=((CostofRedPasta+CostofDrinks+CostofWhitePasta+CostofVegBiryani+CostCoffee+CostMaggi) * 0.2)

    TotalCost=(CostofRedPasta+CostofDrinks+CostofWhitePasta+CostofVegBiryani+CostCoffee+CostMaggi)
 
    Ser_Charge= ((CostofRedPasta+CostofDrinks+CostofWhitePasta+CostofVegBiryani+CostCoffee+CostMaggi)/99)

    Service = "Rs", str ('%.2f' % Ser_Charge)

    OverAllCost ="Rs", str ('%.2f' % (PayTax+TotalCost+Ser_Charge))

    PaidTax= "Rs", str ('%.2f' % PayTax)

    Service_Charge.set(Service)
    Cost.set(CostofMeal)
    Tax.set(PaidTax)
    SubTotal.set(CostofMeal)
    Total.set(OverAllCost)
    
def qExit():
    root.destroy()

def Reset():
    rand.set("Reference Number") 
    RedPasta.set("")
    WhitePasta.set("")
    VegBiryani.set("")
    SubTotal.set("")
    Total.set("")
    Service_Charge.set("")
    Drinks.set("")
    Tax.set("")
    Cost.set("")
    Coffee.set("")
    Maggi.set("")
    
#Restaraunt Info 1
rand = StringVar()
RedPasta=StringVar()
WhitePasta=StringVar()
VegBiryani=StringVar()
SubTotal=StringVar()
Total=StringVar()
Service_Charge=StringVar()
Drinks=StringVar()
Tax=StringVar()
Cost=StringVar()
Coffee=StringVar()
Maggi=StringVar()



lblReference= Label(f1, font=('arial', 16, 'bold'),text="Reference",bd=16,anchor="w")
lblReference.grid(row=0, column=0)
rand = StringVar(root, value='Reference Number')
txtReference=Entry(f1, font=('arial',16,'bold'),textvariable=rand,bd=5,insertwidth=4,bg="powder blue",justify='right')
txtReference.grid(row=0,column=1)

lblRedPasta= Label(f1, font=('arial', 16, 'bold'),text="Red Pasta",bd=16,anchor="w")
lblRedPasta.grid(row=1, column=0)
txtRedPasta=Entry(f1, font=('arial',16,'bold'),textvariable=RedPasta,bd=5,insertwidth=4,bg="powder blue",justify='right')
txtRedPasta.grid(row=1,column=1)


lblWhitePasta= Label(f1, font=('arial', 16, 'bold'),text="White Pasta",bd=16,anchor="w")
lblWhitePasta.grid(row=2, column=0)
txtWhitePasta=Entry(f1, font=('arial',16,'bold'),textvariable=WhitePasta,bd=5,insertwidth=4,bg="powder blue",justify='right')
txtWhitePasta.grid(row=2,column=1)


lblVegBiryani= Label(f1, font=('arial', 16, 'bold'),text="Veg Biryani",bd=16,anchor="w")
lblVegBiryani.grid(row=3, column=0)
txtVegBiryani=Entry(f1, font=('arial',16,'bold'),textvariable=VegBiryani,bd=5,insertwidth=4,bg="powder blue",justify='right')
txtVegBiryani.grid(row=3,column=1)

lblCoffee= Label(f1, font=('arial', 16, 'bold'),text="Coffee",bd=16,anchor="w")
lblCoffee.grid(row=4, column=0)
txtCoffee=Entry(f1, font=('arial',16,'bold'),textvariable=Coffee,bd=5,insertwidth=4,bg="powder blue",justify='right')
txtCoffee.grid(row=4,column=1)

lblMaggi= Label(f1, font=('arial', 16, 'bold'),text="Maggi",bd=16,anchor="w")
lblMaggi.grid(row=5, column=0)
txtMaggi=Entry(f1, font=('arial',16,'bold'),textvariable=Maggi,bd=5,insertwidth=4,bg="powder blue",justify='right')
txtMaggi.grid(row=5,column=1)

#RESTAURANT INFO 2


lblDrinks= Label(f1, font=('arial', 16, 'bold'),text="Drinks",bd=16,anchor="w")
lblDrinks.grid(row=0, column=2)
txtDrinks=Entry(f1, font=('arial',16,'bold'),textvariable=Drinks,bd=5,insertwidth=4,bg="powder blue",justify='right')
txtDrinks.grid(row=0,column=3)

lblCost= Label(f1, font=('arial', 16, 'bold'),text="Cost of Meal",bd=16,anchor="w")
lblCost.grid(row=1, column=2)
txtCost=Entry(f1, font=('arial',16,'bold'),textvariable=Cost,bd=5,insertwidth=4,bg="powder blue",justify='right')
txtCost.grid(row=1,column=3)


lblService= Label(f1, font=('arial', 16, 'bold'),text="Service Charge",bd=16,anchor="w")
lblService.grid(row=2, column=2)
txtService=Entry(f1, font=('arial',16,'bold'),textvariable=Service_Charge,bd=5,insertwidth=4,bg="powder blue",justify='right')
txtService.grid(row=2,column=3)


lblStateTax= Label(f1, font=('arial', 16, 'bold'),text="State Tax",bd=16,anchor="w")
lblStateTax.grid(row=3, column=2)
txtStateTax=Entry(f1, font=('arial',16,'bold'),textvariable=Tax,bd=5,insertwidth=4,bg="powder blue",justify='right')
txtStateTax.grid(row=3,column=3)

lblSubTotal= Label(f1, font=('arial', 16, 'bold'),text="Sub Total",bd=16,anchor="w")
lblSubTotal.grid(row=4, column=2)
txtSubTotal=Entry(f1, font=('arial',16,'bold'),textvariable=SubTotal,bd=5,insertwidth=4,bg="powder blue",justify='right')
txtSubTotal.grid(row=4,column=3)

lblTotalCost= Label(f1, font=('arial', 16, 'bold'),text="Total Cost",bd=16,anchor="w")
lblTotalCost.grid(row=5, column=2)
txtTotalCost=Entry(f1, font=('arial',16,'bold'),textvariable=Total,bd=5,insertwidth=4,bg="powder blue",justify='right')
txtTotalCost.grid(row=5,column=3)

#Buttons
btnTotal=Button(f1,padx=16,pady=8,bd=10,fg="black",font=('arial',16,'bold'),width=10,text="Total",bg="green",command=Ref).grid(row=7,column=1)

btnReset=Button(f1,padx=16,pady=8,bd=10,fg="black",font=('arial',16,'bold'),width=10,text="Reset",bg="yellow",command=Reset).grid(row=7,column=2)

btnExit=Button(f1,padx=16,pady=8,bd=10,fg="black",font=('arial',16,'bold'),width=10,text="Exit",bg="red",command=qExit).grid(row=7,column=3)


root.mainloop()


