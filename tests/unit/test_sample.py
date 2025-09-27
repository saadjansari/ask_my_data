"""Sample test file to demonstrate test structure."""

import pytest


class TestSample:
    """Sample test class."""

    def test_always_passes(self):
        """Test that always passes."""
        assert True

    def test_simple_math(self):
        """Test simple mathematical operations."""
        assert 2 + 2 == 4
        assert 3 * 3 == 9

    @pytest.mark.slow
    def test_slow_operation(self):
        """Test marked as slow."""
        # This would be a slow test
        assert True
