from abc import abstractmethod


class ModelBuilderInterface(object):
    '''Builder Interface'''
    def load_data(self):
        print('Loading Data ...')

    @abstractmethod
    def data_preprocess(self):
        print('Preprocessing Data ...')

    @abstractmethod
    def build_model(self):
        print('Building Model ...')

    def fit(self):
        print('Training Model ...')

    def predict(self):
        print('Predicting ...')

    def evaluate(self):
        print('Evaluating Model ...')
        for _ in range(3):
            self.predict()

    def save_model(self):
        print('Saving Model ...')

    def deploy_model(self):
        print('Deploying model to let it become a service ...')

    def develop_api(self):
        print('Developing model API ...')

    def create_monitor(self):
        print('Creating a model monitor ... ')

    @abstractmethod
    def get_model(self):
        ...

    @abstractmethod
    def get_service(self):
        ...


class ClassificationModel(ModelBuilderInterface):
    '''Concrete Builder'''

    def data_preprocess(self):
        super().data_preprocess()
        print('    Transforming Target into labels ...')

    def build_model(self):
        super().build_model()
        print('''
        Classification Model:
            Fully Connected Layer (128)
            ReLU
            Fully Connected Layer (128)
            Softmax

            - Loss function: Cross Entropy''')

    def get_model(self):
        print('~~~ You got a classification model. ~~~')
        return 'classification model'

    def get_service(self):
        print('~~~ You got a classification model with API and monitor. ~~~')
        return 'classification model with API and monitor'


class RegressionModel(ModelBuilderInterface):
    '''Concrete Builder'''

    def data_preprocess(self):
        super().data_preprocess()
        print('    Normalizing numerical features ... ')

    def build_model(self):
        super().build_model()
        print('''
        Regression Model:
            Fully Connected Layer (128)
            ReLU
            Fully Connected Layer (128)

            - Loss function: Mean Square Error''')

    def get_result(self):
        print('~~~ You got a regression model. ~~~')
        return 'regression model'

    def get_service(self):
        print('~~~ You got a regression model with API and monitor. ~~~')
        return 'regression model with API and monitor'


class MachineLearningEngineer(object):
    def __init__(self, builder: ModelBuilderInterface) -> None:
        self._builder = builder

    def change_builder(self, builder: ModelBuilderInterface):
        self._builder = builder

    def make(self, task):
        if task == 'model':
            self._builder.load_data()
            self._builder.data_preprocess()
            self._builder.fit()
            self._builder.evaluate()
            self._builder.save_model()
            return self._builder.get_model()

        elif task == 'service':
            self._builder.load_data()
            self._builder.data_preprocess()
            self._builder.fit()
            self._builder.evaluate()
            self._builder.deploy_model()
            self._builder.create_monitor()
            self._builder.develop_api()
            return self._builder.get_service()


if __name__ == '__main__':
    model_builder = ClassificationModel()
    engineer = MachineLearningEngineer(model_builder)
    product = engineer.make('model')
    print(f'Resuit: {product}')
    product = engineer.make('service')
    print(f'Resuit: {product}')

    engineer.change_builder(RegressionModel())
    product = engineer.make('model')
    print(f'Resuit: {product}')
    product = engineer.make('service')
    print(f'Resuit: {product}')
