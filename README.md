**Petite application Flask** très simple, avec une route `/data` qui simule une opération coûteuse (ex: une requête lente ou un calcul lourd). On va comparer :

* 🔁 **Sans cache Redis**
* ⚡ **Avec cache Redis**

---

## 📦 Prérequis

Avant de lancer l’application, installe les dépendances :

```bash
pip install -r requirements.txt
```

Et démarre Redis via Docker) :

```bash
bash redis.sh
```

## 🚀 Test de performance

1. Lance l’app :

```bash
python app.py
```

2. Appelle ces URL dans ton navigateur ou avec `curl` :

```bash
curl http://localhost:5000/data_nocache
curl http://localhost:5000/data_cache
```

---

## 📊 Résultats attendus

| Route appelée   | Temps de réponse (1er appel) | Temps de réponse (2e appel) |
| --------------- | ---------------------------- | --------------------------- |
| `/data_nocache` | \~3 secondes                 | \~3 secondes                |
| `/data_cache`   | \~3 secondes                 | ✅ \~0.005 seconde           |

➡️ **Gain de +99% en rapidité** dès le 2e appel.

---

## ✅ À retenir

* Redis est extrêmement efficace pour éviter des traitements répétitifs.
* Il suffit d’un `cache.get()` et `cache.setex()` pour gagner beaucoup de perf.
* Parfait pour des API, pages de stats, dashboard, etc.
