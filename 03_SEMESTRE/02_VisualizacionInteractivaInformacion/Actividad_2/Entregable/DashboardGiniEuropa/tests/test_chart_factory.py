import unittest
import pandas as pd
import sys
import os
import json

# Add project root to path to ensure app module is found
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app.services.chart_factory import ChartFactory

class TestChartFactory(unittest.TestCase):
    
    def setUp(self):
        """Set up a dummy dataframe for testing."""
        self.factory = ChartFactory()
        
        # Create a sample DataFrame matching the structure used in the app
        data = {
            'Country Name': [
                'España', 'España', 'España', 'España', 
                'Alemania', 'Alemania', 'Alemania', 'Alemania',
                'Francia', 'Francia',
                'Suecia', 'Suecia',
                'Polonia', 'Polonia',
                'Rumania', 'Rumania'
            ],
            'Year': [
                2019, 2020, 2021, 2022, 
                2019, 2020, 2021, 2022,
                2020, 2021,
                2020, 2021,
                2020, 2021,
                2020, 2021
            ],
            'Gini': [
                34.0, 35.0, 34.5, 33.0,
                30.0, 31.0, 30.5, 30.0,
                29.0, 29.5,
                27.0, 27.2,
                28.0, 28.5,
                35.0, 36.0
            ]
        }
        self.df = pd.DataFrame(data)

    def _validate_json_response(self, result):
        """Helper to validate that the result is a valid JSON string representing a Plotly figure."""
        self.assertIsInstance(result, str, "Result should be a JSON string")
        
        try:
            parsed = json.loads(result)
        except json.JSONDecodeError:
            self.fail("Result is not a valid JSON string")
            
        self.assertIn('data', parsed, "JSON should contain 'data' key")
        self.assertIn('layout', parsed, "JSON should contain 'layout' key")
        return parsed

    # --- Evolution Charts Tests ---
    def test_create_evolution_chart_correct(self):
        result = self.factory.create_evolution_chart_correct(self.df)
        parsed = self._validate_json_response(result)
        # Check if we have traces for our focus countries
        self.assertTrue(len(parsed['data']) > 0, "Should have data traces")

    def test_create_evolution_chart_manipulated(self):
        result = self.factory.create_evolution_chart_manipulated(self.df)
        parsed = self._validate_json_response(result)
        # Check manipulated layout properties
        self.assertIn('template', parsed['layout'], "Should have a template")
        
    # --- Divergence Charts Tests ---
    def test_create_divergence_chart_correct(self):
        result = self.factory.create_divergence_chart_correct(self.df)
        self._validate_json_response(result)

    def test_create_divergence_chart_bad(self):
        result = self.factory.create_divergence_chart_bad(self.df)
        self._validate_json_response(result)

    # --- Context Charts Tests ---
    def test_create_context_chart_correct(self):
        result = self.factory.create_context_chart_correct(self.df)
        self._validate_json_response(result)

    def test_create_context_chart_bad(self):
        result = self.factory.create_context_chart_bad(self.df)
        self._validate_json_response(result)

    # --- Policy Charts Tests ---
    def test_create_policy_chart_correct(self):
        result = self.factory.create_policy_chart_correct(self.df)
        self._validate_json_response(result)

    def test_create_policy_chart_bad(self):
        result = self.factory.create_policy_chart_bad(self.df)
        self._validate_json_response(result)
        
    # --- Crisis Charts Tests ---
    def test_create_crisis_chart_correct(self):
        result = self.factory.create_crisis_chart_correct(self.df)
        self._validate_json_response(result)
        
    def test_create_crisis_chart_bad(self):
        result = self.factory.create_crisis_chart_bad(self.df)
        self._validate_json_response(result)

if __name__ == '__main__':
    unittest.main()
