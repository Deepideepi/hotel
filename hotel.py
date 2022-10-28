
from tkinter import*
from tkinter import filedialog,messagebox
import random
import time
from urllib import response
from numpy import save
import requests
def reset():
    textReceipt.delete(1.0,END)
    e_roti.set('0')
    e_daal.set('0')
    e_fish.set('0')
    e_naan.set('0')
    e_chicken.set('0')
    e_chapathi.set('0')
    e_paneer.set('0')
    e_mutton.set('0')
    e_cauliflower.set('0')
    e_lemon_tea.set('0')
    e_coffee.set('0')
    e_tea.set('0')
    e_faluda.set('0')
    e_badam_milk.set('0')
    e_rose_milk.set('0')
    e_cold_drinks.set('0')
    e_masala_tea.set('0')
    e_mango_juice.set('0')
    e_oreo.set('0')
    e_apple.set('0')
    e_kitkat.set('0')
    e_vanilla.set('0')
    e_banana.set('0')
    e_brownie.set('0')
    e_pineapple.set('0')
    e_chocolate.set('0')
    e_black_forest.set('0')
    textroti.config(state=DISABLED)
    textdaal.config(state=DISABLED)
    textfish.config(state=DISABLED)
    textnaan.config(state=DISABLED)
    textchicken.config(state=DISABLED)
    textchapathi.config(state=DISABLED)
    textpaneer.config(state=DISABLED)
    textmutton.config(state=DISABLED)
    textcauliflower.config(state=DISABLED) 
    textcoffee.config(state=DISABLED)
    texttea.config(state=DISABLED)
    textfaluda.config(state=DISABLED)
    textbadam_milk.config(state=DISABLED)
    textrose_milk.config(state=DISABLED)
    textcold_drinks.config(state=DISABLED)
    textmasala_tea.config(state=DISABLED)
    textmango_juice.config(state=DISABLED)
    textoreo.config(state=DISABLED)
    textapple.config(state=DISABLED)
    textkitkat.config(state=DISABLED)
    textvanilla.config(state=DISABLED)
    textbanana.config(state=DISABLED)
    textbrownie.config(state=DISABLED)
    textpineapple.config(state=DISABLED)
    textchocolate.config(state=DISABLED)
    textblack_forest.config(state=DISABLED)
    var1.set('0')
    var2.set('0')
    var3.set('0')
    var4.set('0')
    var5.set('0')
    var6.set('0')
    var7.set('0')
    var8.set('0')
    var9.set('0')
    var10.set('0')
    var11.set('0')
    var12.set('0')
    var13.set('0')
    var14.set('0')
    var15.set('0')
    var16.set('0')
    var17.set('0')
    var18.set('0')
    var19.set('0')
    var20.set('0')
    var21.set('0')
    var22.set('0')
    var23.set('0')
    var24.set('0')
    var25.set('0')
    var26.set('0')
    var27.set('0')
    CostofFoodvar.set('')
    CostofDrinksvar.set('')
    CostofCakesvar.set('')
    subtotalvar.set('')
    servicetaxvar.set('')
    totalcostvar.set('')
def send():
    if textReceipt.get(1.0,END)=='\n':
        pass
    else:
        def send_msg():
            message=textarea.get(1.0,END)
            number=numberfield.get()
            auth='pRMuzQCxXeWjLBS4J5TFO0dcVZAoD71NEUk3Gmyr2Iah6KHqbiYdVRwy2Ha0fxSALnTjmtOZWvBIKzJE'
            url='https://www.fast2sms.com/dev/bulkV2'
            params={
                'authorization':auth,
                'message':'bill receipt',
                'number':9952593021,
                'language':'english'
            }
            response=requests.get(url,params=params)
            dic=response.json()
            result=dic.get('return')

            if result==True:
                messagebox.showinfo('Send Successfully','Message Send Successfully')
            else:
                messagebox.showerror('Error','Something went wrong')
        root2=Toplevel()
        

        root2.title("SEND BILL")
        root2.config(bg='red4')
        root2.geometry('485x620+50+50')
        numberLabel=Label(root2,text='Mobile Number',font=('arial',25,'bold underline'),bg='red4',fg='white')
        numberLabel.pack(pady=5)
        numberfield=Entry(root2,font=('helvertica',22,'bold'),bd=3,width=24)
        numberfield.pack(pady=5)
        billLabel=Label(root2,text='Bill Details',font=('arial',25,'bold underline'),bg='red4',fg='white')
        billLabel.pack(pady=5)
        textarea=Text(root2,font=('arial',12,'bold'),bd=3,width=42,height=14)
        textarea.pack(pady=5)
        textarea.insert(END,'Receipt Ref:\t\t'+billnumber+'\t\t'+date+'\n\n')
        
        if CostofFoodvar.get()!='0 Rs':
            textarea.insert(END,f'Cost of Food\t\t\t{priceofFood}Rs\n')
        if CostofDrinksvar.get()!='0 Rs':
            textarea.insert(END,f'Cost of Drinks\t\t\t{priceofDrinks}Rs\n')
        if CostofCakesvar.get()!='0 Rs':
            textarea.insert(END,f'Cost of Cakes\t\t\t{priceofCakes}Rs\n\n')
        textarea.insert(END,f'Sub Total\t\t\t{subtotalofitems}Rs\n')
        textarea.insert(END,f'Service Tax\t\t\t{50}Rs\n')
        textarea.insert(END,f'Total Cost\t\t\t{subtotalofitems+50}Rs\n')
        sendbutton=Button(root2,text='SEND',font=('arial',19,'bold'),bg='white',fg='red4',bd=7,relief=GROOVE,command=send_msg)
        sendbutton.pack(pady=5)
        
        root2.mainloop()
