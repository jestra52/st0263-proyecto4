#  Proyecto 04 - ST0263 - Clústering de documentos a partir de métricas de similitud basado en Big Data

Integrantes del grupo:

* Valentín Quintero Castrillón - vquinte3@eafit.edu.co

* Juan Carlos Estrada Álvarez - jestra52@eafit.edu.co

## 1. Descripción del proyecto:
Este proyecto hace parte de la asignatura Tópicos Especiales en Telemática. Este consiste en; por medio de Big Data agrupar un conjunto de documentos (clustering) utilizando el framework Spark y haciendo uso de sus librerias de Machine Learning: K-Means y TF-IDF, para las métricas de similaridad entre documentos.

## 2. Objetivos:
* Aplicar las tecnologías y modelos de programación en Big Data.
* Analizar los resultados entre un acercamiento paralelo (proyecto 3) y las tecnologías y modelos en Big Data.
* Entender los dos ambientes de supercomputación basados en HPC y Big Data, las limitaciones, software y hardware asociadas a distintos problemas computacionales que podrían sortearse a partir de herramientas y estrategias como computación paralela y big data.

## 3. Modo de ejecución:
Para ejecutar el programa se deben ejecutar los siguientes comandos en la terminal:

De manera local:

    $ spark-submit proyecto4.py hdfs://<directorioDataset> <k> <maxIteraciones> hdfs://<directorioDeSalida>
    

Ejecutar en el cluster:

    $ spark-submit --master yarn --deploy-mode cluster --executor-memory <memoriaGB>G --num-executors <numExecutors> proyecto4.py hdfs://<directorioDataset> <k> <maxIteraciones> hdfs://<directorioDeSalida>

## 4. Algoritmos utilizados:
* TF-IDF (Term frequency-inverse document frequency): Tf-idf (del inglés Term frequency – Inverse document frequency), frecuencia de término – frecuencia inversa de documento (o sea, la frecuencia de ocurrencia del término en la colección de documentos), es una medida numérica que expresa cuán relevante es una palabra para un documento en una colección. Esta medida se utiliza a menudo como un factor de ponderación en la recuperación de información y la minería de texto. El valor tf-idf aumenta proporcionalmente al número de veces que una palabra aparece en el documento, pero es compensada por la frecuencia de la palabra en la colección de documentos, lo que permite manejar el hecho de que algunas palabras son generalmente más comunes que otras.
* K-means: Algoritmo de agrupamiento, se requiere un numero de clusters a generar y una matriz que contiene la frencuencia de terminos obtenida de un conjunto de datos.

## 5. Requisitos:
* Cluster con Spark (>= 2.1.1.2.6.1.0-129) 
* Java Development Kit (>= 1.8.0_144)
* Python (>= 3.6.2)
* Pyspark
* Hadoop (>= 2.7.3.2.6.1.0-129)

## 6. Referencias:
* "Clustering with K-Means with Spark and MLlib". tfadmin. Fuente: http://timothyfox.net/?p=15.
* "TF-IDF, HashingTF and CountVectorizer". Ming Chen. Fuente: https://mingchen0919.github.io/learning-apache-spark/tf-idf.html.
* "TF-IDF with Spark for the Kaggle popcorn competition". logicalguess (Github user). Fuente: https://github.com/logicalguess/tf-idf-spark-and-python.
* "Feature Extraction and Transformation - RDD-based API - Spark 2.2.0 Documentation". Spark org. Fuente: https://spark.apache.org/docs/2.2.0/mllib-feature-extraction.html.
