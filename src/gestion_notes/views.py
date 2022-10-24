from django.shortcuts import render
import requests

from rest_framework import viewsets, status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from gestion_notes.models import URL


class AnneAcademiqueViewSet(viewsets.ViewSet):
    def list(self, request):  # /api/annee-academique
        r = requests.get(URL.BASE_URL + "annee-academique/all")
        return Response(r.json())

    def create(self, request):  # /api/annee-academique
        r = requests.post(URL.BASE_URL + "annee-academique/save", data=request.data)
        return Response(r.json())

    def retrieve(self, request, pk=None):  # /api/annee-academique/<str:code>
        r = requests.get(URL.BASE_URL + "annee-academique/" + pk + "data")
        return Response(r.json())

    def update(self, request, pk=None):  # /api/annee-academique/<str:code>
        r = requests.post(URL.BASE_URL + "annee-academique/update", data=request.data)
        return Response(r.json())

    def destroy(self, request, pk=None):  # /api/annee-academique/<str:code>
        r = requests.get(URL.BASE_URL + "annee-academique/" + pk + "/delete")
        return Response(r.json())


class AnonymatViewSet(viewsets.ViewSet):
    def list(self, request):  # /api/anonymat
        r = requests.get(URL.BASE_URL + "anonymat/all")
        return Response(r.json())

    def create(self, request):  # /api/anonymat
        r = requests.post(URL.BASE_URL + "anonymat/save", data=request.data)
        return Response(r.json())

    def retrieve(self, request, pk=None):  # /api/anonymat/<str:code>
        r = requests.get(URL.BASE_URL + "anonymat/" + pk + "data")
        return Response(r.json())

    def update(self, request, pk=None):  # /api/anonymat/<str:code>
        r = requests.post(URL.BASE_URL + "anonymat/update", data=request.data)
        return Response(r.json())

    def destroy(self, request, pk=None):  # /api/anonymat/<str:code>
        r = requests.get(URL.BASE_URL + "anonymat/" + pk + "/delete")
        return Response(r.json())


class CandidatViewSet(viewsets.ViewSet):
    def list(self, request):  # /api/candidat
        r = requests.get(URL.BASE_URL + "candidat/all")
        return Response(r.json())

    def create(self, request):  # /api/candidat
        r = requests.post(URL.BASE_URL + "candidat/save", data=request.data)
        return Response(r.json())

    def retrieve(self, request, pk=None):  # /api/candidat/<str:code>
        r = requests.get(URL.BASE_URL + "candidat/" + pk + "data")
        return Response(r.json())

    def update(self, request, pk=None):  # /api/candidat/<str:code>
        r = requests.post(URL.BASE_URL + "candidat/update", data=request.data)
        return Response(r.json())

    def destroy(self, request, pk=None):  # /api/candidat/<str:code>
        r = requests.get(URL.BASE_URL + "candidat/" + pk + "/delete")
        return Response(r.json())


class ClasseViewSet(viewsets.ViewSet):
    def list(self, request):  # /api/classe
        r = requests.get(URL.BASE_URL + "classe/all")
        return Response(r.json())

    def create(self, request):  # /api/classe
        r = requests.post(URL.BASE_URL + "classe/save", data=request.data)
        return Response(r.json())

    def retrieve(self, request, pk=None):  # /api/classe/<str:code>
        r = requests.get(URL.BASE_URL + "classe/" + pk + "data")
        return Response(r.json())

    def update(self, request, pk=None):  # /api/classe/<str:code>
        r = requests.post(URL.BASE_URL + "classe/update", data=request.data)
        return Response(r.json())

    def destroy(self, request, pk=None):  # /api/classe/<str:code>
        r = requests.get(URL.BASE_URL + "classe/" + pk + "/delete")
        return Response(r.json())


