from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from .models import Enseignant, Examen, Note, RessourcesUE, UnitesEnseignement, Etudiant
from .forms import EnseignantForm, ExamenForm, NoteForm, RessourceForm, EtudiantForm, UniteForm

def liste_enseignants(request):
    enseignants = Enseignant.objects.all()
    return render(request, 'gestionnaire/liste_enseignants.html', {'enseignants': enseignants})

def ajouter_enseignant(request):
    if request.method == 'POST':
        form = EnseignantForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('liste_enseignants')
    else:
        form = EnseignantForm()
    return render(request, 'gestionnaire/ajouter_enseignant.html', {'form': form})

def modifier_enseignant(request, enseignant_id):
    enseignant = get_object_or_404(Enseignant, pk=enseignant_id)
    if request.method == 'POST':
        form = EnseignantForm(request.POST, instance=enseignant)
        if form.is_valid():
            form.save()
            return redirect('liste_enseignants')
    else:
        form = EnseignantForm(instance=enseignant)
    return render(request, 'gestionnaire/modifier_enseignant.html', {'form': form, 'enseignant': enseignant})

def supprimer_enseignant(request, enseignant_id):
    enseignant = get_object_or_404(Enseignant, pk=enseignant_id)
    if request.method == 'POST':
        enseignant.delete()
        return redirect('liste_enseignants')
    return render(request, 'gestionnaire/supprimer_enseignant.html', {'enseignant': enseignant})

def liste_examens(request):
    examens = Examen.objects.all()
    return render(request, 'gestionnaire/liste_examens.html', {'examens': examens})

def ajouter_examen(request):
    if request.method == 'POST':
        form = ExamenForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('liste_examens')
    else:
        form = ExamenForm()
    return render(request, 'gestionnaire/ajouter_examen.html', {'form': form})

def modifier_examen(request, examen_id):
    examen = get_object_or_404(Examen, pk=examen_id)
    if request.method == 'POST':
        form = ExamenForm(request.POST, instance=examen)
        if form.is_valid():
            form.save()
            return redirect('liste_examens')
    else:
        form = ExamenForm(instance=examen)
    return render(request, 'gestionnaire/modifier_examen.html', {'form': form, 'examen': examen})

def supprimer_examen(request, examen_id):
    examen = get_object_or_404(Examen, pk=examen_id)
    if request.method == 'POST':
        examen.delete()
        return redirect('liste_examens')
    return render(request, 'gestionnaire/supprimer_examen.html', {'examen': examen})

def liste_notes(request):
    notes = Note.objects.all()
    return render(request, 'gestionnaire/liste_notes.html', {'notes': notes})

def ajouter_note(request):
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('liste_notes')
    else:
        form = NoteForm()
    return render(request, 'gestionnaire/ajouter_note.html', {'form': form})

def modifier_note(request, pk):
    note = Note.objects.get(pk=pk)
    if request.method == 'POST':
        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect('liste_notes')
    else:
        form = NoteForm(instance=note)
    return render(request, 'gestionnaire/modifier_note.html', {'form': form})

def supprimer_note(request, pk):
    note = Note.objects.get(pk=pk)
    if request.method == 'POST':
        note.delete()
        return redirect('liste_notes')
    return render(request, 'gestionnaire/supprimer_note.html', {'note': note})

def liste_ressources(request):
    ressources = RessourcesUE.objects.all()
    return render(request, 'gestionnaire/liste_ressources.html', {'ressources': ressources})

def ajouter_ressource(request):
    if request.method == 'POST':
        form = RessourceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('liste_ressources')
    else:
        form = RessourceForm()
    return render(request, 'gestionnaire/ajouter_ressource.html', {'form': form})

def modifier_ressource(request, code_ressource):
    ressource = get_object_or_404(RessourcesUE, code_ressource=code_ressource)
    if request.method == 'POST':
        form = RessourceForm(request.POST, instance=ressource)
        if form.is_valid():
            form.save()
            return redirect('liste_ressources')
    else:
        form = RessourceForm(instance=ressource)
    return render(request, 'gestionnaire/modifier_ressource.html', {'form': form, 'ressource': ressource})

