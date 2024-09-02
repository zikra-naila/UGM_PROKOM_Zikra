#Nama file: nasted_if_statement.py
jenis_kelamin = "pria"
umur = 20
if(jenis_kelamin=="pria"):
    if(umur>= 25):
        print("pria boleh menikah")
    else:
        print("pria tidak boleh menikah")
elif(jenis_kelamin=="wanita"):
    if(umur>=20):
        print("wanita boleh menikah")
    else:
        print("wanita tidak boleh menikah")
else:
   print("jenis kelamin tidak terdaftar")