class DiscipineViewSet(viewsets.ViewSet):
    def list(self, request):  # /api/discipline
        r = requests.get(URL.BASE_URL + "discipline/all")
        return Response(r.json())

    def create(self, request):  # /api/discipline
        r = requests.post(URL.BASE_URL + "discipline/save", data=request.data)
        return Response(r.json())

    def retrieve(self, request, pk=None):  # /api/discipline/<str:code>
        r = requests.get(URL.BASE_URL + "discipline/" + pk + "data")
        return Response(r.json())

    def update(self, request, pk=None):  # /api/discipline/<str:code>
        r = requests.post(URL.BASE_URL + "discipline/update", data=request.data)
        return Response(r.json())

    def destroy(self, request, pk=None):  # /api/discipline/<str:code>
        r = requests.get(URL.BASE_URL + "discipline/" + pk + "/delete")
        return Response(r.json())

@api_view(['GET'])
def search_discipline_by_etudiant_or_semestre_or_date(requests, etudiant, semestre, date_retard):
    r = requests.get(URL.BASE_URL + "discipline/" + etudiant + "/" + semestre + "/" + date_retard)
    return Response(r.json())


class DroitViewSet(viewsets.ViewSet):
    def list(self, request):  # /api/droit
        r = requests.get(URL.BASE_URL + "droit/all")
        return Response(r.json())

    def create(self, request):  # /api/droit
        r = requests.post(URL.BASE_URL + "droit/save", data=request.data)
        return Response(r.json())

    def retrieve(self, request, pk=None):  # /api/droit/<str:code>
        r = requests.get(URL.BASE_URL + "droit/" + pk + "data")
        return Response(r.json())

    def update(self, request, pk=None):  # /api/droit/<str:code>
        r = requests.post(URL.BASE_URL + "droit/update", data=request.data)
        return Response(r.json())

    def destroy(self, request, pk=None):  # /api/droit/<str:code>
        r = requests.get(URL.BASE_URL + "droit/" + pk + "/delete")
        return Response(r.json())


class EmailViewSet(viewsets.ViewSet):
    def list(self, request):  # /api/email
        r = requests.get(URL.BASE_URL + "email/all")
        return Response(r.json())

    def create(self, request):  # /api/email
        r = requests.post(URL.BASE_URL + "email/save", data=request.data)
        return Response(r.json())

    def retrieve(self, request, pk=None):  # /api/email/<str:code>
        r = requests.get(URL.BASE_URL + "email/" + pk + "data")
        return Response(r.json())

    def update(self, request, pk=None):  # /api/email/<str:code>
        r = requests.post(URL.BASE_URL + "email/update", data=request.data)
        return Response(r.json())

    def destroy(self, request, pk=None):  # /api/email/<str:code>
        r = requests.get(URL.BASE_URL + "email/" + pk + "/delete")
        return Response(r.json())


class EnseignantViewSet(viewsets.ViewSet):
    def list(self, request):  # /api/enseignant
        r = requests.get(URL.BASE_URL + "enseignant/all")
        return Response(r.json())

    def create(self, request):  # /api/enseignant
        r = requests.post(URL.BASE_URL + "enseignant/save", data=request.data)
        return Response(r.json())

    def retrieve(self, request, pk=None):  # /api/enseignant/<str:code>
        r = requests.get(URL.BASE_URL + "enseignant/" + pk + "data")
        return Response(r.json())

    def update(self, request, pk=None):  # /api/enseignant/<str:code>
        r = requests.post(URL.BASE_URL + "enseignant/update", data=request.data)
        return Response(r.json())

    def destroy(self, request, pk=None):  # /api/enseignant/<str:code>
        r = requests.get(URL.BASE_URL + "enseignant/" + pk + "/delete")
        return Response(r.json())


