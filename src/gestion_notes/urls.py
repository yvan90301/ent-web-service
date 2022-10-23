from django.urls import path

from .views import *

map_many = {'get': 'list', 'post': 'create'}
map_one = {'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}

urlpatterns = [
    # Année Academique
    path('annee-academique/', AnneAcademiqueViewSet.as_view(map_many)),
    path('annee-academique/<str:pk>/', AnneAcademiqueViewSet.as_view(map_one)),

    # Anonymat
    path('anonymat/', AnonymatViewSet.as_view(map_many)),
    path('anonymat/<str:pk>/', AnonymatViewSet.as_view(map_one)),

    # Candidat
    path('candidat/', CandidatViewSet.as_view(map_many)),
    path('candidat/<str:pk>/', CandidatViewSet.as_view(map_one)),

    # Classe
    path('classe/', ClasseViewSet.as_view(map_many)),
    path('classe/<str:pk>/', ClasseViewSet.as_view(map_one)),

    # Discipline
    path('discipline/', DiscipineViewSet.as_view(map_many)),
    path('discipline/<str:pk>/', DiscipineViewSet.as_view(map_one)),
    path('discipline/search-discipline-by-etudiant-or-semestre-or_date/<str:etudiant>/<str:semestre>/<str:date_retard>/', search_discipline_by_etudiant_or_semestre_or_date),

    # Droit
    path('droit/', DroitViewSet.as_view(map_many)),
    path('droit/<str:pk>/', DroitViewSet.as_view(map_one)),

    # Email
    path('email/', EmailViewSet.as_view(map_many)),
    path('email/<str:pk>/', EmailViewSet.as_view(map_one)),

    # Enseignant
    path('enseignant/', EnseignantViewSet.as_view(map_many)),
    path('enseignant/<str:pk>/', EnseignantViewSet.as_view(map_one)),

    # Enseignement
    path('enseignement/', EnseignementViewSet.as_view(map_many)),
    path('enseignement/<str:pk>/', EnseignementViewSet.as_view(map_one)),

    # EnvoiMessage
    path('envoi-message/', EnvoiMessageViewSet.as_view(map_many)),
    path('envoi-message/<str:pk>/', EnvoiMessageViewSet.as_view(map_one)),

    # Est Inscrit
    path('est-inscrit/', EstInscritViewSet.as_view(map_many)),
    path('est-inscrit/<str:pk>/', EstInscritViewSet.as_view(map_one)),

    # Etudiant
    path('etudiant/', EtudiantViewSet.as_view(map_many)),
    path('etudiant/<str:pk>/', EtudiantViewSet.as_view(map_one)),
    path('etudiant/get-etudiant-by-matricule/<str:matricule>/', get_etudiant_by_matricule),

    # Evaluation
    path('evaluation/', EvaluationViewSet.as_view(map_many)),
    path('evaluation/<str:pk>/', EvaluationViewSet.as_view(map_one)),
    path('evaluation/search-type-evaluation/<str:pk>/', search_type_evaluation),
    path('evaluation/search-type-etudiant/<str:type_ev>/<str:code_ue>/', search_type_etudiant),

    # Filière
    path('filiere/', FiliereViewSet.as_view(map_many)),
    path('filiere/<str:pk>/', FiliereViewSet.as_view(map_one)),
    path('filiere/<str:libele_filiere>/', get_note_by_libelle_filiere),

    # Historique Note
    path('historique-note/', HistoriqueNoteViewSet.as_view(map_many)),
    path('historique-note/<str:pk>/', HistoriqueNoteViewSet.as_view(map_one)),

    # Message
    path('message/', MessageViewSet.as_view(map_many)),
    path('message/<str:pk>/', MessageViewSet.as_view(map_one)),

    # Module
    path('module/', ModuleViewSet.as_view(map_many)),
    path('module/<str:pk>/', ModuleViewSet.as_view(map_one)),

    # Niveau
    path('niveau/', NiveauViewSet.as_view(map_many)),
    path('niveau/<str:pk>/', NiveauViewSet.as_view(map_one)),

    # Note CC
    path('note-cc/', NoteCCViewSet.as_view(map_many)),
    path('note-cc/<str:pk>/', NoteCCViewSet.as_view(map_one)),
    path('note-cc/search-note-cc-by-candidat-or-type-note-cc/<str:candidat>/<str:type_note_cc>/', search_note_cc_by_candidat_or_type_note_cc),

    # Note
    path('note/', NoteViewSet.as_view(map_many)),
    path('note/<str:pk>/', NoteViewSet.as_view(map_one)),

    # Pasword Forgot
    path('password-forgot/', PasswordForgotViewSet.as_view(map_many)),
    path('password-forgot/<str:pk>/', PasswordForgotViewSet.as_view(map_one)),

    # Password Reset
    path('password-reset/', PasswordResetViewSet.as_view(map_many)),
    path('password-reset/<str:pk>/', PasswordResetViewSet.as_view(map_one)),

    # Print
    path('print/generate-carte-etudiant/', generate_carte_etudiant),
    path('print/generate-attestation/', generate_attestation),
    path('print/generate-diplome/', generate_diplome),
    path('print/generate-fiche-absence/', generate_fiche_absence),
    path('print/generate-pv/', generate_pv),
    path('print/generate-notes/', generate_notes),
    path('print/generate-releve-notes/', generate_releve_notes),
    path('print/generate-pv-synthese/', generate_pv_synthese),
    path('print/generate-certificat-scolarite/', generate_certificat_scolarite),

    # Role
    path('role/', RoleViewSet.as_view(map_many)),
    path('role/<str:pk>/', RoleViewSet.as_view(map_one)),
    path('role/get-all-role-by-user/', get_all_role_by_user),

    # Semestre
    path('semestre/', SemestreViewSet.as_view(map_many)),
    path('semestre/<str:pk>/', SemestreViewSet.as_view(map_one)),
    path('search-semestre-by-libelle-or-annee-academique/<str:libelle>/<str:annee_academique>/', search_semestre_by_libelle_or_annee_academique),

    # Session
    path('session/', SessionViewSet.as_view(map_many)),
    path('session/<str:pk>/', SessionViewSet.as_view(map_one)),

    # Sms
    path('sms/', SmsViewSet.as_view(map_many)),
    path('sms/<str:pk>/', SmsViewSet.as_view(map_one)),

    # Specialité
    path('specialite/', SpecialiteViewSet.as_view(map_many)),
    path('specialite/<str:pk>/', SpecialiteViewSet.as_view(map_one)),
    path('specialite/search-specialite-by-specialite-or-filiere/<str:specialite>/<str:filiere>/', search_specialite_by_specialite_or_filiere),

    # Type Evaluation
    path('type-evaluation/', TypeEvaluationViewSet.as_view(map_many)),
    path('type-evaluation/<str:pk>/', TypeEvaluationViewSet.as_view(map_one)),

    # Type Note CC
    path('type-note-cc/', TypeNoteCCViewSet.as_view(map_many)),
    path('type-note-cc/<str:pk>/', TypeNoteCCViewSet.as_view(map_one)),
    path('type-note-cc/search-type-note-cc-by-enseignement-or-numero_cc/<str:type_note_cc>/<str:filiere>/', search_type_note_cc_by_enseignement_or_numero_cc),

    # UE
    path('ue/', UEViewSet.as_view(map_many)),
    path('ue/<str:pk>/', UEViewSet.as_view(map_one)),

    # Utilisateur
    path('utilisateur/', UtilisateurViewSet.as_view(map_many)),
    path('utilisateur/<str:pk>/', UtilisateurViewSet.as_view(map_one)),
    path('utilisateur/login/', login),
    path('utilisateur/deconnect/', deconnect),
    path('utilisateur/roles-utilisateur/', roles_utilisateur),
]
