#word
from datetime import datetime
from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.naive_bayes import GaussianNB
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score

class MachineLearning():

    def __init__(self):
        
        print("Loading dataset ...")
        
        self.counter = 0
        
        self.flow_dataset = pd.read_csv('FlowStatsfile.csv')
# تقوم أسطر التعليمات البرمجية هذه بإزالة النقاط من العمود الثالث والرابع والسادس
#The "iloc" method is used to select the columns  to modify 
        self.flow_dataset.iloc[:, 2] = self.flow_dataset.iloc[:, 2].str.replace('.', '')#flow_id
        self.flow_dataset.iloc[:, 3] = self.flow_dataset.iloc[:, 3].str.replace('.', '')#ip_srcيمكن القيام بذلك لتحويل العنوان  إلى قيمة رقمية مناسبة لخوارزميات التعلم الآلي المختلفة.
        self.flow_dataset.iloc[:, 5] = self.flow_dataset.iloc[:, 5].str.replace('.', '')# ip_dst
        
        self.X_flow = self.flow_dataset.iloc[:, :-1].values#features....حديد جميع الأعمدة باستثناء العمود الأخير (الذي يُفترض أنه عمود التسمية)
        self.X_flow = self.X_flow.astype('float64')

        self.y_flow = self.flow_dataset.iloc[:, -1].values#target/labelعمود التسمية

#يقوم الكود بتقسيم مجموعة البيانات بشكل عشوائي إلى مجموعات بيانات تدريب واختبار، مع استخدام 75% من البيانات للتدريب و25% المتبقية للاختبار.
        self.X_flow_train, self.X_flow_test, self.y_flow_train, self.y_flow_test = train_test_split(self.X_flow, self.y_flow, test_size=0.25, random_state=0)

    def LR(self):
        
        print("------------------------------------------------------------------------------")
        print("Logistic Regression ...")
#LogisticRegression class from scikit-learn
#The 'liblinear' solver is a specialized algorithm used for logistic regression with small datasets
#The 'random_state' parameter ensures that the results are reproducible across multiple runs of the algorithm. 
        self.classifier = LogisticRegression(solver='liblinear', random_state=0)
        self.Confusion_matrix()
        
    def KNN(self):

        print("------------------------------------------------------------------------------")
        print("K-NEAREST NEIGHBORS ...")
#from sklearn.neighbors import KNeighborsClassifier
#The "n_neighbors" parameter is set to 5, which means that the five closest neighbors to a given point will be used to classify that point. 
#The "metric" parameter is set to 'minkowski', which is a generalization of the Euclidean and Manhattan distances.
#The "p" parameter is set to 2, which means that the Euclidean distance is used for the calculation. 
        self.classifier = KNeighborsClassifier(n_neighbors=5, metric='minkowski', p=2)
        self.Confusion_matrix()
 
    def SVM(self):

        print("------------------------------------------------------------------------------")
        print("SUPPORT-VECTOR MACHINE ...")
#from sklearn.svm import SVC
#'rbf', which stands for radial basis function and is a popular kernel function used in SVMs.
#The "random_state" parameter is set to 0 to ensure reproducibility of the results.
        self.classifier = SVC(kernel='rbf', random_state=0)
        self.Confusion_matrix()
        
    def NB(self):

        print("------------------------------------------------------------------------------")
        print("NAIVE-BAYES ...")
#from sklearn.naive_bayes import GaussianNB
        self.classifier = GaussianNB()
        self.Confusion_matrix()
        
        
    def DT(self):

        print("------------------------------------------------------------------------------")
        print("DECISION TREE ...")
#from sklearn.tree import DecisionTreeClassifier
#0 ، مما يضمن استخدام نفس التسلسل من الأرقام العشوائية في كل مرة يتم فيها تشغيل الكود.
        self.classifier = DecisionTreeClassifier(criterion='entropy', random_state=0)
        self.Confusion_matrix()
        
    def RF(self):

        print("------------------------------------------------------------------------------")
        print("RANDOM FOREST ...")
#from sklearn.ensemble import RandomForestClassifier
#The "n_estimators" parameter is set to 10, which specifies the number of trees in the forest. 
#Increasing the number of trees generally leads to better performance, but also increases the computational cost.
        self.classifier = RandomForestClassifier(n_estimators=10, criterion="entropy", random_state=0)
        self.Confusion_matrix()
        
