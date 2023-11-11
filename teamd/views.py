from django.shortcuts import render, redirect,get_object_or_404
from .models import *
from .forms import ModuleForm

# Create your views here.



def login(request):
	return render(request,'login.html')

def menu(request):
	return render(request,'menu.html')



#views pour afficher les enseignants
def view(request):
    Enseignants = Enseignant.objects
    return render(request, 'viewEnseignant.html', {'Enseignants': Enseignants})


def insert(request):
    if request.method == "POST":
        nom_eng = request.POST['nom']
        email = request.POST['email']
        telph = request.POST['telph']
        Diplome = request.POST['Diplome']
        Statut = request.POST['Statut']
        image = request.FILES['image']
        Enseignants = Enseignant(nom_eng=nom_eng, email=email,
                                 telph=telph, Diplome=Diplome, Statut=Statut, image=image)
        Enseignants.save()
        return redirect('enseignants')

    return render(request, "indexEnseignant.html")

# List data from database


def delete(request, id):
    Enseignants = Enseignant.objects.get(id_ensg=id)
    Enseignants.delete()
    return redirect('enseignants')


def update(request, id):
    Enseignants = Enseignant.objects.get(id_ensg=id)
    if request.method == "POST":
        nom_eng = request.POST['nom']
        email = request.POST['email']
        telph = request.POST['telph']
        Diplome = request.POST['Diplome']
        Statut = request.POST['Statut']
        image = request.FILES['image']
        Enseignants.nom_eng = nom_eng
        Enseignants.email = email
        Enseignants.telph = telph
        Enseignants.Diplome = Diplome
        Enseignants.Statut = Statut
        Enseignants.image = image
        Enseignants.save()
        return redirect('enseignants')
    return render(request, "editEnseignant.html",  {'Enseignants': Enseignants})


Enseignants = Enseignant.objects.all()
for enseignant in Enseignants:
    print(enseignant.image.url)
    


# View pour afficher les étudiants
def viewE(request):
    search = request.GET.get('search', '')
    etudiants = Etudiant.objects.filter(nom__icontains=search)
    return render(request, 'viewEtudiant.html', {'etudiants': etudiants})

# View pour insérer un nouvel étudiant
def insertE(request):
    if request.method == "POST":
        matricule = request.POST['matricule']
        nom = request.POST['nom']
        prenom = request.POST['prenom']
        date_naissance = request.POST['date_naissance']
        lieu_naissance = request.POST['lieu_naissance']
        pays_naissance = request.POST['pays_naissance']
        departement = request.POST['departement']
        voie_acces = request.POST['voie_acces']
        nationalite = request.POST['nationalite']
        nni = request.POST['nni']
        statut = request.POST['statut']
        annee_inscription = request.POST['annee_inscription']
        etudiant = Etudiant(matricule=matricule, nom=nom, prenom=prenom, date_naissance=date_naissance,
                            lieu_naissance=lieu_naissance, pays_naissance=pays_naissance, departement=departement,
                            voie_acces=voie_acces, nationalite=nationalite, nni=nni, statut=statut,
                            annee_inscription=annee_inscription)
        etudiant.save()
        return redirect('viewEtudiant')

    return render(request, "indexEtudiant.html")

# View pour supprimer un étudiant
def deleteE(request, id):
    etudiant = Etudiant.objects.get(id=id)
    etudiant.delete()
    return redirect('viewEtudiant')

