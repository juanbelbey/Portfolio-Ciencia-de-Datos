# 📈 Forecasting de Ventas en E-commerce de Suministros de Oficina

## 📌 Descripción General
En este proyecto abordamos el histórico de ventas (ene 2015 – dic 2018) de un e-commerce de consumibles, mobiliario y equipos de oficina.  
Nuestro objetivo es construir y comparar varios modelos de forecasting (SARIMA, SARIMAX, XGBoost, Prophet) para **predecir los próximos 6 meses** con un **MAPE < 20 %** y proveer recomendaciones de inventario, logística y marketing.

---

## 🚀 Características Principales

### 🔍 Análisis Exploratorio de Datos (EDA)
- **Distribución de ventas**: ventas diarias muy volátiles vs. consumibles de bajo ticket y pocos pedidos de alto valor.
- **Series temporales**: tendencias mensuales, picos en Q1 (marzo), back-to-school (septiembre) y Black Friday (noviembre).
- **Segmentación por**:
  - Día de la semana (martes y sábados fuertes, jueves flojo)
  - Productos (top unidades vs. top ingresos)
  - Categoría y región
  - Tiempo y modo de entrega

### 🔬 Pruebas & Transformaciones
- **ADF Test**: p-valor ≈ 0.0003 ⇒ serie estacionaria.
- **Descomposición aditiva**: tendencia, estacionalidad mensual (~30 días) y ruido.

### 🔧 Modelado Clásico
- **SARIMA** manual y grid-search (MAPE 18.26 %).
- **SARIMAX + exógenos** (dummies de trimestre, Tax Day, Black Friday):  
  ‣ **MAPE 16.85 %**, MAE 14 051, RMSE 17 070.

### 🤖 Machine Learning & Ensemble
- **XGBoost** con lags y medias móviles.
- **Ensemble SARIMAX + XGBoost** → MAPE 16.92 %.

### 🧙‍♂️ Prophet
- Ajuste fino de `changepoint_prior_scale` y `seasonality_prior_scale`.
- Estacionalidad mensual y feriados corporativos.
- **MAPE 17.35 %**, MAE 13 778, RMSE 15 333.

---

## 📊 Resumen de Métricas

| Modelo                   | MAE       | RMSE      | MAPE     |
|--------------------------|----------:|----------:|---------:|
| **SARIMA puro**          | 15 448.15 | 18 565.97 | 18.26 %  |
| **SARIMAX + Exógenos**   | 14 051.15 | 17 070.04 | 16.85 %  |
| **Ensemble SARIMA+XGB**  | 14 726.66 | 18 468.62 | 16.92 %  |
| **Prophet afinado**      | 13 778.45 | 15 332.67 | 17.35 %  |

> **Candidato óptimo**: SARIMAX + exógenos (mejor trade-off precisión vs. sencillez).

---

## 🎯 Impacto de un MAPE ~17 % en el Negocio

- **Sin modelo**: MAPE ≈ 25–30 %, safety stock ≈ 30 % ⇒ capital inmovilizado alto y sobrecostos logísticos.  
- **Con modelo (MAPE 17 %)**: safety stock ≈ 19 % ⇒ libera \$55 000 de capital por \$500 000 de inventario.  
- **Reducción de stock-out**: pérdidas de \$100 000→\$80 000 anuales (ahorro \$6 000).  
- **Menos envíos urgentes**: costes courier –7 %→–5 % (ahorro ≈\$3 000/año).  
- **ROI esperado > 200 %** en el primer año.

---

## 🛠 Tecnologías Utilizadas
- **Python**: pandas, numpy, matplotlib, seaborn  
- **Series Temporales**: statsmodels, Prophet  
- **ML/Ensemble**: scikit-learn, xgboost  

---
