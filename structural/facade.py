class DataPreprocessor(object):
    def preprocess(self):
        print("Start Preprocessing Data ...", end=' ')
        print("Finish Preprocessing Data")


class ModelTrainer(object):
    def train(self):
        print("Start Training Model ...", end=' ')
        print("Finish Training Model")


class ModelEvaluator(object):
    def evaluate(self):
        print("Start Evaluating Model ...", end=' ')
        print("Finish Evaluating Model")


class ModelInferencer(object):
    def inference(self):
        print("Start Inferencing Model ...", end=' ')
        print("Finish Inferencing Model")


class ModelFacade(object):
    def __init__(self) -> None:
        self.preprocessor = DataPreprocessor()
        self.trainer = ModelTrainer()
        self.evaluator = ModelEvaluator()
        self.inferencer = ModelInferencer()

    def do(self):
        self.preprocessor.preprocess()
        self.trainer.train()
        self.evaluator.evaluate()
        self.inferencer.inference()


if __name__ == '__main__':
    facade = ModelFacade()
    facade.do()
