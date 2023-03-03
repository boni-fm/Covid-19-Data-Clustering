"""
PROGRAM CLUSTERING DATA COVID PER KELURAHAN JAKARTA

Sumber data : https://riwayat-file-covid-19-dki-jakarta-jakartagis.hub.arcgis.com/

Note : Harus mengganti alamat file csv dan image agar dapat menjalankan program
"""

'''
Block code dibawah mengimpor libary yang dibutuhkan dalam program ini
library untuk plot : matplotlib, matplotlib.backends.backend_tkagg, matplotlib.pyplot
library untuk data : pandas
library untuk GUI : tkinter, PIL
library untuk clustering : sklearn.cluster
'''
#IMPORT LIBRARY
import matplotlib
matplotlib.use("TkAgg")
import tkinter as tk
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from PIL import Image,ImageTk



'''
Pertama program akan membaca data dari csv laporan covid-19 tanggal 17 juni 2021 dengan read_cv()
lalu data csv tersebut dimasukan ke dalam dataframe df. Program dapat membaca data selain tanggal
17 Juni 2021, contohnya data tanggal 20 Juni 2021

Lalu data dicluster dengan algoritma K-Means Clustering. Data dicluster dengan Kmeans().fit()
dari library sklearn.cluster. lalu data centroids dari hasil clustering tersebut disimpan dalam
variable Centroids. Dan data pembagian clusternya dimasukan kedalam clustering_index. Dalam 
clustering_index, index dari clustering_index merupakan index dari kelurahan jakarta

contoh : 
    clustering_index[2] = 0 sama dengan kelurahan pada index ke-2 termasuk dalam cluster 0
'''
#MEMBACA DATA CSV
df = pd.read_csv('/Not Data/Python/covid19_clustering/Standar_Kelurahan_Data_Corona_17_Juni_2021.csv')

#CLUSTERING DATA DENGAN LIBRARY K-MEANS
kmeans = KMeans(n_clusters=3).fit(df[['POSITIF', 'Sembuh', 'Meninggal']])
centroids = kmeans.cluster_centers_
clustering_index = kmeans.fit_predict(df[['POSITIF', 'Sembuh', 'Meninggal']])



'''
Lalu program menyimpan data cluster kedalam kolom baru bernama 'Cluster' pada df
dengan looping. Dalam looping tersebut juga dibagi cluster A, cluster B, dan cluster C.
'''

#MENYIMPAN DATA CLUSTER
pd.options.mode.chained_assignment = None #sintaks untuk mencegah error

df['Cluster'] = " "

clusterA = []
clusterB = []
clusterC = []

for i in range (0, len(df)):
    df['Cluster'][i] = clustering_index[i]
    
    if clustering_index[i] == 0:
        clusterA.append(i)
    elif clustering_index[i] == 1:
        clusterB.append(i)
    elif clustering_index[i] == 2 :
        clusterC.append(i)



'''
Menyatukan data menjadi data perkota. Data yang disatukan adalah data POSITIF, Sembuh,
Meninggal, dirawat, isolasi_mandiri. Data yang sudah disatukan menjadi perkota dimasukan
kedalam array.
'''

#MENGISI DATA COVID PER KOTA
positif_jakTim = 0
positif_jakBar = 0
positif_jakUt = 0
positif_jakSel = 0
positif_jakPus = 0
positif_kepSer = 0

sembuh_jakTim = 0
sembuh_jakBar = 0
sembuh_jakUt = 0
sembuh_jakSel = 0
sembuh_jakPus = 0
sembuh_kepSer = 0

meninggal_jakTim = 0
meninggal_jakBar = 0
meninggal_jakUt = 0
meninggal_jakSel = 0
meninggal_jakPus = 0
meninggal_kepSer = 0

dirawat_jakTim = 0
dirawat_jakBar = 0
dirawat_jakUt = 0
dirawat_jakSel = 0
dirawat_jakPus = 0
dirawat_kepSer = 0

mandiri_jakTim = 0
mandiri_jakBar = 0
mandiri_jakUt = 0
mandiri_jakSel = 0
mandiri_jakPus = 0
mandiri_kepSer = 0

#Looping menjumlahkan data untuk mendapatkan total ditiap kota
for i in range (0, len(df)):
    if df['nama_kota'][i] == ('JAKARTA TIMUR'):
        positif_jakTim += df.iloc[i]['POSITIF']
        sembuh_jakTim += df.iloc[i]['Sembuh']
        meninggal_jakTim += df.iloc[i]['Meninggal']
        dirawat_jakTim += df.iloc[i]['Dirawat']
        mandiri_jakTim += df.iloc[i]['Self Isolation']
        
    elif df['nama_kota'][i] == ('JAKARTA BARAT'):
        positif_jakBar += df.iloc[i]['POSITIF']
        sembuh_jakBar += df.iloc[i]['Sembuh']
        meninggal_jakBar += df.iloc[i]['Meninggal']
        dirawat_jakBar += df.iloc[i]['Dirawat']
        mandiri_jakBar += df.iloc[i]['Self Isolation']
        
    elif df['nama_kota'][i] == ('JAKARTA UTARA'):
        positif_jakUt += df.iloc[i]['POSITIF']
        sembuh_jakUt += df.iloc[i]['Sembuh']
        meninggal_jakUt += df.iloc[i]['Meninggal']
        dirawat_jakUt += df.iloc[i]['Dirawat']
        mandiri_jakUt += df.iloc[i]['Self Isolation']
        
    elif df['nama_kota'][i] == ('JAKARTA SELATAN'):
        positif_jakSel += df.iloc[i]['POSITIF']
        sembuh_jakSel += df.iloc[i]['Sembuh']
        meninggal_jakSel += df.iloc[i]['Meninggal']
        dirawat_jakSel += df.iloc[i]['Dirawat']
        mandiri_jakSel += df.iloc[i]['Self Isolation']
        
    elif df['nama_kota'][i] == ('JAKARTA PUSAT'):
        positif_jakPus += df.iloc[i]['POSITIF']
        sembuh_jakPus += df.iloc[i]['Sembuh']
        meninggal_jakPus += df.iloc[i]['Meninggal']
        dirawat_jakPus += df.iloc[i]['Dirawat']
        mandiri_jakPus += df.iloc[i]['Self Isolation']
        
    elif df['nama_kota'][i] == ('KAB.ADM.KEP.SERIBU'):
        positif_kepSer += df.iloc[i]['POSITIF']
        sembuh_kepSer += df.iloc[i]['Sembuh']
        meninggal_kepSer += df.iloc[i]['Meninggal']
        dirawat_kepSer += df.iloc[i]['Dirawat']
        mandiri_kepSer += df.iloc[i]['Self Isolation']

#memasukan data tiap kota kedalam array
arr_positif = [positif_jakUt, positif_jakSel, positif_jakPus, positif_jakBar, positif_jakTim, positif_kepSer]
arr_sembuh = [sembuh_jakUt, sembuh_jakSel, sembuh_jakPus, sembuh_jakBar, sembuh_jakTim, sembuh_kepSer]
arr_meninggal = [meninggal_jakUt, meninggal_jakSel, meninggal_jakPus, meninggal_jakBar, 
                 meninggal_jakTim, meninggal_kepSer]
arr_dirawat = [dirawat_jakUt, dirawat_jakSel, dirawat_jakPus, dirawat_jakBar, dirawat_jakTim, dirawat_kepSer]
arr_mandiri = [mandiri_jakUt, mandiri_jakSel, mandiri_jakPus, mandiri_jakBar, mandiri_jakTim, mandiri_kepSer]
arr_namaKota = ['Jakarta Utara', 'Jakarta Selatan', 'Jakarta Pusat', 'Jakarta Barat', 'Jakarta Timur', 'Kep.Seribu']



'''
Sintaks dibawah berfungsi untuk membuat frame GUI
'''
#DISPLAY GUI
class displayGui(tk.Tk):
    #
    def __init__(self, *args, **kwargs):
        #inisialisasi kelas turunan
        tk.Tk.__init__(self, *args, **kwargs)

        #Memberi nama frame 'Data Covid-19 Jakarta'
        tk.Tk.wm_title(self,"Data Covid-19 Jakarta")
        
        #Membuat container yang nanti akan diisi dengan frame-frame berbeda
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        
        self.frames = { }
        
        #Looping untuk memasukan frame StartPage, graphCluster, graphTotal, graphAktif kedalam container
        for F in (StartPage, graphCluster, graphTotal, graphAktif):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        #Menampilkan frame StartPage
        self.show_frame(StartPage)
    
    #Untuk menampilkan frame cont. cont merupakan frame yang dimasukan sebagai argumen nanti
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()
        
        
        
'''
Sintaks dibawah membuat GUI Home
'''
#GUI HOME/AWAL
class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        
        #Memasukan gambar head.jpg kedalam label untuk ditampilkan dalam GUI
        image=Image.open("/Not Data/Python/covid19_clustering/head.jpg")
        pic=ImageTk.PhotoImage(image)
        label = tk.Label(self, image=pic)
        label.image = pic
        label.pack()
        
        #Membuat label dalam GUI
        label = tk.Label(self, text= "Data Covid-19 Jakarta, 17 Juni 2021", font=('Arial', 25))
        label.pack(pady=20,padx=20)
        
        #Membuat Button 'Data Clustering' yang akan menampilkan frame clustering, 
        #dengan command controller.show_frame(graphCluster)
        buttonCluster = tk.Button(self, text = "Data Clustering", height=2, width=30, 
                                  command=lambda: controller.show_frame(graphCluster))
        buttonCluster.pack()
        
        #Membuat Button 'Data Kasus' yang akan menampilkan frame data kasus corona, 
        #dengan command controller.show_frame(graphTotal)
        buttonTotal = tk.Button(self, text = "Data Kasus", height=2, width=30, 
                                command=lambda: controller.show_frame(graphTotal))
        buttonTotal.pack()
        
        #Membuat Button 'Kasus Aktif' yang akan menampilkan frame kasus aktif di jakarta, 
        #dengan command controller.show_frame(graphAktif)
        buttonKasus = tk.Button(self, text = "Kasus Aktif", height=2, width=30, 
                                command=lambda: controller.show_frame(graphAktif))
        buttonKasus.pack()
        
        #Membuat label dalam GUI berisi sumber data
        label = tk.Label(self, text= 
                         "Sumber Data : \n Standar Kelurahan Data Corona (17 Juni 2021) " + 
                         "\n https://drive.google.com/file/d/1S0hifKlm3HpSyvYJmAIqX2lU2KT0cOsb/view"
                         , font=('Arial', 8))
        label.pack(pady=20,padx=20)
        
        
        
'''
Sintaks dibawah membuat GUI Cluster
'''

