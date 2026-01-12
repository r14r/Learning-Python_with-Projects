#!/usr/bin/env python3
"""
Metaclass Validator Script
Data validation using metaclasses and descriptors.
"""

from typing import Any, Type

class TypedProperty:
    """Descriptor for type-validated properties."""
    
    def __init__(self, name: str, expected_type: Type):
        """
        Initialize typed property.
        
        Args:
            name: Property name
            expected_type: Expected type
        """
        self.name = name
        self.expected_type = expected_type
        self.data_name = f'_{name}'
    
    def __get__(self, instance, owner):
        """Get property value."""
        if instance is None:
            return self
        return getattr(instance, self.data_name, None)
    
    def __set__(self, instance, value):
        """Set property value with type validation."""
        if not isinstance(value, self.expected_type):
            raise TypeError(
                f"{self.name} must be {self.expected_type.__name__}, "
                f"got {type(value).__name__}"
            )
        setattr(instance, self.data_name, value)

class RangeValidator:
    """Descriptor for range-validated numeric properties."""
    
    def __init__(self, name: str, min_value: float = None, max_value: float = None):
        """
        Initialize range validator.
        
        Args:
            name: Property name
            min_value: Minimum allowed value
            max_value: Maximum allowed value
        """
        self.name = name
        self.min_value = min_value
        self.max_value = max_value
        self.data_name = f'_{name}'
    
    def __get__(self, instance, owner):
        """Get property value."""
        if instance is None:
            return self
        return getattr(instance, self.data_name, None)
    
    def __set__(self, instance, value):
        """Set property value with range validation."""
        if not isinstance(value, (int, float)):
            raise TypeError(f"{self.name} must be a number")
        
        if self.min_value is not None and value < self.min_value:
            raise ValueError(f"{self.name} must be >= {self.min_value}")
        
        if self.max_value is not None and value > self.max_value:
            raise ValueError(f"{self.name} must be <= {self.max_value}")
        
        setattr(instance, self.data_name, value)

class ValidatorMeta(type):
    """Metaclass that automatically creates validators for annotated fields."""
    
    def __new__(mcs, name, bases, namespace, **kwargs):
        """
        Create new class with automatic validators.
        
        Args:
            name: Class name
            bases: Base classes
            namespace: Class namespace
        
        Returns:
            New class
        """
        # Get type annotations
        annotations = namespace.get('__annotations__', {})
        
        # Get validation rules
        validators = namespace.get('__validators__', {})
        
        # Create descriptors for annotated fields
        for field_name, field_type in annotations.items():
            if field_name.startswith('_'):
                continue
            
            # Check if custom validator is defined
            if field_name in validators:
                validator_config = validators[field_name]
                
                if 'min' in validator_config or 'max' in validator_config:
                    namespace[field_name] = RangeValidator(
                        field_name,
                        validator_config.get('min'),
                        validator_config.get('max')
                    )
                else:
                    namespace[field_name] = TypedProperty(field_name, field_type)
            else:
                # Use type validation by default
                namespace[field_name] = TypedProperty(field_name, field_type)
        
        return super().__new__(mcs, name, bases, namespace)

def main():
    print("Step 3: Kernbausteine geladen.")

if __name__ == "__main__":
    main()
