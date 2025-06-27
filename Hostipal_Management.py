patient_record=[]
def add_patient():
    patient={}
    patient['id']=input("Enter the patient ID: ")
    patient['name']=input("Enter the patient name: ")
    patient['age']=input("Entet the patient age: ")
    patient['gender']=input("Enter the patient Genter (Male/Female): ")
    patient['dob']=input("Enter the patient DOB(12 Dec)")
    print("succesfully record")
    patient_record.append(patient)


def view_patient_detail():
    if not patient_record:
        print(" No patient records found.\n")
        return
    for patient in patient_record:
        print(f"ID: {patient['id']}, Name: {patient['name']}, Age: {patient['age']}, Gender: {patient['gender']},DOB:{patient['dob']}")

def appointment_patient():
    appointment=input("Enter the Time and Date (12 dec-5pm): ")

def generate_Bill():
        for patient in patient_record:
            Fees=int(input("Enter the amount: "))
            Medical_amount=int(input("Enter the medical amount: "))
            Total =Fees+Medical_amount
            print("Total bill for the patient ",Total)
def call():
    while True:
        choose=int(input("Enter the type (1.add_patient,2.view_patient_detail,3.appointment_patient,4.generate_Bill): "))
        if choose == 1:
            add_patient()
        elif choose==2:
            view_patient_detail()
        elif choose==3:
            appointment_patient()
        elif choose==4:
            generate_Bill()
            break


call()