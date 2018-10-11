class Personne:
    
    def __init__(self,nom, prenom, telephone, adress_mail, adress_post):
        self.nom = nom
        self.prenom = prenom
        self.telephone = telephone            
        self.adress_mail = adress_mail
        self.adress_post = adress_post


    def saisirprofil(self):
        liste = []
        self.nom = input("saisir votre nom\n")
        self.prenom   = input("saisir votre prénom\n")
        self.telephone = input ("saisir votre numéro de téléphone sans espace\n")
        self.adress_mail = input ("saisir votre adresse email\n")
        self.adress_post = input ("saisir votre adresse postale\n")
        liste.append(self.nom)
        liste.append(self.prenom)
        liste.append (self.telephone)
        liste.append (self.adress_mail)
        liste.append (self.adress_post)
        f = open('C:/Users/ousseynou/Desktop/client.txt','a')
        for i in liste:
            f.write("{} ".format(i))
    
        f.close()

p1 = Personne('diop', 'ousseynou', '0622743009', 'diopwas@yahoo.fr', '2 avenue de leurope villepinte')
p1.saisirprofil()


        
        
            
        
        
