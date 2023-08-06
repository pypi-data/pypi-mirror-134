#!/usr/bin/env python3

'''
MIT License

Copyright (c) 2021 Mikhail Hyde & Cole Crescas

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
'''

'''
import tkinter as tk
import qrcode
import boto3
from botocore.exceptions import NoCredentialsError
import pandas as pd
import os


class QR_Code ():
    def __init__(self):   
    
        # AWS S3 Access Key - Points to the appropriate bucket
        self.ACCESS_KEY = os.environ['AWS_ACCESS_KEY']
        # AWS S3 Secret Key - S3 Bucket Password
        self.SECRET_KEY = os.environ['AWS_SECRET_KEY']
        # AWS S3 Bucket Name
        self.bucket = os.environ['BUCKET']
        self.s3 = boto3.client('s3', aws_access_key_id=self.ACCESS_KEY, 
                               aws_secret_access_key=self.SECRET_KEY)
        self.s3.download_file(self.bucket, 'SKU_LOOKUP.csv', '/home/hal/HALsn/HALsn/sample_data/SKU_ID_LOCAL.csv')
        self.s3.download_file(self.bucket, 'TEST_TYPE_LOOKUP.csv', '/home/hal/HALsn/HALsn/sample_data/TEST_TYPE_LOCAL.csv')
        self.s3.download_file(self.bucket, 'QR_CODE_HASH.csv', '/home/hal/HALsn/HALsn/sample_data/QRCODE_HASH_LOCAL.csv')
        s3 = boto3.client('s3', aws_access_key_id=self.ACCESS_KEY, 
                               aws_secret_access_key=self.SECRET_KEY)
        bucket = os.environ['BUCKET']
        def SKU_name():
            sku = str(var_SKU.get())
            for i in range(len(sku_local)):
                if(sku == sku_names[i]):
                    sku_ind = sku_index[i]
            SKU_number(str(sku_ind))
        
        def SKU_number(unit):
            var_SKUnum.set('')
            skunum_label = tk.Label(root, text = "SKU Number")
            skunum_label.grid(column = 1, row = 0)        
            dropdown_SKUnum = tk.OptionMenu(root, var_SKUnum, *SKU_num[unit])
            dropdown_SKUnum.grid(column = 1, row = 1)
            
            skunum_label = tk.Label(root, text = "Month")
            skunum_label.grid(column = 2, row = 0)
            dropdown_month = tk.OptionMenu(root, var_month, *month)
            dropdown_month.grid(column = 2, row = 1)
            
            skunum_label = tk.Label(root, text = "Test Type")
            skunum_label.grid(column = 3, row = 0)
            dropdown_test = tk.OptionMenu(root, var_test, *test_type)
            dropdown_test.grid(column = 3, row = 1)
            
            descript = tk.Label(root, text = "Description", width = 10)
            descript.grid(column =4, row = 0)
            des = tk.Entry(root, textvariable = var_description)
            des.grid(column = 4, row = 1)
            
            button_test = tk.Button(root, text="QR-CODE", command=lambda: qr(unit))
            button_test.grid(column=2, row =2)
         
        def qr(sku_ind):
            
            sku_ind = str(sku_ind)
            skunum = str(var_SKUnum.get())
            testmonth = str(var_month.get())
            testtype = str(var_test.get())
            qr_data = sku_ind + skunum + testmonth + testtype
            filter_list = []
            for i in range(len(hash_qr)):
                if str(hash_qr['QR_CODE_HASH'][i]).find(qr_data) != -1:
                    filter_list.append(hash_qr['QR_CODE_HASH'][i])
            filtered_df = pd.DataFrame(filter_list, columns = ["QR_CODE_HASH"])
                      
            
            if(len(filter_list) == 0):
            #Looks through filtered df and selects next value
                new_num = '00001'
            else: 
                hash_index = (filtered_df["QR_CODE_HASH"].astype(str).str[-5:]).sort_values(ascending=True)
                new_num = str(hash_index.astype(int).max() + 1).zfill(5)
                
            qr_data = qr_data + new_num
            print("Is this the correct hash key?", qr_data)
            #Check that new hash was created correctly:?
            new_desc = str(var_description.get())
           
            
            added_df = pd.DataFrame(data = [[qr_data, new_desc]], columns=["QR_CODE_HASH", "Human Readable Desc"])
            df = hash_qr.append(added_df, ignore_index=True)
            print(df)
            df.to_csv('/home/hal/HALsn/HALsn/sample_data/QRCODE_HASH_LOCAL.csv')
            upload_to_s3('QR_CODE_HASH.csv', '/home/hal/HALsn/HALsn/sample_data/QRCODE_HASH_LOCAL.csv')
            
            qr_generation(qr_data, new_desc)
        
        def upload_to_s3(file_name, local_file):
            
            try:
                s3.upload_file(local_file, bucket, file_name)
                print("Upload Successful")
                return True
            except FileNotFoundError:
                print("The file was not found")
                return False
            except NoCredentialsError:
                print("Credentials not available")
                return False

      

        #Uploads a single file to the AWS s3 bucket.
        
        def qr_generation(data,desc):
            if(len(data)>2):
                #Creating an instance of qrcode
                physical_code = data + desc
                #print(physical_code)
                qr = qrcode.QRCode(version=1, box_size=10, border=5)
                qr.add_data(physical_code)
                qr.make(fit=True)
                img = qr.make_image(fill='black', back_color='white')
                qr_save_path = '/home/hal/QR_CODES/'
                qr_save = qr_save_path + str(data) + '.png'
            img.save(qr_save)
            #print(qr)
      
        sku_local = pd.read_csv('/home/hal/HALsn/HALsn/sample_data/SKU_ID_LOCAL.csv')
        test_local = pd.read_csv('/home/hal/HALsn/HALsn/sample_data/TEST_TYPE_LOCAL.csv')
        hash_qr = pd.read_csv('/home/hal/HALsn/HALsn/sample_data/QRCODE_HASH_LOCAL.csv', index_col = False)
        
        sku_names = list(sku_local['SKU'])
        sku_index = list(sku_local['ID'])
        test_types = list(test_local['ID'])
        
        root = tk.Tk()
        root.geometry("%dx%d+%d+%d" % (330, 80, 200, 150))
        root.title("tk.Optionmenu as combobox")
        
        var_SKU = tk.StringVar(root)
        var_SKUnum = tk.StringVar(root)
        var_month = tk.StringVar(root)
        var_test = tk.StringVar(root)
        var_description = tk.StringVar(root)
        
        SKU = sku_names  
        SKU_num = {"1": [300,301,350, 351, 999], 
                   "2": [300,301,350,351],
                   "3": [600],
                   "4": [200],
                   "5": [102,302,402],
                   "6": [550, 250],
                   "7": [501,550,610,650,701,750], 
                   "8": [400,401]}
        month = ['01','02','03','04','05','06','07','08','09','10','11','12']
        for i in range(len(test_types)):
            if(len(str(test_types[i])) == 1):
                test_types[i] = '0' + str(test_types[i])
        test_type = test_types
        
        
        sku_label = tk.Label(root, text = "SKU", width = 5)
        sku_label.grid(column = 0, row = 0)
        
        option = tk.OptionMenu(root, var_SKU, *SKU)
        option.grid(column = 0, row =1)
        
        button_SKU = tk.Button(root, text="Enter SKU Number", command=lambda: SKU_name())
        button_SKU.grid(column=0, row =2)
        
        root.mainloop()

win = QR_Code()

win.qr_generation()
'''