# View pour mettre à jour les informations d'un étudiant
def updateE(request, id):
    etudiant = Etudiant.objects.get(id=id)
    if request.method == "POST":
        nom = request.POST['nom']
        prenom = request.POST['prenom']
        date_naissance = request.POST['date_naissance']
        lieu_naissance = request.POST['lieu_naissance']
        pays_naissance = request.POST['pays_naissance']
        departement = request.POST['departement']
        voie_acces = request.POST['voie_acces']
        nationalite = request.POST['nationalite']
        nni = request.POST['nni']
        statut = request.POST['statut']
        annee_inscription = request.POST['annee_inscription']
        etudiant.nom = nom
        etudiant.prenom = prenom
        etudiant.date_naissance = date_naissance
        etudiant.lieu_naissance = lieu_naissance
        etudiant.pays_naissance = pays_naissance
        etudiant.departement = departement
        etudiant.voie_acces = voie_acces
        etudiant.nationalite = nationalite
        etudiant.nni = nni
        etudiant.statut = statut
        etudiant.annee_inscription = annee_inscription
        etudiant.save()
        return redirect('viewEtudiant')
    return render(request, "editEtudiant.html", {'etudiant': etudiant})

etudiants = Etudiant.objects.all()

# View pour mettre à jour les informations d'une note
def viewN(request):
    Notes = Note.objects
    return render(request, 'viewNote.html', {'Notes': Notes})


def insertN(request):
    if request.method == "POST":
        Matricule=request.POST['Matricule']
        Nom = request.POST['Nom']
        moyenne_S1 = request.POST['moyenne_S1']
        moyenne_S2 = request.POST['moyenne_S2']
        moyenne_generale = request.POST['moyenne_generale']
        Decision = request.POST['Decision']
        Notes = Note( Matricule=Matricule, Nom=Nom, moyenne_S1=moyenne_S1, moyenne_S2=moyenne_S2, moyenne_generale=moyenne_generale , Decision=Decision)
        Notes.save()
        return redirect('viewNote')

    return render(request, "indexNote.html")

# List data from database


def deleteN(request, id):
    Notes = Note.objects.get(Matricule=id)
    Notes.delete()
    return redirect('viewNote')


def updateN(request, id):
    Notes = Note.objects.get(id_ensg=id)
    if request.method == "POST":
        Matricule=request.POST['Matricule']
        Nom = request.POST['Nom']
        moyenne_S1 = request.POST['moyenne_S1']
        moyenne_S2 = request.POST['moyenne_S2']
        moyenne_generale = request.POST['moyenne_generale']
        Decision = request.POST['Decision']
        Notes.Matricule=Matricule
        Notes.Nom = Nom
        Notes.moyenne_S1 = moyenne_S1
        Notes.moyenne_S2 = moyenne_S2
        Notes.moyenne_generale = moyenne_generale
        Notes.Decision = Decision
        Notes.save()
        return redirect('viewNote')
    return render(request, "editNote.html",  {'Notes': Notes})


Notes = Note.objects.all()


#Element module travail l7aj 4e ta7t 

def create_module(request):
    if request.method == 'POST':
        form = ModuleForm(request.POST)
        if form.is_valid():
            module = form.save(commit=False)
            module.code = generate_module_code(module.departement, module.semestre)
            module.save()
            return redirect('module_list')
    else:
        form = ModuleForm()
    
    return render(request, 'create_module.html', {'form': form})

def generate_module_code(departement_code, semestre):
    modules_count = Module.objects.filter(departement=departement_code, semestre=semestre).count()
    return f"{departement_code}{semestre:2d}{modules_count+1:2d}"

def module_list(request):
    modules = Module.objects.all()
    return render(request, 'module_list.html', {'modules': modules})


def update_module(request, pk):
    module = get_object_or_404(Module, pk=pk)

    if request.method == 'POST':
        form = ModuleForm(request.POST, instance=module)
        if form.is_valid():
            form.save()
            return redirect('module_list')  # Rediriger vers la liste des modules après la mise à jour
    else:
        form = ModuleForm(instance=module)
    
    return render(request, 'update_module.html', {'form': form})

def delete_module(request, pk):
    module = get_object_or_404(Module, pk=pk)

    if request.method == 'POST':
        module.delete()
        return redirect(request.META.get('HTTP_REFERER'))  # Rediriger vers l'URL de référence (la liste des modules)
    
    return redirect('module_list')  # Rediriger vers la vue de liste des modules si la méthode de requête n'est pas POST















