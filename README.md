# 🤝 Parrainage ESP — application Streamlit

![Python](https://img.shields.io/badge/Python-3776ab?style=flat-square&logo=python&logoColor=white) ![Streamlit](https://img.shields.io/badge/Streamlit-ff4b4b?style=flat-square&logo=streamlit&logoColor=white) ![MySQL](https://img.shields.io/badge/MySQL-4479a1?style=flat-square&logo=mysql&logoColor=white)

Application web de parrainage entre étudiants de l'ESP : les anciens (parrains) et les nouveaux (filleuls) s'inscrivent, puis un administrateur lance l'appariement.

## Fonctionnalités

- Inscription des parrains et des filleuls, connexion
- Listes des inscrits
- Appariement aléatoire parrain ↔ filleul, enregistré en base
- Espace administrateur (réinitialisation des correspondances)

## Structure

```
parrainage/
├── app.py          point d'entrée et navigation
├── inscription.py  connexion.py  liste.py
├── matching.py     appariement parrain ↔ filleul
├── admin.py        ajouter_admin.py
├── db.py           connexion MySQL
└── parrainnage.sql correspondances.sql
```

## Lancer

```bash
pip install streamlit mysql-connector-python pandas
# importer parrainage/parrainnage.sql dans MySQL (base « parainnage »)
cd parrainage && streamlit run app.py
```

---

<p align="center">Réalisé par <a href="https://github.com/Moussa-Ndioukh-Faye"><b>Moussa Ndioukh Faye</b></a> · École Supérieure Polytechnique de Dakar (ESP/UCAD)</p>