def save():
    if textReceipt.get(1.0,END)=='\n':
        pass
    else:
        url=filedialog.asksaveasfile(mode='w',defaultextension='.txt')
        if url==None:
            pass
        else:
            bill_data=textReceipt.get(1.0,END)
            url.write(bill_data)
            url.close()
            messagebox.showinfo('Information','Your Bill Is Successfully Saved')    
def receipt():
    global billnumber,date
    if CostofFoodvar.get() !='' or CostofDrinksvar.get() !='' or CostofCakesvar.get() !='':
        textReceipt.delete(1.0,END)
        x=random.randint(100,10000)
        billnumber='BILL'+str(x)
        date=time.strftime('%d-%m-%Y')
        textReceipt.insert(END,'ReceiptRef:\t'+billnumber+'\t\t'+date+'\n')
        textReceipt.insert(END,'***************************************************************\n')
        textReceipt.insert(END,'Items:\t\t Cost of Items(Rs)\n')
        textReceipt.insert(END,'***************************************************************\n')
        if e_roti.get()!='0':
            textReceipt.insert(END,f'Roti\t\t\t{int(e_roti.get())*10}\n\n')
        if e_daal.get()!='0':
            textReceipt.insert(END,f'Daal\t\t\t{int(e_daal.get())*30}\n\n')
        if e_fish.get()!='0':
            textReceipt.insert(END,f'Fish\t\t\t{int(e_fish.get())*70}\n\n')
        if e_naan.get()!='0':
            textReceipt.insert(END,f'Naan\t\t\t{int(e_naan.get())*20}\n\n')
        if e_chicken.get()!='0':
            textReceipt.insert(END,f'Chicken\t\t\t{int(e_chicken.get())*80}\n\n')
        if e_chapathi.get()!='0':
            textReceipt.insert(END,f'Chapathi\t\t\t{int(e_chapathi.get())*15}\n\n')
        if e_paneer.get()!='0':
            textReceipt.insert(END,f'Paneer\t\t\t{int(e_paneer.get())*40}\n\n')
        if e_mutton.get()!='0':
            textReceipt.insert(END,f'Mutton\t\t\t{int(e_mutton.get())*90}\n\n')
        if e_cauliflower.get()!='0':
            textReceipt.insert(END,f'Cauliflower\t\t\t{int(e_cauliflower.get())*60}\n\n')
        if e_lemon_tea.get()!='0':
            textReceipt.insert(END,f'Lemon Tea\t\t\t{int(e_lemon_tea.get())*10}\n\n')
        if e_coffee.get()!='0':
            textReceipt.insert(END,f'Coffee\t\t\t{int(e_coffee.get())*15}\n\n')
        if e_tea.get()!='0':
            textReceipt.insert(END,f'Tea\t\t\t{int(e_tea.get())*20}\n\n')
        if e_faluda.get()!='0':
            textReceipt.insert(END,f'Faluda\t\t\t{int(e_faluda.get())*60}\n\n')
        if e_badam_milk.get()!='0':
            textReceipt.insert(END,f'Badam Milk\t\t\t{int(e_badam_milk.get())*35}\n\n')
        if e_rose_milk.get()!='0':
            textReceipt.insert(END,f'Rose Milk\t\t\t{int(e_rose_milk.get())*30}\n\n')
        if e_cold_drinks.get()!='0':
            textReceipt.insert(END,f'Cold Drinks\t\t\t{int(e_cold_drinks.get())*25}\n\n')
        if e_masala_tea.get()!='0':
            textReceipt.insert(END,f'Masala Tea\t\t\t{int(e_masala_tea.get())*30}\n\n')
        if e_mango_juice.get()!='0':
            textReceipt.insert(END,f'Mango Juice\t\t\t{int(e_mango_juice.get())*30}\n\n')
        if e_oreo.get()!='0':
            textReceipt.insert(END,f'Oreo\t\t\t{int(e_oreo.get())*600}\n\n')
        if e_apple.get()!='0':
            textReceipt.insert(END,f'Apple\t\t\t{int(e_apple.get())*200}\n\n')
        if e_kitkat.get()!='0':
            textReceipt.insert(END,f'Kitkat\t\t\t{int(e_kitkat.get())*300}\n\n')
        if e_vanilla.get()!='0':
            textReceipt.insert(END,f'Vanilla\t\t\t{int(e_vanilla.get())*560}\n\n')
        if e_banana.get()!='0':
            textReceipt.insert(END,f'Banana\t\t\t{int(e_banana.get())*770}\n\n')
        if e_brownie.get()!='0':
            textReceipt.insert(END,f'Brownie\t\t\t{int(e_brownie.get())*620}\n\n')
        if e_pineapple.get()!='0':
            textReceipt.insert(END,f'Pineapple\t\t\t{int(e_pineapple.get())*700}\n\n')
        if e_chocolate.get()!='0':
            textReceipt.insert(END,f'Chocolate\t\t\t{int(e_chocolate.get())*880}\n\n')
        if e_black_forest.get()!='0':   
            textReceipt.insert(END,f'Black Forest\t\t\t{int(e_black_forest.get())*900}\n\n')
        textReceipt.insert(END,'***************************************************************\n')
        if CostofFoodvar.get()!='0 Rs':
            textReceipt.insert(END,f'Cost of Food\t\t\t{priceofFood}Rs\n\n')
        if CostofDrinksvar.get()!='0 Rs':
            textReceipt.insert(END,f'Cost of Drinks\t\t\t{priceofDrinks}Rs\n\n')
        if CostofCakesvar.get()!='0 Rs':
            textReceipt.insert(END,f'Cost of Cakes\t\t\t{priceofCakes}Rs\n\n')
        textReceipt.insert(END,f'Sub Total\t\t\t{subtotalofitems}Rs\n\n')
        textReceipt.insert(END,f'Service Tax\t\t\t{50}Rs\n\n')
        textReceipt.insert(END,f'Total Cost\t\t\t{subtotalofitems+50}Rs\n\n')
        textReceipt.insert(END,'***************************************************************\n')
    else:
        messagebox.showerror('Error','Something went wrong')
