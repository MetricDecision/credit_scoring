import streamlit as st
import pandas as pd
import numpy as np



st.sidebar.image('metrics.png', use_column_width=True)

st.sidebar.title("Application de Credit Scoring")

pages = ["Présentation de la méthodologie", "Détermination du score d'un client"]

page = st.sidebar.radio("", pages)

if page == pages[0]:
    st.markdown('<h1 style="color: #093A48;">Présentation de la méthodologie</h1>', unsafe_allow_html=True)
    #st.title(pages[0])

    st.markdown('<h3 style="color: #1482A0;">1. Définition Credit Scoring</h3>', unsafe_allow_html=True)
    texte3 = "Le scoring de crédit est une méthode utilisée pour prédire la probabilité que les demandeurs de crédit ou les emprunteurs existants fassent défaut ou se révèlent être des mauvais payeurs."
    st.write(f'<div style="text-align: justify;">{texte3}</div>', unsafe_allow_html=True)
    texte4 = "Sur cette base, une évaluation numérique de la solvabilité est déterminée. Plus la valeur est élevée, plus la probabilité de défaut de remboursement par une personne donnée est faible et inversement."
    st.write(f'<div style="text-align: justify;">{texte4}</div>', unsafe_allow_html=True)
    st.image('score.jpg')


    st.markdown('<h3 style="color: #1482A0;">2. Dictionnaire des variables</h3>', unsafe_allow_html=True)

    st.write("Le modèle a été entraîné à partir d'une base de données historique portant sur 1000 clients et constituée de 10 variables. Ci-après la description de ces variables :")
    
    donnees = [
    ['Variable', 'Sens', 'Valeurs possibles'],
    ['Age', 'Age du client', 'Entre 19 et 75 ans'],
    ['Sexe', 'Sexe du client', 'Masculin, Féminin'],
    ['Emploi', 'Le type d\'emploi du client','Non qualifié et non résident, Non qualifié et résident, Qualifié, Très qualifié' ],
    ['Logement', 'Statut de logement', 'Propriétaire, Location, Gratuit'],
    ['Epargne', 'Type du compte d\'épargne', 'Peu, Modéré, Assez riche, Riche'],
    ['Courant', 'Type du compte courant', 'Peu, Modéré, Riche'],
    ['Montant', 'Montant du crédit', 'Numérique'],
    ['Durée' , 'Durée du crédit', 'En mois'],
    ['But ', 'Le but du crédit', 'Voiture, Mobilier/Equipement, Radio/TV, Appareils électroménagers, Réparations, Education, Affaires, Vacances/Autres'],
    ['Risque','Statut du client', 'Bon, Mauvais'] ]

    data = pd.DataFrame(donnees[1:], columns=donnees[0])
    data = data.reset_index(drop=True)
    st.dataframe(data= data, hide_index=True, use_container_width=False)

    st.markdown('<h3 style="color: #1482A0;">3. Description de la méthode</h3>', unsafe_allow_html=True)
    #st.write("La méthode WOE (Weight of Evidence) et l'IV (Information Value) sont des techniques utilisées en modélisation de crédit pour évaluer la relation entre les variables explicatives et la variable cible (dans ce cas, le statut du client).")
    #st.write("L'IV, agrège l'efficacité prédictive de chaque catégorie de variable explicative en calculant la somme pondérée des différences entre les taux de succès et d'échecs pour chaque catégorie. Une IV plus élevée indique une variable explicative plus prédictive du statut de la décision de crédit.")
    #st.image('iv.webp')

    texte1 = "Dans ce projet, la méthode WOE est appliquée pour transformer les variables explicatives afin qu'elles soient plus informatives pour la modélisation de crédit. Cela implique de regrouper les valeurs des variables continues en intervalles et de calculer le WOE pour chaque intervalle."
    st.write(f'<div style="text-align: justify;">{texte1}</div>', unsafe_allow_html=True)
    st.image('woe.webp', use_column_width=True)
    #image = 'score.jpg'
    #st.markdown(f'<div style="display: flex; justify-content: center;">' f'<img src="score.jpg" style="width: 50%;">' f'</div>', unsafe_allow_html=True)

    texte2 = "Nous utilisons la regression logistique pour modéliser le risque de crédit des clients. La régression logistique est un algorithme d'apprentissage automatique supervisé. Il s'agit d'une régression binomiale utilisée pour prédire le statut d'une décision de crédit en fonction de variables sélectionnées. Elle est souvent présentée sous forme d\'une fonction de probabilité sigmoïde sur l\'intervalle 0-1."
    st.write(f'<div style="text-align: justify;">{texte2}</div>', unsafe_allow_html=True)


