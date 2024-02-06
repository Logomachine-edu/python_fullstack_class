text1 = "Logomachine"
t1l = len(text1) // 2  # text1_len, считаем кол-во символов в строке и делим на 2
text2 = "ArtSpace"
t2l = len(text2) // 2  # text2_len, считаем кол-во символов в строке и делим на 2
text3 = "Designify"
t3l = len(text3) // 2  # text3_len, считаем кол-во символов в строке и делим на 2
print(text1[t1l::] + text1[0:t1l])
print(text2[t2l::] + text2[0:t2l])
print(text3[t3l::] + text3[0:t3l])