class EnseignementViewSet(viewsets.ViewSet):
    def list(self, request):  # /api/enseignement
        r = requests.get(URL.BASE_URL + "enseignement/all")
        return Response(r.json())

    def create(self, request):  # /api/enseignement
        r = requests.post(URL.BASE_URL + "enseignement/save", data=request.data)
        return Response(r.json())

    def retrieve(self, request, pk=None):  # /api/enseignement/<str:code>
        r = requests.get(URL.BASE_URL + "enseignement/" + pk + "data")
        return Response(r.json())

    def update(self, request, pk=None):  # /api/enseignement/<str:code>
        r = requests.post(URL.BASE_URL + "enseignement/update", data=request.data)
        return Response(r.json())

    def destroy(self, request, pk=None):  # /api/enseignement/<str:code>
        r = requests.get(URL.BASE_URL + "enseignement/" + pk + "/delete")
        return Response(r.json())


class EnvoiMessageViewSet(viewsets.ViewSet):
    def list(self, request):  # /api/envoi-message
        r = requests.get(URL.BASE_URL + "envoi-message/all")
        return Response(r.json())

    def create(self, request):  # /api/envoi-message
        r = requests.post(URL.BASE_URL + "envoi-message/save", data=request.data)
        return Response(r.json())

    def retrieve(self, request, pk=None):  # /api/envoi-message/<str:code>
        r = requests.get(URL.BASE_URL + "envoi-message/" + pk + "data")
        return Response(r.json())

    def update(self, request, pk=None):  # /api/envoi-message/<str:code>
        r = requests.post(URL.BASE_URL + "envoi-message/update", data=request.data)
        return Response(r.json())

    def destroy(self, request, pk=None):  # /api/envoi-message/<str:code>
        r = requests.get(URL.BASE_URL + "envoi-message/" + pk + "/delete")
        return Response(r.json())


class EstInscritViewSet(viewsets.ViewSet):
    def list(self, request):  # /api/est-inscrit
        r = requests.get(URL.BASE_URL + "est-inscrit/all")
        return Response(r.json())

    def create(self, request):  # /api/est-inscrit
        r = requests.post(URL.BASE_URL + "est-inscrit/save", data=request.data)
        return Response(r.json())

    def retrieve(self, request, pk=None):  # /api/est-inscrit/<str:code>
        r = requests.get(URL.BASE_URL + "est-inscrit/" + pk + "data")
        return Response(r.json())

    def update(self, request, pk=None):  # /api/est-inscrit/<str:code>
        r = requests.post(URL.BASE_URL + "est-inscrit/update", data=request.data)
        return Response(r.json())

    def destroy(self, request, pk=None):  # /api/est-inscrit/<str:code>
        r = requests.get(URL.BASE_URL + "est-inscrit/" + pk + "/delete")
        return Response(r.json())


class EtudiantViewSet(viewsets.ViewSet):
    def list(self, request):  # /api/etudiant
        r = requests.get(URL.BASE_URL + "etudiant/all")
        return Response(r.json())

    def create(self, request):  # /api/etudiant
        r = requests.post(URL.BASE_URL + "etudiant/save", data=request.data)
        return Response(r.json())

    def retrieve(self, request, pk=None):  # /api/etudiant/<str:code>
        r = requests.get(URL.BASE_URL + "etudiant/" + pk + "data")
        return Response(r.json())

    def update(self, request, pk=None):  # /api/etudiant/<str:code>
        r = requests.post(URL.BASE_URL + "etudiant/update", data=request.data)
        return Response(r.json())

    def destroy(self, request, pk=None):  # /api/etudiant/<str:code>
        r = requests.get(URL.BASE_URL + "etudiant/" + pk + "/delete")
        return Response(r.json())

@api_view(['GET'])
def get_etudiant_by_matricule(request, matricule):
    r = requests.get(URL.BASE_URL + "etudiant/" + matricule + "/get")
    return Response(r.json())


