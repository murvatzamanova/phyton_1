# Home task
# 3)
# numbers = [1, 2, 3]


# def hesabla(numbers):
#     hasil = 1
#     for eded in numbers:
#         if eded.isdigit():
#             reqem = int(eded)
#             hasil *= reqem
#     return hasil


# print(hesabla(numbers))

# def hesabla(numbers):
#     hasil = 1
#     for eded in numbers:
#        hasil *= eded
#     return hasil

# print(hesabla(numbers))


# 7)
# num1 = [1, 2, 3]
# num2 = [3, 4, 5]

# result = [(num1[i] + num2[i]) / 2 for i in range(len(num2))]
# print(result)


"""
OOP >> Object Oriented Programming 

Class:
Ozellikler: yas, reng, ad
Davranislar: uze bilme, danisa bilme, mahni oxuya bilme

class attributes: Meselen butun pinqivinlerin sinifi "Qus"dur
instance attributes: Her bir obyektin sirf ozune xas ozelliklerini ozunde dasiyir

Butun obyektleri bir yerde tutan ve ozelliklerini dasiyan hissedir
"""

# class Penguen():
#     pass


"""
Obyekt ise Classin ozelliklerini dasiyir
Istenilen qeder obyekt yara biler
"""

# class Penguen():
#     # Class atribut:
#     sinif = "Quş"
    
#     # Instance atribut:
#     #     kralPinqivin, Kral Pinqivin 
#     def _init_(self, ad, yas, reng):
#         self.ad = ad
#         self.yas = yas
#         self.reng = reng
        
#     def uze_bilme(self):
#         return f"{self.ad} uze bilir"
    
#     def mahni_oxuya_bilme(self, mahni_oxuya_bilme = False):
#         if mahni_oxuya_bilme == True:
#             return f"{self.ad} mahni oxuya bilir"
#         else:
#             return f"{self.ad} mahni oxuya bilmir"
        
#     def reqs_ede_bilme(self, reqs_ede_bilme = False):
#         if reqs_ede_bilme == True:
#             return f"{self.ad} reqs ede bilir"
#         else:
#             return f"{self.ad} reqs ede bilmir"
    
    

# # Obyetkler:  
# kralPinqivin = Penguen("Kral Pinqivin", 4, "Qara")
# sariPinqivin = Penguen("Sari Pinqivin", 2, "Sari")
# neseliAyaklar = Penguen("Neşeli ayaklar", 5, "Ağ")


# Obyektin dasidigi ozellikleri cagirmaq ucun >> object.objectOzellik

# print(f"{kralPinqivin.ad}-nin {kralPinqivin.yas} yasi var ve rengi {kralPinqivin.reng}-dir. {kralPinqivin.sinif} sinifine aiddir")

# print(f"{sariPinqivin.ad}-nin {sariPinqivin.yas} yasi var ve rengi {sariPinqivin.reng}-dir. {sariPinqivin.sinif} sinifine aiddir")

# print(kralPinqivin.uze_bilme())
# print(f"{neseliAyaklar.ad}")
# print(neseliAyaklar.mahni_oxuya_bilme(mahni_oxuya_bilme=False))
# print(f"{sariPinqivin.mahni_oxuya_bilme(True)} ve {kralPinqivin.reqs_ede_bilme(False)}")

# print(neseliAyaklar.mahni_oxuya_bilme())\





# ---------------------------------------------------------------------------------

# ...........NEW TASK...........

class Meyvə:
        nov = "meyve"
    def __init__(self, ad, rəng,qiymet):
        self.ad = ad
        self.rəng = rəng
        self.qiymet = qiymet

    def təsvir_et(self):
        return f"{self.ad} adlı meyvə, {self.rəng} rəngdədir."

alma = Meyvə("alma", "qırmızı",2)
armud = Meyvə("armud", "yaşıl",4)

print(alma.ad)
print(alma.qiymet)
print(alma.təsvir_et())
print(armud.təsvir_et())



