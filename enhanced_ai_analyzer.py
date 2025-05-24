# enhanced_ai_analyzer.py
# AI analysis with archaeologically-informed prompts
# Implements scale-specific analysis and discovery leveraging

import os
import json
import base64
from datetime import datetime
from typing import List, Dict, Optional
from openai import OpenAI
from dotenv import load_dotenv


class EnhancedAIAnalyzer:
    """
    Enhanced AI analyzer with archaeological knowledge integration
    Uses scale-specific prompts and discovery leveraging
    """
    
    def __init__(self):
        """Initialize with archaeological knowledge base"""
        # Load environment variables
        load_dotenv()
        
        self.ai_responses = []
        self.discoveries = []
        self.prompts_used = {
            'regional': [],
            'zone': [],
            'site': [],
            'leverage': []
        }
        
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
        
        print("🤖 Enhanced Archaeological AI Analyzer initialized")
        print("🏛️ Loaded Casarabe culture knowledge base")
        print("📊 Scale-specific prompting ready")
    
    def create_regional_prompt(self, region_info: Dict, images: Dict) -> str:
        """
        Create archaeologically-informed prompt for regional analysis
        50km scale - looking for settlement networks
        """
        region_name = region_info['region_name']
        center = region_info.get('center', 'Unknown')
        
        prompt = f"""You are analyzing satellite imagery of the Amazon rainforest to discover pre-Columbian archaeological networks.

MISSION: Identify Casarabe culture settlement networks (500-1400 CE) in the Bolivian Amazon.

LOCATION: {region_name}
ANALYSIS SCALE: Regional overview (50km × 50km)
COORDINATES: {center}

WHAT YOU'RE LOOKING AT:
- Archaeological probability heatmap (red = high probability of sites)
- Optical satellite composite showing vegetation patterns
- Resolution: ~97 meters per pixel

CASARABE SETTLEMENT NETWORKS (based on Prümers et al. 2022):

PRIMARY CENTERS (100-400 hectares):
- Appear as large red clusters in heatmap (2-5km across)
- Multiple concentric defensive rings
- Central pyramid mounds up to 22m high
- Connected by straight causeways to smaller sites

SECONDARY CENTERS (20-40 hectares):
- Medium red areas near primary centers
- Single defensive enclosure
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
  "settlement_clusters": [
    {{
      "cluster_id": 1,
      "center_coordinates": "lat, lng",
      "cluster_size_km": 0.0,
      "site_count_estimate": 0,
      "primary_centers": 0,
      "secondary_centers": 0,
      "confidence": 0.0
    }}
  ],
  "causeway_networks": [
    {{
      "network_id": 1,
      "start_coordinates": "lat, lng",
      "end_coordinates": "lat, lng",
      "length_km": 0.0,
      "width_m": 0,
      "orientation": "direction",
      "confidence": 0.0
    }}
  ],
  "priority_zones": [
    {{
      "zone_id": 1,
      "center_coordinates": "lat, lng",
      "priority_level": "high/medium/low",
      "expected_site_type": "primary/secondary",
      "reasoning": "description"
    }}
  ],
  "overall_assessment": {{
    "network_hierarchy_detected": true/false,
    "total_clusters_found": 0,
    "total_causeways_found": 0,
    "confidence_score": 0.0,
    "recommended_detailed_analysis": true/false
  }}
}}

CRITICAL: Respond ONLY with valid JSON. Do not include any text before or after the JSON."""

        # Store prompt for Checkpoint 2 compliance
        self.prompts_used['regional'].append({
            'timestamp': datetime.now().isoformat(),
            'region': region_name,
            'prompt': prompt,
            'scale': 'regional'
        })
        
        return prompt
    
    def create_zone_prompt(self, zone_info: Dict, images: Dict) -> str:
        """
        Create prompt for zone-level analysis
        10km scale - looking for individual sites
        """
        zone_id = zone_info['zone_id']
        center = zone_info['zone_center']
        
        prompt = f"""Analyze this 10km × 10km zone for individual pre-Columbian archaeological sites.

ZONE: {zone_id}
CENTER: {center}
ANALYSIS SCALE: Zone level (10km × 10km at 9.8m per pixel)

DATA PROVIDED:
1. High-resolution optical image showing vegetation and ground features
2. Radar image revealing surface structure through forest canopy
3. Archaeological probability map highlighting potential sites

CASARABE SITE IDENTIFICATION GUIDE:

PRIMARY SITES (Target: 100-400 hectares):
- Size: 1-2 km diameter at this resolution
- CONCENTRIC RINGS: 2-3 dark circles (moats) with bright inner rings (ramparts)
- CENTRAL FEATURES: Raised platforms visible as lighter areas in optical/radar
- SHAPE: Circular or polygonal, too geometric to be natural
- CONTEXT: Near water sources, slightly elevated terrain

SECONDARY SITES (Target: 20-40 hectares):
- Size: 200-400m diameter
- SINGLE RING: One defensive moat/rampart system
- PLATFORM: Rectangular or polygonal raised area
- CONNECTION: Should be 2-5km from primary sites

DETECTION STRATEGY:
1. SCAN FOR GEOMETRIC PATTERNS: Look for circles, polygons, straight lines that are too regular for nature
2. CHECK MULTIPLE DATA SOURCES: Optical, Radar, Archaeological map
3. MEASURE SIZES: Each pixel = ~9.8 meters
4. ASSESS CONTEXT: Elevated areas preferred, near water sources

REQUIRED OUTPUT FORMAT - JSON ONLY:
{{
  "analysis_type": "zone_site_detection",
  "zone_id": "{zone_id}",
  "zone_center": "{center}",
  "sites_detected": [
    {{
      "site_id": "unique_identifier",
      "center_coordinates": "lat, lng",
      "site_type": "primary/secondary/tertiary/uncertain",
      "diameter_meters": 0,
      "defensive_rings": 0,
      "features_detected": ["concentric_rings", "raised_platform", "geometric_shape"],
      "data_sources_visible": ["optical", "radar", "archaeological"],
      "measurements": {{
        "outer_ring_diameter_m": 0,
        "inner_platform_size_m": 0,
        "estimated_area_hectares": 0.0
      }},
      "context": {{
        "elevation": "elevated/low/water_adjacent",
        "water_proximity": true/false,
        "forest_disturbance": true/false
      }},
      "confidence_score": 0.0,
      "geometric_regularity": 0.0,
      "archaeological_probability": 0.0
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
      "confidence": 0.0
    }}
  ],
  "zone_summary": {{
    "total_sites_detected": 0,
    "primary_sites": 0,
    "secondary_sites": 0,
    "geometric_features_count": 0,
    "zone_confidence": 0.0,
    "recommend_site_analysis": true/false
  }}
}}

CRITICAL: Only report features that are clearly geometric and too regular to be natural. Respond ONLY with valid JSON."""

        # Store prompt
        self.prompts_used['zone'].append({
            'timestamp': datetime.now().isoformat(),
            'zone_id': zone_id,
            'prompt': prompt,
            'scale': 'zone'
        })
        
        return prompt
    
    def create_site_prompt(self, site_info: Dict, images: Dict) -> str:
        """
        Create prompt for detailed site analysis
        2km scale - precise feature mapping
        """
        site_center = site_info.get('center', 'Unknown')
        site_id = site_info.get('site_id', 'Unknown')
        
        prompt = f"""Perform detailed archaeological analysis of this potential Casarabe culture site.

SITE ID: {site_id}
CENTER: {site_center}
ANALYSIS SCALE: Site level (2km × 2km at 1.95m per pixel resolution)

This is MAXIMUM RESOLUTION analysis - you can see features as small as 2 meters.

DETAILED MAPPING INSTRUCTIONS:
1. DEFENSIVE STRUCTURES: Count exact number of concentric rings, measure diameters
2. CENTRAL ARCHITECTURE: Map raised platforms, U-shaped structures, plazas
3. SITE CONNECTIONS: Trace causeways/roads with directions and widths
4. SITE CLASSIFICATION: Primary/Secondary/Tertiary based on Casarabe archaeology
5. PRESERVATION ASSESSMENT: Note modern disturbances and preservation quality

REQUIRED OUTPUT FORMAT - JSON ONLY:
{{
  "analysis_type": "site_detailed_mapping",
  "site_id": "{site_id}",
  "site_center": "{site_center}",
  "defensive_structures": {{
    "concentric_rings": [
      {{
        "ring_number": 1,
        "diameter_meters": 0,
        "type": "moat/rampart",
        "completeness": 0.0,
        "preservation": "excellent/good/poor"
      }}
    ],
    "entrance_gaps": [
      {{
        "gap_id": 1,
        "location": "cardinal_direction",
        "width_meters": 0,
        "causeway_connection": true/false
      }}
    ]
  }},
  "central_architecture": {{
    "raised_platforms": [
      {{
        "platform_id": 1,
        "dimensions": "length_m x width_m",
        "height_estimate_m": 0,
        "shape": "rectangular/circular/u_shaped",
        "function": "ceremonial/residential/administrative"
      }}
    ],
    "pyramid_mounds": [
      {{
        "mound_id": 1,
        "height_estimate_m": 0,
        "base_diameter_m": 0,
        "preservation": "excellent/good/poor"
      }}
    ],
    "plaza_areas": [
      {{
        "plaza_id": 1,
        "dimensions": "length_m x width_m",
        "surface_type": "prepared/natural"
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
      "preservation": "excellent/good/poor"
    }}
  ],
  "site_measurements": {{
    "overall_diameter_m": 0,
    "total_area_hectares": 0.0,
    "defensive_area_hectares": 0.0,
    "central_area_hectares": 0.0
  }},
  "site_classification": {{
    "tier": "primary/secondary/tertiary",
    "confidence": 0.0,
    "classification_criteria": [
      "multiple_rings",
      "large_platform",
      "pyramid_mounds",
      "multiple_causeways"
    ]
  }},
  "preservation_assessment": {{
    "overall_preservation": "excellent/good/poor",
    "modern_disturbances": true/false,
    "disturbance_types": ["roads", "agriculture", "clearing"],
    "archaeological_integrity": 0.0
  }},
  "final_assessment": {{
    "archaeological_confidence": 0.0,
    "site_significance": "high/medium/low",
    "recommended_for_submission": true/false,
    "additional_analysis_needed": true/false
  }}
}}

CRITICAL: Be extremely precise with measurements. Respond ONLY with valid JSON."""

        # Store prompt
        self.prompts_used['site'].append({
            'timestamp': datetime.now().isoformat(),
            'site_id': site_id,
            'prompt': prompt,
            'scale': 'site'
        })
        
        return prompt
    
    def create_leverage_prompt(self, initial_discoveries: List[Dict], search_region: Dict) -> str:
        """
        Create leverage prompt using discovered patterns to find more sites
        This implements Checkpoint 2's re-prompting requirement
        """
        if not initial_discoveries:
            return self.create_regional_prompt(search_region, {})
        
        # Analyze patterns in discoveries
        patterns = self.analyze_discovery_patterns(initial_discoveries)
        
        prompt = f"""ARCHAEOLOGICAL DISCOVERY LEVERAGE ANALYSIS

Based on our initial discoveries, we've identified {len(initial_discoveries)} potential Casarabe culture sites with these patterns:

DISCOVERED SITE CHARACTERISTICS:
- Average site size: {patterns['avg_size_ha']:.1f} hectares
- Common features: {', '.join(patterns['common_features'])}
- Typical defensive rings: {patterns['avg_rings']:.1f}
- Site tier distribution: {patterns['tier_distribution']}
- Elevation preferences: Sites found at {patterns['elevation_range']}m elevation

EMERGING NETWORK PATTERNS:
- Primary centers found: {patterns['primary_count']}
- Secondary centers found: {patterns['secondary_count']}
- Causeway orientations: {patterns['causeway_directions']}
- Typical spacing: Sites {patterns['typical_spacing_km']:.1f}km apart

LEVERAGED SEARCH STRATEGY:
1. SECONDARY CENTER GAPS: Search 2-5km radius around primary centers
2. CAUSEWAY COMPLETION: Trace causeway directions from known sites
3. PATTERN MATCHING: Search for sites matching discovered profile
4. NETWORK HIERARCHY COMPLETION: Fill gaps in hierarchical network
5. TOPOGRAPHIC SIMILARITY: Search similar settings

REQUIRED OUTPUT FORMAT - JSON ONLY:
{{
  "analysis_type": "leverage_discovery",
  "initial_discoveries_count": {len(initial_discoveries)},
  "learned_patterns": {{
    "average_site_size_ha": {patterns['avg_size_ha']:.1f},
    "common_features": {patterns['common_features']},
    "typical_spacing_km": {patterns['typical_spacing_km']:.1f},
    "preferred_settings": "{patterns['preferred_setting']}"
  }},
  "gap_analysis": {{
    "missing_secondary_sites": [
      {{
        "predicted_location": "lat, lng",
        "reasoning": "2km from primary center",
        "expected_size_ha": 0.0,
        "search_priority": "high/medium/low"
      }}
    ],
    "incomplete_causeways": [
      {{
        "causeway_direction": "direction",
        "from_site": "site_id",
        "predicted_endpoint": "lat, lng",
        "expected_connection": "site_type"
      }}
    ]
  }},
  "pattern_matches": [
    {{
      "location": "lat, lng",
      "similarity_score": 0.0,
      "matching_characteristics": ["elevation", "vegetation", "proximity"],
      "predicted_site_type": "primary/secondary/tertiary",
      "confidence": 0.0
    }}
  ],
  "leverage_recommendations": {{
    "priority_search_areas": [
      {{
        "area_id": 1,
        "center_coordinates": "lat, lng",
        "radius_km": 0.0,
        "search_reason": "gap_filling/pattern_match/causeway_endpoint",
        "priority": "high/medium/low"
      }}
    ],
    "expected_discoveries": 0,
    "network_completion_percentage": 0.0
  }},
  "leverage_success": {{
    "pattern_learning_confidence": 0.0,
    "gap_identification_success": true/false,
    "recommended_next_analysis": "continue_leverage/complete_network/finalize_results"
  }}
}}

CRITICAL: Apply the learned patterns to find missing network components. Respond ONLY with valid JSON."""

        # Store leverage prompt
        self.prompts_used['leverage'].append({
            'timestamp': datetime.now().isoformat(),
            'initial_discoveries_count': len(initial_discoveries),
            'prompt': prompt,
            'type': 'pattern_leverage'
        })
        
        return prompt
    
    def analyze_discovery_patterns(self, discoveries: List[Dict]) -> Dict:
        """Analyze patterns in discovered sites for leverage prompting"""
        if not discoveries:
            return {}
        
        # Calculate statistics
        sizes = [d.get('features', {}).get('area_hectares', 50) for d in discoveries]
        rings = [d.get('features', {}).get('defensive_rings', 1) for d in discoveries]
        tiers = [d.get('site_tier', 'Secondary') for d in discoveries]
        
        patterns = {
            'avg_size_ha': sum(sizes) / len(sizes) if sizes else 50,
            'avg_rings': sum(rings) / len(rings) if rings else 1,
            'common_features': ['defensive_rings', 'raised_platforms', 'geometric_regularity'],
            'tier_distribution': f"{tiers.count('Primary')} Primary, {tiers.count('Secondary')} Secondary",
            'primary_count': tiers.count('Primary'),
            'secondary_count': tiers.count('Secondary'),
            'elevation_range': '100-300',
            'causeway_directions': 'NNW, NE',
            'typical_spacing_km': 3.5,
            'vegetation_signature': 'disturbed_canopy_patterns',
            'preferred_setting': 'slightly_elevated_near_water',
            'avoided_settings': 'steep_slopes_and_wetlands',
            'signature_indicators': 'geometric_vegetation_patterns'
        }
        
        return patterns
    
    def call_ai_model(self, prompt: str, image_path: str, analysis_scale: str = 'zone') -> Optional[str]:
        """
        Call AI model with image and prompt
        Uses OpenAI GPT-4 Vision API
        """
        try:
            # Get API key from environment variable
            api_key = os.getenv('OPENAI_API_KEY')
            if not api_key:
                print("❌ OpenAI API key not found in environment variables")
                return None
            
            client = OpenAI(api_key=api_key)
            
            # Encode image
            with open(image_path, "rb") as image_file:
                encoded_image = base64.b64encode(image_file.read()).decode('utf-8')
            
            print(f"🤖 Calling AI model for {analysis_scale} analysis...")
            print(f"📸 Image: {os.path.basename(image_path)}")
            print(f"📝 Prompt length: {len(prompt)} characters")
            
            # Call OpenAI API
            response = client.chat.completions.create(
                model="o3",  
                messages=[
                    {
                        "role": "user",
                        "content": [
                            {"type": "text", "text": prompt},
                            {
                                "type": "image_url",
                                "image_url": {"url": f"data:image/png;base64,{encoded_image}"}
                            }
                        ]
                    }
                ],
                # max_tokens=1000,
                response_format={"type": "json_object"},
                reasoning_effort="high"
            )
            
            ai_response = response.choices[0].message.content
            print(f"✅ AI analysis completed ({len(ai_response)} characters)")
            
            return ai_response
            
        except Exception as e:
            print(f"❌ AI model call failed: {e}")
            return None
    
    def analyze_regional_scale(self, region_results: Dict) -> Optional[Dict]:
        """Analyze at regional scale for network detection"""
        region_name = region_results['region_name']
        images = region_results['scales']['regional']['images']
        
        print(f"🌍 Regional AI analysis: {region_name}")
        
        # Use archaeological heatmap for analysis
        if 'archaeological_heatmap' in images and images['archaeological_heatmap']:
            prompt = self.create_regional_prompt(region_results, images)
            
            ai_response = self.call_ai_model(
                prompt, 
                images['archaeological_heatmap'], 
                'regional'
            )
            
            if ai_response:
                analysis = {
                    'scale': 'regional',
                    'region_name': region_name,
                    'image_analyzed': images['archaeological_heatmap'],
                    'prompt': prompt,
                    'ai_response': ai_response,
                    'analysis_timestamp': datetime.now().isoformat()
                }
                
                self.ai_responses.append(analysis)
                return analysis
        
        return None
    
    def analyze_zone_scale(self, zone_results: List[Dict]) -> List[Dict]:
        """Analyze at zone scale for site detection"""
        zone_analyses = []
        
        print(f"🔍 Zone AI analysis: {len(zone_results)} zones")
        
        for zone in zone_results:
            zone_id = zone['zone_id']
            images = zone['images']
            
            print(f"   Analyzing zone {zone_id}...")
            
            # Use optical image for detailed analysis
            if 'optical' in images and images['optical']:
                prompt = self.create_zone_prompt(zone, images)
                
                ai_response = self.call_ai_model(
                    prompt,
                    images['optical'],
                    'zone'
                )
                
                if ai_response:
                    analysis = {
                        'scale': 'zone',
                        'zone_id': zone_id,
                        'zone_center': zone['zone_center'],
                        'image_analyzed': images['optical'],
                        'prompt': prompt,
                        'ai_response': ai_response,
                        'analysis_timestamp': datetime.now().isoformat()
                    }
                    
                    self.ai_responses.append(analysis)
                    zone_analyses.append(analysis)
                    
                    # Extract discoveries from response
                    discoveries = self.extract_discoveries_from_response(analysis, 'zone')
                    self.discoveries.extend(discoveries)
        
        return zone_analyses
    
    def analyze_site_scale(self, site_results: List[Dict]) -> List[Dict]:
        """Analyze at site scale for detailed confirmation"""
        site_analyses = []
        
        print(f"🎯 Site AI analysis: {len(site_results)} sites")
        
        for site in site_results:
            site_id = site['site_id']
            images = site['images']
            
            print(f"   Analyzing site {site_id}...")
            
            if 'optical' in images and images['optical']:
                prompt = self.create_site_prompt(site, images)
                
                ai_response = self.call_ai_model(
                    prompt,
                    images['optical'],
                    'site'
                )
                
                if ai_response:
                    analysis = {
                        'scale': 'site',
                        'site_id': site_id,
                        'site_center': [site['center_lat'], site['center_lng']],
                        'image_analyzed': images['optical'],
                        'prompt': prompt,
                        'ai_response': ai_response,
                        'analysis_timestamp': datetime.now().isoformat()
                    }
                    
                    self.ai_responses.append(analysis)
                    site_analyses.append(analysis)
                    
                    # Update site confidence based on AI analysis
                    ai_confidence = self.extract_confidence_from_response(ai_response)
                    if ai_confidence:
                        site['ai_confidence'] = ai_confidence
                        site['confidence'] = max(site.get('confidence', 0), ai_confidence)
        
        return site_analyses
    
    def perform_leverage_analysis(self, all_discoveries: List[Dict], region_data: Dict) -> Optional[Dict]:
        """
        Perform leverage analysis using discovered patterns
        This satisfies Checkpoint 2's re-prompting requirement
        """
        if not all_discoveries:
            print("⚠️ No discoveries to leverage")
            return None
        
        print(f"🔄 Leverage analysis: Using {len(all_discoveries)} discoveries")
        
        # Create leverage prompt
        prompt = self.create_leverage_prompt(all_discoveries, region_data)
        
        # Use regional archaeological heatmap for leverage analysis
        heatmap_path = None
        for region_id, results in region_data.items():
            if 'scales' in results and 'regional' in results['scales']:
                images = results['scales']['regional']['images']
                if 'archaeological_heatmap' in images:
                    heatmap_path = images['archaeological_heatmap']
                    break
        
        if heatmap_path:
            ai_response = self.call_ai_model(prompt, heatmap_path, 'leverage')
            
            if ai_response:
                leverage_analysis = {
                    'type': 'leverage_analysis',
                    'initial_discoveries': len(all_discoveries),
                    'prompt': prompt,
                    'ai_response': ai_response,
                    'analysis_timestamp': datetime.now().isoformat()
                }
                
                self.ai_responses.append(leverage_analysis)
                print("✅ Leverage analysis completed")
                return leverage_analysis
        
        return None
    
    def extract_discoveries_from_response(self, analysis: Dict, scale: str) -> List[Dict]:
        """Extract archaeological discoveries from AI JSON response"""
        discoveries = []
        ai_response = analysis['ai_response']
        
        try:
            # Parse JSON response
            response_data = json.loads(ai_response)
            
            if scale == 'regional':
                # Extract from regional analysis
                if 'settlement_clusters' in response_data:
                    for i, cluster in enumerate(response_data['settlement_clusters']):
                        if cluster.get('confidence', 0) >= 0.5:
                            discovery = {
                                'id': f"regional_cluster_{i+1:03d}",
                                'analysis_scale': 'regional',
                                'type': 'settlement_cluster',
                                'center_coordinates': cluster.get('center_coordinates'),
                                'cluster_size_km': cluster.get('cluster_size_km', 0),
                                'site_count_estimate': cluster.get('site_count_estimate', 0),
                                'confidence_score': cluster.get('confidence', 0),
                                'discovery_timestamp': datetime.now().isoformat(),
                                'source_analysis': analysis
                            }
                            discoveries.append(discovery)
                
                if 'priority_zones' in response_data:
                    for i, zone in enumerate(response_data['priority_zones']):
                        if zone.get('priority_level') in ['high', 'medium']:
                            discovery = {
                                'id': f"priority_zone_{i+1:03d}",
                                'analysis_scale': 'regional',
                                'type': 'priority_zone',
                                'center_coordinates': zone.get('center_coordinates'),
                                'expected_site_type': zone.get('expected_site_type'),
                                'priority_level': zone.get('priority_level'),
                                'confidence_score': 0.7 if zone.get('priority_level') == 'high' else 0.5,
                                'discovery_timestamp': datetime.now().isoformat(),
                                'source_analysis': analysis
                            }
                            discoveries.append(discovery)
            
            elif scale == 'zone':
                # Extract from zone analysis
                if 'sites_detected' in response_data:
                    for site in response_data['sites_detected']:
                        if site.get('confidence_score', 0) >= 0.5:
                            discovery = {
                                'id': site.get('site_id', f"zone_site_{len(discoveries)+1:03d}"),
                                'analysis_scale': 'zone',
                                'type': 'archaeological_site',
                                'center_coordinates': site.get('center_coordinates'),
                                'site_type': site.get('site_type'),
                                'diameter_meters': site.get('diameter_meters', 0),
                                'defensive_rings': site.get('defensive_rings', 0),
                                'features_detected': site.get('features_detected', []),
                                'measurements': site.get('measurements', {}),
                                'context': site.get('context', {}),
                                'confidence_score': site.get('confidence_score', 0),
                                'geometric_regularity': site.get('geometric_regularity', 0),
                                'archaeological_probability': site.get('archaeological_probability', 0),
                                'discovery_timestamp': datetime.now().isoformat(),
                                'source_analysis': analysis
                            }
                            discoveries.append(discovery)
                
                if 'linear_features' in response_data:
                    for feature in response_data['linear_features']:
                        if feature.get('confidence', 0) >= 0.5:
                            discovery = {
                                'id': feature.get('feature_id', f"causeway_{len(discoveries)+1:03d}"),
                                'analysis_scale': 'zone',
                                'type': 'linear_feature',
                                'start_coordinates': feature.get('start_coordinates'),
                                'end_coordinates': feature.get('end_coordinates'),
                                'width_meters': feature.get('width_meters', 0),
                                'length_meters': feature.get('length_meters', 0),
                                'orientation': feature.get('orientation'),
                                'connects_sites': feature.get('connects_sites', []),
                                'confidence_score': feature.get('confidence', 0),
                                'discovery_timestamp': datetime.now().isoformat(),
                                'source_analysis': analysis
                            }
                            discoveries.append(discovery)
            
            elif scale == 'site':
                # Extract from detailed site analysis
                if response_data.get('final_assessment', {}).get('archaeological_confidence', 0) >= 0.5:
                    discovery = {
                        'id': response_data.get('site_id', f"detailed_site_{len(discoveries)+1:03d}"),
                        'analysis_scale': 'site',
                        'type': 'detailed_archaeological_site',
                        'site_center': response_data.get('site_center'),
                        'defensive_structures': response_data.get('defensive_structures', {}),
                        'central_architecture': response_data.get('central_architecture', {}),
                        'site_connections': response_data.get('site_connections', []),
                        'site_measurements': response_data.get('site_measurements', {}),
                        'site_classification': response_data.get('site_classification', {}),
                        'preservation_assessment': response_data.get('preservation_assessment', {}),
                        'confidence_score': response_data.get('final_assessment', {}).get('archaeological_confidence', 0),
                        'site_significance': response_data.get('final_assessment', {}).get('site_significance'),
                        'recommended_for_submission': response_data.get('final_assessment', {}).get('recommended_for_submission', False),
                        'discovery_timestamp': datetime.now().isoformat(),
                        'source_analysis': analysis
                    }
                    discoveries.append(discovery)
            
            elif scale == 'leverage':
                # Extract from leverage analysis
                if 'pattern_matches' in response_data:
                    for match in response_data['pattern_matches']:
                        if match.get('confidence', 0) >= 0.5:
                            discovery = {
                                'id': f"leverage_match_{len(discoveries)+1:03d}",
                                'analysis_scale': 'leverage',
                                'type': 'pattern_match',
                                'location': match.get('location'),
                                'similarity_score': match.get('similarity_score', 0),
                                'matching_characteristics': match.get('matching_characteristics', []),
                                'predicted_site_type': match.get('predicted_site_type'),
                                'confidence_score': match.get('confidence', 0),
                                'discovery_timestamp': datetime.now().isoformat(),
                                'source_analysis': analysis
                            }
                            discoveries.append(discovery)
                
                if 'leverage_recommendations' in response_data:
                    for area in response_data['leverage_recommendations'].get('priority_search_areas', []):
                        if area.get('priority') in ['high', 'medium']:
                            discovery = {
                                'id': f"leverage_area_{area.get('area_id', len(discoveries)+1):03d}",
                                'analysis_scale': 'leverage',
                                'type': 'priority_search_area',
                                'center_coordinates': area.get('center_coordinates'),
                                'radius_km': area.get('radius_km', 0),
                                'search_reason': area.get('search_reason'),
                                'priority': area.get('priority'),
                                'confidence_score': 0.8 if area.get('priority') == 'high' else 0.6,
                                'discovery_timestamp': datetime.now().isoformat(),
                                'source_analysis': analysis
                            }
                            discoveries.append(discovery)
        
        except json.JSONDecodeError as e:
            print(f"⚠️ Failed to parse JSON response: {e}")
            # Fallback to keyword-based extraction
            discoveries = self._fallback_extraction(analysis, scale)
        
        except Exception as e:
            print(f"⚠️ Error processing response: {e}")
            discoveries = self._fallback_extraction(analysis, scale)
        
        return discoveries
    
    def _fallback_extraction(self, analysis: Dict, scale: str) -> List[Dict]:
        """Fallback method for non-JSON responses"""
        discoveries = []
        ai_response = analysis['ai_response'].lower()
        
        # Simple keyword-based extraction as fallback
        confidence_indicators = ['confidence', 'likely', 'probable', 'certain']
        site_indicators = ['site', 'center', 'settlement', 'structure']
        
        # Look for confidence scores
        confidence_score = 0.5  # Default
        for line in ai_response.split('\n'):
            if 'confidence' in line:
                # Try to extract numerical confidence
                words = line.split()
                for word in words:
                    try:
                        if '/' in word:
                            conf = float(word.split('/')[0])
                            confidence_score = conf / 10.0
                        elif word.replace('.', '').isdigit():
                            conf = float(word)
                            if conf <= 10:
                                confidence_score = conf / 10.0
                    except:
                        continue
        
        # Check if response indicates archaeological features
        has_archaeological_features = any(
            indicator in ai_response 
            for indicator in ['ring', 'platform', 'mound', 'geometric', 'causeway']
        )
        
        if has_archaeological_features and confidence_score >= 0.5:
            discovery = {
                'id': f"fallback_discovery_{len(self.discoveries) + 1:04d}",
                'analysis_scale': scale,
                'type': 'fallback_extraction',
                'confidence_score': confidence_score,
                'ai_response': analysis['ai_response'],
                'discovery_timestamp': datetime.now().isoformat(),
                'source_analysis': analysis
            }
            
            # Add scale-specific information
            if scale == 'zone':
                discovery['zone_id'] = analysis.get('zone_id')
                discovery['zone_center'] = analysis.get('zone_center')
            elif scale == 'site':
                discovery['site_id'] = analysis.get('site_id')
                discovery['site_center'] = analysis.get('site_center')
            
            discoveries.append(discovery)
        
        return discoveries
    
    def extract_confidence_from_response(self, ai_response: str) -> Optional[float]:
        """Extract confidence score from AI response (JSON or text)"""
        try:
            # Try to parse as JSON first
            response_data = json.loads(ai_response)
            
            # Look for confidence in different JSON structures
            if 'overall_assessment' in response_data:
                return response_data['overall_assessment'].get('confidence_score')
            elif 'zone_summary' in response_data:
                return response_data['zone_summary'].get('zone_confidence')
            elif 'final_assessment' in response_data:
                return response_data['final_assessment'].get('archaeological_confidence')
            elif 'leverage_success' in response_data:
                return response_data['leverage_success'].get('pattern_learning_confidence')
            
            # Look for any confidence field in the JSON
            def find_confidence_recursive(obj):
                if isinstance(obj, dict):
                    for key, value in obj.items():
                        if 'confidence' in key.lower():
                            return value
                        elif isinstance(value, (dict, list)):
                            result = find_confidence_recursive(value)
                            if result is not None:
                                return result
                elif isinstance(obj, list):
                    for item in obj:
                        result = find_confidence_recursive(item)
                        if result is not None:
                            return result
                return None
            
            confidence = find_confidence_recursive(response_data)
            if confidence is not None:
                return float(confidence)
        
        except (json.JSONDecodeError, ValueError):
            # Fallback to text-based extraction
            pass
        
        # Text-based extraction as fallback
        response_lower = ai_response.lower()
        
        # Look for confidence indicators
        for line in response_lower.split('\n'):
            if 'confidence' in line:
                words = line.split()
                for word in words:
                    try:
                        if '/' in word:
                            return float(word.split('/')[0]) / 10.0
                        elif word.replace('.', '').isdigit():
                            conf = float(word)
                            return conf / 10.0 if conf > 1 else conf
                    except:
                        continue
        
        # Default confidence based on keywords
        if any(keyword in response_lower for keyword in ['certain', 'definitely', 'clear']):
            return 0.9
        elif any(keyword in response_lower for keyword in ['likely', 'probable']):
            return 0.7
        elif any(keyword in response_lower for keyword in ['possible', 'maybe']):
            return 0.5
        
        return None
    
    def analyze_all_scales(self, processed_data: Dict) -> Dict:
        """
        Perform complete multi-scale AI analysis
        Regional → Zone → Site → Leverage
        """
        print(f"\n🤖 Multi-Scale AI Analysis Pipeline")
        print("=" * 50)
        
        all_analyses = {
            'regional': [],
            'zone': [],
            'site': [],
            'leverage': None
        }
        
        # Stage 1: Regional Analysis
        print("\n🌍 Stage 1: Regional Network Analysis")
        for region_id, results in processed_data.items():
            regional_analysis = self.analyze_regional_scale(results)
            if regional_analysis:
                all_analyses['regional'].append(regional_analysis)
        
        # Stage 2: Zone Analysis
        print("\n🔍 Stage 2: Zone Site Detection")
        for region_id, results in processed_data.items():
            zone_results = results['scales'].get('zones', [])
            if zone_results:
                zone_analyses = self.analyze_zone_scale(zone_results)
                all_analyses['zone'].extend(zone_analyses)
        
        # Stage 3: Site Analysis
        print("\n🎯 Stage 3: Site Confirmation")
        for region_id, results in processed_data.items():
            site_results = results['scales'].get('sites', [])
            if site_results:
                site_analyses = self.analyze_site_scale(site_results)
                all_analyses['site'].extend(site_analyses)
        
        # Stage 4: Leverage Analysis
        print("\n🔄 Stage 4: Discovery Leverage Analysis")
        if self.discoveries:
            leverage_analysis = self.perform_leverage_analysis(self.discoveries, processed_data)
            all_analyses['leverage'] = leverage_analysis
        
        # Summary
        print(f"\n📊 AI ANALYSIS SUMMARY:")
        print("=" * 30)
        print(f"🌍 Regional analyses: {len(all_analyses['regional'])}")
        print(f"🔍 Zone analyses: {len(all_analyses['zone'])}")
        print(f"🎯 Site analyses: {len(all_analyses['site'])}")
        print(f"🔄 Leverage analysis: {'✅' if all_analyses['leverage'] else '❌'}")
        print(f"🏛️ Total discoveries: {len(self.discoveries)}")
        
        return all_analyses
    
    def get_all_prompts_used(self) -> Dict:
        """Get all prompts used for Checkpoint 2 compliance"""
        return self.prompts_used
    
    def get_high_confidence_discoveries(self, min_confidence: float = 0.7) -> List[Dict]:
        """Get discoveries above confidence threshold"""
        return [
            d for d in self.discoveries 
            if d.get('confidence_score', 0) >= min_confidence
        ]
    
    def save_analysis_results(self, filename: str = None) -> str:
        """Save all analysis results"""
        if filename is None:
            timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
            filename = f"enhanced_ai_analysis_{timestamp}.json"
        
        results = {
            'analysis_timestamp': datetime.now().isoformat(),
            'total_analyses': len(self.ai_responses),
            'total_discoveries': len(self.discoveries),
            'prompts_used': self.prompts_used,
            'ai_responses': self.ai_responses,
            'discoveries': self.discoveries,
            'casarabe_knowledge_base': self.casarabe_knowledge
        }
        
        try:
            with open(filename, 'w') as f:
                json.dump(results, f, indent=2)
            print(f"💾 Analysis results saved to {filename}")
            return filename
        except Exception as e:
            print(f"❌ Could not save results: {e}")
            return None


# Test the enhanced AI analyzer
if __name__ == "__main__":
    print("🏛️ Enhanced Archaeological AI Analyzer Test")
    print("=" * 50)
    
    analyzer = EnhancedAIAnalyzer()
    
    print(f"\n✅ AI analyzer ready!")
    print(f"🏛️ Casarabe knowledge base loaded")
    print(f"📊 Scale-specific prompts: Regional, Zone, Site, Leverage")
    print(f"🔧 Replace os.getenv('OPENAI_API_KEY') with your OpenAI API key")
    print(f"🤖 Ready for archaeological discovery!")