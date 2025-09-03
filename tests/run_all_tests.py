"""
Run all unit tests for webextractionhelper package
"""

import unittest
import sys
import os

# Add the parent directory to the path so we can import the package
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from webextractionhelper import Selectors

def run_all_tests():
    """Discover and run all tests"""
    print("🧪 Running all webextractionhelper tests...")
    print("=" * 60)

    # Create test suite
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()

    # Discover all tests in the tests directory
    start_dir = os.path.dirname(__file__)
    pattern = 'test_*.py'

    suite = loader.discover(start_dir, pattern)

    # Run the tests
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)

    # Print summary
    print("\n" + "=" * 60)
    if result.wasSuccessful():
        print("✅ All tests passed!")
        return 0
    else:
        print(f"❌ {len(result.failures)} tests failed, {len(result.errors)} errors")
        return 1

def show_selectors_summary():
    """Show a summary of available selectors"""
    print("\n📊 Available Selectors Summary:")
    selectors = Selectors()
    categories = {}

    for key, value in selectors.selectors.items():
        category = key.split('.')[0]
        if category not in categories:
            categories[category] = []
        categories[category].append(key)

    for category, keys in categories.items():
        print(f"  • {category}: {len(keys)} selectors")

    print(f"\nTotal: {len(selectors.selectors)} selectors")

if __name__ == '__main__':
    show_selectors_summary()
    exit_code = run_all_tests()
    sys.exit(exit_code)