def totalcost():
    global priceofFood,priceofDrinks,priceofCakes,subtotalofitems
    if var1.get()!=0 or var2.get !=0 or var3.get !=0 or var4.get !=0 or var5.get !=0 or var6.get !=0 or var7.get !=0 or var8.get !=0 or var9.get !=0 or var10.get() !=0 or var11.get !=0 or var12.get !=0 or var13.get !=0 or var14.get !=0  or var15.get !=0 or var16.get !=0 or var17.get !=0 or var18.get !=0 or var19.get() !=0 or var20.get !=0 or var21.get !=0 or var22.get !=0 or var23.get !=0  or var24.get !=0 or var25.get !=0 or var26.get !=0 or var27.get !=0: 
        item1=int(e_roti.get())
        item2=int(e_daal.get())
        item3=int(e_fish.get())
        item4=int(e_naan.get())
        item5=int(e_chicken.get())
        item6=int(e_chapathi.get())
        item7=int(e_paneer.get())
        item8=int(e_mutton.get())
        item9=int(e_cauliflower.get())
        item10=int(e_lemon_tea.get())
        item11=int(e_coffee.get())
        item12=int(e_tea.get())
        item13=int(e_faluda.get())
        item14=int(e_badam_milk.get())
        item15=int(e_rose_milk.get())
        item16=int(e_cold_drinks.get())
        item17=int(e_masala_tea.get())
        item18=int(e_mango_juice.get())
        item19=int(e_oreo.get())
        item20=int(e_apple.get())
        item21=int(e_kitkat.get())
        item22=int(e_vanilla.get())
        item23=int(e_banana.get())
        item24=int(e_brownie.get())
        item25=int(e_pineapple.get())
        item26=int(e_chocolate.get())
        item27=int(e_black_forest.get())                                                                                                                                                                                                                                                     
        priceofFood=(item1*10)+(item2*30)+(item3*70)+(item4*20)+(item5*80)+(item6*15)+(item7*40)+(item8*90)+(item9*60)
        priceofDrinks=(item10*10)+(item11*15)+(item12*20)+(item13*60)+(item14*35)+(item15*30)+(item16*25)+(item17*30)+(item18*30)
        priceofCakes=(item19*600)+(item20*200)+(item21*300)+(item22*560)+(item23*770)+(item24*620)+(item25*700)+(item26*880)+(item27*900)
        CostofFoodvar.set(str(priceofFood)+' Rs')
        CostofDrinksvar.set(str(priceofDrinks)+' Rs')
        CostofCakesvar.set(str(priceofCakes)+' Rs')
        subtotalofitems=priceofFood+priceofDrinks+priceofCakes
        subtotalvar.set(str(subtotalofitems)+' Rs')
        servicetaxvar.set('50 Rs')
        tottalcost=subtotalofitems+50
        totalcostvar.set(str(tottalcost)+'Rs')
    else:
        messagebox.showerror('Error','No Item Is Selected')
def roti():
    if var1.get()==1:
        textroti.config(state=NORMAL)
        textroti.delete(0,END)
        textroti.focus()
    else:
        textroti.config(state=DISABLED)
        e_roti.set('0')
