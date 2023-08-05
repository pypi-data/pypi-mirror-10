import os.path, sys
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir))
import unittest
import itertools
from chevrons.pipeline_base import PipelineBlock, Zip
from chevrons.pipeline_hof import Filter, Map, Fold
from chevrons.pipeline_parallel import FilterParallel, FoldParallel, MapParallel, BeginParallel, EndParallel
from chevrons.pipeline_extra import TrainScikitModel
import numpy as np

class Square(PipelineBlock):
    def run(self, input_data):
        return input_data ** 2

class AddOne(PipelineBlock):
    def run(self, input_data):
        return input_data + 1

class SwapInputs(PipelineBlock):
    def run(self, input_data):
        a,b = input_data
        return b,a

def square(x):
        return x ** 2

def add_one(x):
    return x+1

def is_even(x):
    return x%2==0

def is_odd(x):
    return x%2==1

def add_one_batch(batch):
    return [x+1 for x in batch]

def infinite_generator():
    while True:
        yield 1

def infinite_generator_2():
    while True:
        yield 2

def add(x1,x2):
    return x1+x2

class SyntaxTest(unittest.TestCase):
    def test_pipe(self):
        assert (2 | Square()) == 4

    def test_shift(self):
        f = Square() >> Square() >> AddOne()
        assert f(2) == 17

    def test_pipe_and_shift(self):
        assert (2 | Square() >> Square() >> AddOne()) == 17

    def test_multiple_input(self):
        assert ((1,2) | SwapInputs()) == (2,1)

class BaseComponentTest(unittest.TestCase):
    def test_zip(self):
        input_1 = itertools.islice(infinite_generator(),0,1000)
        input_2 = itertools.islice(infinite_generator_2(),0,1000)
        output = (input_1,input_2) | Zip()
        assert next(output) == (1,2)

class HigherOrderFunctionTest(unittest.TestCase):
    def test_map(self):
        assert list([1,2] | Map(square) >> Map(square)  >> Map(add_one)) == [2,17]

    def test_reuse(self):
        square_map = Map(square) >> Map(square)
        assert list([1,2] | square_map >> Map(add_one)) == [2,17]
        assert list([1,2] | square_map >> Map(add_one)) == [2,17]

    def test_imap(self):
        assert list([1,2] | BeginParallel(1) >> MapParallel(square) >> MapParallel(square)  >> MapParallel(add_one) >> EndParallel()) == [2,17]

    def test_map_infinite(self):
        data = infinite_generator()
        output_stream = data | Map(square) >> Map(square)
        assert next(output_stream) == 1

    def test_filter(self):
        data = range(0,10)
        output = data | Filter(is_even)
        assert list(output) == [0,2,4,6,8]

    def test_filter_parallel(self):
        data = [0,1,2,3,4,5,6,7,8,9]
        output = data | BeginParallel(1) >> FilterParallel(is_even) >> EndParallel()
        assert list(output) == [0,2,4,6,8]

    def test_filter_infinite(self):
        data = infinite_generator()
        is_odd = lambda x: x%2==1
        output = data | Filter(is_odd)
        assert next(output) == 1

    def test_filter_parallel_infinite(self):
        data = infinite_generator()
        output = data |  BeginParallel(1) >> FilterParallel(is_odd) >> EndParallel()
        assert next(output) == 1

    def test_fold(self):
        data = [0,1,2,3]
        output = data | Fold(add)
        assert output == 6

    def test_fold_parallel(self):
        data = [0,1,2,3]
        output = data | BeginParallel(1) >> FoldParallel(add)
        assert output == 6

def parse_row( element):
        return np.array([int(element['COL_1']), int(element['COL_2'])])

def sum_vectors(input_1, input_2):
        return input_1 + input_2

class UseCaseTest(unittest.TestCase):
    def test_end_to_end(self):
        import csv
        input_file = csv.DictReader(open('test_data.csv'))
        run_data_pipeline = Map(parse_row) >> Map(sum_vectors)
        run_data_pipeline(input_file) == [4, 6]

def can_import_scikit():
    try:
        import sklearn
        return True
    except:
        return False

@unittest.skipUnless(can_import_scikit(), 'no scikit learn, skipping test')
class SciKitLearnTest(unittest.TestCase):
    def test_model_training(self):
        from sklearn.ensemble import RandomForestClassifier
        X = [[0,0],[1,1],[0,0],[1,1],[0,0],[1,1],[0,0],[1,1],[0,0],[1,1]]
        y = [0,1,0,1,0,1,0,1,0,1]
        model = RandomForestClassifier()
        list(zip(X,y) | TrainScikitModel(model, batch_size=2))
        assert list(model.predict([[0,0], [1,1]])) == [0,1]