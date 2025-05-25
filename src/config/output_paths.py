# output_config.py
# Archaeological Discovery System - Clean Output Configuration
# Uses temporary processing folders and creates only clean final results

import os
import tempfile
from datetime import datetime

# Clean output structure - only final results in outputs
BASE_OUTPUT_DIR = "outputs"

def get_paths() -> dict:
    """
    Get all paths for processing - uses temp directories during processing
    Only the final organized results go to outputs/final_results_*
    """
    
    # Create timestamp for this session
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    
    # Use temporary directories for intermediate processing
    temp_base = tempfile.mkdtemp(prefix="archaeology_temp_")
    
    paths = {
        'base': BASE_OUTPUT_DIR,
        'timestamp': timestamp,
        'temp_base': temp_base,
        
        # Temporary processing paths (will be cleaned up)
        'satellite_imagery': os.path.join(temp_base, 'satellite_imagery'),
        'archaeological_analysis': os.path.join(temp_base, 'archaeological_analysis'),
        'competition_submissions': os.path.join(temp_base, 'competition_submissions'),
        'processed_data': os.path.join(temp_base, 'processed_data'),
        
        # Imagery subcategories (temporary)
        'regional_imagery': os.path.join(temp_base, 'satellite_imagery', 'regional'),
        'zone_imagery': os.path.join(temp_base, 'satellite_imagery', 'zone'),
        'site_imagery': os.path.join(temp_base, 'satellite_imagery', 'site'),
        
        # Analysis subcategories (temporary)
        'ai_responses': os.path.join(temp_base, 'archaeological_analysis', 'ai_responses'),
        'discoveries': os.path.join(temp_base, 'archaeological_analysis', 'discoveries'),
        'prompts_database': os.path.join(temp_base, 'archaeological_analysis', 'prompts_database'),
        'pattern_analysis': os.path.join(temp_base, 'archaeological_analysis', 'pattern_analysis'),
        
        # Submission subcategories (temporary)
        'checkpoint2_final': os.path.join(temp_base, 'competition_submissions', 'checkpoint2_final'),
        'final_submission': os.path.join(temp_base, 'competition_submissions', 'final_submission'),
        
        # Legacy compatibility paths (temporary)
        'images': os.path.join(temp_base, 'satellite_imagery'),
        'enhanced_images': os.path.join(temp_base, 'satellite_imagery'),
        'analysis_results': os.path.join(temp_base, 'archaeological_analysis'),
        'submissions': os.path.join(temp_base, 'competition_submissions'),
        'leverage_responses': os.path.join(temp_base, 'archaeological_analysis', 'ai_responses', "leverage_analysis.json")
    }
    
    # Create all temporary directories
    for path_key, path_value in paths.items():
        if path_key not in ['timestamp', 'leverage_responses', 'base', 'temp_base'] and not path_value.endswith('.json'):
            os.makedirs(path_value, exist_ok=True)
    
    return paths

def get_meaningful_filename(file_type: str, timestamp: str = None, region: str = None, scale: str = None) -> str:
    """Generate meaningful filenames without redundant words"""
    if timestamp is None:
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    
    # Define meaningful filename patterns
    filename_patterns = {
        'checkpoint2_submission': f"checkpoint2_submission_{timestamp}.json",
        'checkpoint2_summary': f"checkpoint2_summary_{timestamp}.md",
        'ai_analysis': f"ai_archaeological_analysis_{timestamp}.json",
        'discovery_catalog': f"archaeological_discoveries_{timestamp}.json",
        'prompt_database': f"ai_prompts_used_{timestamp}.json",
        'processing_log': f"pipeline_execution_log_{timestamp}.txt",
        'validation_report': f"checkpoint2_validation_{timestamp}.md",
        'regional_heatmap': f"{region}_archaeological_heatmap.png" if region else f"regional_heatmap_{timestamp}.png",
        'zone_analysis': f"{region}_zone_{scale}_analysis.png" if region and scale else f"zone_analysis_{timestamp}.png",
        'site_detail': f"{region}_site_{scale}_detail.png" if region and scale else f"site_detail_{timestamp}.png"
    }
    
    return filename_patterns.get(file_type, f"{file_type}_{timestamp}")

def get_checkpoint2_submission_path(timestamp: str = None) -> str:
    """Get path for checkpoint 2 submission with meaningful name"""
    if timestamp is None:
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    
    paths = get_paths()
    filename = get_meaningful_filename('checkpoint2_submission', timestamp)
    return os.path.join(paths['checkpoint2_final'], filename)

def get_checkpoint2_summary_path(timestamp: str = None) -> str:
    """Get path for checkpoint 2 summary with meaningful name"""
    if timestamp is None:
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    
    paths = get_paths()
    filename = get_meaningful_filename('checkpoint2_summary', timestamp)
    return os.path.join(paths['checkpoint2_final'], filename)

def get_ai_analysis_path(timestamp: str = None) -> str:
    """Get path for AI analysis results"""
    if timestamp is None:
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    
    paths = get_paths()
    filename = get_meaningful_filename('ai_analysis', timestamp)
    return os.path.join(paths['ai_responses'], filename)

def get_discovery_catalog_path(timestamp: str = None) -> str:
    """Get path for discovery catalog"""
    if timestamp is None:
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    
    paths = get_paths()
    filename = get_meaningful_filename('discovery_catalog', timestamp)
    return os.path.join(paths['discoveries'], filename)

def clear_outputs_for_fresh_run():
    """
    Clear only old temporary files and final_results (keep directory clean)
    """
    import shutil
    import glob
    
    print(f"🧹 Preparing clean workspace...")
    
    # Clean up any old temporary archaeology folders
    temp_dirs = glob.glob("/tmp/archaeology_temp_*")
    for temp_dir in temp_dirs:
        try:
            shutil.rmtree(temp_dir)
        except:
            pass
    
    print("✅ Temporary directories cleared")

def cleanup_temp_directories(temp_base: str):
    """
    Clean up temporary directories after processing is complete
    """
    import shutil
    
    if temp_base and os.path.exists(temp_base):
        try:
            shutil.rmtree(temp_base)
            print(f"🧹 Cleaned up temporary processing directory")
        except Exception as e:
            print(f"⚠️ Could not clean temp directory: {e}")

def create_submission_package(timestamp: str = None) -> dict:
    """
    Create a complete submission package with meaningful names
    Returns paths to all created files
    """
    if timestamp is None:
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    
    package = {
        'submission_json': get_checkpoint2_submission_path(timestamp),
        'summary_markdown': get_checkpoint2_summary_path(timestamp),
        'ai_analysis': get_ai_analysis_path(timestamp),
        'discovery_catalog': get_discovery_catalog_path(timestamp),
        'timestamp': timestamp,
        'package_directory': f"checkpoint2_complete_{timestamp}"
    }
    
    return package

def show_organized_structure():
    """Show the organized structure that will be created"""
    print("📁 Clean Output Structure:")
    print("=" * 30)
    print("outputs/")
    print("└── final_results_YYYYMMDD_HHMMSS/")
    print("    ├── 1_submission/          # Competition files")
    print("    ├── 2_discoveries/         # Top discoveries with images")
    print("    ├── 3_processed_images/    # All satellite imagery")
    print("    └── 4_metadata/            # Technical analysis")
    print()
    print("🧹 Temporary processing folders are automatically cleaned up")
    print("✨ Only clean organized results remain")

if __name__ == "__main__":
    show_organized_structure() 