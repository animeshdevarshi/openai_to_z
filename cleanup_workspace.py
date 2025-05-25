#!/usr/bin/env python3
"""
Workspace Cleanup Script
Removes old messy folder structures, keeping only clean organized results
"""

import os
import shutil
import glob
from datetime import datetime

def cleanup_workspace():
    """Clean up old messy folder structures"""
    print("🧹 WORKSPACE CLEANUP")
    print("=" * 40)
    print("🗂️ Removing old messy folder structures...")
    
    # Folders to remove (old messy structure)
    folders_to_remove = [
        "submissions",  # old submissions folder if exists
        ".ipynb_checkpoints"
    ]
    
    # Clean up old outputs structure but preserve final_results
    if os.path.exists("outputs"):
        print(f"   🔍 Cleaning outputs folder...")
        # Keep only final_results folders in outputs
        for item in os.listdir("outputs"):
            item_path = os.path.join("outputs", item)
            if not item.startswith("final_results_"):
                try:
                    if os.path.isdir(item_path):
                        shutil.rmtree(item_path)
                        print(f"   🗑️ Removed outputs/{item}/")
                        removed_count += 1
                    else:
                        os.remove(item_path)
                        print(f"   🗑️ Removed outputs/{item}")
                        removed_count += 1
                except Exception as e:
                    print(f"   ⚠️ Could not remove outputs/{item}: {e}")
    
    # Files to remove (unnecessary)
    files_to_remove = [
        "test_real_ai.py",
        "test_ai_output.py", 
        "implementation_guide.md",
        "main.py",
        "comprehensive_regions.json"
    ]
    
    removed_count = 0
    
    # Remove old folders
    for folder in folders_to_remove:
        if os.path.exists(folder):
            try:
                shutil.rmtree(folder)
                print(f"   🗑️ Removed folder: {folder}/")
                removed_count += 1
            except Exception as e:
                print(f"   ⚠️ Could not remove {folder}: {e}")
    
    # Remove unnecessary files
    for file in files_to_remove:
        if os.path.exists(file):
            try:
                os.remove(file)
                print(f"   🗑️ Removed file: {file}")
                removed_count += 1
            except Exception as e:
                print(f"   ⚠️ Could not remove {file}: {e}")
    
    print(f"\n✅ Cleanup complete! Removed {removed_count} items")
    
    # Show what we have left
    print(f"\n📁 CLEAN WORKSPACE STRUCTURE:")
    print("=" * 30)
    
    # List remaining items
    items = []
    for item in os.listdir('.'):
        if os.path.isdir(item):
            if item == 'outputs':
                # Check for final_results inside outputs
                final_results_count = len(glob.glob("outputs/final_results_*"))
                if final_results_count > 0:
                    items.append(f"📂 {item}/ - 🏛️ CLEAN ORGANIZED RESULTS ({final_results_count} runs)")
                else:
                    items.append(f"📂 {item}/")
            elif item == 'archive':
                items.append(f"📦 {item}/ - Previous runs backup")
            elif item == 'src':
                items.append(f"⚙️ {item}/ - System source code")
            elif item == '.git':
                items.append(f"🔗 {item}/ - Git repository")
            else:
                items.append(f"📂 {item}/")
        else:
            if item.endswith('.py'):
                if 'clean' in item:
                    items.append(f"🚀 {item} - Main clean runner")
                elif 'organize' in item:
                    items.append(f"📁 {item} - Results organizer")
                else:
                    items.append(f"⚙️ {item}")
            elif item.endswith('.md'):
                items.append(f"📖 {item}")
            elif item.endswith('.json'):
                items.append(f"⚙️ {item}")
            else:
                items.append(f"📄 {item}")
    
    # Sort and display
    for item in sorted(items):
        print(f"   {item}")
    
    # Find the latest results folder
    results_folders = glob.glob("outputs/final_results_*")
    if results_folders:
        latest_results = max(results_folders, key=os.path.getmtime)
        print(f"\n🎯 LATEST RESULTS: {latest_results}/")
        print(f"   📖 Start here: {latest_results}/README.md")
        print(f"   🔍 Discoveries: {latest_results}/2_discoveries/")
        print(f"   🏛️ Submission: {latest_results}/1_submission/")

def main():
    """Main cleanup function"""
    print("🧹 ARCHAEOLOGICAL WORKSPACE CLEANUP")
    print("=" * 50)
    print("📁 This will remove old messy folder structures")
    print("✅ Clean organized results will be preserved")
    print("📦 Previous runs are safely archived")
    
    confirm = input(f"\nProceed with cleanup? (y/N): ").strip().lower()
    if confirm != 'y':
        print("❌ Cleanup cancelled")
        return
    
    cleanup_workspace()
    
    print(f"\n🎉 WORKSPACE IS NOW CLEAN!")
    print("=" * 30)
    print("✅ Only clean organized results remain")
    print("🚀 Ready for easy navigation and sharing")

if __name__ == "__main__":
    main() 