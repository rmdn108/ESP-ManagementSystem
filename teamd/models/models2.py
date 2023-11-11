from django.db import models

# Create your models here.


    
    
    #model etudiants      
class Etudiant(models.Model):
    nom = models.CharField(max_length=50)
    prenom = models.CharField(max_length=50)
    date_naissance = models.DateField()
    lieu_naissance = models.CharField(max_length=50)
    pays_naissance = models.CharField(max_length=50)
    departement = models.CharField(max_length=50)
    voie_acces = models.CharField(max_length=10)
    matricule = models.CharField(max_length=50)
    nationalite = models.CharField(max_length=50)
    nni = models.CharField(max_length=50)
    statut = models.CharField(max_length=50)
    annee_inscription = models.IntegerField()
    #class Meta:
    #     db_table = "Etudiants"

    # def __str__(self):
    #     return str(self.matricule)

#model notes
class Note(models.Model):
    Matricule=models.AutoField(primary_key=True)
    Nom=models.CharField(max_length=50)
    moyenne_S1=models.FloatField()
    moyenne_S2=models.FloatField()
    moyenne_generale=models.FloatField()
    Decision=models.CharField(max_length=50)
    #class Meta:
    #    db_table = "Notes"
    #
    #def __str__(self):
    #    return str(self.Matricule)
    
    
    
    
    
    
    
    
    
    
