# Unified Selectors for Web Scraping

This module provides a comprehensive and unified collection of selectors for extracting various elements from web pages. It includes methods for XPath, regex, and CSS selectors, with a focus on Google search features and general web scraping.

## Key Features

- **Unified Structure**: Each selector is an object that can contain multiple extraction methods (`xpath`, `regex`, `css`).
- **Namespaced Selectors**: Clear and organized naming conventions (e.g., `google.*`, `og.*`, `x.*`).
- **Dynamic Parameters**: Support for parameterized selectors for flexible and reusable extraction logic.
- **Comprehensive Coverage**: Extensive library of selectors for Google SERPs, meta tags, content elements, and more.
- **Easy-to-Use API**: Simple convenience functions for quick access to selectors and extraction methods.

## Installation

This module requires `lxml` for XPath processing.

```bash
pip install lxml
```

## Basic Usage

### Import the Module

```python
from src.helpers.selectors import get_selector, get_explanation, extract
```

### Extracting Data

The primary function `extract` allows you to specify the selector name, the HTML content, and the extraction method.

```python
# Extract all H1 headings using XPath (default method)
h1_headings = extract('headings.h1', html_string)

# Extract Google Analytics ID using regex
ga_id = extract('analytics.google_analytics_id', html_string, method='regex')

# Extract Open Graph title using XPath
og_title = extract('og.title', html_string, method='xpath')
```

### Dynamic Selectors with Parameters

Use keyword arguments to pass parameters to dynamic selectors.

```python
# Extract all links to a specific domain
domain_links = extract('links.to_domain', html_string, domain='example.com')

# Extract all elements with a specific class
elements = extract('generic.elements_by_class', html_string, class_name='product-card')
```

### Getting Selector Information

You can also retrieve the raw selector pattern and its explanation.

```python
# Get the XPath for Open Graph titles
og_title_xpath = get_selector('og.title', method='xpath')

# Get the regex for Google Analytics IDs
ga_id_regex = get_selector('analytics.google_analytics_id', method='regex')

# Get the explanation for a selector
explanation = get_explanation('og.title')
```

## Complete Selector Reference

The following table provides a comprehensive list of all available selectors, their extraction methods, and their sources.

