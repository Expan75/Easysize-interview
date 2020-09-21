from django.test import TestCase
from .models import Prediction

# Create your tests here.
class PredictionTestCase(TestCase):
    """ Set up test cases for all things predictions """

    def setUp(self):
        """ Basic setup of a valid prediction object that can be used later """
        Prediction.objects.create(
            numerical_input1=1.0, numerical_input2=1.2, categorical_input="a"
        )

    def test_correct_prediction_generation(self):
        """ Test for if model instance was created (incl. regression output) when fed valid inputs """
        sample_prediction = Prediction.objects.get(
            numerical_input1=1.0, numerical_input2=1.2, categorical_input="a"
        )
        self.assertIsNotNone(
            sample_prediction.output,
            msg="sample_output generated /w prediction model was none",
        )
        self.assertIsInstance(
            sample_prediction.output,
            float,
            msg="generated output should have type float",
        )

    def test_invalid_prediction_inputs(self):
        """ Basic test for ensuring that ValueErrors are raised on invalid input """

        with self.assertRaises(ValueError) as context:
            prediction = Prediction.objects.create(
                numerical_input1=9, numerical_input2="a", categorical_input="sigma"
            )
        self.assertTrue(
            type(context.exception) == ValueError,
            msg="Faulty prediction input did not result in value exception",
        )
