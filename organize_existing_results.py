#!/usr/bin/env python3
"""
Standalone Output Organizer
Organizes existing archaeological discovery results into clean structure:
1. submission/ - JSON and MD submission files
2. discoveries/ - Top discoveries with images and details  
3. processed_images/ - All processed satellite images
4. metadata/ - Technical analysis data
"""

import os
import sys

# Add src to path
sys.path.append('src')

from src.utils.output_organizer import OutputOrganizer

def main():
    """Organize existing results into clean structure"""
    print("🏛️ STANDALONE OUTPUT ORGANIZER")
    print("=" * 50)
    print("📁 Organizing existing archaeological results...")
    
    # Check if we have any results to organize
    check_dirs = [
        "outputs/competition_submissions",
        "outputs/satellite_imagery", 
        "outputs/archaeological_analysis"
    ]
    
    has_results = any(os.path.exists(d) for d in check_dirs)
    
    if not has_results:
        print("❌ No existing results found to organize")
        print("💡 Run the main pipeline first: python3 main.py")
        return
    
    # Initialize organizer
    organizer = OutputOrganizer()
    
    # Organize outputs
    try:
        clean_output_dir = organizer.organize_outputs(temp_base=None)
        
        print(f"\n🎉 SUCCESS! Results organized into clean structure")
        print("=" * 50)
        print(f"📁 Clean results location: {clean_output_dir}/")
        print(f"\n📂 Folder structure:")
        print(f"   🏛️ 1_submission/     - JSON and MD submission files")
        print(f"   🔍 2_discoveries/    - Top discoveries with images")  
        print(f"   📸 3_processed_images/ - All processed satellite imagery")
        print(f"   📊 4_metadata/       - Technical analysis data")
        print(f"\n🚀 Quick Start:")
        print(f"   1. Open {clean_output_dir}/README.md for overview")
        print(f"   2. Browse {clean_output_dir}/2_discoveries/ for detailed findings")
        print(f"   3. Check {clean_output_dir}/1_submission/ for competition files")
        
    except Exception as e:
        print(f"❌ Error organizing results: {e}")
        print("💡 Check that you have valid results to organize")

if __name__ == "__main__":
    main() 