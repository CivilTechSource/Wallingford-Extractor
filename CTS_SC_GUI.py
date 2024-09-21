import tkinter as tk
from WS_Wallingford import Extract_SC
from WS_Wallingford import extract_strings

class MyGUI:
    def __init__(self):
        #GUI - Window Element
        self.root = tk.Tk()
        self.root.geometry("300x300")
        self.root.title("HR Wallingford Data Extractor")

        #GUI - Labels & Buttons
        self.lbl_Lat = tk.Label(self.root, text="Lat: ")
        self.entry_Lat = tk.Entry(self.root) #entry is alternative to textbox, textbox is multiline
        self.lbl_Long = tk.Label(self.root, text="Long: ")
        self.entry_Long = tk.Entry(self.root)
        #Tell the button which function to execute
        self.btn_GetData =tk.Button(self.root, text="Get Data",command=self.GetData) 
        self.lbl_Soil = tk.Label(self.root,text="Soil Type: ")
        self.lbl_M560 = tk.Label(self.root,text="M5-60: ")
        self.lbl_RatioR = tk.Label(self.root,text="Ratio 'r': ")
        self.lbl_SAAR = tk.Label(self.root,text="SAAR: ")
        self.lbl_Region = tk.Label(self.root,text="Region: ")

        #GUI - Layout Placement
        self.lbl_Lat.pack(padx=5, pady=5) 
        self.entry_Lat.pack(padx=5, pady=5)
        self.lbl_Long.pack(padx=5, pady=5)
        self.entry_Long.pack(padx=5, pady=5)
        self.btn_GetData.pack(padx=5, pady=5)
        self.lbl_Soil.pack()
        self.lbl_M560.pack()
        self.lbl_RatioR.pack()
        self.lbl_SAAR.pack()
        self.lbl_Region.pack()

        self.root.mainloop()

    def GetData(self):
        #Assign values to variables MyLat & MyLong to send into the Extract_SC function
        MyLat = self.entry_Lat.get()
        MyLong = self.entry_Long.get()
        #Call Extract_SC Function - Extract HR Wallingford Data
        HR_Results = Extract_SC(MyLat,MyLong)
        #Call Extract_String Function - Extract Data from returned String from Extract_SC Function
        soil, saar, m5_60, r_ratio, region = extract_strings(HR_Results)

        # Print the extracted values - For Terminal Checking Purposes
        #print("Soil:", soil)
        #print("Saar:", saar)
        #print("m5_60:", m5_60)
        #print("Ratio R:", r_ratio)

        #Present information back to the Labels
        self.lbl_Soil.config(text="Soil: " + str(soil))
        self.lbl_M560.config(text="M5-60: " + str(m5_60))
        self.lbl_RatioR.config(text="Ratio 'r': " + str(r_ratio))
        self.lbl_SAAR.config(text="SAAR: " + str(saar))
        self.lbl_Region.config(text="Region: " + str(region))
    
MyGUI()