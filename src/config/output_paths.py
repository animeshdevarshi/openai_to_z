# output_config.py
# Archaeological Discovery System - Output Configuration
# Creates organized folder structure with meaningful naming conventions

import os
from datetime import datetime

# Base output directory
BASE_OUTPUT_DIR = "outputs"

# Organized subdirectories with meaningful names
SUBDIRS = {
    'imagery': {
        'root': 'satellite_imagery',
        'regional': 'satellite_imagery/regional_50km',
        'zone': 'satellite_imagery/zone_10km', 
        'site': 'satellite_imagery/site_2km',
        'composite': 'satellite_imagery/composite_maps'
    },
    'analysis': {
        'root': 'archaeological_analysis',
        'ai_responses': 'archaeological_analysis/ai_responses',
        'discoveries': 'archaeological_analysis/discoveries',
        'prompts': 'archaeological_analysis/prompts_database',
        'patterns': 'archaeological_analysis/pattern_analysis'
    },
    'submissions': {
        'root': 'competition_submissions',
        'checkpoint2': 'competition_submissions/checkpoint2_final',
        'final': 'competition_submissions/final_submission',
        'drafts': 'competition_submissions/draft_versions'
    },
    'data': {
        'root': 'processed_data',
        'satellite': 'processed_data/satellite_downloads',
        'archaeological': 'processed_data/archaeological_indices',
        'regional_data': 'processed_data/regional_summaries'
    },
    'documentation': {
        'root': 'project_documentation',
        'methodology': 'project_documentation/methodology',
        'validation': 'project_documentation/validation_reports',
        'logs': 'project_documentation/pipeline_logs'
    }
}

