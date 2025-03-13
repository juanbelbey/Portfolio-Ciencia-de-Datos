# 💧 Optimización del Análisis de Agua con Aprendizaje Automático  

## 📌 Descripción General  

El acceso a agua potable segura es un **derecho fundamental y un desafío global**. La calidad del agua influye directamente en **la salud pública, la sostenibilidad ambiental y la eficiencia operativa** en los procesos de potabilización.  

### 🎯 Objetivo del Proyecto  
Este proyecto aplica **técnicas de aprendizaje automático** para desarrollar un **modelo predictivo** que **clasifique muestras de agua como potables o no potables**, basándose en variables fisicoquímicas clave.  

## 🔎 Descripción del Problema  

En los sistemas de potabilización, los análisis de calidad del agua requieren **pruebas de laboratorio** que pueden ser **costosas y demoradas**. Un modelo predictivo eficiente puede ayudar a **reducir costos operativos y mejorar la toma de decisiones**.  

📌 **Riesgos a considerar en la clasificación:**  
✔ **Falso positivo** → Clasificar erróneamente agua contaminada como potable representa **un riesgo grave para la salud pública**.  
✔ **Falso negativo** → Clasificar agua segura como no potable genera **ineficiencias y costos innecesarios**.  

📌 **Solución propuesta:**  
✔ **Implementar modelos de Machine Learning** que optimicen la clasificación del agua potable.  
✔ **Minimizar los falsos positivos** para evitar riesgos sanitarios.  
✔ **Optimizar el uso de insumos y reducir gastos operativos** en el proceso de tratamiento de agua.  

---

## 📊 Características Principales  

### 🔎 Análisis Exploratorio de Datos (EDA)  
✔️ Manejo de valores faltantes mediante imputación de datos.  
✔️ Visualización de distribuciones con histogramas y boxplots.  
✔️ Mapa de calor para analizar correlaciones entre variables.  
✔️ Detección de outliers y su impacto en el modelo.  

---

## 📂 Datos del Dataset  
📌 **Fuente:** [Dataset en Kaggle](https://www.kaggle.com/datasets/adityakadiwal/water-potability)  
📌 **Registros:** 3,276 muestras de agua  

🏷 **Variables Incluidas:**  

| 🔢 Variable | 📌 Descripción |
|------------|--------------|
| **pH** | Nivel de acidez/alcalinidad del agua. |
| **Hardness** | Cantidad de minerales disueltos en el agua. |
| **Solids (TDS)** | Sólidos disueltos totales en mg/L. |
| **Chloramines** | Nivel de cloraminas utilizadas en el tratamiento. |
| **Sulfate** | Cantidad de sulfatos en el agua. |
| **Conductivity** | Medida de la conductividad eléctrica del agua. |
| **Organic Carbon** | Nivel de carbono orgánico presente. |
| **Trihalomethanes** | Subproductos del tratamiento con cloro. |
| **Turbidity** | Nivel de turbidez en el agua. |
| **Potability** | Variable objetivo (1 = potable, 0 = no potable). |

---

## 💰 Impacto y Beneficios Económicos  

📌 **Optimización del uso de insumos químicos** → Ajustar las dosis de reactivos en función de predicciones precisas.  
📌 **Ahorro en análisis físico-químicos** → Menos pruebas innecesarias sin comprometer la seguridad.  
📌 **Monitoreo en tiempo real** → Posibilidad de alertar sobre cambios en la calidad del agua.  

💵 **Estimación de Ahorro Anual:**  
✔ **Reducción del uso de insumos químicos** → **$51,840 USD**  
✔ **Ahorro en análisis físicos y químicos** → **$2,160 USD**  
✔ **Total estimado** → **$54,000 USD / año**  

---

## 🛠 Tecnologías Utilizadas  

📚 **Librerías en Python:**  
✅ `pandas`, `numpy` → Manipulación de datos.  
✅ `matplotlib`, `seaborn`, `plotly` → Visualización de datos.  
✅ `scikit-learn`, `tensorflow` → Modelado predictivo y evaluación.  

🎯 **Modelos aplicados:**  
🔹 **KNN, Random Forest y Redes Neuronales**  

### 🎯 Modelado Predictivo  
Se probaron diferentes algoritmos de **Machine Learning** para encontrar el modelo más efectivo:  

| 🔢 Modelo                 | Accuracy | F1-Score Clase 1 (Potable) |
|---------------------------|----------|---------------------------|
| **K-Nearest Neighbors**    | 63%      | 44%                        |
| **Random Forest**          | 69%      | 46%                        |
| **Red Neuronal (Optimizada)** | 67%  | 48%                        |

✔️ **Optimización de hiperparámetros** con GridSearchCV y RandomizedSearchCV.  
✔️ **Balanceo de clases** con SMOTE para mejorar la predicción del agua potable.  

### 📊 Evaluación del Modelo  
📌 **Métricas utilizadas:**  
✅ **F1-Score** → Prioridad en minimizar falsos positivos (clasificar agua contaminada como potable).  
✅ **Matriz de Confusión** → Análisis detallado de los errores.  

---

🎯 **Conclusiones y Mejoras Futuras**
✅ El modelo Random Forest optimizado obtuvo el mejor desempeño en términos de precisión y balance de clases.
✅ El modelo de Red Neuronal también mostró un rendimiento competitivo, especialmente tras la optimización de hiperparámetros.
✅ La falta de datos históricos impide analizar tendencias temporales → Se recomienda recolectar datos en el tiempo.
✅ Se sugiere mejorar la calidad de los datos incluyendo sensores en tiempo real para mejorar la toma de decisiones.

---

🤝 **Contribuciones y Contacto**
📢 ¡Cualquier comentario o contribución es bienvenida!
Si tienes sugerencias o ideas adicionales, no dudes en:
📌 Crear un Pull Request.
📌 Abrir un Issue con tu propuesta.

🙌 ¡Gracias por tu interés en este proyecto! 🚀
