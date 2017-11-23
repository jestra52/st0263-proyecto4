import sys
from pyspark.ml.feature import HashingTF, IDF, Tokenizer, CountVectorizer
from pyspark.ml.feature import StopWordsRemover
from pyspark.ml.clustering import KMeans
from pyspark.sql import SparkSession
from pyspark import SparkContext

if __name__ == "__main__":
    if len(sys.argv) < 4: # Verificar parametros
        print("Uso: spark-submit proyecto4.py <directorioDataset> <k> <maxIteraciones> <directorioDeSalida>")
        sys.exit(1)

    #path = "hdfs:///user/vquinte3/examples" Ejemplo de ruta
    path = sys.argv[1] #El primer parametro ingresado por consola corresponde a la ruta del directorio del dataset
    k = int(sys.argv[2]) #El segundo parametro es el k
    maximoIter = int(sys.argv[3]) #El tercer parametro corresponde al maximo de iteraciones
    outputPath = sys.argv[4] #Parametro donde se guardara la salida de la ejecucion


    sc = SparkContext(appName="Proyecto4")  # SparkContext 
    spark = SparkSession(sc) #Crea una sesion de spark sql para poder usar algunos metodos necesarios (toDF())

    # Lee todos los archivos dentro del directorio especificado y obtiene un RDD
    text_files = sc.wholeTextFiles(path)

    # Se convierte el RDD obtenido a un DataFrame
    df = text_files.toDF(["Ruta", "Documento(String)"])

    df.show()

    # Crea los tokens que corresponden a las palabras de los documentos
    tokenizer = Tokenizer(inputCol="Documento(String)", outputCol="Tokens")
    tokenized = tokenizer.transform(df)

    tokenized.show()

    remover = StopWordsRemover(inputCol="Tokens", outputCol="Tokens sin stopwords")
    stopWordsRemoved_df = remover.transform(tokenized)

    stopWordsRemoved_df.show()

    hashingTF = HashingTF (inputCol="Tokens sin stopwords", outputCol="rawFeatures", numFeatures=200000)
    tfVectors = hashingTF.transform(stopWordsRemoved_df)

    tfVectors.show()

    idf = IDF(inputCol="rawFeatures", outputCol="features", minDocFreq=5)
    idfModel = idf.fit(tfVectors)

    tfIdfVectors = idfModel.transform(tfVectors)

    tfIdfVectors.show()

    # Trains a KMeans model.
    kmeans = KMeans().setK(k).setMaxIter(maximoIter)
    km_model = kmeans.fit(tfIdfVectors)

    clustersTable = km_model.transform(tfIdfVectors)
    clustersTable.show()
    clustersTable.select("Ruta","prediction").repartition(1).write.format("com.databricks.spark.csv").option("header", "true").save(outputPath);
