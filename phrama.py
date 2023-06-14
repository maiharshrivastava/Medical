from tkinter import *
from PIL import Image,ImageTk
from tkinter import ttk
import mysql.connector
from tkinter import messagebox


class PharmacyManagementSystem:
    def __init__(self,root):
        self.root=root
        self.root.title("Pharamcy Mangement System")
        self.root.geometry("1550x800+0+0")

        lbltitle=Label(self.root,text="PHARAMACY MANAGMENT SYSTEM",bd=15,relief=RIDGE
                            ,bg='white',fg="darkgreen",font=("times new roman",50,"bold"),padx=2,pady=4)

        lbltitle.pack(side=TOP,fill=X)
        

        self.addmed_var=StringVar()
        self.refMed_var=StringVar()
        #=====================================DataFrame==========================
        DataFrame=Frame(self.root,bd=15,relief=RIDGE,padx=20)
        DataFrame.place(x=0,y=120,width=1530,height=400)

        DataFrameLeft=LabelFrame(DataFrame,bd=10,relief=RIDGE,padx=20,text="Medicine Information",
                                 fg="darkgreen",font=("arial",12,"bold"))
        DataFrameLeft.place(x=0,y=5,width=900,height=350)

        DataFrameRight=LabelFrame(DataFrame,bd=10,relief=RIDGE,padx=20,text="Medicine Add Department",
                                 fg="darkgreen",font=("arial",12,"bold"))
        DataFrameRight.place(x=910,y=5,width=540,height=350)

        #====================================buttonsFrame=======================================

        ButtonFrame=Frame(self.root,bd=15,relief=RIDGE,padx=20)
        ButtonFrame.place(x=0,y=520,width=1530,height=65)

        #======================================MainButton================================================
        btnAddData=Button(ButtonFrame,text="Medicine Add",font=("arial",12,"bold"),bg="darkgreen",fg="white")
        btnAddData.grid(row=0,column=0)

        btnUpdateData=Button(ButtonFrame,text="UPDATE",font=("arial",12,"bold"),bg="darkgreen",fg="white")
        btnUpdateData.grid(row=0,column=1)

        btnDeleteData=Button(ButtonFrame,text="DELETE",font=("arial",12,"bold"),bg="red",fg="white")
        btnDeleteData.grid(row=0,column=2)

        btnResetData=Button(ButtonFrame,text="RESET",font=("arial",12,"bold"),bg="darkgreen",fg="white")
        btnResetData.grid(row=0,column=3)

        btnExitData=Button(ButtonFrame,text="EXIT",font=("arial",12,"bold"),bg="darkgreen",fg="white")
        btnExitData.grid(row=0,column=4)

        # ===========================Search By=====================
        lblSearch=Label(ButtonFrame,font=("arial",17,"bold"),text="Search By", padx=2,bg="red",fg="white")
        lblSearch.grid(row=0,column=5,sticky=W)

        serch_combo=ttk.Combobox(ButtonFrame,width=12,font=("arial",12,"bold"),state="read")
        serch_combo["values"]=("Ref","Medname","Lot")
        serch_combo.grid(row=0,column=6)
        serch_combo.current(0)
        
        txtSerch=Entry(ButtonFrame,bd=3,relief=RIDGE,width=12,font=("arial",17,"bold"))
        txtSerch.grid(row=0,column=7)

        searchBtn=Button(ButtonFrame,text="SEARCH",font=("arial",13,"bold"),width=13,bg="darkgreen",fg="white")
        searchBtn.grid(row=0,column=8)
         
        showAll=Button(ButtonFrame,text="SHOWALL",font=("arial",13,"bold"),width=13,bg="darkgreen",fg="white")
        showAll.grid(row=0,column=9)
        #==============================label and entry ================================

        lblRef_no=Label(DataFrameLeft,font=("arial",12,"bold"),text="Reference No.:", padx=2)
        lblRef_no.grid(row=1,column=0,sticky=W)

        comboRef_no=ttk.Combobox(DataFrameLeft,width=27,font=("arial",12,"bold"),state="read")
        comboRef_no["values"]=("Ref","Medname","Lot")
        comboRef_no.grid(row=1,column=1)
        comboRef_no.current()
        
        lblCompanyName=Label(DataFrameLeft,font=("arial",12,"bold"),text="Company Name",padx=2,pady=6)
        lblCompanyName.grid(row=2,column=0,sticky=W)
        textCompanyName=Entry(DataFrameLeft,font=("arial",13,"bold"),bg="white",relief=RIDGE,width=29)
        textCompanyName.grid(row=2,column=1)


        
        #===========================================    typeofMedicine===================
        
        lblTypeofMedicine=Label(DataFrameLeft,font=("arial",12,"bold"),text="Type Of Medicine", padx=2)
        lblTypeofMedicine.grid(row=3,column=0,sticky=W)

        comTypeofMedicine=ttk.Combobox(DataFrameLeft,state="readonly",width=27,font=("arial",12,"bold"))
        
        comTypeofMedicine['value']=("Tablet","Liqiud","Calsules","Topical Medicines","Drops","Inhales","Injection")
        comTypeofMedicine.current(0)
        comTypeofMedicine.grid(row=3,column=1)

        #=============================AddMedicine==============    
        lblMedicineName=Label(DataFrameLeft,font=("arial",12,"bold"),text="Medicine Name", padx=2)
        lblMedicineName.grid(row=4,column=0,sticky=W)

        comMedicineName=ttk.Combobox(DataFrameLeft,state="readonly",width=27,font=("arial",12,"bold"))

        comMedicineName["values"]=("Nice","Noval")
        comMedicineName.current(0)
        comMedicineName.grid(row=4,column=1)
       
        lblLotNo=Label(DataFrameLeft,font=("arial",12,"bold"),text="Lot No:",padx=2,pady=6)
        lblLotNo.grid(row=5,column=0,sticky=W)
        textLotNo=Entry(DataFrameLeft,font=("arial",13,"bold"),bg="white",relief=RIDGE,width=29)
        textLotNo.grid(row=5,column=1)

        lblIssueDate=Label(DataFrameLeft,font=("arial",12,"bold"),text="Issue Date:",padx=2,pady=6)
        lblIssueDate.grid(row=6,column=0,sticky=W)
        textIssueDate=Entry(DataFrameLeft,font=("arial",13,"bold"),bg="white",relief=RIDGE,width=29)
        textIssueDate.grid(row=6,column=1)
        
        lblExDate=Label(DataFrameLeft,font=("arial",12,"bold"),text="Exp Date:",padx=2,pady=6)
        lblExDate.grid(row=7,column=0,sticky=W)
        textExDate=Entry(DataFrameLeft,font=("arial",13,"bold"),bg="white",relief=RIDGE,width=29)
        textExDate.grid(row=7,column=1)
     
        
        lblUses=Label(DataFrameLeft,font=("arial",12,"bold"),text="Uses:",padx=2,pady=6)
        lblUses.grid(row=8,column=0,sticky=W)
        textUses=Entry(DataFrameLeft,font=("arial",13,"bold"),bg="white",relief=RIDGE,width=29)
        textUses.grid(row=8,column=1)

        
        lblSideEffect=Label(DataFrameLeft,font=("arial",12,"bold"),text="Side Effect:",padx=2,pady=6)
        lblSideEffect.grid(row=9,column=0,sticky=W)
        textSideEffect=Entry(DataFrameLeft,font=("arial",13,"bold"),bg="white",relief=RIDGE,width=29)
        textSideEffect.grid(row=9,column=1)

        lblPrecWarning=Label(DataFrameLeft,font=("arial",12,"bold"),text="Prec&Warning:",padx=2,pady=6)
        lblPrecWarning.grid(row=1,column=2,sticky=W)
        textPrecWarning=Entry(DataFrameLeft,font=("arial",13,"bold"),bg="white",relief=RIDGE,width=29)
        textPrecWarning.grid(row=1,column=5)

        
        lblDosage=Label(DataFrameLeft,font=("arial",12,"bold"),text="Dosage:",padx=2,pady=6)
        lblDosage.grid(row=2,column=2,sticky=W)
        textDosage=Entry(DataFrameLeft,font=("arial",13,"bold"),bg="white",relief=RIDGE,width=29)
        textDosage.grid(row=2,column=5)
          
        lblPrice=Label(DataFrameLeft,font=("arial",12,"bold"),text="Price:",padx=2,pady=6)
        lblPrice.grid(row=3,column=2,sticky=W)
        textPrice=Entry(DataFrameLeft,font=("arial",13,"bold"),bg="white",relief=RIDGE,width=29)
        textPrice.grid(row=3,column=5)
        

        lblProductQt=Label(DataFrameLeft,font=("arial",12,"bold"),text="ProductQt:",padx=2,pady=6)
        lblProductQt.grid(row=4,column=2,sticky=W)
        textProductQt=Entry(DataFrameLeft,font=("arial",13,"bold"),bg="white",relief=RIDGE,width=29)
        textProductQt.grid(row=4,column=5)

        lblrefno=Label(DataFrameRight,font=("arial",12,"bold"),text="Refrence No:")
        lblrefno.place(x=0,y=25)
        textrefno=Entry(DataFrameRight,textvariable=self.refMed_var,font=("arial",13,"bold"),bg="white",relief=RIDGE,width=14)
        textrefno.place(x=135,y=25)

        
        lblmedName=Label(DataFrameRight,font=("arial",12,"bold"),text="Medicine Name:")
        lblmedName.place(x=0,y=53)
        txtmedName=Entry(DataFrameRight,textvariable=self.addmed_var,font=("arial",13,"bold"),bg="white",relief=RIDGE,width=14)
        txtmedName.place(x=135,y=53)


        #===================side Frame===========================
        side_frame=Frame(DataFrameRight,bd=4,relief=RIDGE,bg="white")
        side_frame.place(x=0,y=100,width=300,height=210)

        sc_x=ttk.Scrollbar(side_frame,orient=HORIZONTAL)
        sc_x.pack(side=BOTTOM,fill=X)
        sc_y=ttk.Scrollbar(side_frame,orient=VERTICAL)
        sc_y.pack(side=RIGHT,fil=Y)

        self.medicine_table=ttk.Treeview(side_frame,column=("ref","medname"),xscrollcommand=sc_x.set,yscrollcommand=sc_y.set)

        
        sc_x.config(command=self.medicine_table.xview)
        sc_y.config(command=self.medicine_table.yview)

        self.medicine_table.heading("ref",text="Ref")
        self.medicine_table.heading("medname",text="Medicine Name")

        
        self.medicine_table["show"]="headings"
        self.medicine_table.pack(fill=BOTH,expand=1)

        self.medicine_table.column("ref",width=100)
        self.medicine_table.column("medname",width=100)


        #========================================Medicine Add Button =========================

        down_frame=Frame(DataFrameRight,bd=4,relief=RIDGE,bg="darkgreen")
        down_frame.place(x=330,y=150,width=135,height=160)

        btnAddmed=Button(down_frame,text="ADD",font=("arial",12,"bold"),width=12,bg="lime",fg="white",pady=4)
        btnAddmed.grid(row=0,column=0)

        
        btnUpdatemed=Button(down_frame,text="UPDATE",font=("arial",12,"bold"),width=12,bg="purple",fg="white",pady=4)
        btnUpdatemed.grid(row=1,column=0)
        
        
        btnDeletemed=Button(down_frame,text="DELETE",font=("arial",12,"bold"),width=12,bg="red",fg="white",pady=4)
        btnDeletemed.grid(row=2,column=0)

        
        btnClearmed=Button(down_frame,text="CLEAR",font=("arial",12,"bold"),width=12,bg="orange",fg="white",pady=4)
        btnClearmed.grid(row=3,column=0)
        

        #=================================Frame Details===================
        Framedetails=Frame(self.root,bd=15,relief=RIDGE)
        Framedetails.place(x=0,y=580,width=1530,height=210)
        
        #=================================Main Table AND srollbar===================
        
        Table_Frame=Frame(Framedetails,bd=15,relief=RIDGE,padx=20)
        Table_Frame.place(x=0,y=1,width=1500,height=180)

        scroll_x=ttk.Scrollbar(Table_Frame,orient=HORIZONTAL)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y=ttk.Scrollbar(Table_Frame,orient=VERTICAL)
        scroll_y.pack(side=RIGHT,fil=Y)

        self.pharmacy_table=ttk.Treeview(Table_Frame,column=("reg","companyname","type","tabletname","lotno","issuedate",
                                                             "expdate","uses","sideEffect","warning","dosage","price","productqt"),
                                                             xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.pharmacy_table.xview)
        scroll_y.config(command=self.pharmacy_table.yview)

        self.pharmacy_table["show"] = "headings"

        self.pharmacy_table.heading("reg",text="Reference No")
        self.pharmacy_table.heading("companyname",text="Company Name")
        self.pharmacy_table.heading("type",text="Type of medicine")
        self.pharmacy_table.heading("tabletname",text="Tablet Name")
        self.pharmacy_table.heading("lotno",text="Lot No")
        self.pharmacy_table.heading("issuedate",text="Issue Date")
        self.pharmacy_table.heading("expdate",text="Exp Date")
        self.pharmacy_table.heading("uses",text="Uses")
        self.pharmacy_table.heading("sideEffect",text="Side Effect")
        self.pharmacy_table.heading("warning",text="Prec&Warning")
        self.pharmacy_table.heading("dosage",text="Dosage")
        self.pharmacy_table.heading("price",text="Price")
        self.pharmacy_table.heading("productqt",text="Product")
        self.pharmacy_table.pack(fill=BOTH,expand=1)

        self.pharmacy_table.column("reg",width=100)
        self.pharmacy_table.column("companyname",width=100)
        self.pharmacy_table.column("type",width=100)
        self.pharmacy_table.column("tabletname",width=100)
        self.pharmacy_table.column("lotno",width=100)
        self.pharmacy_table.column("issuedate",width=100)
        self.pharmacy_table.column("expdate",width=100)
        self.pharmacy_table.column("uses",width=100)
        self.pharmacy_table.column("sideEffect",width=100)
        self.pharmacy_table.column("warning",width=100)
        self.pharmacy_table.column("dosage",width=100)
        self.pharmacy_table.column("price",width=100)
        self.pharmacy_table.column("productqt",width = 100)
           
        
    def Addmed(self):
        conn=mysql.connector.connect(host="localhost",user="root",password="********",database="mydata")
        my_cursor=conn.cursor()
        my_cursor.execute("insert into pharma(Ref,MedName) values(%s,%s)",(
                                                     
                                                                 self.refMed_var.get(),
                                                                 self.addmed_var.get(),       

                                      ))
        
        conn.commit()
        conn.close()  
        messagebox.showinfo("success","Medicine Added")

if __name__ == "__main__":
    root=Tk()
    obj=PharmacyManagementSystem(root)
    root.mainloop()