| Selector Name | Methods | Description | Source |
|---|---|---|---|
| **Google Search Features** |
| `google.featured_snippet_title` | `xpath` | Featured snippet page title | [screamingfrog](https://www.screamingfrog.co.uk/blog/how-to-scrape-google-search-features-using-xpath/) |
| `google.featured_snippet_text` | `xpath` | Featured snippet description text | [screamingfrog](https://www.screamingfrog.co.uk/blog/how-to-scrape-google-search-features-using-xpath/) |
| `google.related_questions_all` | `xpath` | All "People also ask" questions | [screamingfrog](https://www.screamingfrog.co.uk/blog/how-to-scrape-google-search-features-using-xpath/) |
| `google.search_result_links` | `xpath` | Search result links | [screamingfrog](https://www.screamingfrog.co.uk/blog/how-to-scrape-google-search-features-using-xpath/) |
| **Meta Tags** |
| `meta.title` | `xpath` | Page title from title tag | [screamingfrog](https://www.screamingfrog.co.uk/seo-spider/tutorials/web-scraping/) |
| `meta.description` | `xpath` | Meta description content | [screamingfrog](https://www.screamingfrog.co.uk/seo-spider/tutorials/web-scraping/) |
| **Open Graph (og:)** |
| `og.title` | `xpath` | Open Graph title | [screamingfrog](https://www.screamingfrog.co.uk/seo-spider/tutorials/web-scraping/) |
| `og.description` | `xpath` | Open Graph description | [screamingfrog](https://www.screamingfrog.co.uk/seo-spider/tutorials/web-scraping/) |
| `og.image` | `xpath` | Open Graph image URL | [screamingfrog](https://www.screamingfrog.co.uk/seo-spider/tutorials/web-scraping/) |
| **Twitter/X Cards** |
| `x.title` | `xpath` | Twitter title | [screamingfrog](https://www.screamingfrog.co.uk/seo-spider/tutorials/web-scraping/) |
| `x.description` | `xpath` | Twitter description | [screamingfrog](https://www.screamingfrog.co.uk/seo-spider/tutorials/web-scraping/) |
| **Structured Data** |
| `structured_data.json_ld` | `xpath`, `regex` | JSON-LD structured data scripts | [screamingfrog](https://www.screamingfrog.co.uk/seo-spider/tutorials/web-scraping/) |
| `structured_data.microdata` | `xpath` | Microdata structured data elements | [screamingfrog](https://www.screamingfrog.co.uk/seo-spider/tutorials/web-scraping/) |
| `structured_data.product` | `regex` | Product name from JSON-LD | [screamingfrog](https://www.screamingfrog.co.uk/seo-spider/tutorials/web-scraping/) |
| **Analytics and Tracking** |
| `analytics.google_analytics_id` | `xpath`, `regex` | Google Analytics UA tracking ID | [screamingfrog](https://www.screamingfrog.co.uk/seo-spider/tutorials/web-scraping/) |
| `analytics.google_tag_manager_id` | `xpath`, `regex` | Google Tag Manager GTM ID | [screamingfrog](https://www.screamingfrog.co.uk/seo-spider/tutorials/web-scraping/) |
| `analytics.google_analytics_ga4` | `regex` | Google Analytics 4 measurement ID | [screamingfrog](https://www.screamingfrog.co.uk/seo-spider/tutorials/web-scraping/) |
| **General Content** |
| `headings.all` | `xpath` | All heading elements | [screamingfrog](https://www.screamingfrog.co.uk/seo-spider/tutorials/web-scraping/) |
| `headings.h1` | `xpath` | H1 headings | [screamingfrog](https://www.screamingfrog.co.uk/seo-spider/tutorials/web-scraping/) |
| `images.all` | `xpath` | All images | [screamingfrog](https://www.screamingfrog.co.uk/seo-spider/tutorials/web-scraping/) |
| **Dynamic/Parameterized Selectors** |
| `links.to_domain` | `xpath` | Links to specific domain (`domain` parameter) | [screamingfrog](https://www.screamingfrog.co.uk/seo-spider/tutorials/web-scraping/) |
| `generic.elements_by_class` | `xpath` | Elements with specific class (`class_name` parameter) | [screamingfrog](https://www.screamingfrog.co.uk/seo-spider/tutorials/web-scraping/) |
| `generic.elements_by_attribute` | `xpath` | Elements by attribute (`attribute_name`, `attribute_value`) | [screamingfrog](https://www.screamingfrog.co.uk/seo-spider/tutorials/web-scraping/) |

## Full Usage Example

```python
import re
from src.helpers.selectors import extract

# Sample HTML content
html_string = """
<html>
  <head>
    <title>My Awesome Page</title>
    <meta property="og:title" content="Open Graph Title" />
    <script>
      var gaId = 'UA-123456-7';
    </script>
  </head>
  <body>
    <h1>Main Heading</h1>
    <a href="https://example.com/page1">Link 1</a>
    <div class="product-card">Product A</div>
  </body>
</html>
"""

# Extract data using various selectors and methods
page_title = extract('meta.title', html_string, method='xpath')
og_title = extract('og.title', html_string, method='xpath')
ga_id = extract('analytics.google_analytics_id', html_string, method='regex')
links = extract('links.to_domain', html_string, domain='example.com')
product_cards = extract('generic.elements_by_class', html_string, class_name='product-card')

print(f"Page Title: {page_title}")
print(f"Open Graph Title: {og_title}")
print(f"Google Analytics ID: {ga_id}")
print(f"Links to example.com: {links}")
print(f"Product Cards: {product_cards}")
```

## Advanced Usage

For more advanced use cases, you can create your own instance of the `Selectors` class.

```python
from src.helpers.selectors import Selectors

# Create an instance
selectors = Selectors()

# Get all available selectors
all_selectors = selectors.get_all_selectors()

# Iterate and apply selectors
for name, data in all_selectors.items():
    if 'xpath' in data:
        print(f"Extracting {name} with XPath...")
        results = selectors.extract(name, html_string, method='xpath')
        print(results)
```

## Sources

- [How to Scrape Google Search Features Using XPath](https://www.screamingfrog.co.uk/blog/how-to-scrape-google-search-features-using-xpath/)
- [Web Scraping & Custom Extraction Tutorial](https://www.screamingfrog.co.uk/seo-spider/tutorials/web-scraping/)

## License

This module is provided for educational and development purposes. Please respect the original sources and website Terms of Service.
