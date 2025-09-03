#!/usr/bin/env python3
"""
Example usage of the webextractionhelper package.

This script demonstrates how to use the Selectors class to access
various web scraping selectors for Google search results.
"""

from webextractionhelper import Selectors

def main():
    """Demonstrate the webextractionhelper package functionality."""
    print("🌐 WebExtractionHelper Package Demo")
    print("=" * 50)
    
    # Create a Selectors instance
    selectors = Selectors()
    
    print(f"\n📊 Total selectors available: {len(selectors.selectors)}")
    
    # Show different categories of selectors
    categories = {}
    for key, value in selectors.selectors.items():
        category = key.split('.')[0]
        if category not in categories:
            categories[category] = []
        categories[category].append(key)
    
    print(f"\n📁 Selector categories:")
    for category, keys in categories.items():
        print(f"  • {category}: {len(keys)} selectors")
    
    # Show some example selectors
    print(f"\n🔍 Example selectors:")
    
    # Featured snippet examples
    featured_examples = [k for k in selectors.selectors.keys() if 'featured_snippet' in k][:3]
    for key in featured_examples:
        selector_info = selectors.selectors[key]
        print(f"  • {key}")
        print(f"    Explanation: {selector_info['explanation']}")
        print(f"    XPath: {selector_info['xpath']}")
        print()
    
    # Related questions examples
    related_examples = [k for k in selectors.selectors.keys() if 'related_question' in k][:2]
    for key in related_examples:
        selector_info = selectors.selectors[key]
        print(f"  • {key}")
        print(f"    Explanation: {selector_info['explanation']}")
        print(f"    XPath: {selector_info['xpath']}")
        print()
    
    print("✅ Package is working correctly!")
    print("\n💡 To use in your own code:")
    print("   from webextractionhelper import Selectors")
    print("   selectors = Selectors()")
    print("   xpath = selectors.selectors['google.featured_snippet_title']['xpath']")

if __name__ == "__main__":
    main()
