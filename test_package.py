#!/usr/bin/env python3
"""
Simple test script to verify the webextractionhelper package works correctly.
"""

try:
    from webextractionhelper import Selectors
    print("✓ Successfully imported Selectors from webextractionhelper")
    
    # Test creating an instance
    selectors = Selectors()
    print("✓ Successfully created Selectors instance")
    
    # Test accessing selectors
    if hasattr(selectors, 'selectors'):
        print(f"✓ Selectors object has {len(selectors.selectors)} selectors")
        
        # Show a few example selectors
        for i, (key, value) in enumerate(list(selectors.selectors.items())[:3]):
            print(f"  - {key}: {value['explanation']}")
    else:
        print("✗ Selectors object missing 'selectors' attribute")
    
    print("\n🎉 Package test completed successfully!")
    
except ImportError as e:
    print(f"✗ Failed to import package: {e}")
except Exception as e:
    print(f"✗ Error during testing: {e}")
