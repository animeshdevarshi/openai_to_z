#!/usr/bin/env python3
"""
Clean End-to-End Archaeological Discovery System
- Simple region selection
- Auto-archive previous runs
- Smooth execution without interruptions
"""

import os
import shutil
import json
import glob
from datetime import datetime
from pathlib import Path

# Import system components
from src.core.main_system import ArchaeologicalDiscoverySystem
from src.config.regions import load_regions_from_file
from src.utils.output_organizer import OutputOrganizer

def archive_previous_runs():
    """Archive previous runs with datetime stamp"""
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    archive_dir = f"archive/run_{timestamp}"
    
    # Create archive directory
    os.makedirs(archive_dir, exist_ok=True)
    
    # Archive directories that contain results  
    to_archive = [
        "outputs/satellite_imagery",
        "outputs/archaeological_analysis", 
        "outputs/processed_data",
        "outputs/competition_submissions",
        "outputs/pipeline_progress.json"
    ]
    
    # Also archive any previous final_results directories
    final_results_dirs = glob.glob("outputs/final_results_*")
    to_archive.extend(final_results_dirs)
    
    archived_count = 0
    for item in to_archive:
        if os.path.exists(item):
            if os.path.isdir(item):
                shutil.move(item, f"{archive_dir}/{os.path.basename(item)}")
            else:
                shutil.move(item, f"{archive_dir}/{os.path.basename(item)}")
            archived_count += 1
    
    # Clean up any remaining messy directories in outputs
    if os.path.exists("outputs"):
        for item in os.listdir("outputs"):
            item_path = os.path.join("outputs", item)
            if not item.startswith("final_results_") and os.path.isdir(item_path):
                # These are messy folders - remove them
                shutil.rmtree(item_path)
                print(f"🧹 Cleaned up messy folder: outputs/{item}")
                archived_count += 1
    
    if archived_count > 0:
        print(f"📦 Archived {archived_count} items to: {archive_dir}")
    else:
        print("🔍 No previous runs found to archive")
    
    return archive_dir

def select_regions():
    """Simple region selection interface"""
    print("\n🌍 REGION SELECTION")
    print("=" * 50)
    
    # Load available regions
    regions = load_regions_from_file()
    region_list = list(regions.items())
    
    print("Available regions:")
    for i, (region_id, region_data) in enumerate(region_list, 1):
        priority = region_data.get('priority', 'medium')
        region_type = region_data.get('type', 'exploration')
        priority_emoji = "🔴" if priority == "high" else "🟡" if priority == "medium" else "🔵"
        type_emoji = "🏛️" if region_type == "known_sites" else "🔍"
        
        print(f"  {i}. {region_id}: {region_data['name']} - {priority_emoji} {priority} - {type_emoji} {region_type}")
    
    print(f"\nOptions:")
    print(f"  A. All regions ({len(regions)} total)")
    print(f"  R. Recommended regions (high priority)")
    print(f"  1-{len(regions)}. Select specific region(s) by number")
    print(f"       Example: '2' for one region, '1,3' for multiple regions")
    
    while True:
        choice = input(f"\nSelect option (A/R/1-{len(regions)}): ").strip().upper()
        
        if choice == 'A':
            selected = list(regions.keys())
            print(f"\n✅ Selected ALL regions:")
            for i, region_id in enumerate(selected, 1):
                print(f"  {i}. {region_id}: {regions[region_id]['name']}")
            return selected
            
        elif choice == 'R':
            # Return high priority regions
            selected = [rid for rid, data in regions.items() if data.get('priority') == 'high']
            print(f"\n✅ Selected RECOMMENDED regions:")
            for i, region_id in enumerate(selected, 1):
                print(f"  {i}. {region_id}: {regions[region_id]['name']}")
            return selected
            
        else:
            try:
                # Handle comma-separated numbers
                if ',' in choice:
                    indices = [int(x.strip()) for x in choice.split(',')]
                else:
                    indices = [int(choice)]
                
                # Validate indices
                if all(1 <= i <= len(regions) for i in indices):
                    selected = [region_list[i-1][0] for i in indices]  # Get region_id from tuple
                    print(f"\n✅ Selected {len(selected)} region(s):")
                    for i, region_id in enumerate(selected, 1):
                        print(f"  {i}. {region_id}: {regions[region_id]['name']}")
                    return selected
                else:
                    print(f"❌ Invalid selection. Please choose numbers 1-{len(regions)}")
            except ValueError:
                print("❌ Invalid input. Please enter A, R, or numbers (e.g., '2' or '1,3')")

