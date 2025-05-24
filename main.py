#!/usr/bin/env python3
"""
Archaeological Discovery System - Main Launcher
Clean entry point for the organized archaeological discovery system
"""

import sys
import os

# Add src directory to Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

# Import from organized structure
from core.main_system import main

if __name__ == "__main__":
    main() 