def get_paths() -> dict:
    """
    Get all organized output paths with meaningful names
    Creates directories if they don't exist
    """
    
    # Create timestamp for this session
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    
    paths = {
        'base': BASE_OUTPUT_DIR,
        'timestamp': timestamp,
        
        # Main categories with meaningful names
        'satellite_imagery': os.path.join(BASE_OUTPUT_DIR, SUBDIRS['imagery']['root']),
        'archaeological_analysis': os.path.join(BASE_OUTPUT_DIR, SUBDIRS['analysis']['root']),
        'competition_submissions': os.path.join(BASE_OUTPUT_DIR, SUBDIRS['submissions']['root']),
        'processed_data': os.path.join(BASE_OUTPUT_DIR, SUBDIRS['data']['root']),
        'project_documentation': os.path.join(BASE_OUTPUT_DIR, SUBDIRS['documentation']['root']),
        
        # Imagery subcategories by scale
        'regional_imagery': os.path.join(BASE_OUTPUT_DIR, SUBDIRS['imagery']['regional']),
        'zone_imagery': os.path.join(BASE_OUTPUT_DIR, SUBDIRS['imagery']['zone']),
        'site_imagery': os.path.join(BASE_OUTPUT_DIR, SUBDIRS['imagery']['site']),
        'composite_maps': os.path.join(BASE_OUTPUT_DIR, SUBDIRS['imagery']['composite']),
        
        # Analysis subcategories
        'ai_responses': os.path.join(BASE_OUTPUT_DIR, SUBDIRS['analysis']['ai_responses']),
        'discoveries': os.path.join(BASE_OUTPUT_DIR, SUBDIRS['analysis']['discoveries']),
        'prompts_database': os.path.join(BASE_OUTPUT_DIR, SUBDIRS['analysis']['prompts']),
        'pattern_analysis': os.path.join(BASE_OUTPUT_DIR, SUBDIRS['analysis']['patterns']),
        
        # Submission subcategories
        'checkpoint2_final': os.path.join(BASE_OUTPUT_DIR, SUBDIRS['submissions']['checkpoint2']),
        'final_submission': os.path.join(BASE_OUTPUT_DIR, SUBDIRS['submissions']['final']),
        'draft_submissions': os.path.join(BASE_OUTPUT_DIR, SUBDIRS['submissions']['drafts']),
        
        # Data subcategories  
        'satellite_downloads': os.path.join(BASE_OUTPUT_DIR, SUBDIRS['data']['satellite']),
        'archaeological_indices': os.path.join(BASE_OUTPUT_DIR, SUBDIRS['data']['archaeological']),
        'regional_summaries': os.path.join(BASE_OUTPUT_DIR, SUBDIRS['data']['regional_data']),
        
        # Documentation subcategories
        'methodology_docs': os.path.join(BASE_OUTPUT_DIR, SUBDIRS['documentation']['methodology']),
        'validation_reports': os.path.join(BASE_OUTPUT_DIR, SUBDIRS['documentation']['validation']),
        'pipeline_logs': os.path.join(BASE_OUTPUT_DIR, SUBDIRS['documentation']['logs']),
        
        # Legacy compatibility paths (but with better names)
        'images': os.path.join(BASE_OUTPUT_DIR, SUBDIRS['imagery']['root']),  # For backward compatibility
        'enhanced_images': os.path.join(BASE_OUTPUT_DIR, SUBDIRS['imagery']['root']),
        'analysis_results': os.path.join(BASE_OUTPUT_DIR, SUBDIRS['analysis']['root']),
        'submissions': os.path.join(BASE_OUTPUT_DIR, SUBDIRS['submissions']['root']),
        'leverage_responses': os.path.join(BASE_OUTPUT_DIR, SUBDIRS['analysis']['ai_responses'], "leverage_analysis.json")
    }
    
    # Create all directories
    for path_key, path_value in paths.items():
        if path_key not in ['timestamp', 'leverage_responses'] and not path_value.endswith('.json'):
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
    Clear all output files for a completely fresh run
    Keeps directory structure but removes files
    """
    import shutil
    
    if os.path.exists(BASE_OUTPUT_DIR):
        print(f"🧹 Clearing outputs directory: {BASE_OUTPUT_DIR}")
        shutil.rmtree(BASE_OUTPUT_DIR)
        print("✅ All outputs cleared")
    
    # Recreate directory structure
    paths = get_paths()
    print("📁 Directory structure recreated")
    
    # Also clear pipeline progress
    if os.path.exists('pipeline_progress.json'):
        os.remove('pipeline_progress.json')
        print("🔄 Pipeline progress cleared")

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
        'submission_folder': get_paths()['checkpoint2_final']
    }
    
    return package

def show_organized_structure():
    """Display the new organized structure with meaningful names"""
    paths = get_paths()
    
    print("\n📁 ARCHAEOLOGICAL DISCOVERY SYSTEM - OUTPUT STRUCTURE")
    print("=" * 60)
    print(f"📂 {BASE_OUTPUT_DIR}/")
    
    structure_display = {
        'satellite_imagery/': ['regional_50km/', 'zone_10km/', 'site_2km/', 'composite_maps/'],
        'archaeological_analysis/': ['ai_responses/', 'discoveries/', 'prompts_database/', 'pattern_analysis/'],
        'competition_submissions/': ['checkpoint2_final/', 'final_submission/', 'draft_versions/'],
        'processed_data/': ['satellite_downloads/', 'archaeological_indices/', 'regional_summaries/'],
        'project_documentation/': ['methodology/', 'validation_reports/', 'pipeline_logs/']
    }
    
    for main_folder, subfolders in structure_display.items():
        print(f"   📁 {main_folder}")
        for subfolder in subfolders:
            print(f"      📁 {subfolder}")
    
    print(f"\n✅ All directories ready with meaningful names")
    print(f"🎯 Checkpoint 2 Final: {paths['checkpoint2_final']}")
    print(f"📊 Archaeological Analysis: {paths['archaeological_analysis']}")
    print(f"📸 Satellite Imagery: {paths['satellite_imagery']}")
    print(f"📋 Documentation: {paths['project_documentation']}")

if __name__ == "__main__":
    show_organized_structure() 