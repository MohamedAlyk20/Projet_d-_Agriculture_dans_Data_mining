# Projet_d-_Agriculture_dans_Data_mining
Ce projet vise la prévision du rendement des cultures à l'aide du sol et de la météo à partir d’un jeu de données intégrant des variables clés telles que l’apport en engrais, la température et la composition du sol (azote, phosphore et potassium)

Ce projet a été realisé par :
1- Mohamed Aly KOUYATE; 

2- André KPOMY; 

3- Amé Ethiam Godwin Gozo; 

4- Bréma SIDIBE; 

5- Oumar COULIBALY et 

6- Mamadou DIABY 

# 🌱 Projet Agriculture

##  Table des matières
1. [Introduction](#introduction)
2. [Objectifs du projet](#objectifs-du-projet)
3. [Données utilisées](#données-utilisées)
4. [Méthodologie](#méthodologie)
5. [Résultats](#résultats)
6. [Installation et utilisation](#installation-et-utilisation)
7. [Structure du projet](#structure-du-projet)
8. [Perspectives](#perspectives)
9. [Auteur](#auteur)

---

##  Introduction
Ce projet a pour objectif d’analyser et de prédire les **rendements agricoles** à partir de données agronomiques (fertilisation, nutriments, température, etc.) en utilisant des méthodes de **machine learning**.  

---

##  Objectifs du projet
- Explorer et comprendre la relation entre fertilisation, climat et rendement.  
- Mettre en œuvre plusieurs modèles de prédiction (Régression Linéaire, Random Forest, Gradient Boosting).  
- Comparer leurs performances avec des métriques adaptées (MAE, RMSE, R²).  
- Proposer une base pour une future application de prédiction du rendement agricole.  

---

##  Données utilisées
- Source : fichier `.csv` contenant des données agricoles simulées/réelles.  
- Variables principales :  
  - `Fertilizer` (engrais appliqué)  
  - `Temp` (température)  
  - `N`, `P`, `K` (nutriments azote, phosphore, potassium)  
  - `Yield` (rendement observé)  

---

## 🛠Méthodologie
1. Prétraitement des données : nettoyage, gestion des valeurs manquantes, normalisation.  
2. Séparation en **train/test**.  
3. Entraînement des modèles suivants :  
   - Régression Linéaire  
   - Random Forest  
   - Gradient Boosting  
4. Évaluation avec les métriques :  
   - **MAE** (Mean Absolute Error)  
   - **MSE** (Mean Squared Error)  
   - **RMSE** (Root Mean Squared Error)  
   - **R²** (Coefficient de détermination)  
5. Visualisation des performances avec **matplotlib** et **seaborn**.  

---

## Résultats

###  Résumé des performances
- **Random Forest**  
  - MAE : 0.1247  
  - RMSE : 0.1929  
  - R² : 0.9901  (meilleur modèle)  

- **Gradient Boosting**  
  - MAE : 0.2008  
  - RMSE : 0.2803  
  - R² : 0.9791  

- **Régression Linéaire**  
  - MSE: 0.5162
  - RMSE: 0.7185
  - R²: 0.8626
  - Moins performante par rapport aux modèles d’ensemble.  

➡ Le modèle **Random Forest** est celui qui capture le mieux la variabilité des données et offre les prédictions les plus fiables.  

##  Conclusion

Ce projet a permis de démontrer la pertinence des méthodes de **machine learning** pour la prédiction des rendements agricoles. L’évaluation comparative a mis en évidence que le modèle **Random Forest** surpasse les autres approches, avec un coefficient de détermination (**R² ≈ 0.99**) indiquant une excellente capacité de généralisation. Cette performance montre que l’utilisation de variables telles que la fertilisation, les nutriments et la température constitue une base solide pour la modélisation des rendements.

En revanche, la régression linéaire s’est révélée moins adaptée, confirmant que la relation entre les variables agronomiques et le rendement est **non linéaire et complexe**.

---

##  Perspectives

Pour aller plus loin, plusieurs pistes d’amélioration peuvent être envisagées :

1. **Enrichissement des données** : inclure d’autres variables (humidité du sol, pluviométrie, type de sol, pratiques culturales).
2. **Extension géographique** : tester le modèle sur des données provenant de différentes régions/pays pour valider sa robustesse.
3. **Méthodes avancées** : explorer des approches de **Deep Learning** (réseaux de neurones, LSTM pour séries temporelles) afin de capturer la dynamique saisonnière.
4. **Application pratique** : développer une **interface web ou mobile** permettant aux agriculteurs de prédire le rendement en fonction de leurs intrants.
5. **Intégration avec IoT** : connecter le modèle à des capteurs agricoles (température, humidité, fertilité du sol) pour des prédictions en temps réel.

