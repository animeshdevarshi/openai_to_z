# prompt_config.py
# Centralized prompt configuration for archaeological AI analysis
# All OpenAI prompts organized by scale and analysis type

from typing import Dict, List
import json

class PromptConfig:
    """
    Centralized configuration for all archaeological AI analysis prompts
    Organizes prompts by scale (regional/zone/site) and includes domain knowledge
    """
    
    def __init__(self):
        """Initialize with Casarabe archaeological knowledge base"""
        
        # Archaeological knowledge base from Prümers et al. 2022
        self.casarabe_knowledge = {
            'primary_centers': {
                'size_ha': (100, 400),
                'features': ['multiple_concentric_rings', 'central_platform', 'pyramid_mounds'],
                'defensive_rings': (2, 3),
                'examples': ['Cotoca (147 ha)', 'Landívar (315 ha)']
            },
            'secondary_centers': {
                'size_ha': (20, 40),
                'features': ['single_defensive_ring', 'rectangular_platform'],
                'defensive_rings': (1, 1),
                'connection': 'connected_to_primary_via_causeways'
            },
            'tertiary_sites': {
                'size_ha': (2, 20),
                'features': ['single_platform', 'simple_structure'],
                'function': 'satellite_settlements'
            },
            'causeways': {
                'width_m': (10, 30),
                'length_km': (2, 5),
                'orientation': 'north_northwest',
                'characteristics': 'perfectly_straight'
            },
            'time_period': '500-1400 CE',
            'culture': 'Casarabe'
        }
        
        # Triple data source descriptions
        self.data_sources = {
            'sentinel2': {
                'name': 'Sentinel-2 MSI Level-2A',
                'type': 'Optical Multispectral Imagery',
                'resolution_m': 10,
                'purpose': 'Regional pattern detection and vegetation analysis'
            },
            'radar': {
                'name': 'ALOS PALSAR / Sentinel-1',
                'type': 'Synthetic Aperture Radar',
                'resolution_m': 25,
                'purpose': 'Ground surface structure through forest canopy'
            },
            'planet': {
                'name': 'Planet NICFI High-Resolution',
                'type': 'Very High Resolution Optical',
                'resolution_m': 4.77,
                'purpose': 'Detailed site confirmation and precise feature measurement'
            }
        }
        
        print("📝 Prompt configuration initialized")
        print("🏛️ Casarabe knowledge base loaded")
        print("🛰️ Triple data source definitions ready")
    
    def get_regional_prompt_template(self) -> str:
        """Regional analysis prompt template (50km scale)"""
        return """You are analyzing satellite imagery of the Amazon rainforest to discover pre-Columbian archaeological networks.

MISSION: Identify Casarabe culture settlement networks (500-1400 CE) in the Bolivian Amazon.

LOCATION: {region_name}
ANALYSIS SCALE: Regional overview (50km × 50km)
COORDINATES: {center}

TRIPLE DATA SOURCES AVAILABLE:
1. Sentinel-2 Optical: Vegetation patterns and surface features
2. {radar_type} Radar: Ground structure through forest canopy  
3. Planet NICFI: Ultra-high resolution confirmation data

WHAT YOU'RE LOOKING AT:
- Archaeological probability heatmap (red = high probability of sites)
- Optical satellite composite showing vegetation patterns
- Radar data revealing subsurface earthworks
- Resolution: ~97 meters per pixel

CASARABE SETTLEMENT NETWORKS (based on Prümers et al. 2022):

PRIMARY CENTERS (100-400 hectares):
- Appear as large red clusters in heatmap (2-5km across)
- Multiple concentric defensive rings (2-3 rings)
- Central pyramid mounds up to 22m high
- Connected by straight causeways to smaller sites
- Examples: Cotoca (147 ha), Landívar (315 ha)

SECONDARY CENTERS (20-40 hectares):
- Medium red areas near primary centers
- Single defensive enclosure
- Rectangular platforms (2-6 hectares)
- Connected to primary sites by causeways 2-5km long

CAUSEWAY NETWORKS:
- Perfectly straight lines radiating from centers
- 10-30m wide (visible as linear features)
- North-Northwest orientation preferred
- Connect hierarchical settlement tiers

YOUR TASK - NETWORK DETECTION:
1. IDENTIFY SETTLEMENT CLUSTERS: Look for groups of high-probability areas (red zones) that suggest multiple connected sites within 5-10km of each other

2. TRACE CAUSEWAY NETWORKS: Find straight linear features that connect high-probability zones - these are ancient roads linking settlements

3. RECOGNIZE HIERARCHY: Primary centers should be largest red areas with multiple smaller red areas nearby connected by linear features

4. MARK DISCOVERY ZONES: Identify the most promising areas for detailed analysis

REQUIRED OUTPUT FORMAT - JSON ONLY:
{{
  "analysis_type": "regional_network",
  "region_name": "{region_name}",
  "coordinates": "{center}",
  "data_sources_analyzed": ["optical", "radar", "ultra_high_res"],
  "settlement_clusters": [
    {{
      "cluster_id": 1,
      "center_coordinates": "lat, lng",
      "cluster_size_km": 0.0,
      "site_count_estimate": 0,
      "primary_centers": 0,
      "secondary_centers": 0,
      "causeway_connections": 0,
      "confidence": 0.0,
      "reasoning": "description of detected features"
    }}
  ],
  "causeway_networks": [
    {{
      "network_id": 1,
      "origin_coordinates": "lat, lng",
      "terminus_coordinates": "lat, lng",
      "length_km": 0.0,
      "width_estimate_m": 0,
      "orientation": "direction",
      "confidence": 0.0
    }}
  ],
  "priority_zones": [
    {{
      "zone_id": 1,
      "center_coordinates": "lat, lng",
      "priority_level": "high/medium/low",
      "expected_site_type": "primary/secondary/tertiary",
      "reasoning": "why this zone should be analyzed in detail"
    }}
  ],
  "overall_assessment": {{
    "network_hierarchy_detected": true/false,
    "total_clusters_found": 0,
    "total_causeways_found": 0,
    "confidence_score": 0.0,
    "recommended_detailed_analysis": true/false,
    "data_source_quality": {{
      "optical_quality": "excellent/good/poor",
      "radar_penetration": "excellent/good/poor", 
      "ultra_high_res_coverage": "complete/partial/minimal"
    }}
  }}
}}

CRITICAL: Only report features that are clearly geometric and too regular to be natural. Archaeological sites show perfect circles, straight lines, and geometric patterns that nature cannot create. Respond ONLY with valid JSON."""

    def get_zone_prompt_template(self) -> str:
        """Zone analysis prompt template (10km scale)"""
        return """Analyze this 10km × 10km zone for individual pre-Columbian archaeological sites.

ZONE: {zone_id}
CENTER: {zone_center}
ANALYSIS SCALE: Zone level (10km × 10km at 9.8m per pixel)

TRIPLE DATA SOURCES PROVIDED:
1. High-resolution optical image - vegetation and ground features
2. {radar_type} radar image - surface structure through forest canopy
3. Planet NICFI ultra-high-res - detailed confirmation data
4. Archaeological probability map - highlighting potential sites

CASARABE SITE IDENTIFICATION GUIDE:

PRIMARY SITES (Target: 100-400 hectares):
- Size: 1-2 km diameter at this resolution
- CONCENTRIC RINGS: 2-3 dark circles (moats) with bright inner rings (ramparts)
- CENTRAL FEATURES: Raised platforms visible as lighter areas in optical/radar
- PYRAMID MOUNDS: Elevated features up to 22m high
- SHAPE: Circular or polygonal, too geometric to be natural
- CONTEXT: Near water sources, slightly elevated terrain

SECONDARY SITES (Target: 20-40 hectares):
- Size: 200-400m diameter
- SINGLE RING: One defensive moat/rampart system
- PLATFORM: Rectangular or polygonal raised area (2-6 ha)
- CONNECTION: Should be 2-5km from primary sites
- CAUSEWAY ACCESS: Connected by straight paths

TERTIARY SITES (Target: 2-20 hectares):
- Size: 50-200m diameter
- SIMPLE PLATFORM: Single raised area
- MINIMAL DEFENSES: Little to no earthwork fortification
- SATELLITE FUNCTION: Support settlements for larger centers

DETECTION STRATEGY:
1. SCAN FOR GEOMETRIC PATTERNS: Look for circles, polygons, straight lines that are too regular for nature
2. CHECK MULTIPLE DATA SOURCES: Optical shows vegetation stress, Radar reveals earthworks, Ultra-high-res confirms details
3. MEASURE SIZES: Each pixel = ~9.8 meters
4. ASSESS CONTEXT: Elevated areas preferred, near water sources
5. VERIFY HIERARCHY: Primary sites should have secondary sites nearby

REQUIRED OUTPUT FORMAT - JSON ONLY:
{{
  "analysis_type": "zone_site_detection",
  "zone_id": "{zone_id}",
  "zone_center": "{zone_center}",
  "data_sources_analyzed": ["optical", "radar", "ultra_high_res", "archaeological"],
  "sites_detected": [
    {{
      "site_id": "unique_identifier",
      "center_coordinates": "lat, lng",
      "site_type": "primary/secondary/tertiary/uncertain",
      "diameter_meters": 0,
      "defensive_rings": 0,
      "features_detected": ["concentric_rings", "raised_platform", "pyramid_mounds", "geometric_shape"],
      "data_sources_visible": ["optical", "radar", "ultra_high_res"],
      "measurements": {{
        "outer_ring_diameter_m": 0,
        "inner_platform_size_m": 0,
        "estimated_area_hectares": 0.0,
        "platform_height_estimate_m": 0
      }},
      "context": {{
        "elevation": "elevated/low/water_adjacent",
        "water_proximity": true/false,
        "forest_disturbance": true/false,
        "topographic_advantage": true/false
      }},
      "confidence_score": 0.0,
      "geometric_regularity": 0.0,
      "archaeological_probability": 0.0,
      "cultural_attribution": "casarabe/other/uncertain"
    }}
  ],
  "linear_features": [
    {{
      "feature_id": "causeway_1",
      "start_coordinates": "lat, lng",
      "end_coordinates": "lat, lng",
      "width_meters": 0,
      "length_meters": 0,
      "orientation": "direction",
      "connects_sites": ["site_id1", "site_id2"],
      "confidence": 0.0,
      "data_source_visibility": ["optical", "radar", "ultra_high_res"]
    }}
  ],
  "zone_summary": {{
    "total_sites_detected": 0,
    "primary_sites": 0,
    "secondary_sites": 0,
    "tertiary_sites": 0,
    "geometric_features_count": 0,
    "zone_confidence": 0.0,
    "recommend_site_analysis": true/false,
    "network_potential": "high/medium/low",
    "data_quality_assessment": {{
      "optical_clarity": "excellent/good/poor",
      "radar_penetration": "excellent/good/poor",
      "ultra_high_res_detail": "excellent/good/poor"
    }}
  }}
}}

CRITICAL: Only report features that are clearly geometric and too regular to be natural. Casarabe sites show perfect geometric patterns impossible in nature. Respond ONLY with valid JSON."""

    def get_site_prompt_template(self) -> str:
        """Site analysis prompt template (2km scale)"""
        return """Perform detailed archaeological analysis of this potential Casarabe culture site.

SITE ID: {site_id}
CENTER: {site_center}
ANALYSIS SCALE: Site level (2km × 2km at 1.95m per pixel resolution)

This is MAXIMUM RESOLUTION analysis - you can see features as small as 2 meters.

TRIPLE DATA SOURCES AT MAXIMUM RESOLUTION:
1. Sentinel-2 Optical: Vegetation patterns and surface visibility
2. {radar_type} Radar: Subsurface earthwork detection
3. Planet NICFI: Ultra-high resolution confirmation (4.77m resolution)

DETAILED MAPPING INSTRUCTIONS:

DEFENSIVE STRUCTURES:
- Count exact number of concentric rings
- Measure precise diameters of each ring
- Identify entrance gaps and their orientations
- Assess preservation quality

CENTRAL ARCHITECTURE:
- Map raised platforms with exact dimensions
- Identify pyramid mounds and estimate heights
- Locate plaza areas and ceremonial spaces
- Document U-shaped structures (diagnostic of Casarabe)

SITE CONNECTIONS:
- Trace causeway directions and measure widths
- Document connection points to defensive rings
- Map internal pathway systems

CLASSIFICATION CRITERIA:
- Primary: 100-400 ha, multiple rings, pyramid mounds, multiple causeways
- Secondary: 20-40 ha, single ring, rectangular platform, causeway connection
- Tertiary: 2-20 ha, simple platform, minimal defenses

REQUIRED OUTPUT FORMAT - JSON ONLY:
{{
  "analysis_type": "site_detailed_mapping",
  "site_id": "{site_id}",
  "site_center": "{site_center}",
  "data_sources_analyzed": ["optical", "radar", "ultra_high_res"],
  "defensive_structures": {{
    "concentric_rings": [
      {{
        "ring_number": 1,
        "diameter_meters": 0,
        "type": "moat/rampart/combined",
        "completeness": 0.0,
        "preservation": "excellent/good/poor",
        "depth_estimate_m": 0,
        "width_estimate_m": 0
      }}
    ],
    "entrance_gaps": [
      {{
        "gap_id": 1,
        "location": "cardinal_direction",
        "width_meters": 0,
        "causeway_connection": true/false,
        "orientation_degrees": 0
      }}
    ]
  }},
  "central_architecture": {{
    "raised_platforms": [
      {{
        "platform_id": 1,
        "dimensions": "length_m x width_m",
        "height_estimate_m": 0,
        "shape": "rectangular/circular/u_shaped/irregular",
        "function": "ceremonial/residential/administrative",
        "area_hectares": 0.0
      }}
    ],
    "pyramid_mounds": [
      {{
        "mound_id": 1,
        "height_estimate_m": 0,
        "base_diameter_m": 0,
        "shape": "conical/stepped/platform",
        "preservation": "excellent/good/poor",
        "cultural_significance": "high/medium/low"
      }}
    ],
    "plaza_areas": [
      {{
        "plaza_id": 1,
        "dimensions": "length_m x width_m",
        "surface_type": "prepared/natural",
        "central_features": ["altar", "stone_arrangement", "none"]
      }}
    ]
  }},
  "site_connections": [
    {{
      "causeway_id": 1,
      "direction": "cardinal_direction",
      "width_meters": 0,
      "length_visible_m": 0,
      "destination": "visible_endpoint/continues_beyond",
      "preservation": "excellent/good/poor",
      "construction_quality": "high/medium/low"
    }}
  ],
  "site_measurements": {{
    "overall_diameter_m": 0,
    "total_area_hectares": 0.0,
    "defensive_area_hectares": 0.0,
    "central_area_hectares": 0.0,
    "platform_area_hectares": 0.0
  }},
  "site_classification": {{
    "tier": "primary/secondary/tertiary",
    "confidence": 0.0,
    "classification_criteria": [
      "multiple_rings",
      "large_platform", 
      "pyramid_mounds",
      "multiple_causeways",
      "geometric_precision"
    ],
    "cultural_attribution": "casarabe/other/uncertain",
    "time_period_estimate": "500-1400 CE"
  }},
  "preservation_assessment": {{
    "overall_preservation": "excellent/good/poor",
    "modern_disturbances": true/false,
    "disturbance_types": ["roads", "agriculture", "clearing", "mining"],
    "archaeological_integrity": 0.0,
    "research_potential": "high/medium/low"
  }},
  "data_source_analysis": {{
    "optical_features_visible": ["vegetation_stress", "geometric_patterns", "elevation_changes"],
    "radar_subsurface_detection": ["earthworks", "platforms", "causeways"],
    "ultra_high_res_confirmation": ["precise_measurements", "fine_details", "validation"]
  }},
  "final_assessment": {{
    "archaeological_confidence": 0.0,
    "site_significance": "exceptional/high/medium/low",
    "recommended_for_submission": true/false,
    "additional_analysis_needed": true/false,
    "priority_for_excavation": "urgent/high/medium/low"
  }}
}}

CRITICAL: Be extremely precise with measurements. Each pixel = 1.95 meters. Use all three data sources for validation. Respond ONLY with valid JSON."""

    def get_leverage_prompt_template(self) -> str:
        """Leverage analysis prompt template (discovery-based search)"""
        return """ARCHAEOLOGICAL DISCOVERY LEVERAGE ANALYSIS

Based on our initial discoveries, we've identified {discovery_count} potential Casarabe culture sites with these patterns:

DISCOVERED SITE CHARACTERISTICS:
- Average site size: {avg_size_ha} hectares
- Common features: {common_features}
- Typical defensive rings: {avg_rings}
- Site tier distribution: {tier_distribution}
- Elevation preferences: Sites found at {elevation_range}m elevation

EMERGING NETWORK PATTERNS:
- Primary centers found: {primary_count}
- Secondary centers found: {secondary_count}
- Tertiary sites found: {tertiary_count}
- Causeway orientations: {causeway_directions}
- Typical spacing: Sites {typical_spacing_km} km apart

TRIPLE DATA SOURCE INSIGHTS:
- Optical signatures: {optical_patterns}
- Radar detection patterns: {radar_patterns}
- Ultra-high-res confirmations: {ultra_high_res_patterns}

LEVERAGED SEARCH STRATEGY:
1. SECONDARY CENTER GAPS: Search 2-5km radius around primary centers for missing secondary sites
2. CAUSEWAY COMPLETION: Trace causeway directions from known sites to find connected settlements
3. PATTERN MATCHING: Search for sites matching discovered profile and characteristics
4. NETWORK HIERARCHY COMPLETION: Fill gaps in hierarchical settlement network
5. TOPOGRAPHIC SIMILARITY: Search similar environmental settings that hosted successful sites
6. TRIPLE-SOURCE VALIDATION: Use all three data sources to confirm pattern-predicted locations

SEARCH PARAMETERS LEARNED:
- Preferred site sizes: {preferred_sizes}
- Typical geometric signatures: {geometric_signatures}
- Environmental contexts: {environmental_contexts}
- Defensive configurations: {defensive_patterns}

REQUIRED OUTPUT FORMAT - JSON ONLY:
{{
  "analysis_type": "leverage_discovery",
  "initial_discoveries_count": {discovery_count},
  "learned_patterns": {{
    "average_site_size_ha": {avg_size_ha},
    "common_features": {common_features},
    "typical_spacing_km": {typical_spacing_km},
    "preferred_settings": "{preferred_setting}",
    "geometric_signatures": {geometric_signatures},
    "data_source_signatures": {{
      "optical_indicators": {optical_patterns},
      "radar_indicators": {radar_patterns},
      "ultra_high_res_indicators": {ultra_high_res_patterns}
    }}
  }},
  "targeted_search_zones": [
    {{
      "search_zone_id": 1,
      "center_coordinates": "lat, lng", 
      "search_radius_km": 0.0,
      "search_rationale": "gap_in_network/causeway_terminus/pattern_match",
      "expected_site_type": "primary/secondary/tertiary",
      "confidence_prediction": 0.0,
      "environmental_match": 0.0
    }}
  ],
  "network_completion_predictions": [
    {{
      "prediction_id": 1,
      "predicted_coordinates": "lat, lng",
      "prediction_type": "missing_secondary/causeway_endpoint/network_hub",
      "reasoning": "explanation of why site should exist here",
      "confidence": 0.0,
      "data_sources_supporting": ["optical", "radar", "ultra_high_res"]
    }}
  ],
  "improved_detection_criteria": {{
    "refined_size_range_ha": [0, 0],
    "enhanced_geometric_patterns": ["pattern1", "pattern2"],
    "validated_environmental_contexts": ["context1", "context2"],
    "optimized_data_source_combinations": ["combo1", "combo2"]
  }},
  "leverage_effectiveness": {{
    "pattern_recognition_strength": 0.0,
    "network_understanding": 0.0,
    "prediction_confidence": 0.0,
    "search_efficiency_improvement": 0.0
  }}
}}

YOUR TASK: Use the learned patterns to predict where additional Casarabe sites should exist. Focus on:
1. Network gaps that need filling
2. Causeway endpoints that should have sites
3. Environmental conditions that match successful discoveries
4. Hierarchical relationships requiring secondary/tertiary sites

CRITICAL: This is pattern-based prediction using archaeological knowledge. Be specific about WHY each predicted location should have a site. Respond ONLY with valid JSON."""

    def get_regional_prompt(self, region_info: Dict, images: Dict, radar_type: str = "ALOS PALSAR") -> str:
        """Get formatted regional prompt"""
        template = self.get_regional_prompt_template()
        return template.format(
            region_name=region_info.get('region_name', 'Unknown Region'),
            center=region_info.get('center', [0, 0]),
            radar_type=radar_type
        )
    
    def get_zone_prompt(self, zone_info: Dict, images: Dict, radar_type: str = "ALOS PALSAR") -> str:
        """Get formatted zone prompt"""
        template = self.get_zone_prompt_template()
        return template.format(
            zone_id=zone_info.get('zone_id', 'unknown_zone'),
            zone_center=zone_info.get('zone_center', [0, 0]),
            radar_type=radar_type
        )
    
    def get_site_prompt(self, site_info: Dict, images: Dict, radar_type: str = "ALOS PALSAR") -> str:
        """Get formatted site prompt"""
        template = self.get_site_prompt_template()
        return template.format(
            site_id=site_info.get('site_id', 'unknown_site'),
            site_center=site_info.get('center', [0, 0]),
            radar_type=radar_type
        )
    
    def get_leverage_prompt(self, discoveries: List[Dict], search_region: Dict) -> str:
        """Get formatted leverage prompt with discovery patterns"""
        if not discoveries:
            return self.get_regional_prompt(search_region, {})
        
        # Analyze patterns in discoveries
        patterns = self._analyze_discovery_patterns(discoveries)
        
        template = self.get_leverage_prompt_template()
        return template.format(**patterns)
    
    def _analyze_discovery_patterns(self, discoveries: List[Dict]) -> Dict:
        """Analyze patterns in discovered sites for leverage prompting"""
        if not discoveries:
            return {}
        
        # Calculate statistics
        sizes = [d.get('estimated_area_hectares', 0) for d in discoveries if d.get('estimated_area_hectares')]
        avg_size = sum(sizes) / len(sizes) if sizes else 0
        
        # Extract common features
        all_features = []
        for d in discoveries:
            features = d.get('features_detected', [])
            if isinstance(features, list):
                all_features.extend(features)
        
        from collections import Counter
        feature_counts = Counter(all_features)
        common_features = [f for f, count in feature_counts.most_common(3)]
        
        # Site tier distribution
        tiers = [d.get('site_classification', 'uncertain') for d in discoveries]
        tier_counter = Counter(tiers)
        
        return {
            'discovery_count': len(discoveries),
            'avg_size_ha': round(avg_size, 1),
            'common_features': common_features,
            'avg_rings': 1.2,  # Estimated average
            'tier_distribution': dict(tier_counter),
            'elevation_range': '200-500',  # Typical Amazon elevation
            'primary_count': tier_counter.get('Primary', 0),
            'secondary_count': tier_counter.get('Secondary', 0),
            'tertiary_count': tier_counter.get('Tertiary', 0),
            'causeway_directions': ['North-Northwest', 'Northeast'],
            'typical_spacing_km': 3.5,
            'optical_patterns': ['vegetation_stress', 'geometric_shapes'],
            'radar_patterns': ['elevated_returns', 'linear_features'],
            'ultra_high_res_patterns': ['precise_geometry', 'fine_details'],
            'preferred_setting': 'elevated_areas_near_water',
            'geometric_signatures': ['circular_patterns', 'straight_lines'],
            'environmental_contexts': ['forest_clearings', 'elevated_terrain'],
            'defensive_patterns': ['concentric_rings', 'strategic_positioning'],
            'preferred_sizes': f'{int(avg_size/2)}-{int(avg_size*2)} hectares'
        }
    
    def get_prompt_metadata(self, prompt_type: str, prompt_content: str) -> Dict:
        """Get metadata for a prompt"""
        return {
            'prompt_type': prompt_type,
            'prompt_length': len(prompt_content),
            'includes_casarabe_knowledge': 'Casarabe' in prompt_content,
            'includes_data_sources': 'triple data sources' in prompt_content.lower() or 'three data sources' in prompt_content.lower(),
            'includes_measurements': 'meters' in prompt_content,
            'output_format': 'JSON',
            'archaeological_framework': 'Casarabe culture settlement networks',
            'scale_specific': True
        }
    
    def save_prompts_documentation(self, output_dir: str) -> str:
        """Save complete prompt documentation"""
        import os
        from datetime import datetime
        
        documentation = {
            'prompt_system_version': '1.0',
            'creation_timestamp': datetime.now().isoformat(),
            'archaeological_framework': 'Casarabe culture (500-1400 CE)',
            'data_sources_supported': self.data_sources,
            'casarabe_knowledge_base': self.casarabe_knowledge,
            'prompt_templates': {
                'regional': self.get_regional_prompt_template(),
                'zone': self.get_zone_prompt_template(),
                'site': self.get_site_prompt_template(),
                'leverage': self.get_leverage_prompt_template()
            },
            'prompt_characteristics': {
                'output_format': 'JSON structured responses',
                'scale_specific': 'Different prompts for different analysis scales',
                'domain_knowledge': 'Integrated archaeological expertise',
                'data_source_aware': 'References all three data sources',
                'measurement_precise': 'Pixel-accurate measurements requested'
            }
        }
        
        doc_file = os.path.join(output_dir, f'prompt_documentation_{datetime.now().strftime("%Y%m%d_%H%M%S")}.json')
        os.makedirs(output_dir, exist_ok=True)
        
        with open(doc_file, 'w') as f:
            json.dump(documentation, f, indent=2)
        
        print(f"📝 Prompt documentation saved: {doc_file}")
        return doc_file


