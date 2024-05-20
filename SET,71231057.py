#!/usr/bin/env python
# coding: utf-8

# In[1]:


# set 
contoh_set = {2,4,5,3,6}
print(contoh_set) # elemen unik dan tidak berurutan 


# In[2]:


# dict
contoh_dict = {'key1':'value1','key2':'value2'}
print(contoh_dict) (pasangan kunci:nilai)


# In[3]:


nim = {'71200120', '71200195', '71200214'}
jumlah_nim = len(nim)
print(jumlah_nim) # akan menghasilkan output 3


# In[7]:


#definisikan sebuah set kosong
plat_nomor = set()
# tambahkan plat nomor 'AB 1890 XA'
plat_nomor.add('AB 1890 XA')
# tambahkan plat nomor 'AD 6810 MT'
plat_nomor.add('AD 6810 MT')
# jumlah anggota di dalam Set
print(len(plat_nomor))
# tambahkan plat yang sama sekali lagi
plat_nomor.add('AB 1890 XA')
# tampilkan semua plat nomor
for plat in plat_nomor:
    print(plat)


# In[1]:


#operasi Union 
ganjil = {1,3,5,7,9}
genap = {2,4,6,8,10}
prima = {2,3,5,7}
print(ganjil.union(genap))


# In[2]:


#operasi intersection
ganjil = {1,3,5,7,9}
genap = {2,4,6,8,10}
prima = {2,3,5,7}
print(ganjil.intersection(prima))


# In[3]:


#operasi Difference
s1 = {1,2,3,4,5}
s2 = {3,4,5,6,7}
s3 = {8,9,10,11}
set_selisih = s1.difference(s2)
print(f'hasil selisih: {set_selisih}')


# In[4]:


#symmetric difference 
s1 = {1,2,3,4,5}
s2 = {3,4,5,6,7}
s3 = {8,9,10,11}
beda_setangkup = s1.symmetric_difference(s2)
print(f'beda setagkup : {beda_setangkup}')


# In[8]:


# Operasi add
nama ={"caca",
"wisnu",
"erika",
"jasmin",
"mutlak"}

nama.add("echa")
nama.add("wisnu")
print(nama)


# In[9]:


# tidak menerima nilai duplikasi
list_kata = [
  'pagi', 'ini', 'adalah', 'pagi', 'yang',
  'sangat', 'cerah'
]

print(list_kata)


# In[10]:


# soal nomor 2
# List ke Set
data_list = [1, 2, 3, 1, 4, 5]
print(f"Data List: {data_list}")

data_set = set(data_list)
print(f"Data Set (setelah konversi): {data_set}")

# Set ke List
data_list = list(data_set)
print(f"\nData List (setelah konversi dari Set): {data_list}")

# Tuple ke Set
data_tuple = (1, 2, 3, 1, 4, 5)
print(f"\nData Tuple: {data_tuple}")

data_set = set(data_tuple)
print(f"Data Set (setelah konversi): {data_set}")

# Set ke Tuple
data_tuple = tuple(data_set)
print(f"\nData Tuple (setelah konversi dari Set): {data_tuple}")


# In[11]:


#soal ke 1 
aplikasi_kategori = {
    "WhatsApp": ["Pesan", "Komunikasi"],
    "Instagram": ["Foto & Video", "Sosial"],
    "Spotify": ["Musik & Audio"],
    "Facebook": ["Sosial"],
    "Twitter": ["Sosial", "Berita"],
    "Snapchat": ["Foto & Video", "Sosial"],
    "Zoom": ["Bisnis", "Produktivitas"],
    "Google Maps": ["Peta", "Navigasi"],
    "TikTok": ["Foto & Video", "Hiburan"]
}

def aplikasi_di_satu_kategori(aplikasi_kategori):
    single_category_apps = []
    for app, categories in aplikasi_kategori.items():
        if len(categories) == 1:
            single_category_apps.append(app)
    return single_category_apps

def aplikasi_di_dua_kategori(aplikasi_kategori, n):
    dual_category_apps = []
    for app, categories in aplikasi_kategori.items():
        if len(categories) == n:
            dual_category_apps.append(app)
    return dual_category_apps

print("Aplikasi yang hanya muncul di satu kategori saja:")
print(aplikasi_di_satu_kategori(aplikasi_kategori))

print(f"\nAplikasi yang muncul tepat di {n} kategori sekaligus:")
print(aplikasi_di_dua_kategori(aplikasi_kategori, n))


# In[ ]:




