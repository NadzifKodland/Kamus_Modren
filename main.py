Modern_dict = { "CRINGE": "Sesuatu yang sangat aneh atau memalukan",
            "LOL": "Tanggapan umum terhadap sesuatu yang lucu",}
word = input("Ketik kata yang tidak Kamu mengerti (gunakan huruf kapital semua!): ")  
if word in Modern_dict.keys():
    print("Makna dari" , word, "adalah" , Modern_dict[word])
else:
    print("kata tidak di temukan")
           
