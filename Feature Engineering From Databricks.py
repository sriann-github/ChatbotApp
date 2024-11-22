from pyspark.sql import SparkSession
from pyspark.sql import SQLContext
from pyspark.ml.feature import CountVectorizer, StringIndexer
from pyspark.ml.classification import NaiveBayes
from pyspark.ml.evaluation import MulticlassClassificationEvaluation
import pandas as pd

#Set up SparkSession (Databricks has Spark pre-configured, so this line)
spark = SparkSession.builder.appName("TextClassification").getOrCreate()

#1. Set Database Connection Details
jdbc_hostname = ""
jdbc_port = "1433"
database_name = ""
table_name = ""
username = ""
password = ""

#2. Build JDBC URL
jdbc_url = f"jdbc:sqlserver://{jdbc_hostname}:{jdbc_port};databaseName={database_name}"

#3. Read Data from SQL Database into Spark DataFrame
data_df = spark.read\
          .format("jdbc")\
          .option("url", jdbc_url)\
          .option("dbtable", table_name)\
          .option("user", username)\
          .option("password", password)\
          .load()
#4. display the data to ensure it's loaded correctly
data_df.show()

#5. Select relevant columns and convert to Pandas DataFrame if needed for
# make sure you have the right column names
data_pandas = data_df.select("column1", "column2").toPandas()

#6. Split Data into Train And Test sets
from sklearn.model_selection import train_test_split
X = data_pandas['col1']
y = data_pandas['col2']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

#7. Vectorize Text Data
from sklearn.naive_bayes import MultinomialNB
mnb = MultinomialNB()
mnb.fit(X_train_vec, y_train)

#9. Predict and Evaluate MNB Model
from sklearn.metrics import accuracy_score, classification_report
y_pred_mnb = mnb.predict(X_test_vec)
print("Multinomial Naive Bayes Accuracy:", accuracy_score(y_test, y_pred_mnb))
print("Classification Report:\n", classification_report(y_test, y_pred_mnb))

from sklearn.svm import SVC
svm = SVC(kernel= 'linear')
svm.fit(X_train_vec, y_train)
y_pred_svm = svm.predict(X_test_vec)
print("SVM Accuracy:", accuracy_score(y_test, y_pred_svm))
print("Classification Report:\n", classification_report(y_test, y_pred_svm))

#10. Save Models if needed
import joblib
joblib.dump(mnb, "/dbfs/mnt/models/mnb_model.pkl")
joblib.dump(svm, "/dbfs/mnt/models/svm_model.pkl")