
import joblib
import numpy as np

# Charger le modèle
model = joblib.load("best_crop_yield_model_RandomForest.joblib")

# Exemple d'entrée: Fertilizer, temp, N, P, K
X_new = np.array([[100, 27, 80, 24, 20]], dtype=float)

# Prédiction
y_pred = model.predict(X_new)
print("Rendement prédit:", float(y_pred[0]))