#function named "Confusion_matrix" that calculates and prints the confusion matrix for the model's prediction.
    def Confusion_matrix(self):
        self.counter += 1
    # trains the model using the classifier's fit method 
    #انتبه مين تابع التدريب
    #انتبه classifier هو يستدعي التدريب
        self.flow_model = self.classifier.fit(self.X_flow_train, self.y_flow_train)
#the predict method is used with the test data (self.X_flow_test) to generate the predicted class labels (self.y_flow_pred).
#انتبه اخد الاكس
        self.y_flow_pred = self.flow_model.predict(self.X_flow_test)

        print("------------------------------------------------------------------------------")

        print("confusion matrix")
        #from sklearn.metrics import confusion_matrix
        #انتبه بارمتراتا:تسميات الفئة الفعلية&&والتسميات المتوقعة
        cm = confusion_matrix(self.y_flow_test, self.y_flow_pred)
        print(cm)
#from sklearn.metrics import accuracy_score
     #انتبه بارمتراتا:تسميات الفئة الفعلية&&والتسميات المتوقعة
     #وهي جزء من المثيلات المصنفة بشكل صحيح بين جميع المثيلات.
        acc = accuracy_score(self.y_flow_test, self.y_flow_pred)

        print("succes accuracy = {0:.2f} %".format(acc*100))
        fail = 1.0 - acc
        print("fail accuracy = {0:.2f} %".format(fail*100))
        print("------------------------------------------------------------------------------")
#-----------------------------------------الرسمممممم----------------------
        x = ['TP','FP','FN','TN']
        x_indexes = np.arange(len(x))
        width = 0.10
        plt.xticks(ticks=x_indexes, labels=x)
        plt.title("Résultats des algorithmes")
        plt.xlabel('Classe predite')
        plt.ylabel('Nombre de flux')
        plt.tight_layout()
        plt.style.use("seaborn-darkgrid")
        # plt.style.use("dark_background")
        # plt.style.use("ggplot")
        if self.counter == 1:
            y1 = [cm[0][0],cm[0][1],cm[1][0],cm[1][1]]
            plt.bar(x_indexes-2*width,y1, width=width, color="#1b7021", label='LR')
            plt.legend()
        if self.counter == 2:
            y2 = [cm[0][0],cm[0][1],cm[1][0],cm[1][1]]
            plt.bar(x_indexes-width,y2, width=width, color="#e46e6e", label='KNN')
            plt.legend()
        if self.counter == 3:
            y3 = [cm[0][0],cm[0][1],cm[1][0],cm[1][1]]
            plt.bar(x_indexes,y3, width=width, color="#0000ff", label='NB')
            plt.legend()
        if self.counter == 4:
            y4 = [cm[0][0],cm[0][1],cm[1][0],cm[1][1]]
            plt.bar(x_indexes+width,y4, width=width, color="#e0d692", label='DT')
            plt.legend()
        if self.counter == 5:
            y5 = [cm[0][0],cm[0][1],cm[1][0],cm[1][1]]
            plt.bar(x_indexes+2*width,y5, width=width, color="#000000", label='RF')
            plt.legend()
            plt.show()
        
        
def main():
    
    start_script = datetime.now()
    
    ml = MachineLearning()
    
    start = datetime.now()
    ml.LR()
    end = datetime.now()
    print("LEARNING and PREDICTING Time: ", (end-start)) 
    
    start = datetime.now()
    ml.KNN()
    end = datetime.now()
    print("LEARNING and PREDICTING Time: ", (end-start))
    
    # start = datetime.now()
    # ml.SVM()
    # end = datetime.now()
    # print("LEARNING and PREDICTING Time: ", (end-start))
    
    start = datetime.now()
    ml.NB()
    end = datetime.now()
    print("LEARNING and PREDICTING Time: ", (end-start))
    
    start = datetime.now()
    ml.DT()
    end = datetime.now()
    print("LEARNING and PREDICTING Time: ", (end-start))
    
    start = datetime.now()
    ml.RF()
    end = datetime.now()
    print("LEARNING and PREDICTING Time: ", (end-start))
    
    end_script = datetime.now()
    print("Script Time: ", (end_script-start_script))

if __name__ == "__main__":
    main()