def supprimer_ressource(request, code_ressource):
    ressource = RessourcesUE.objects.get(code_ressource=code_ressource)
    if request.method == 'POST':
        ressource.delete()
        return redirect('liste_ressources')
    return render(request, 'gestionnaire/supprimer_ressource.html', {'ressource': ressource})

def liste_unites(request):
    unites = UnitesEnseignement.objects.all()
    return render(request, 'gestionnaire/liste_unites.html', {'unites': unites})

def ajouter_unite(request):
    if request.method == 'POST':
        form = UniteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('liste_unites')
    else:
        form = UniteForm()
    return render(request, 'gestionnaire/ajouter_unite.html', {'form': form})

def modifier_unite(request, code):
    unite = UnitesEnseignement.objects.get(code=code)
    if request.method == 'POST':
        form = UniteForm(request.POST, instance=unite)
        if form.is_valid():
            form.save()
            return redirect('liste_unites')
    else:
        form = NoteForm(instance=unite)
    return render(request, 'gestionnaire/modifier_unite.html', {'form': form, 'unite': unite})

def supprimer_unite(request, code):
    unite = UnitesEnseignement.objects.get(code=code)
    if request.method == 'POST':
        unite.delete()
        return redirect('liste_unites')
    return render(request, 'gestionnaire/supprimer_unite.html', {'unite': unite})

def liste_etudiants(request):
    # Logique pour récupérer les étudiants depuis la base de données
    etudiants = Etudiant.objects.all()
    context = {
        'etudiants': etudiants,
    }

    return render(request, 'gestionnaire/liste_etudiants.html', context)

def ajouter_etudiant(request):
    if request.method == 'POST':
        form = EtudiantForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('liste_etudiants')
    else:
        form = EtudiantForm()
    return render(request, 'gestionnaire/ajouter_etudiant.html', {'form': form})

def modifier_etudiant(request, numero_etudiant):
    etudiant = Etudiant.objects.get(numero_etudiant=numero_etudiant)
    if request.method == 'POST':
        form = EtudiantForm(request.POST, request.FILES, instance=etudiant)
        if form.is_valid():
            form.save()  # Appel à form.save() après validation du formulaire
            return redirect('liste_etudiants')
    else:
        form = EtudiantForm(instance=etudiant)
    return render(request, 'gestionnaire/modifier_etudiant.html', {'form': form, 'etudiant': etudiant})

def supprimer_etudiant(request, numero_etudiant):
    etudiant = Etudiant.objects.get(numero_etudiant=numero_etudiant)
    if request.method == 'POST':
        etudiant.delete()
        return redirect('liste_etudiants')
    return render(request, 'gestionnaire/supprimer_etudiant.html', {'etudiant': etudiant})

def accueil(request):
    return render(request, 'gestionnaire/index.html')

def rechercher(request):
    if 'query' in request.GET:
        query = request.GET['query']
        enseignants = Enseignant.objects.filter(Q(nom__icontains=query) | Q(prenom__icontains=query))
        examens = Examen.objects.filter(Q(titre__icontains=query) | Q(date__icontains=query))
        notes = Note.objects.filter(Q(appreciation__icontains=query))
        ressources = RessourcesUE.objects.filter(Q(nom__icontains=query) | Q(descriptif__icontains=query))
        unites = UnitesEnseignement.objects.filter(Q(nom__icontains=query) | Q(semestre__icontains=query))
        etudiants = Etudiant.objects.filter(Q(nom__icontains=query) | Q(prenom__icontains=query) | Q(email__icontains=query))

        results = {
            'enseignants': enseignants,
            'examens': examens,
            'notes': notes,
            'ressources': ressources,
            'unites': unites,
            'etudiants': etudiants
        }
    else:
        results = {}

    return render(request, 'gestionnaire/search_results.html', {'results': results})