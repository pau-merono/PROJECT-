{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "installation",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Celda 1: Instalación de librerías necesarias\n",
    "# Ejecuta esto en tu entorno si las librerías no están instaladas.\n",
    "# !pip install pandas numpy matplotlib seaborn scikit-learn"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "import-libraries",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Celda 2: Verificación de instalación\n",
    "import pandas as pd\n",
    "import numpy as np\n",
    "import matplotlib.pyplot as plt\n",
    "import seaborn as sns\n",
    "from sklearn.model_selection import train_test_split\n",
    "from sklearn.preprocessing import StandardScaler\n",
    "from sklearn.ensemble import RandomForestClassifier\n",
    "from sklearn.metrics import classification_report, confusion_matrix\n",
    "\n",
    "print(\"\u00a1Todas las librerías se importaron correctamente!\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "initial-setup",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Celda 3: Configuración inicial\n",
    "import warnings\n",
    "warnings.filterwarnings('ignore')\n",
    "\n",
    "# Configurar el estilo de las gráficas\n",
    "plt.style.use('seaborn')\n",
    "sns.set_palette(\"husl\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "data-preparation",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Celda 4: Carga y preparación de datos\n",
    "# Cargar los datos\n",
    "df = pd.read_csv('fertility_Diagnosis.csv', sep=';')\n",
    "\n",
    "# Mapear las estaciones a valores más interpretables\n",
    "season_map = {-1: 'Invierno', -0.33: 'Primavera', 0.33: 'Verano', 1: 'Oto\u00f1o'}\n",
    "df['Season_Name'] = df['Season'].map(season_map)\n",
    "\n",
    "# Mostrar las primeras filas y la información del dataset\n",
    "print(\"Primeras filas del dataset:\")\n",
    "print(df.head())\n",
    "print(\"\\nInformación del dataset:\")\n",
    "print(df.info())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "eda-first-plot",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Celda 5: Análisis Exploratorio de Datos - Primera Gráfica\n",
    "plt.figure(figsize=(12, 6))\n",
    "diagnosis_by_season = pd.crosstab(df['Season_Name'], df['Diagnosis'], normalize='index') * 100\n",
    "diagnosis_by_season.plot(kind='bar', stacked=True)\n",
    "plt.title('Distribución de Diagnósticos por Estación')\n",
    "plt.xlabel('Estación')\n",
    "plt.ylabel('Porcentaje')\n",
    "plt.legend(title='Diagnóstico', bbox_to_anchor=(1.05, 1))\n",
    "plt.tight_layout()\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "eda-second-plot",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Celda 6: Análisis Exploratorio de Datos - Segunda Gráfica\n",
    "plt.figure(figsize=(10, 6))\n",
    "for diagnosis in df['Diagnosis'].unique():\n",
    "    mask = df['Diagnosis'] == diagnosis\n",
    "    plt.scatter(df[mask]['Age'], df[mask]['Sitting_hours'], \n",
    "               label=f'Diagnóstico {diagnosis}', alpha=0.6)\n",
    "\n",
    "plt.title('Relación entre Edad y Horas Sentado por Diagnóstico')\n",
    "plt.xlabel('Edad (normalizada)')\n",
    "plt.ylabel('Horas Sentado (normalizada)')\n",
    "plt.legend()\n",
    "plt.tight_layout()\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "eda-third-plot",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Celda 7: Análisis Exploratorio de Datos - Tercera Gráfica\n",
    "plt.figure(figsize=(10, 8))\n",
    "numeric_cols = ['Season', 'Age', 'Childish_diseases', 'Accident_or_trauma',\n",
    "                'Surgical_intervention', 'High_fevers', 'Alcohol_consumption',\n",
    "                'Smoking_habit', 'Sitting_hours']\n",
    "corr_matrix = df[numeric_cols].corr()\n",
    "sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', center=0)\n",
    "plt.title('Matriz de Correlación entre Variables')\n",
    "plt.tight_layout()\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "statistical-analysis",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Celda 8: Análisis Estadístico\n",
    "print(\"Estadísticas Descriptivas:\")\n",
    "print(df.describe())\n",
    "\n",
    "print(\"\\nDistribución de Diagnósticos:\")\n",
    "print(df['Diagnosis'].value_counts(normalize=True) * 100)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "predictive-modeling",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Celda 9: Modelado Predictivo\n",
    "# Preparar los datos\n",
    "X = df.drop(['Diagnosis', 'Season_Name'], axis=1)\n",
    "y = df['Diagnosis']\n",
    "\n",
    "# Dividir los datos\n",
    "X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)\n",
    "\n",
    "# Entrenar el modelo\n",
    "rf = RandomForestClassifier(random_state=42)\n",
    "rf.fit(X_train, y_train)\n",
    "\n",
    "# Evaluar el modelo\n",
    "y_pred = rf.predict(X_test)\n",
    "\n",
    "print(\"\\nReporte de Clasificación:\")\n",
    "print(classification_report(y_test, y_pred))\n",
    "\n",
    "# Importancia de características\n",
    "feature_importance = pd.DataFrame({\n",
    "    'feature': X.columns,\n",
    "    'importance': rf.feature_importances_\n",
    "}).sort_values('importance', ascending=False)\n",
    "\n",
    "print(\"\\nImportancia de Variables:\")\n",
    "print(feature_importance)"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
