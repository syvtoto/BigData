class ClassifModel:
    fileName = 'model.sav'
    model

    def _init_():
        self.fileName = 'model.sav'

    def loadModel():
        model = pickle.load(open(filename, 'rb'))

    def predict(sepal_length,sepal_width,petal_length,petal_width):
        return model.predict([[[[sepal_length,sepal_width,petal_length,petal_width]])

    def saveModel():
        pickle.dump(clf, open(filename, 'wb'))