def daal():
    if var2.get()==1:
        textdaal.config(state=NORMAL)
        textdaal.delete(0,END)
        textdaal.focus()
    else:
        textdaal.config(state=DISABLED)
        e_daal.set('0')
def fish():
    if var3.get()==1:
        textfish.config(state=NORMAL)
        textfish.delete(0,END)
        textfish.focus()
    else:
        textfish.config(state=DISABLED)
        e_fish.set('0')
def naan():
    if var4.get()==1:
        textnaan.config(state=NORMAL)
        textnaan.delete(0,END)
        textnaan.focus()
    else:
        textnaan.config(state=DISABLED)
        e_naan.set('0')
def chicken():
    if var5.get()==1:
        textchicken.config(state=NORMAL)
        textchicken.delete(0,END)
        textchicken.focus()
    else:
        textchicken.config(state=DISABLED)
        e_chicken.set('0')
def chapathi():
    if var6.get()==1:
        textchapathi.config(state=NORMAL)
        textchapathi.delete(0,END)
        textchapathi.focus()
    else:
        textchapathi.config(state=DISABLED)
        e_chapathi.set('0')
def paneer():
    if var7.get()==1:
        textpaneer.config(state=NORMAL)
        textpaneer.delete(0,END)
        textpaneer.focus()
    else:
        textpaneer.config(state=DISABLED)
        e_paneer.set('0')
def mutton():
    if var8.get()==1:
        textmutton.config(state=NORMAL)
        textmutton.delete(0,END)
        textmutton.focus()
    else:
        textmutton.config(state=DISABLED)
        e_mutton.set('0')
def cauliflower():
    if var9.get()==1:
        textcauliflower.config(state=NORMAL)
        textcauliflower.delete(0,END)
        textcauliflower.focus()
    else:
        textcauliflower.config(state=DISABLED)
        e_cauliflower.set('0')
def lemon_tea():
    if var10.get()==1:
        textlemon_tea.config(state=NORMAL)
        textlemon_tea.delete(0,END)
        textlemon_tea.focus()
    else:
        textlemon_tea.config(state=DISABLED)
        e_lemon_tea.set('0')
def coffee():
    if var11.get()==1:
        textcoffee.config(state=NORMAL)
        textcoffee.delete(0,END)
        textcoffee.focus()
    else:
        textcoffee.config(state=DISABLED)
        e_coffee.set('0')
def tea():
    if var12.get()==1:
        texttea.config(state=NORMAL)
        texttea.delete(0,END)
        texttea.focus()
    else:
        texttea.config(state=DISABLED)
        e_tea.set('0')
def faluda():
    if var13.get()==1:
        textfaluda.config(state=NORMAL)
        textfaluda.delete(0,END)
        textfaluda.focus()
    else:
        textfaluda.config(state=DISABLED)
        e_faluda.set('0')
def badam_milk():
    if var14.get()==1:
        textbadam_milk.config(state=NORMAL)
        textbadam_milk.delete(0,END)
        textbadam_milk.focus()
    else:
        textbadam_milk.config(state=DISABLED)
        e_badam_milk.set('0')
def rose_milk():
    if var15.get()==1:
        textrose_milk.config(state=NORMAL)
        textrose_milk.delete(0,END)
        textrose_milk.focus()
    else:
        textrose_milk.config(state=DISABLED)
        e_rose_milk.set('0')
def cold_drinks():
    if var16.get()==1:
        textcold_drinks.config(state=NORMAL)
        textcold_drinks.delete(0,END)
        textcold_drinks.focus()
    else:
        textcold_drinks.config(state=DISABLED)
        e_cold_drinks.set('0')
def masala_tea():
    if var17.get()==1:
        textmasala_tea.config(state=NORMAL)
        textmasala_tea.delete(0,END)
        textmasala_tea.focus()
    else:
        textmasala_tea.config(state=DISABLED)
        e_masala_tea.set('0')
def mango_juice():
    if var18.get()==1:
        textmango_juice.config(state=NORMAL)
        textmango_juice.delete(0,END)
        textmango_juice.focus()
    else:
        textmango_juice.config(state=DISABLED)
        e_mango_juice.set('0')
def oreo():
    if var19.get()==1:
        textoreo.config(state=NORMAL)
        textoreo.delete(0,END)
        textoreo.focus()
    else:
        textoreo.config(state=DISABLED)
        e_oreo.set('0')
def apple():
    if var20.get()==1:
        textapple.config(state=NORMAL)
        textapple.delete(0,END)
        textapple.focus()
    else:
        textapple.config(state=DISABLED)
        e_apple.set('0')
def kitkat():
    if var21.get()==1:
        textkitkat.config(state=NORMAL)
        textkitkat.delete(0,END)
        textkitkat.focus()
    else:
        textkitkat.config(state=DISABLED)
        e_kitkat.set('0')

def vanilla():
    if var22.get()==1:
        textvanilla.config(state=NORMAL)
        textvanilla.delete(0,END)
        textvanilla.focus()
    else:
        textvanilla.config(state=DISABLED)
        e_vanilla.set('0')