if page == pages[1]:
    st.markdown("<h1 style='color: #093A48;'>Détermination du score d'un client</h1>", unsafe_allow_html=True)
    #st.title(pages[1])

    model = pd.read_csv('scorecard.csv')
    score = 0

    # Ligne 1
    col1, col2 = st.columns([1, 1])
    with col1:
        # Age
        age = st.number_input("L'âge du client :", step=1)
    with col2:
        # Sexe de la personne
        Response1 = st.selectbox(label = "Quel est le sexe du client ?", options = ['Femme', 'Homme'])
        if Response1 == 'Femme' :
            sexe = 'female'
        elif Response1 == 'Homme' :
            sexe = 'male'

    # Ligne 2
    col1, col2 = st.columns([1, 1])
    with col1:
        # Emploi
        Response2 = st.selectbox(label = "Quel est l'emploi du client ?", options = ['Non qualifié et non résident', 'Non qualifié et résident', 'Qualifié', 'Très qualifié'])
        if Response2 == 'Non qualifié et non résident' :
            job = 0
        elif Response2 == 'Non qualifié et résident' :
            job = 1
        elif Response2 == 'Qualifié' :
            job = 2
        elif Response2 == 'Très qualifié' :
            job = 3
    with col2:
        # Logement
        Response3 = st.selectbox(label = "Quel est le type de logement du client ?", options = ['Propriétaire', 'Location', 'Gratuit'])
        if Response3 == 'Propriétaire' :
            housing = 'own'
        elif Response3 == 'Location' :
            housing = 'rent'
        elif Response3 == 'Gratuit' :
            housing = 'free'

    # Ligne 3
    col1, col2 = st.columns([1, 1])
    with col1:
        # Saving Accounts
        Response4 = st.selectbox(label = "Quel est le type de comptes d'épargne du client ?", options = ['Peu', 'Modéré', 'Assez riche', 'Riche'])
        if Response4 == 'Peu' :
            sav_account = 'little'
        elif Response4 == 'Modéré' :
            sav_account = 'moderate'
        elif Response4 == 'Assez riche' :
            sav_account = 'quite rich'
        elif Response4 == 'Riche' :
            sav_account = 'rich'
    with col2:
        # Cheking Account
        Response5 = st.selectbox(label = "Quel est le type de comptes d'épargne du client ?", options = ['Peu', 'Modéré', 'Riche'])
        if Response5 == 'Peu' :
            check_account = 'little'
        elif Response5 == 'Modéré' :
            check_account = 'moderate'
        elif Response5 == 'Riche' :
            check_account = 'rich'

    # Ligne 4
    col1, col2 = st.columns([1, 1])
    with col1:
        # Montant du Credit
        credi_amount = st.number_input("Le montant du crédit du client : (K FCFA)", step=1)
    with col2:
        # Durée
        duration = st.number_input("La durée du crédit : (En mois)", step=1)

    # But
    Response6 = st.selectbox(label = "Quel est le but du client ?", options = ['Voiture', 'Mobilier/Equipement', 'Radio/TV', 'Appareils électroménagers', 'Réparations', 'Education', 'Affaires', 'Vacances/Autres'])
    if Response6 == 'Voiture' :
        purpose = 'car'
    elif Response6 == 'Mobilier/Equipement' :
        purpose = 'furniture/equipment'
    elif Response6 == 'Radio/TV' :
        purpose = 'radio/TV'
    elif Response6 == 'Appareils électroménagers' :
        purpose = 'domestic appliances'
    elif Response6 == 'Réparations' :
        purpose = 'repairs'
    elif Response6 == 'Education' :
        purpose = 'education'
    elif Response6 == 'Affaires' :
        purpose = 'business'
    elif Response6 == 'Vacances/Autres' :
        purpose = 'vacation/others'


    # Création des fonctions
    def variable_str(valeur) :
        score_str =  0
        score_str = score_str + model.loc[model['MAX_VALUE'] == valeur, 'SCORE'].values[0]
        return score_str

    def variable_num(nom_lign, valeur) :
        data = model.loc[model['VAR_NAME'] == nom_lign]

        score_num = 0
        for index, row in data.iterrows() :
            if valeur >= int(row['MIN_VALUE'])   and valeur <= int(row['MAX_VALUE']) :
                score_num = 0
                score_num = score_num + row['SCORE']
        return score_num
                
    # Calcul du Score
    score = score + variable_str(housing)
    score = score + variable_str(sav_account)
    score = score + variable_str(check_account)
    score = score + variable_str(purpose)

    score = score + variable_num("Age", age)
    score = score + variable_num("Job", job)
    score = score + variable_num("Credit amount", credi_amount)
    score = score + variable_num("Duration", duration)


    if(st.button("Obtenir les résultats")):
        if score <= 516.8061340914082 :
            st.error("Le score de ce client est : {}  \n".format(score) + "Ce score de crédit indique un risque élevé de défaut de paiement. Il est déconseillé d'octroyer du crédit à ce type de client.")
        elif score <= 528.2333808895181 :
            st.warning("Le score de ce client est : {}  \n".format(score) + "Ce score de crédit suggère un risque modéré de défaut de paiement. Des mesures préventives sont fortement recommandées.")
        elif score <= 540.1701409059169 :
            st.success("Le score de ce client est : {}  \n".format(score) + "Ce score de crédit indique un risque relativement faible de défaut de paiement. Les prêts peuvent être accordés avec confiance.")
        elif score >= 540.1701409059169 :
            st.success("Le score de ce client est : {}  \n".format(score) + "Ce score de crédit suggère un risque très faible de défaut de paiement. Cet emprunteur est très fiable.")


#