class EvaluationViewSet(viewsets.ViewSet):
    def list(self, request):  # /api/evaluation
        r = requests.get(URL.BASE_URL + "evaluation/all")
        return Response(r.json())

    def create(self, request):  # /api/evaluation
        r = requests.post(URL.BASE_URL + "evaluation/save", data=request.data)
        return Response(r.json())

    def retrieve(self, request, pk=None):  # /api/evaluation/<str:code>
        r = requests.get(URL.BASE_URL + "evaluation/" + pk + "data")
        return Response(r.json())

    def update(self, request, pk=None):  # /api/evaluation/<str:code>
        r = requests.post(URL.BASE_URL + "evaluation/update", data=request.data)
        return Response(r.json())

    def destroy(self, request, pk=None):  # /api/evaluation/<str:code>
        r = requests.get(URL.BASE_URL + "evaluation/" + pk + "/delete")
        return Response(r.json())

@api_view(['GET'])
def search_type_evaluation(request, pk):  # /api/evaluation/<str:code>/search-evaluation
    r = requests.get(URL.BASE_URL + "evaluation/" + pk + "/searchEvaluation")
    return Response(r.json())

@api_view(['GET'])
def search_type_etudiant(request, type_ev, code_ue, an):
    r = requests.get(URL.BASE_URL + "evaluation/" + type_ev + "/" + code_ue + "/" + an + "/searchTypeEtudiant")
    return Response(r.json())


class FiliereViewSet(viewsets.ViewSet):
    def list(self, request):  # /api/filiere
        r = requests.get(URL.BASE_URL + "filiere/all")
        return Response(r.json())

    def create(self, request):  # /api/filiere
        r = requests.post(URL.BASE_URL + "filiere/save", data=request.data)
        return Response(r.json())

    def retrieve(self, request, pk=None):  # /api/filiere/<str:code>
        r = requests.get(URL.BASE_URL + "filiere/" + pk + "data")
        return Response(r.json())

    def update(self, request, pk=None):  # /api/filiere/<str:code>
        r = requests.post(URL.BASE_URL + "filiere/update", data=request.data)
        return Response(r.json())

    def destroy(self, request, pk=None):  # /api/filiere/<str:code>
        r = requests.get(URL.BASE_URL + "filiere/" + pk + "/delete")
        return Response(r.json())

@api_view(['GET'])
def get_note_by_libelle_filiere(request, libele_filiere): # search-semestre-by-libelle-or-annee-academique/<str:libelle>/<str:annee_academique>/
    r = requests.get(URL.BASE_URL + "filiere/" + libele_filiere + "/search")
    return Response(r.json())


class HistoriqueNoteViewSet(viewsets.ViewSet):
    def list(self, request):  # /api/historique-note
        r = requests.get(URL.BASE_URL + "historiqueNote/all")
        return Response(r.json())

    def create(self, request):  # /api/historique-note
        r = requests.post(URL.BASE_URL + "historiqueNote/save", data=request.data)
        return Response(r.json())

    def retrieve(self, request, pk=None):  # /api/historique-note/<str:code>
        r = requests.get(URL.BASE_URL + "historiqueNote/" + pk + "data")
        return Response(r.json())

    def update(self, request, pk=None):  # /api/historique-note/<str:code>
        r = requests.post(URL.BASE_URL + "historiqueNote/update", data=request.data)
        return Response(r.json())

    def destroy(self, request, pk=None):  # /api/historique-note/<str:code>
        r = requests.get(URL.BASE_URL + "historiqueNote/" + pk + "/delete")
        return Response(r.json())


class MessageViewSet(viewsets.ViewSet):
    def list(self, request):  # /api/message
        r = requests.get(URL.BASE_URL + "message/all")
        return Response(r.json())

    def create(self, request):  # /api/message
        r = requests.post(URL.BASE_URL + "message/save", data=request.data)
        return Response(r.json())

    def retrieve(self, request, pk=None):  # /api/message/<str:code>
        r = requests.get(URL.BASE_URL + "message/" + pk + "data")
        return Response(r.json())

    def update(self, request, pk=None):  # /api/message/<str:code>
        r = requests.post(URL.BASE_URL + "message/update", data=request.data)
        return Response(r.json())

    def destroy(self, request, pk=None):  # /api/message/<str:code>
        r = requests.get(URL.BASE_URL + "message/" + pk + "/delete")
        return Response(r.json())