def banana():
    if var23.get()==1:
        textbanana.config(state=NORMAL)
        textbanana.delete(0,END)
        textbanana.focus()
    else:
        textbanana.config(state=DISABLED)
        e_banana.set('0')
def brownie():
    if var24.get()==1:
        textbrownie.config(state=NORMAL)
        textbrownie.delete(0,END)
        textbrownie.focus()
    else:
        textbrownie.config(state=DISABLED)
        e_brownie.set('0')
def pineapple():
    if var25.get()==1:
        textpineapple.config(state=NORMAL)
        textpineapple.delete(0,END)
        textpineapple.focus()
    else:
        textpineapple.config(state=DISABLED)
        e_pineapple.set('0')
def chocolate():
    if var26.get()==1:
        textchocolate.config(state=NORMAL)
        textchocolate.delete(0,END)
        textchocolate.focus()
    else:
        textchocolate.config(state=DISABLED)
        e_chocolate.set('0')
def black_forest():
    if var27.get()==1:
        textblack_forest.config(state=NORMAL)
        textblack_forest.delete(0,END)
        textblack_forest.focus()
    else:
        textblack_forest.config(state=DISABLED)
        e_black_forest.set('0')
root=Tk()
root.geometry('1270x690+0+0')
root.resizable(0,0)
root.title('RESTAURENT MANAGEMENT SYSTEM')
root.config(bg='firebrick')
topframe=Frame(root,bd=10,relief=RIDGE,bg='firebrick')
topframe.pack(side=TOP)
labelTitle=Label(topframe,text='RESTAURANT MANAGAEMENT SYSTEM',font=('arial',30,'bold'),fg='yellow',bg='red4',width=51)
labelTitle.grid(row=0,column=0)
menuFrame=Frame(root,bd=10,relief=RIDGE,bg='firebrick4')
menuFrame.pack(side=LEFT)
costFrame=Frame(menuFrame,bd=4,relief=RIDGE,bg='firebrick4',pady=1)
costFrame.pack(side=BOTTOM)
FoodFrame=LabelFrame(menuFrame,text='Food',font=('arial',19,'bold'),bd=10,relief=RIDGE,fg='red4')
FoodFrame.pack(side=LEFT)
DrinksFrame=LabelFrame(menuFrame,text='Drinks',font=('arial',19,'bold'),bd=10,relief=RIDGE,fg='red4')
DrinksFrame.pack(side=LEFT)
CakesFrame=LabelFrame(menuFrame,text='Cakes',font=('arial',19,'bold'),bd=10,relief=RIDGE,fg='red4')
CakesFrame.pack(side=LEFT)
rightFrame=Frame(root,bd=15,relief=RIDGE)
rightFrame.pack(side=RIGHT)
caluculatorFrame=Frame(rightFrame,bd=1,relief=RIDGE)
caluculatorFrame.pack()
receiptFrame=Frame(rightFrame,bd=4,relief=RIDGE)
receiptFrame.pack()
buttonFrame=Frame(rightFrame,bd=3,relief=RIDGE)
buttonFrame.pack()
var1=IntVar()
var2=IntVar()
var3=IntVar()
var4=IntVar()
var5=IntVar()
var6=IntVar()
var7=IntVar()
var8=IntVar()
var9=IntVar()
var10=IntVar()
var11=IntVar()
var12=IntVar()
var13=IntVar()
var14=IntVar()
var15=IntVar()
var16=IntVar()
var17=IntVar()
var18=IntVar()
var19=IntVar()
var20=IntVar()
var21=IntVar()
var22=IntVar()
var23=IntVar()
var24=IntVar()
var25=IntVar()
var26=IntVar()
var27=IntVar()
e_roti=StringVar()
e_daal=StringVar()
e_fish=StringVar()
e_naan=StringVar()
e_chicken=StringVar()
e_chapathi=StringVar()
e_paneer=StringVar()
e_mutton=StringVar()
e_cauliflower=StringVar()
e_lemon_tea=StringVar()
e_coffee=StringVar()
e_tea=StringVar()
e_faluda=StringVar()
e_badam_milk=StringVar()
e_rose_milk=StringVar()
e_cold_drinks=StringVar()
e_masala_tea=StringVar()
e_mango_juice=StringVar()
e_oreo=StringVar()
e_apple=StringVar()
e_kitkat=StringVar()
e_vanilla=StringVar()
e_banana=StringVar()
e_brownie=StringVar()
e_pineapple=StringVar()
e_chocolate=StringVar()
e_black_forest=StringVar()
CostofFoodvar=StringVar()
CostofDrinksvar=StringVar()
CostofCakesvar=StringVar()
subtotalvar=StringVar()
servicetaxvar=StringVar()
totalcostvar=StringVar()
e_roti.set('0')
e_daal.set('0')
e_fish.set('0')
e_naan.set('0')
e_chicken.set('0')
e_chapathi.set('0')
e_paneer.set('0')
e_mutton.set('0')
e_cauliflower.set('0')
e_lemon_tea.set('0')
e_coffee.set('0')
e_tea.set('0')
e_faluda.set('0')
e_badam_milk.set('0')
e_rose_milk.set('0')
e_cold_drinks.set('0')
e_masala_tea.set('0')
e_mango_juice.set('0')
e_oreo.set('0')
e_apple.set('0')
e_kitkat.set('0')
e_vanilla.set('0')
e_banana.set('0')
e_brownie.set('0')
e_pineapple.set('0')
e_chocolate.set('0')
e_black_forest.set('0')
roti=Checkbutton(FoodFrame,text='Roti',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var1,command=roti)
roti.grid(row=0,column=0,sticky=W)
daal=Checkbutton(FoodFrame,text='Daal',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var2,command=daal)
daal.grid(row=1,column=0,sticky=W)
fish=Checkbutton(FoodFrame,text='Fish',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var3,command=fish)
fish.grid(row=2,column=0,sticky=W)
naan=Checkbutton(FoodFrame,text='Naan',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var4,command=naan)
naan.grid(row=3,column=0,sticky=W)
chicken=Checkbutton(FoodFrame,text='Chicken',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var5,command=chicken)
chicken.grid(row=4,column=0,sticky=W)
chapathi=Checkbutton(FoodFrame,text='Chapathi',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var6,command=chapathi)
chapathi.grid(row=5,column=0,sticky=W)
paneer=Checkbutton(FoodFrame,text='Paneer',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var7,command=paneer)
paneer.grid(row=6,column=0,sticky=W)
mutton=Checkbutton(FoodFrame,text='Mutton',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var8,command=mutton)
mutton.grid(row=7,column=0,sticky=W)
cauliflower=Checkbutton(FoodFrame,text='Cauliflower',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var9,command=cauliflower)
cauliflower.grid(row=8,column=0,sticky=W)
textroti=Entry(FoodFrame,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_roti)
textroti.grid(row=0,column=1)
textdaal=Entry(FoodFrame,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_daal)
textdaal.grid(row=1,column=1)
textfish=Entry(FoodFrame,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_fish)
textfish.grid(row=2,column=1)
textnaan=Entry(FoodFrame,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_naan)
textnaan.grid(row=3,column=1)
textchicken=Entry(FoodFrame,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_chicken)
textchicken.grid(row=4,column=1)
textchapathi=Entry(FoodFrame,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_chapathi)
textchapathi.grid(row=5,column=1)
textpaneer=Entry(FoodFrame,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_paneer)
textpaneer.grid(row=6,column=1)
textmutton=Entry(FoodFrame,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_mutton)
textmutton.grid(row=7,column=1)
textcauliflower=Entry(FoodFrame,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_cauliflower)
textcauliflower.grid(row=8,column=1)
lemon_tea=Checkbutton(DrinksFrame,text='Lemon Tea',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var10,command=lemon_tea)
lemon_tea.grid(row=0,column=0,sticky=W)
coffee=Checkbutton(DrinksFrame,text='Coffee',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var11,command=coffee)
coffee.grid(row=1,column=0,sticky=W)
tea=Checkbutton(DrinksFrame,text='Tea',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var12,command=tea)
tea.grid(row=2,column=0,sticky=W)
faluda=Checkbutton(DrinksFrame,text='Faluda',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var13,command=faluda)
faluda.grid(row=3,column=0,sticky=W)
badam_milk=Checkbutton(DrinksFrame,text='Badam Milk',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var14,command=badam_milk)
badam_milk.grid(row=4,column=0,sticky=W)
rose_milk=Checkbutton(DrinksFrame,text='Rose Milk',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var15,command=rose_milk)
rose_milk.grid(row=5,column=0,sticky=W)
cold_drinks=Checkbutton(DrinksFrame,text='Cold Drinks',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var16,command=cold_drinks)
cold_drinks.grid(row=6,column=0,sticky=W)
masala_tea=Checkbutton(DrinksFrame,text='Masala Tea',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var17,command=masala_tea)
masala_tea.grid(row=7,column=0,sticky=W)
mango_juice=Checkbutton(DrinksFrame,text='Mango Juice',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var18,command=mango_juice)
mango_juice.grid(row=8,column=0,sticky=W)
textlemon_tea=Entry(DrinksFrame,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_lemon_tea)
textlemon_tea.grid(row=0,column=1)
textcoffee=Entry(DrinksFrame,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_coffee)
textcoffee.grid(row=1,column=1)
texttea=Entry(DrinksFrame,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_tea)
texttea.grid(row=2,column=1)
textfaluda=Entry(DrinksFrame,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_faluda)
textfaluda.grid(row=3,column=1)
textbadam_milk=Entry(DrinksFrame,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_badam_milk)
textbadam_milk.grid(row=4,column=1)
textrose_milk=Entry(DrinksFrame,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_rose_milk)
textrose_milk.grid(row=5,column=1)
textcold_drinks=Entry(DrinksFrame,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_cold_drinks)
textcold_drinks.grid(row=6,column=1)
textmasala_tea=Entry(DrinksFrame,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_masala_tea)
textmasala_tea.grid(row=7,column=1)
textmango_juice=Entry(DrinksFrame,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_mango_juice)
textmango_juice.grid(row=8,column=1)
oreo=Checkbutton(CakesFrame,text='Oreo',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var19,command=oreo)
oreo.grid(row=0,column=0,sticky=W)
apple=Checkbutton(CakesFrame,text='Apple',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var20,command=apple)
apple.grid(row=1,column=0,sticky=W)
kitkat=Checkbutton(CakesFrame,text='Kitkat',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var21,command=kitkat)
kitkat.grid(row=2,column=0,sticky=W)
vanilla=Checkbutton(CakesFrame,text='Vanilla',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var22,command=vanilla)
vanilla.grid(row=3,column=0,sticky=W)
banana=Checkbutton(CakesFrame,text='Banana',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var23,command=banana)
banana.grid(row=4,column=0,sticky=W)
brownie=Checkbutton(CakesFrame,text='Brownie',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var24,command=brownie)
brownie.grid(row=5,column=0,sticky=W)
pineapple=Checkbutton(CakesFrame,text='Pineapple',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var25,command=pineapple)
pineapple.grid(row=6,column=0,sticky=W)
chocolate=Checkbutton(CakesFrame,text='Chocolate',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var26,command=chocolate)
chocolate.grid(row=7,column=0,sticky=W)
black_forest=Checkbutton(CakesFrame,text='Black Forest',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var27,command=black_forest)
black_forest.grid(row=8,column=0,sticky=W)
textoreo=Entry(CakesFrame,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_oreo)
textoreo.grid(row=0,column=1)
textapple=Entry(CakesFrame,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_apple)
textapple.grid(row=1,column=1)
textkitkat=Entry(CakesFrame,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_kitkat)
textkitkat.grid(row=2,column=1)
textvanilla=Entry(CakesFrame,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_vanilla)
textvanilla.grid(row=3,column=1)
textbanana=Entry(CakesFrame,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_banana)
textbanana.grid(row=4,column=1)
textbrownie=Entry(CakesFrame,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_brownie)
textbrownie.grid(row=5,column=1)
textpineapple=Entry(CakesFrame,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_pineapple)
textpineapple.grid(row=6,column=1)
textchocolate=Entry(CakesFrame,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_chocolate)
textchocolate.grid(row=7,column=1)
textblack_forest=Entry(CakesFrame,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_black_forest)
textblack_forest.grid(row=8,column=1)
labelCosttoFood=Label(costFrame,text='Cost of Food',font=('arial',16,'bold'),bg='firebrick4',fg='white')
labelCosttoFood.grid(row=0,column=0)
textCostofFood=Entry(costFrame,font=('arial',16,'bold'),bd=6,width=14,state='readonly',textvariable=CostofFoodvar)
textCostofFood.grid(row=0,column=1,padx=41)
labelCosttoFood=Label(costFrame,text='Cost of Drinks',font=('arial',16,'bold'),bg='firebrick4',fg='white')
labelCosttoFood.grid(row=1,column=0)
textCostofFood=Entry(costFrame,font=('arial',16,'bold'),bd=6,width=14,state='readonly',textvariable=CostofDrinksvar)
textCostofFood.grid(row=1,column=1,padx=41)
labelCosttoFood=Label(costFrame,text='Cost of Cakes',font=('arial',16,'bold'),bg='firebrick4',fg='white')
labelCosttoFood.grid(row=2,column=0)
textCostofFood=Entry(costFrame,font=('arial',16,'bold'),bd=6,width=14,state='readonly',textvariable=CostofCakesvar)
textCostofFood.grid(row=2,column=1,padx=41)
labelCosttoFood=Label(costFrame,text='Sub Total',font=('arial',16,'bold'),bg='firebrick4',fg='white')
labelCosttoFood.grid(row=0,column=2)
textsubtotal=Entry(costFrame,font=('arial',16,'bold'),bd=6,width=14,state='readonly',textvariable=subtotalvar)
textsubtotal.grid(row=0,column=3,padx=41)
labelCosttoFood=Label(costFrame,text='Service Tax',font=('arial',16,'bold'),bg='firebrick4',fg='white')
labelCosttoFood.grid(row=1,column=2)
textservicetax=Entry(costFrame,font=('arial',16,'bold'),bd=6,width=14,state='readonly',textvariable=servicetaxvar)
textservicetax.grid(row=1,column=3,padx=41)
labelCosttoFood=Label(costFrame,text='Total Cost',font=('arial',16,'bold'),bg='firebrick4',fg='white')
labelCosttoFood.grid(row=2,column=2)
texttotalcost=Entry(costFrame,font=('arial',16,'bold'),bd=6,width=14,state='readonly',textvariable=totalcostvar)
texttotalcost.grid(row=2,column=3,padx=41)
buttonTotal=Button(buttonFrame,text='Total',font=('arial',14,'bold'),fg='white',bg='red4',command=totalcost)
buttonTotal.grid(row=0,column=0)
buttonReceipt=Button(buttonFrame,text='Receipt',font=('arial',14,'bold'),fg='white',bg='red4',command=receipt)
buttonReceipt.grid(row=0,column=1)
buttonSave=Button(buttonFrame,text='Save',font=('arial',14,'bold'),fg='white',bg='red4',command=save)
buttonSave.grid(row=0,column=2)
buttonSend=Button(buttonFrame,text='Send',font=('arial',14,'bold'),fg='white',bg='red4',command=send)
buttonSend.grid(row=0,column=3)
buttonReset=Button(buttonFrame,text='Reset',font=('arial',14,'bold'),fg='white',bg='red4',command=reset)
buttonReset.grid(row=0,column=4)
textReceipt=Text(receiptFrame,font=('arial',12,'bold'),bd=3,width=42,height=14)
textReceipt.grid(row=0,column=0)
operator=''
def buttonClick(numbers): 
    global operator
    operator=operator+numbers    
    caluculatorField.delete(0,END)
    caluculatorField.insert(END,operator)
