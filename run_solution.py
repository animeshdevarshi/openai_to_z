#!/usr/bin/env python3
"""
Quick Terminal Runner for Archaeological Discovery Solution
Run with: python run_solution.py
"""

import os
import sys
from datetime import datetime

def check_environment():
    """Check if environment is properly configured"""
    print("🔍 Checking environment...")
    
    # Check if .env file exists
    if not os.path.exists('.env'):
        print("❌ .env file not found. Please create it with your OpenAI API key.")
        print("Example: echo 'OPENAI_API_KEY=your-key-here' > .env")
        return False
    
    # Check if OpenAI key is set
    from dotenv import load_dotenv
    load_dotenv()
    
    api_key = os.getenv('OPENAI_API_KEY')
    if not api_key:
        print("❌ OPENAI_API_KEY not found in .env file")
        return False
    
    print("✅ Environment configured correctly")
    return True

def test_components():
    """Test individual components"""
    print("\n🧪 Testing system components...")
    
    try:
        # Test AI Analyzer
        from enhanced_ai_analyzer import EnhancedAIAnalyzer
        analyzer = EnhancedAIAnalyzer()
        print("✅ AI Analyzer: Ready")
        
        # Test Region Config
        from simple_region_config import SimpleRegionConfig
        config = SimpleRegionConfig()
        print("✅ Region Config: Ready")
        
        # Test Data Processor
        from enhanced_data_processor import EnhancedDataProcessor
        processor = EnhancedDataProcessor()
        print("✅ Data Processor: Ready")
        
        # Test Results Manager
        from enhanced_results_manager import EnhancedResultsManager
        results = EnhancedResultsManager()
        print("✅ Results Manager: Ready")
        
        return True
        
    except ImportError as e:
        print(f"❌ Import error: {e}")
        return False
    except Exception as e:
        print(f"❌ Component test failed: {e}")
        return False

def run_simple_test():
    """Run a simple test of the AI analyzer"""
    print("\n🤖 Running AI Analyzer test...")
    
    try:
        from enhanced_ai_analyzer import EnhancedAIAnalyzer
        analyzer = EnhancedAIAnalyzer()
        
        # Test prompt creation
        test_prompt = analyzer.create_regional_prompt(
            region_info={'region_name': 'Test Region', 'center': '10.5°S, 65.8°W'},
            images={}
        )
        
        print("✅ AI Analyzer test completed")
        print(f"📝 Generated prompt: {len(test_prompt)} characters")
        return True
        
    except Exception as e:
        print(f"❌ AI Analyzer test failed: {e}")
        return False

def run_full_system():
    """Run the complete system"""
    print("\n🚀 Starting full archaeological discovery system...")
    
    try:
        # Import the main system
        from enhanced_main_system import EnhancedAmazonArchaeology
        
        # Initialize system
        system = EnhancedAmazonArchaeology()
        
        print("\n" + "="*60)
        print("🏛️ ENHANCED AMAZON ARCHAEOLOGICAL DISCOVERY")
        print("="*60)
        
        # Step 1: Authentication
        print("\n1️⃣ Setting up authentication...")
        if not system.step_1_setup_and_authentication():
            print("❌ Authentication failed")
            return False
        
        # Step 2: Load data (small test)
        print("\n2️⃣ Loading test data...")
        if not system.step_2_load_dual_source_data(max_regions=1):
            print("❌ Data loading failed")
            return False
        
        print("\n✅ System test completed successfully!")
        print(f"📁 Check the 'enhanced_images' folder for generated images")
        return True
        
    except Exception as e:
        print(f"❌ Full system test failed: {e}")
        return False

def main():
    """Main execution function"""
    print("🏛️ Archaeological Discovery Solution - Terminal Runner")
    print("=" * 60)
    
    # Check environment
    if not check_environment():
        sys.exit(1)
    
    # Test components
    if not test_components():
        print("\n❌ Component tests failed. Please check your installation.")
        sys.exit(1)
    
    # Run simple test
    if not run_simple_test():
        print("\n❌ AI Analyzer test failed. Please check your OpenAI API key.")
        sys.exit(1)
    
    # Ask user what to do
    print("\n🎯 What would you like to do?")
    print("1. Run full archaeological discovery system")
    print("2. Run component tests only")
    print("3. Exit")
    
    choice = input("\nEnter choice (1-3): ").strip()
    
    if choice == "1":
        if run_full_system():
            print("\n🎉 Full system completed successfully!")
        else:
            print("\n❌ Full system failed")
            sys.exit(1)
    elif choice == "2":
        print("\n✅ Component tests completed")
    else:
        print("\n👋 Goodbye!")
    
    print(f"\n📝 Execution completed at {datetime.now()}")

if __name__ == "__main__":
    main() 