#GUI CLUSTER
class graphCluster(tk.Frame) :
      def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        
        #Mengubah background frame menjadi warna putih
        tk.Frame.configure(self, bg='white')
        
        
        #Membuat label dalam GUI
        label = tk.Label(self, text="Clustering Kasus Corona Jakarta tiap Kelurahan", 
                         font=('Arial', 20), bg='blue', fg='white')
        label.pack(pady=5,padx=20)
        
        
        #Membuat visualisasi 3d dari hasil clustering dan dimasukan dalam GUI
        figure3 = plt.Figure(figsize=(9,4.5))
        ax3 = figure3.add_subplot(111, projection='3d')
        ax3.scatter(df['POSITIF'], df['Sembuh'], df['Meninggal'], c= kmeans.labels_.astype(float), edgecolor='k')
        ax3.scatter(centroids[:, 0], centroids[:, 1], c='red', s=50)
        scatter3 = FigureCanvasTkAgg(figure3, self) 
        scatter3.get_tk_widget().pack(side=tk.TOP)
        
        ax3.set_xlabel("Positif")
        ax3.set_ylabel("Sembuh")
        ax3.set_zlabel("Meninggal")
        ax3.set_title('Visualisasi Clustering')
        
        #Membuat pie chart untuk jumlah kelurahan tiap cluster dan dimasukan dalam GUI
        figure1 = plt.Figure(figsize=(4,3))
        ax1 = figure1.add_subplot(111)
        bar1 = FigureCanvasTkAgg(figure1, self)
        bar1.get_tk_widget().pack(side=tk.RIGHT)
        ax1.pie([len(clusterA), len(clusterB), len(clusterC)], colors=['orange', 'red', 'yellow'],
                labels = ['Cluster A', 'Cluster B', 'Cluster C'], startangle=90, shadow=True)
        ax1.set_title('Chart Cluster')
        
        
        #Membuat label dalam GUI
        label = tk.Label(self, text= "Cluster Covid-19 Jakarta, 17 Juni 2021", 
                         font=('Arial', 25), bg='blue', fg='white')
        label.pack(pady=15,padx=15)
        
        #Membuat label dalam GUI berisi pembagian cluster beserta jumlah kelurahan tiap clusternya
        label = tk.Label(self, text="Jumlah Custer A : "+ str(len(clusterA)) + " Kelurahan", 
                         font=('Arial', 12), bg='white')
        label.pack(pady=5,padx=20)
        label = tk.Label(self, text="Jumlah Custer B : "+ str(len(clusterB)) + " Kelurahan", 
                         font=('Arial', 12), bg='white')
        label.pack(pady=5,padx=20)
        label = tk.Label(self, text="Jumlah Custer C : "+ str(len(clusterC)) + " Kelurahan", 
                         font=('Arial', 12), bg='white')
        label.pack(pady=5,padx=20)
        
        
        #Membuat label dalam GUI
        label = tk.Label(self, text="Centroid K-Means", font=('Arial', 20), bg='cyan', fg='white')
        label.pack(pady=5,padx=20)
        
        #Membuat label dalam GUI berisi nilai centroid pada clustering
        label = tk.Label(self, text='A : ' + str(centroids[0][0]) + ", " + str(centroids[0][1]) + ", " +
                         str(centroids[0][2]) + ", ", font=('Arial', 10), bg='white')
        label.pack(pady=5,padx=20)
        label = tk.Label(self, text='B : ' + str(centroids[1][0]) + ", " + str(centroids[1][1]) + ", " +
                         str(centroids[1][2]) + ", ", font=('Arial', 10), bg='white')
        label.pack(pady=5,padx=20)
        label = tk.Label(self, text='C : ' + str(centroids[2][0]) + ", " + str(centroids[2][1]) + ", " +
                         str(centroids[2][2]) + ", \n\n", font=('Arial', 10), bg='white')
        label.pack(pady=5,padx=20)
        
        
        #Membuat Button 'Home' yang akan mengembalikan ke Frame utama, dengan command controller.show_frame(StartPage)
        buttonH = tk.Button(self, text = "Home", height=2, width=30, command=lambda: 
                            controller.show_frame(StartPage))
        buttonH.pack()
        
        
        
'''
Sintaks dibawah membuat GUI Kasus Corona
'''
#GUI KASUS CORONA
class graphTotal(tk.Frame) :
      def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        
        #Mengubah background frame menjadi warna putih
        tk.Frame.configure(self, bg='white')
         
        
        #Membuat label dalam GUI
        label = tk.Label(self, text="Data Kasus Corona Jakarta", 
                         font=('Arial', 20), bg='blue', fg='white')
        label.pack(pady=5,padx=20)
        
        
        #Membuat bar chart dari data arr_positif dan dimasukan dalam GUI
        figure1 = plt.Figure(figsize=(9,3))
        ax1 = figure1.add_subplot(111)
        bar1 = FigureCanvasTkAgg(figure1, self)
        bar1.get_tk_widget().pack(side=tk.TOP)
        ax1.bar(arr_namaKota ,arr_positif, color='orange')
        
        #Proses looping untuk memasukan value data tiap bar data, kemudian dibuat bbox pada text value tersebut
        for i, v in enumerate(arr_positif):
            ax1.text(i, v+25, "%d" %v, ha="center", color = 'white', bbox = dict(facecolor = 'red', alpha =.8))
        ax1.set_title('Total Positif') #Memberi judul dari chartnya
        

        #Membuat bar chart dari data arr_sembuh dan dimasukan dalam GUI
        figure2 = plt.Figure(figsize=(9,3))
        ax2 = figure2.add_subplot(111)
        bar2 = FigureCanvasTkAgg(figure2, self)
        bar2.get_tk_widget().pack(side=tk.TOP)
        ax2.bar(arr_namaKota ,arr_sembuh, color='lightgreen')
        
        #Proses looping untuk memasukan value data tiap bar data, kemudian dibuat bbox pada text value tersebut
        for i, v in enumerate(arr_sembuh):
            ax2.text(i, v+25, "%d" %v, ha="center", color = 'white', bbox = dict(facecolor = 'red', alpha =.8))
        ax2.set_title('Total Sembuh') #Memberi judul dari chartnya
        
        
        #Membuat bar chart dari data arr_meninggal dan dimasukan dalam GUI
        figure3 = plt.Figure(figsize=(9,3))
        ax3 = figure3.add_subplot(111)
        bar3 = FigureCanvasTkAgg(figure3, self)
        bar3.get_tk_widget().pack(side=tk.TOP)
        ax3.bar(arr_namaKota ,arr_meninggal, color='black')

        #Proses looping untuk memasukan value data tiap bar data, kemudian dibuat bbox pada text value tersebut
        for i, v in enumerate(arr_meninggal):
            ax3.text(i, v+25, "%d" %v, ha="center", color = 'white', bbox = dict(facecolor = 'red', alpha =.8))
        ax3.set_title('Total Meninggal') #Memberi judul dari chartnya
        
        
        #Membuat Button 'Home' yang akan mengembalikan ke Frame utama, dengan command controller.show_frame(StartPage)
        buttonH = tk.Button(self, text = "Home", height=2, width=30, 
                            command=lambda: controller.show_frame(StartPage))
        buttonH.pack()
        
        
        