def clear():
    global operator
    operators=''
    caluculatorField.delete(0,END)
def answer():
    global operator
    result=str(eval(operator))
    caluculatorField.delete(0,END)
    caluculatorField.insert(0,result)
    operator=''
caluculatorField=Entry(caluculatorFrame,font=('arial',16,'bold'),width=32,bd=4)
caluculatorField.grid(row=0,column=0,columnspan=4)
button7=Button(caluculatorFrame,text='7',font=('arial',16,'bold'),fg='yellow',bg='red4',bd=4,width=6,command=lambda:buttonClick('7'))
button7.grid(row=1,column=0)
button8=Button(caluculatorFrame,text='8',font=('arial',16,'bold'),fg='yellow',bg='red4',bd=4,width=6,command=lambda:buttonClick('8'))
button8.grid(row=1,column=1)
button9=Button(caluculatorFrame,text='9',font=('arial',16,'bold'),fg='yellow',bg='red4',bd=4,width=6,command=lambda:buttonClick('9'))
button9.grid(row=1,column=2)
buttonplus=Button(caluculatorFrame,text='+',font=('arial',16,'bold'),fg='yellow',bg='red4',bd=4,width=6,command=lambda:buttonClick('+'))
buttonplus.grid(row=1,column=3)
button4=Button(caluculatorFrame,text='4',font=('arial',16,'bold'),fg='yellow',bg='red4',bd=4,width=6,command=lambda:buttonClick('4'))
button4.grid(row=2,column=0)
button5=Button(caluculatorFrame,text='5',font=('arial',16,'bold'),fg='yellow',bg='red4',bd=4,width=6,command=lambda:buttonClick('5'))
button5.grid(row=2,column=1)
button6=Button(caluculatorFrame,text='6',font=('arial',16,'bold'),fg='yellow',bg='red4',bd=4,width=6,command=lambda:buttonClick('6'))
button6.grid(row=2,column=2)
buttonminus=Button(caluculatorFrame,text='-',font=('arial',16,'bold'),fg='yellow',bg='red4',bd=4,width=6,command=lambda:buttonClick('-'))
buttonminus.grid(row=2,column=3)
button1=Button(caluculatorFrame,text='1',font=('arial',16,'bold'),fg='yellow',bg='red4',bd=4,width=6,command=lambda:buttonClick('1'))
button1.grid(row=3,column=0)
button2=Button(caluculatorFrame,text='2',font=('arial',16,'bold'),fg='yellow',bg='red4',bd=4,width=6,command=lambda:buttonClick('2'))
button2.grid(row=3,column=1)
button3=Button(caluculatorFrame,text='3',font=('arial',16,'bold'),fg='yellow',bg='red4',bd=4,width=6,command=lambda:buttonClick('3'))
button3.grid(row=3,column=2)
buttonmult=Button(caluculatorFrame,text='*',font=('arial',16,'bold'),fg='yellow',bg='red4',bd=4,width=6,command=lambda:buttonClick('*'))
buttonmult.grid(row=3,column=3)
buttonans=Button(caluculatorFrame,text='Ans',font=('arial',16,'bold'),fg='yellow',bg='red4',bd=4,width=6,command=answer)
buttonans.grid(row=4,column=0)
buttonclear=Button(caluculatorFrame,text='Clear',font=('arial',16,'bold'),fg='yellow',bg='red4',bd=4,width=6,command=clear)
buttonclear.grid(row=4,column=1)
button0=Button(caluculatorFrame,text='0',font=('arial',16,'bold'),fg='yellow',bg='red4',bd=4,width=6,command=lambda:buttonClick('0'))
button0.grid(row=4,column=2)
buttondivi=Button(caluculatorFrame,text='/',font=('arial',16,'bold'),fg='yellow',bg='red4',bd=4,width=6,command=lambda:buttonClick('/'))
buttondivi.grid(row=4,column=3)
root.mainloop()