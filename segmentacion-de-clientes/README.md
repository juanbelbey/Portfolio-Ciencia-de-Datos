# 🚀 **Segmentación de Clientes Usando Clustering K-Means**  

## 📌 **Descripción General**  
Este proyecto aplica técnicas de **clustering**, específicamente **K-Means**, para segmentar clientes según sus patrones de uso de **tarjetas de crédito**.  

A través del análisis y visualización de datos, se identifican distintos **grupos de clientes**, proporcionando información valiosa para:  
✅ Estrategias de marketing dirigidas.  
✅ Mejoras operativas.  
✅ Planes de retención de clientes.  

---

## 📊 **Características Principales**  

### 🔎 **Análisis Exploratorio de Datos (EDA)**  
✔️ Manejo de **valores faltantes** y **estandarización de datos** para mejorar el clustering.  
✔️ **Estadísticas descriptivas** y **visualizaciones** para comprender la distribución de los datos.  
✔️ **Pair Plots** y **mapas de calor** para explorar correlaciones entre variables.  

### 🎯 **Clustering con K-Means**  
🔹 Uso del **método del codo (Elbow Method)** para determinar el número óptimo de clusters.  
🔹 Implementación de **K-Means** para agrupar clientes en diferentes segmentos.  
🔹 Implementación de **DBSCAN**.
🔹 Elección del modelo a usar en base a rendimiento.
🔹 Visualización de los **clusters con gráficos de dispersión** para interpretar patrones.  

### 📊 **Análisis de Clusters**  
📌 Evaluación de cada cluster mediante **estadísticas descriptivas**.  
📌 Comparación de clusters basada en el comportamiento de los clientes:  
   - **Límites de crédito** 💳  
   - **Frecuencia de visitas al banco** 🏦  
   - **Interacciones en línea** 🌐  
   - **Llamadas al banco** 📞  

### 📏 **Métricas de Evaluación**  
📌 **Silhouette Score** para medir la calidad de los clusters.   

---

## 📂 **Datos del Dataset**  
El dataset contiene información anónima sobre clientes, incluyendo:  

| 🏷 **Variable**            | 📌 **Descripción** |
|-------------------------|----------------|
| 💳 **Avg_Credit_Limit** | Límite promedio de crédito por cliente. |
| 💰 **Total_Credit_Cards** | Número total de tarjetas de crédito del cliente. |
| 🏦 **Total_visits_bank** | Número de visitas al banco. |
| 🌍 **Total_visits_online** | Frecuencia de interacciones en línea. |
| 📞 **Total_calls_made** | Número de llamadas realizadas al banco. |

---

## 🛠 **Tecnologías Utilizadas**  

### 📚 **Librerías de Python**  
✅ `pandas`, `numpy` → Manipulación y preprocesamiento de datos.  
✅ `matplotlib`, `seaborn` → Visualización de datos.  
✅ `scikit-learn` → Algoritmos de clustering y métricas de evaluación.  

### 🏷 **Algoritmos de Clustering**  
🔹 **K-Means** y **DBSCAN** para análisis comparativo.  

---

## 🎯 **Resultados e Insights**  

Se identificaron **tres grupos principales de clientes**:  

1️⃣ **Clientes con bajo gasto y poca interacción** 🔵  
2️⃣ **Usuarios moderados con actividad equilibrada** 🟡  
3️⃣ **Clientes de alto gasto con necesidades especializadas** 🔴  

Estos insights permiten:  
✅ **Diseñar campañas de marketing** dirigidas.  
✅ **Optimizar recursos** para clientes de alto valor.  
✅ **Mejorar el servicio al cliente** según patrones de interacción.  

---

## 🤝 **Contribuciones**  

📢 ¡Cualquier comentario o contribución es bienvenida!  
Si tienes sugerencias o ideas adicionales, no dudes en:  
📌 **Crear un Pull Request**.  
📌 **Abrir un Issue**.  

🙌 ¡Gracias por tu interés en este proyecto! 🚀  

---
