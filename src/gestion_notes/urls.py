from django.urls import path

from .views import *

map_many = {'get': 'list', 'post': 'create'}
map_one = {'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}

urlpatterns = [
    # Année Academique
    path('annee-academique', AnneAcademiqueViewSet.as_view(map_many)),
    path('annee-academique/<str:pk>', AnneAcademiqueViewSet.as_view(map_one)),

    # Anonymat
    path('anonymat', AnonymatViewSet.as_view(map_many)),
    path('anonymat/<str:pk>', AnonymatViewSet.as_view(map_one)),

    # Candidat
    path('candidat', CandidatViewSet.as_view(map_many)),
    path('candidat/<str:pk>', CandidatViewSet.as_view(map_one)),

    # Classe
    path('classe', ClasseViewSet.as_view(map_many)),
    path('classe/<str:pk>', ClasseViewSet.as_view(map_one)),

    # Discipline
    path('discipline', DiscipineViewSet.as_view(map_many)),
    path('discipline/<str:pk>', DiscipineViewSet.as_view(map_one)),

    # Droit
    path('droit', DroitViewSet.as_view(map_many)),
    path('droit/<str:pk>', DroitViewSet.as_view(map_one)),

    # Email
    path('email', EmailViewSet.as_view(map_many)),
    path('email/<str:pk>', EmailViewSet.as_view(map_one)),

    # Enseignant
    path('enseignant', EnseignantViewSet.as_view(map_many)),
    path('enseignant/<str:pk>', EnseignantViewSet.as_view(map_one)),

    # Enseignement
    path('enseignement', EnseignementViewSet.as_view(map_many)),
    path('enseignement/<str:pk>', EnseignementViewSet.as_view(map_one)),

    # EnvoiMessage
    path('envoi-message', EnvoiMessageViewSet.as_view(map_many)),
    path('envoi-message/<str:pk>', EnvoiMessageViewSet.as_view(map_one)),

    # Est Inscrit
    path('est-inscrit', EstInscritViewSet.as_view(map_many)),
    path('est-inscrit/<str:pk>', EstInscritViewSet.as_view(map_one)),

    # Etudiant
    path('etudiant', EtudiantViewSet.as_view(map_many)),
    path('etudiant/<str:pk>', EtudiantViewSet.as_view(map_one)),

    # Evaluation
    path('evaluation', EvaluationViewSet.as_view(map_many)),
    path('evaluation/<str:pk>', EvaluationViewSet.as_view(map_one)),

    # Filière
    path('filiere', FiliereViewSet.as_view(map_many)),
    path('filiere/<str:pk>', FiliereViewSet.as_view(map_one)),

    # Historique Note
    path('historique-note', HistoriqueNoteViewSet.as_view(map_many)),
    path('historique-note/<str:pk>', HistoriqueNoteViewSet.as_view(map_one)),

    # Message
    path('message', MessageViewSet.as_view(map_many)),
    path('message/<str:pk>', MessageViewSet.as_view(map_one)),

    # Module
    path('module', ModuleViewSet.as_view(map_many)),
    path('module/<str:pk>', ModuleViewSet.as_view(map_one)),

    # Niveau
    path('niveau', NiveauViewSet.as_view(map_many)),
    path('niveau/<str:pk>', NiveauViewSet.as_view(map_one)),

    # Note CC
    path('note-cc', NoteCCViewSet.as_view(map_many)),
    path('note-cc/<str:pk>', NoteCCViewSet.as_view(map_one)),

    # Note
    path('note', NoteViewSet.as_view(map_many)),
    path('note/<str:pk>', NoteViewSet.as_view(map_one)),

    # Pasword Forgot
    path('password-forgot', PasswordForgotViewSet.as_view(map_many)),
    path('password-forgot/<str:pk>', PasswordForgotViewSet.as_view(map_one)),

    # Password Reset
    path('password-reset', PasswordResetViewSet.as_view(map_many)),
    path('password-reset/<str:pk>', PasswordResetViewSet.as_view(map_one)),

    # Print
    path('print', PrintViewSet.as_view(map_many)),
    path('print/<str:pk>', PrintViewSet.as_view(map_one)),

    # Role
    path('role', RoleViewSet.as_view(map_many)),
    path('role/<str:pk>', RoleViewSet.as_view(map_one)),

    # Semestre
    path('semestre', SemestreViewSet.as_view(map_many)),
    path('semestre/<str:pk>', SemestreViewSet.as_view(map_one)),

    # Session
    path('session', SessionViewSet.as_view(map_many)),
    path('session/<str:pk>', SessionViewSet.as_view(map_one)),

    # Sms
    path('sms', SmsViewSet.as_view(map_many)),
    path('sms/<str:pk>', SmsViewSet.as_view(map_one)),

    # Specialité
    path('specialite', SpecialiteViewSet.as_view(map_many)),
    path('specialite/<str:pk>', SpecialiteViewSet.as_view(map_one)),

    # Type Evaluation
    path('type-evaluation', TypeEvaluationViewSet.as_view(map_many)),
    path('type-evaluation/<str:pk>', TypeEvaluationViewSet.as_view(map_one)),

    # Type Note CC
    path('type-note-cc', TypeNoteCCViewSet.as_view(map_many)),
    path('type-note-cc/<str:pk>', TypeNoteCCViewSet.as_view(map_one)),

    # UE
    path('ue', UEViewSet.as_view(map_many)),
    path('ue/<str:pk>', UEViewSet.as_view(map_one)),

    # Utilisateur
    path('utilisateur', UtilisateurViewSet.as_view(map_many)),
    path('utilisateur/<str:pk>', UtilisateurViewSet.as_view(map_one)),
]