class ModuleViewSet(viewsets.ViewSet):
    def list(self, request):  # /api/module
        r = requests.get(URL.BASE_URL + "module/all")
        return Response(r.json())

    def create(self, request):  # /api/module
        r = requests.post(URL.BASE_URL + "module/save", data=request.data)
        return Response(r.json())

    def retrieve(self, request, pk=None):  # /api/module/<str:code>
        r = requests.get(URL.BASE_URL + "module/" + pk + "data")
        return Response(r.json())

    def update(self, request, pk=None):  # /api/module/<str:code>
        r = requests.post(URL.BASE_URL + "module/update", data=request.data)
        return Response(r.json())

    def destroy(self, request, pk=None):  # /api/module/<str:code>
        r = requests.get(URL.BASE_URL + "module/" + pk + "/delete")
        return Response(r.json())


class NiveauViewSet(viewsets.ViewSet):
    def list(self, request):  # /api/niveau
        r = requests.get(URL.BASE_URL + "niveau/all")
        return Response(r.json())

    def create(self, request):  # /api/niveau
        r = requests.post(URL.BASE_URL + "niveau/save", data=request.data)
        return Response(r.json())

    def retrieve(self, request, pk=None):  # /api/niveau/<str:code>
        r = requests.get(URL.BASE_URL + "niveau/" + pk + "data")
        return Response(r.json())

    def update(self, request, pk=None):  # /api/niveau/<str:code>
        r = requests.post(URL.BASE_URL + "niveau/update", data=request.data)
        return Response(r.json())

    def destroy(self, request, pk=None):  # /api/niveau/<str:code>
        r = requests.get(URL.BASE_URL + "niveau/" + pk + "/delete")
        return Response(r.json())


class NoteCCViewSet(viewsets.ViewSet):
    def list(self, request):  # /api/note-cc
        r = requests.get(URL.BASE_URL + "notecc/all")
        return Response(r.json())

    def create(self, request):  # /api/note-cc
        r = requests.post(URL.BASE_URL + "notecc/save", data=request.data)
        return Response(r.json())

    def retrieve(self, request, pk=None):  # /api/note-cc/<str:code>
        r = requests.get(URL.BASE_URL + "notecc/" + pk + "data")
        return Response(r.json())

    def update(self, request, pk=None):  # /api/note-cc/<str:code>
        r = requests.post(URL.BASE_URL + "notecc/update", data=request.data)
        return Response(r.json())

    def destroy(self, request, pk=None):  # /api/note-cc/<str:code>
        r = requests.get(URL.BASE_URL + "notecc/" + pk + "/delete")
        return Response(r.json())

@api_view(['GET'])
def search_note_cc_by_candidat_or_type_note_cc(request, candiat, type_note_cc): # type-note-cc/search-type-note-cc-by-enseignement-or-numero_cc/<str:type_note_cc>/<str:filiere>/
    r = requests.get(URL.BASE_URL + "notecc/" + candiat + "/" + type_note_cc + "/recherche")
    return Response(r.json())


class NoteViewSet(viewsets.ViewSet):
    def list(self, request):  # /api/note
        r = requests.get(URL.BASE_URL + "note/all")
        return Response(r.json())

    def create(self, request):  # /api/note
        r = requests.post(URL.BASE_URL + "note/save", data=request.data)
        return Response(r.json())

    def retrieve(self, request, pk=None):  # /api/note/<str:code>
        r = requests.get(URL.BASE_URL + "note/" + pk + "data")
        return Response(r.json())

    def update(self, request, pk=None):  # /api/note/<str:code>
        r = requests.post(URL.BASE_URL + "note/update", data=request.data)
        return Response(r.json())

    def destroy(self, request, pk=None):  # /api/note/<str:code>
        r = requests.get(URL.BASE_URL + "note/" + pk + "/delete")
        return Response(r.json())