# Test the prompt configuration
if __name__ == "__main__":
    print("📝 Testing Prompt Configuration System")
    print("=" * 50)
    
    config = PromptConfig()
    
    # Test regional prompt
    test_region = {'region_name': 'Test Amazon Region', 'center': [-1.0, -70.0]}
    regional_prompt = config.get_regional_prompt(test_region, {})
    print(f"\n✅ Regional prompt: {len(regional_prompt)} characters")
    
    # Test zone prompt
    test_zone = {'zone_id': 'test_zone_1', 'zone_center': [-1.0, -70.0]}
    zone_prompt = config.get_zone_prompt(test_zone, {})
    print(f"✅ Zone prompt: {len(zone_prompt)} characters")
    
    # Test site prompt
    test_site = {'site_id': 'test_site_1', 'center': [-1.0, -70.0]}
    site_prompt = config.get_site_prompt(test_site, {})
    print(f"✅ Site prompt: {len(site_prompt)} characters")
    
    # Test leverage prompt
    test_discoveries = [{'estimated_area_hectares': 25, 'features_detected': ['concentric_rings'], 'site_classification': 'Secondary'}]
    leverage_prompt = config.get_leverage_prompt(test_discoveries, test_region)
    print(f"✅ Leverage prompt: {len(leverage_prompt)} characters")
    
    print(f"\n🎉 All prompt templates ready!")
    print(f"🏛️ Archaeological knowledge base integrated")
    print(f"🛰️ Triple data source support enabled") 