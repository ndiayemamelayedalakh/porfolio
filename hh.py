 curseur = connexion.cursor()
    # Requête pour obtenir le nombre total d'incidents où l'arme est connue
    req = """SELECT count(id_incident) AS statut_connu FROM details_incidents 
              WHERE arme is NOT NULL AND arme != "undetermined";
          """
    curseur.execute(req)
    total_connu = dict(curseur.fetchone())
    # Requête pour obtenir le nombre d'incidents où la victime est non armée
    req = """
            SELECT count(id_incident) AS vict_non_armee FROM details_incidents
            WHERE arme = "unarmed" AND arme is NOT NULL;
          """
    curseur.execute(req)
    non_armee = dict(curseur.fetchone())
    # Calcul des pourcentages des  personnes armees ou non
    if total_connu['statut_connu'] != 0:  # Verifie si le nbre total de victime est différent de 0
        prct_non_armee = round(non_armee['vict_non_armee']*100 / total_connu['statut_connu'], 2)
        prct_armee = 100 - prct_non_armee
    else:
        prct_non_armee = 0
        prct_armee = 0
    resultats = {} # Variable qui va contenir le resultat
    resultats['armee'] = prct_armee
    resultats['non_armee'] = prct_non_armee
    
    return resultats