class PasswordForgotViewSet(viewsets.ViewSet):
    def list(self, request):  # /api/items
        pass

    def create(self, request):  # /api/items
        pass

    def retrieve(self, request, pk=None):  # /api/items/<str:code>
        pass

    def update(self, request, pk=None):  # /api/items/<str:code>
        pass

    def destroy(self, request, pk=None):  # /api/items/<str:code>
        pass


class PasswordResetViewSet(viewsets.ViewSet):
    def list(self, request):  # /api/items
        pass

    def create(self, request):  # /api/items
        pass

    def retrieve(self, request, pk=None):  # /api/items/<str:code>
        pass

    def update(self, request, pk=None):  # /api/items/<str:code>
        pass

    def destroy(self, request, pk=None):  # /api/items/<str:code>
        pass


# Print

@api_view(['GET'])
def generate_carte_etudiant(request):  # print/generate-carte-etudiant/
    r = requests.get(URL.BASE_URL + "print/generatecarteetudiant")
    return Response(r.json())


@api_view(['GET'])
def generate_attestation(request):  # print/generate-attestation/
    r = requests.get(URL.BASE_URL + "print/generateatestation")
    return Response(r.json())


@api_view(['GET'])
def generate_diplome(request):  # print/generate-diplome/
    r = requests.get(URL.BASE_URL + "print/generatediplome")
    return Response(r.json())


@api_view(['GET'])
def generate_fiche_absence(request):  # print/generate-fiche-absence/
    r = requests.get(URL.BASE_URL + "print/generateficheabsence")
    return Response(r.json())


@api_view(['GET'])
def generate_pv(request):  # print/generate-pv/
    r = requests.get(URL.BASE_URL + "print/generatePv")
    return Response(r.json())


@api_view(['GET'])
def generate_notes(request):  # print/generate-notes/
    r = requests.get(URL.BASE_URL + "print/generateNotes")
    return Response(r.json())


@api_view(['GET'])
def generate_releve_notes(request):  # print/generate-releve-notes/
    r = requests.get(URL.BASE_URL + "print/generateReleve")
    return Response(r.json())


@api_view(['GET'])
def generate_pv_synthese(request):  # print/generate-pv-synthese/
    r = requests.get(URL.BASE_URL + "print/generatePVSynthese")
    return Response(r.json())


@api_view(['GET'])
def generate_certificat_scolarite(request):  # print/generate-certificat-scolarite/
    r = requests.get(URL.BASE_URL + "print/generateCertificat")
    return Response(r.json())


class RoleViewSet(viewsets.ViewSet):
    def list(self, request):  # /api/role
        r = requests.get(URL.BASE_URL + "role/all")
        return Response(r.json())

    def create(self, request):  # /api/role
        r = requests.post(URL.BASE_URL + "role/save", data=request.data)
        return Response(r.json())

    def retrieve(self, request, pk=None):  # /api/role/<str:code>
        pass

    def update(self, request, pk=None):  # /api/role/<str:code>
        r = requests.post(URL.BASE_URL + "role/update", data=request.data)
        return Response(r.json())

    def destroy(self, request, pk=None):  # /api/role/<str:code>
        r = requests.get(URL.BASE_URL + "role/" + pk + "/delete")
        return Response(r.json())


@api_view(['POST'])
def get_all_role_by_user(request):
    r = requests.post(URL.BASE_URL + "/allByUtilisateur", data=request.data)
    return Response(r.json())