def run_clean_pipeline():
    """Run the complete pipeline cleanly"""
    print("🏛️ CLEAN ARCHAEOLOGICAL DISCOVERY SYSTEM")
    print("=" * 60)
    print("🎯 OpenAI to Z Challenge - Checkpoint 2 Solution")
    print("🔬 Multi-scale Analysis: 50km → 10km → 2km")
    print("🤖 AI-powered with o3 Model + Open Discovery Prompts")
    print("✅ Full Checkpoint 2 Compliance")
    
    # Step 1: Archive previous runs
    print(f"\n📦 STEP 1: Clean Previous Runs")
    print("-" * 30)
    archive_dir = archive_previous_runs()
    
    # Step 2: Select regions
    selected_regions = select_regions()
    print(f"\n✅ Selected {len(selected_regions)} regions: {', '.join(selected_regions)}")
    
    # Step 3: Confirm and run
    print(f"\n🚀 STEP 2: Execute Pipeline")
    print("-" * 30)
    print(f"📍 Regions: {', '.join(selected_regions)}")
    print(f"🤖 AI Model: o3 with high reasoning effort")
    print(f"📝 Prompts: Open discovery approach")
    print(f"⏱️ Estimated time: {len(selected_regions) * 10}-{len(selected_regions) * 20} minutes")
    
    confirm = input(f"\nProceed with clean pipeline? (y/N): ").strip().lower()
    if confirm != 'y':
        print("❌ Operation cancelled")
        return
    
    # Step 4: Initialize and run system
    print(f"\n🔧 Initializing system...")
    try:
        # Initialize the system
        system = ArchaeologicalDiscoverySystem()
        print("✅ System initialized")
        
        # Run the complete pipeline
        print(f"\n🚀 EXECUTING COMPLETE PIPELINE")
        print("=" * 50)
        
        # Override the region selection in the system
        system.selected_regions = selected_regions
        
        # Run each step cleanly
        print("🔑 Step 1: Authentication...")
        auth_result = system.setup_authentication()
        if not auth_result:
            print("❌ Authentication failed")
            return
        print("✅ Authentication complete")
        
        print(f"\n📡 Step 2: Loading data for {len(selected_regions)} regions...")
        data_result = system.load_satellite_data()
        if not data_result:
            print("❌ Data loading failed")
            return
        print("✅ Data loading complete")
        
        print(f"\n🔬 Step 3: Multi-scale processing...")
        processing_result = system.process_multi_scale()
        if not processing_result:
            print("❌ Processing failed")
            return
        print("✅ Processing complete")
        
        print(f"\n🤖 Step 4: AI analysis with o3 model...")
        ai_result = system.run_ai_analysis()
        if not ai_result:
            print("❌ AI analysis failed")
            return
        print("✅ AI analysis complete")
        
        print(f"\n📦 Step 5: Creating submission...")
        submission_result = system.create_submission()
        if submission_result:
            print("🎉 SUCCESS! Checkpoint 2 submission created")
            
            # Step 6: Organize outputs into clean structure
            print(f"\n📁 Step 6: Organizing clean outputs...")
            organizer = OutputOrganizer()
            clean_output_dir = organizer.organize_outputs(system.final_submission, system.temp_base)
            
            print(f"\n🎉 COMPLETE SUCCESS!")
            print("=" * 50)
            print(f"📁 Clean results organized in: {clean_output_dir}/")
            print(f"📂 Folder structure:")
            print(f"   🏛️ 1_submission/ - JSON and MD submission files")
            print(f"   🔍 2_discoveries/ - Top discoveries with images")
            print(f"   📸 3_processed_images/ - All processed satellite imagery")
            print(f"   📊 4_metadata/ - Technical analysis data")
            print(f"\n🚀 Quick Start:")
            print(f"   1. Open {clean_output_dir}/README.md for overview")
            print(f"   2. Browse 2_discoveries/ for detailed findings")
            print(f"   3. Check 1_submission/ for competition files")
        else:
            print("❌ Submission creation failed")
            
    except Exception as e:
        print(f"❌ Pipeline failed: {e}")
        print(f"📦 Previous runs archived in: {archive_dir}")
        raise

def main():
    """Main entry point"""
    try:
        run_clean_pipeline()
    except KeyboardInterrupt:
        print(f"\n\n⚠️ Pipeline interrupted by user")
    except Exception as e:
        print(f"\n\n❌ Pipeline failed with error: {e}")
        print(f"💡 Try running again or check the archived data")

if __name__ == "__main__":
    main() 