'''
Sintaks dibawah membuat GUI Kasus Aktif
'''

#GUI KASUS AKTIF
class graphAktif(tk.Frame) :
      def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        
        #Mengubah background frame menjadi warna putih
        tk.Frame.configure(self, bg='white')
        
        
        #Membuat label dalam GUI
        label = tk.Label(self, text="Informasi Kasus Aktif Jakarta", 
                         font=('Arial', 20), bg='blue', fg='white')
        label.pack(pady=5,padx=20)


        #Membuat bar chart dari data arr_dirawat dan dimasukan dalam GUI
        figure1 = plt.Figure(figsize=(9,3))
        ax1 = figure1.add_subplot(111)
        bar1 = FigureCanvasTkAgg(figure1, self)
        bar1.get_tk_widget().pack(side=tk.TOP)
        ax1.bar(arr_namaKota ,arr_dirawat, color='grey')
        
        #Proses looping untuk memasukan value data tiap bar data, kemudian dibuat bbox pada text value tersebut
        for i, v in enumerate(arr_dirawat):
            ax1.text(i, v+25, "%d" %v, ha="center", color = 'white', bbox = dict(facecolor = 'red', alpha =.8))
        ax1.set_title('Total Dirawat') #Memberi judul dari chartnya
        
        
        #Membuat bar chart dari data arr_mandiri dan dimasukan dalam GUI
        figure2 = plt.Figure(figsize=(9,3))
        ax2 = figure2.add_subplot(111)
        bar2 = FigureCanvasTkAgg(figure2, self)
        bar2.get_tk_widget().pack(side=tk.TOP)
        ax2.bar(arr_namaKota ,arr_mandiri, color='lightgrey')
        
        #Proses looping untuk memasukan value data tiap bar data, kemudian dibuat bbox pada text value tersebut
        for i, v in enumerate(arr_mandiri):
            ax2.text(i, v+25, "%d" %v, ha="center", color = 'white', bbox = dict(facecolor = 'red', alpha =.8))
        ax2.set_title('Total Isolasi Mandiri') #Memberi judul dari chartnya
        
        
        #Membuat Button 'Home' yang akan mengembalikan ke Frame utama, dengan command controller.show_frame(StartPage)
        buttonH = tk.Button(self, text = "Home", height=2, width=30, 
                            command=lambda: controller.show_frame(StartPage))
        buttonH.pack()
  
    
        
'''
DISPLAY GUY
'''

#DISPLAY GUI
app = displayGui() #memanggil displayGui() dan dimasukan ke variable app
app.mainloop()     #memanggil mainloop() untuk menampilkan GUI
        