class SemestreViewSet(viewsets.ViewSet):
    def list(self, request):  # /api/semestre
        r = requests.get(URL.BASE_URL + "semestre/all")
        return Response(r.json())

    def create(self, request):  # /api/semestre
        r = requests.post(URL.BASE_URL + "semestre/save", data=request.data)
        return Response(r.json())

    def retrieve(self, request, pk=None):  # /api/semestre/<str:code>
        r = requests.get(URL.BASE_URL + "semestre/" + pk + "data")
        return Response(r.json())

    def update(self, request, pk=None):  # /api/semestre/<str:code>
        r = requests.post(URL.BASE_URL + "semestre/update", data=request.data)
        return Response(r.json())

    def destroy(self, request, pk=None):  # /api/semestre/<str:code>
        r = requests.get(URL.BASE_URL + "semestre/" + pk + "/delete")
        return Response(r.json())


@api_view(['GET'])
def search_semestre_by_libelle_or_annee_academique(request, libelle, annee_academique):
    r = requests.get(URL.BASE_URL + "semestre/" + libelle + "/" + annee_academique)
    return Response(r.json())


class SessionViewSet(viewsets.ViewSet):
    def list(self, request):  # /api/session
        r = requests.get(URL.BASE_URL + "session/all")
        return Response(r.json())

    def create(self, request):  # /api/session
        r = requests.post(URL.BASE_URL + "session/save", data=request.data)
        return Response(r.json())

    def retrieve(self, request, pk=None):  # /api/session/<str:code>
        pass

    def update(self, request, pk=None):  # /api/session/<str:code>
        r = requests.post(URL.BASE_URL + "session/update", data=request.data)
        return Response(r.json())

    def destroy(self, request, pk=None):  # /api/session/<str:code>
        r = requests.get(URL.BASE_URL + "session/" + pk + "/delete")
        return Response(r.json())


class SmsViewSet(viewsets.ViewSet):
    def list(self, request):  # /api/sms
        r = requests.get(URL.BASE_URL + "sms/all")
        return Response(r.json())

    def create(self, request):  # /api/sms
        r = requests.post(URL.BASE_URL + "sms/save", data=request.data)
        return Response(r.json())

    def retrieve(self, request, pk=None):  # /api/sms/<str:code>
        pass

    def update(self, request, pk=None):  # /api/sms/<str:code>
        r = requests.post(URL.BASE_URL + "sms/update", data=request.data)
        return Response(r.json())

    def destroy(self, request, pk=None):  # /api/sms/<str:code>
        r = requests.get(URL.BASE_URL + "sms/" + pk + "/delete")
        return Response(r.json())


class SpecialiteViewSet(viewsets.ViewSet):
    def list(self, request):  # /api/specialite
        r = requests.get(URL.BASE_URL + "specialite/all")
        return Response(r.json())

    def create(self, request):  # /api/specialite
        r = requests.post(URL.BASE_URL + "specialite/save", data=request.data)
        return Response(r.json())

    def retrieve(self, request, pk=None):  # /api/specialite/<str:code>
        pass

    def update(self, request, pk=None):  # /api/specialite/<str:code>
        r = requests.post(URL.BASE_URL + "specialite/update", data=request.data)
        return Response(r.json())

    def destroy(self, request, pk=None):  # /api/specialite/<str:code>
        r = requests.get(URL.BASE_URL + "specialite/" + pk + "/delete")
        return Response(r.json())


@api_view(['GET'])
def search_specialite_by_specialite_or_filiere(request, specialite, filiere): #  specialite/search-specialite-by-specialite-or-filiere/<str:specialite>/<str:filiere>/
    r = request.get(URL.BASE_URL + "specialite/" + specialite + "/" + filiere + "/recherche")
    return Response(r.json())


class TypeEvaluationViewSet(viewsets.ViewSet):
    def list(self, request):  # /api/type-evaluation
        r = requests.get(URL.BASE_URL + "type-evaluation/all")
        return Response(r.json())

    def create(self, request):  # /api/type-evaluation
        r = requests.post(URL.BASE_URL + "type-evaluation/save", data=request.data)
        return Response(r.json())

    def retrieve(self, request, pk=None):  # /api/type-evaluation/<str:code>
        r = requests.get(URL.BASE_URL + "type-evaluation/" + pk + "data")
        return Response(r.json())

    def update(self, request, pk=None):  # /api/type-evaluation/<str:code>
        r = requests.post(URL.BASE_URL + "type-evaluation/update", data=request.data)
        return Response(r.json())

    def destroy(self, request, pk=None):  # /api/type-evaluation/<str:code>
        r = requests.get(URL.BASE_URL + "type-evaluation/" + pk + "/delete")
        return Response(r.json())


