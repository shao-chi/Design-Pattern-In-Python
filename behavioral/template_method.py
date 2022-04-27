from abc import abstractmethod


class BaseModel(object):
    '''Template'''
    def do(self):
        self.load_data()
        self.build_model()
        self.fit()
        self.evaluate()
        self.save_model()

    def load_data(self):
        print('Loading Data ...')

    @abstractmethod
    def build_model(self):
        ...

    def fit(self):
        print('Training Model ...')

    @abstractmethod
    def predict(self):
        ...

    def evaluate(self):
        print('Evaluating Model ...')
        for _ in range(3):
            self.predict()

    @abstractmethod
    def save_model(self):
        ...


class MLModel(BaseModel):
    def build_model(self):
        print('Building ML Model ...')

    def predict(self):
        print('Predicting by ML Model ...')

    def save_model(self):
        print('Saving ML Model')


class DLModel(BaseModel):
    def build_model(self):
        print('Building DL Model ...')

    def fit(self):
        super().fit()
        for epoch in range(1, 11):
            print(f'Epoch {epoch} ...')
        print('Finish Training DL Model')

    def predict(self):
        print('Predicting by DL Model ...')

    def save_model(self):
        print('Saving DL Model')


if __name__ == '__main__':
    ml_model = MLModel()
    ml_model.do()

    dl_model = DLModel()
    dl_model.do()
