#!/usr/bin/env python3
"""
Enhanced Amazon Archaeological Discovery System - Setup Script
Automates the complete installation and verification process
"""

import os
import sys
import subprocess
import platform

def check_python_version():
    """Check if Python version is adequate"""
    if sys.version_info < (3, 8):
        print("❌ Python 3.8+ required. Current version:", sys.version)
        print("📥 Download from: https://python.org")
        return False
    print(f"✅ Python {sys.version.split()[0]} detected")
    return True

def install_dependencies():
    """Install required Python packages"""
    print("📦 Installing dependencies...")
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
        print("✅ Dependencies installed successfully!")
        return True
    except subprocess.CalledProcessError:
        print("❌ Failed to install dependencies")
        print("💡 Try: pip install --upgrade pip")
        return False

def test_imports():
    """Test critical imports"""
    print("🔍 Testing imports...")
    
    critical_imports = [
        'google.earthengine',
        'numpy', 'pandas', 'matplotlib',
        'openai', 'PIL', 'cv2'
    ]
    
    failed_imports = []
    
    for module in critical_imports:
        try:
            if module == 'google.earthengine':
                import ee
                print("   ✅ Google Earth Engine API")
            elif module == 'cv2':
                import cv2
                print("   ✅ OpenCV")
            elif module == 'PIL':
                from PIL import Image
                print("   ✅ Pillow (PIL)")
            else:
                __import__(module)
                print(f"   ✅ {module}")
        except ImportError:
            failed_imports.append(module)
            print(f"   ❌ {module}")
    
    if failed_imports:
        print(f"\n❌ Failed imports: {', '.join(failed_imports)}")
        return False
    
    print("✅ All critical imports successful!")
    return True

def check_earth_engine():
    """Check Google Earth Engine authentication"""
    print("🌍 Checking Google Earth Engine...")
    
    try:
        import ee
        # Try to initialize (this will fail if not authenticated)
        ee.Initialize()
        print("✅ Google Earth Engine authenticated and ready!")
        return True
    except Exception as e:
        print("⚠️ Google Earth Engine not fully setup")
        print("\n🔧 Setup Instructions:")
        print("1. Go to: https://earthengine.google.com/")
        print("2. Sign up with Google account")
        print("3. Wait for approval (1-2 days)")
        print("4. Run: python -c 'import ee; ee.Authenticate(); ee.Initialize()'")
        print(f"\nError details: {e}")
        return False

def create_directories():
    """Create necessary output directories"""
    print("📁 Creating directory structure...")
    
    dirs = [
        'outputs/images/regional',
        'outputs/images/zones', 
        'outputs/images/sites',
        'outputs/analysis_results',
        'outputs/submissions'
    ]
    
    for dir_path in dirs:
        os.makedirs(dir_path, exist_ok=True)
        print(f"   ✅ {dir_path}")
    
    print("✅ Directory structure created!")

def check_openai_setup():
    """Check OpenAI API setup (optional)"""
    print("🤖 Checking OpenAI API setup...")
    
    # Check environment variable
    api_key = os.getenv('OPENAI_API_KEY')
    if api_key:
        print("✅ OpenAI API key found in environment")
        return True
    
    # Check keyring
    try:
        import keyring
        stored_key = keyring.get_password('openai', 'api_key')
        if stored_key:
            print("✅ OpenAI API key found in keyring")
            return True
    except:
        pass
    
    # Check .env file
    if os.path.exists('.env'):
        with open('.env', 'r') as f:
            if 'OPENAI_API_KEY' in f.read():
                print("✅ OpenAI API key found in .env file")
                return True
    
    print("⚠️ OpenAI API key not found (optional for testing)")
    print("💡 System will use mock AI responses for testing")
    print("🔑 To add real OpenAI API:")
    print("   export OPENAI_API_KEY='your-key-here'")
    return False

def test_system():
    """Test the main system startup"""
    print("🧪 Testing system startup...")
    
    try:
        # Try to import main system
        sys.path.insert(0, '.')
        from enhanced_main_system import EnhancedAmazonArchaeology
        
        print("✅ Main system imports successfully!")
        
        # Try to initialize (this tests all components)
        print("   🔧 Testing component initialization...")
        system = EnhancedAmazonArchaeology()
        print("✅ All components initialized successfully!")
        
        return True
        
    except Exception as e:
        print(f"❌ System test failed: {e}")
        return False

def main():
    """Main setup routine"""
    print("🏛️ Enhanced Amazon Archaeological Discovery System")
    print("=" * 60)
    print("🚀 AUTOMATED SETUP & VERIFICATION")
    print()
    
    setup_steps = [
        ("Python Version", check_python_version),
        ("Dependencies", install_dependencies),
        ("Imports", test_imports),
        ("Directories", create_directories),
        ("Google Earth Engine", check_earth_engine),
        ("OpenAI API", check_openai_setup),
        ("System Test", test_system)
    ]
    
    results = {}
    
    for step_name, step_func in setup_steps:
        print(f"\n📋 {step_name}...")
        print("-" * 30)
        results[step_name] = step_func()
    
    # Summary
    print(f"\n🎯 SETUP SUMMARY")
    print("=" * 30)
    
    critical_steps = ["Python Version", "Dependencies", "Imports", "System Test"]
    optional_steps = ["Google Earth Engine", "OpenAI API"]
    
    critical_passed = all(results[step] for step in critical_steps)
    optional_passed = sum(results[step] for step in optional_steps)
    
    for step, passed in results.items():
        status = "✅ PASS" if passed else "❌ FAIL"
        critical = "🔴 CRITICAL" if step in critical_steps else "🟡 OPTIONAL"
        print(f"{status} {critical} {step}")
    
    print()
    
    if critical_passed:
        print("🎉 SETUP SUCCESSFUL!")
        print("✅ All critical components working")
        print(f"📊 Optional components: {optional_passed}/2 working")
        print()
        print("🚀 Ready to run:")
        print("   python enhanced_main_system.py")
        print()
        if not results["Google Earth Engine"]:
            print("⚠️ Note: Complete Google Earth Engine setup for real data")
        if not results["OpenAI API"]:
            print("⚠️ Note: System will use mock AI responses until OpenAI API configured")
    else:
        print("❌ SETUP INCOMPLETE")
        print("🔧 Please fix critical issues above before proceeding")
        failed_critical = [step for step in critical_steps if not results[step]]
        print(f"❌ Failed: {', '.join(failed_critical)}")

if __name__ == "__main__":
    main() 