class TypeNoteCCViewSet(viewsets.ViewSet):
    def list(self, request):  # /api/type-note-cc
        r = requests.get(URL.BASE_URL + "TypeNoteCC/all")
        return Response(r.json())

    def create(self, request):  # /api/type-note-cc
        r = requests.post(URL.BASE_URL + "TypeNoteCC/save", data=request.data)
        return Response(r.json())

    def retrieve(self, request, pk=None):  # /api/type-note-cc/<str:code>
        pass

    def update(self, request, pk=None):  # /api/type-note-cc/<str:code>
        r = requests.post(URL.BASE_URL + "TypeNoteCC/update", data=request.data)
        return Response(r.json())

    def destroy(self, request, pk=None):  # /api/type-note-cc/<str:code>
        r = requests.get(URL.BASE_URL + "TypeNoteCC/" + pk + "/delete")
        return Response(r.json())


@api_view(['GET'])
def search_type_note_cc_by_enseignement_or_numero_cc(request, type_note_cc, filiere):
    r = requests.get(URL.BASE_URL + "TypeNoteCC/" + type_note_cc + "/" + filiere + "/recherche")
    return Response(r.json())


class UEViewSet(viewsets.ViewSet):
    def list(self, request):  # /api/ue
        r = requests.get(URL.BASE_URL + "ue/all")
        return Response(r.json())

    def create(self, request):  # /api/ue
        r = requests.post(URL.BASE_URL + "ue/save", data=request.data)
        return Response(r.json())

    def retrieve(self, request, pk=None):  # /api/ue/<str:code>
        r = requests.get(URL.BASE_URL + "ue/" + pk + "data")
        return Response(r.json())

    def update(self, request, pk=None):  # /api/ue/<str:code>
        r = requests.post(URL.BASE_URL + "ue/update", data=request.data)
        return Response(r.json())

    def destroy(self, request, pk=None):  # /api/ue/<str:code>
        r = requests.get(URL.BASE_URL + "ue/" + pk + "/delete")
        return Response(r.json())


class UtilisateurViewSet(viewsets.ViewSet):
    def list(self, request):  # /api/utilisateur
        r = requests.get(URL.BASE_URL + "utilisateur/all")
        return Response(r.json())

    def create(self, request):  # /api/utilisateur
        r = requests.post(URL.BASE_URL + "utilisateur/save", data=request.data)
        return Response(r.json())

    def retrieve(self, request, pk=None):  # /api/utilisateur/<str:code>
        r = requests.get(URL.BASE_URL + "utilisateur/" + pk + "data")
        return Response(r.json())

    def update(self, request, pk=None):  # /api/utilisateur/<str:code>
        r = requests.post(URL.BASE_URL + "utilisateur/update", data=request.data)
        return Response(r.json())

    def destroy(self, request, pk=None):  # /api/utilisateur/<str:code>
        r = requests.get(URL.BASE_URL + "utilisateur/" + pk + "/delete")
        return Response(r.json())


@api_view(['POST'])
def login(request): # utilisateur/login/
    r = requests.post(URL.BASE_URL + "utilisateur/login", data=request.data)
    return Response(r.json())


@api_view(['POST'])
def deconnect(request): # utilisateur/deconnect/
    r = requests.post(URL.BASE_URL + "utilisateur/deconnect", data=request.data)
    return Response(r.json())


@api_view(['POST'])
def roles_utilisateur(request): # utilisateur/roles-utilisateur/
    r = requests.post(URL.BASE_URL + "utilisateur/rolesuser", data=request.data)
    return Response(r.json())
