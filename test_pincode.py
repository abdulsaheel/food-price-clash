#!/usr/bin/env python3
"""
Test script for pincode functionality
"""

from pincode_mapping import (
    get_city_from_pincode, 
    validate_pincode, 
    get_nearby_cities,
    get_supported_cities
)

def test_pincode_functionality():
    """Test the pincode mapping functionality"""
    
    print("🚀 Testing Pincode Functionality\n")
    
    # Test validation
    print("1. Testing Pincode Validation:")
    test_codes = ["110001", "12345", "abcdef", "1100011", ""]
    for code in test_codes:
        is_valid = validate_pincode(code)
        print(f"   {code:<8} → {'✅ Valid' if is_valid else '❌ Invalid'}")
    
    print()
    
    # Test city mapping
    print("2. Testing City Mapping:")
    test_pincodes = ["110001", "400001", "560001", "500001", "600001", "999999"]
    for pincode in test_pincodes:
        city = get_city_from_pincode(pincode)
        print(f"   {pincode} → {city if city else 'Not found'}")
    
    print()
    
    # Test nearby cities
    print("3. Testing Nearby Cities:")
    test_pincode = "110001"
    nearby = get_nearby_cities(test_pincode, radius=2)
    print(f"   {test_pincode} nearby cities: {nearby}")
    
    print()
    
    # Show supported cities
    print("4. Supported Cities:")
    cities = get_supported_cities()
    print(f"   Total cities: {len(cities)}")
    print(f"   Cities: {', '.join(sorted(cities))}")
    
    print("\n✅ All tests completed!")

if __name__ == "__main__":
    test_pincode_functionality()
