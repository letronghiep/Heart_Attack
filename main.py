import pandas as pd
import numpy as np
import ForwardChaning as fw
import tkinter as tk
from tkinter import  messagebox
# Lấy dữ liệu training
data = pd.read_csv('heart.csv')
diagnosis_system = fw.RuleBasedDiagnosisSystem()
for index, row in data.iterrows():
    conditions = {
        'age': row['age'],
        'sex': row['sex'],
        'cp': row['cp'],
        'trtbps': row['trtbps'],
        'chol': row['chol'],
        'fbs': row['fbs'],
        'restecg': row['restecg'],
        'thalachh': row['thalachh'],
        'exng': row['exng'],
        'oldpeak': row['oldpeak'],


    }
    diagnosis = row['output']
    new_rule = fw.Rule(conditions, diagnosis)
    diagnosis_system.add_rule(new_rule)
def diagnose_patient():
    patient_info = {
        'age': int(entry_age.get()),
        'sex': entry_sex.get(),
        'cp': entry_cp.get(),
        'trtbps': int(entry_trtbps.get()),
        'chol': int(entry_chol.get()),
        'fbs': int(entry_fbs.get()),
        'restecg': entry_restecg.get(),
        'thalachh': int(entry_thalachh.get()),
        'exng': entry_exng.get(),
        'oldpeak': float(entry_oldpeak.get()),
    }
    diagnosis = diagnosis_system.diagnose(patient_info)
    mess = ""
    if(diagnosis == 1):
        mess = "Bệnh nhân có nguy cơ mắc bệnh tim cao"
    else:
        mess = "Bệnh nhân có nguy cơ thấp mắc bệnh tim"
    messagebox.showinfo("Kết quả chẩn đoán", mess)
# def print_hi():
#     main()
    # Use a breakpoint in the code line below to debug your script.
    # print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
def on_entry_click(event):
    if entry_fbs.get() == '1: true, 0: false':
       entry_fbs.delete(0, "end") # Xóa văn bản mô tả khi người dùng bắt đầu nhập liệu
       entry_fbs.config(fg='black') # Thay đổi màu văn bản sang màu đen

def on_focusout(event):
    if entry_fbs.get() == '':
        entry_fbs.insert(0, '1: true, 0: false') # Thêm văn bản mô tả khi ô nhập liệu trống
        entry_fbs.config(fg='grey')
root = tk.Tk()
root.title = "Chẩn đoán bệnh tim"
# root.geometry('400x400')
# root.winfo_height()
tk.Label(root, text="Tuổi: ", justify='left').grid(row=0, column=0)
entry_age = tk.Entry(root, width=40)
entry_age.grid(row=0, column=1)

tk.Label(root, text="Giới tính: ").grid(row=1, column=0)
entry_sex = tk.Entry(root, width=40)
entry_sex.grid(row=1, column=1)

tk.Label(root, text="Loại đau ngực: ", justify='left').grid(row=2, column=0)
entry_cp = tk.Entry(root, width=40)
entry_cp.grid(row=2, column=1)

tk.Label(root, text="Huyết áp lúc nghỉ: ").grid(row=3, column=0)
entry_trtbps = tk.Entry(root, width=40)
entry_trtbps.grid(row=3, column=1)

tk.Label(root, text="Cholesterol(mg/dl): ").grid(row=4, column=0)
entry_chol = tk.Entry(root, width=40)
entry_chol.grid(row=4, column=1)

tk.Label(root, text="Lượng đường trong máu(>120mg/dl): ").grid(row=5, column=0)
entry_fbs = tk.Entry(root, width=40)
entry_fbs.grid(row=5, column=1)
entry_fbs.insert(0, "1: true, 0: false")
entry_fbs.bind('<FocusIn>', on_entry_click) # Sự kiện khi ô nhập liệu được nhấp chuột
entry_fbs.bind('<FocusOut>', on_focusout)


tk.Label(root, text="KQ điện tâm đồ: ").grid(row=6, column=0)
entry_restecg = tk.Entry(root, width=40)
entry_restecg.grid(row=6, column=1)

tk.Label(root, text="Nhịp tim tối đa đạt được: ").grid(row=7, column=0)
entry_thalachh = tk.Entry(root, width=40)
entry_thalachh.grid(row=7, column=1)

tk.Label(root, text="Đau thắt ngực do tập thể dục: ").grid(row=8, column=0)
entry_exng = tk.Entry(root, width=40)
entry_exng.grid(row=8, column=1)


tk.Label(root, text="Chênh lệch đoạn ST: ").grid(row=9, column=0)
entry_oldpeak = tk.Entry(root, width=40)
entry_oldpeak.grid(row=9, column=1)
# Button để chẩn đoán
diagnose_button = tk.Button(root, text="Chẩn đoán", command=diagnose_patient)
diagnose_button.grid(row=10, columnspan=2)
root.mainloop()
# Press the green button in the gutter to run the script.
# if __name__ == '__main__':
    # main()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
