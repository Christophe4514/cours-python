# class A:
#     def affichage(self):
#         print("Bonjour")
 
# class B(A):
#     def affichage(self):
#         print("Au revoir")
        
#     def test_super(self):
#         super().affichage()
 
 
# mon_instance = B()
# mon_instance.test_super()

class A:
    def methode():
        print("Bonjour")
 
class B(A):
    def methode():
        print("Au revoir")
 
    def appel_methode():
        B.methode()
 
B.appel_methode()