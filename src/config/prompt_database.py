# Updated Multi-Cultural Archaeological Prompt Configuration
# Open discovery approach - let AI find patterns without templates

import os
import json
from typing import Dict, List

# Simplified system prompt for open discovery
ARCHAEOLOGICAL_SYSTEM_PROMPT = (
    "You are an expert archaeological remote sensing analyst specializing in Amazon landscape analysis. "
    "Your mission is to detect ANY evidence of human landscape modification from satellite imagery, "
    "regardless of time period or cultural origin. Look for geometric patterns, earthworks, or anomalies "
    "too regular for nature. Think like an explorer discovering something entirely new. "
    "CRITICAL: Output ONLY valid JSON format with no additional text."
)

class PromptConfig:
    """
    Open discovery prompt configuration for Amazon archaeological analysis
    Let AI discover patterns without predetermined cultural templates
    """
    
    def __init__(self):
        """Initialize open discovery prompt system"""
        
        # Simplified system prompt for open discovery
        self.ARCHAEOLOGICAL_SYSTEM_PROMPT = """You are an expert archaeological analyst with deep remote sensing experience in the Amazon basin. Your mission is to identify ANY evidence of human landscape modification from satellite imagery.

APPROACH:
- Fresh eyes analysis - no preconceptions about what should be there
- Look for geometric patterns, earthworks, anomalies too regular for nature  
- Consider all time periods from recent to thousands of years old
- Focus on what you actually observe, not what textbooks say

OUTPUT: Return ONLY valid JSON format with your discoveries."""

        # Keep basic data source info
        self.data_sources = {
            'optical': 'Sentinel-2 MSI 10m',
            'radar': 'ALOS PALSAR / Sentinel-1 SAR 25m'
        }
        
        print("📝 Open Discovery Prompt Configuration initialized")
        print("🔍 AI-driven pattern recognition approach")
        print("🆓 No cultural templates - pure discovery mode")

    def _json_only_line(self) -> str:
        """Standard JSON compliance instruction"""
        return "Return ONE valid minified JSON object and nothing else."

    def get_regional_prompt_template(self) -> str:
        """Open discovery regional analysis template"""
        return """CONTEXT:
- Region: {region_name}
- Center: {center}
- Scale: Regional overview (50km × 50km, ~97m per pixel)
- Data: optical ({optical}), radar ({radar})

MISSION: Scan this Amazon region for ANY evidence of human landscape modification across all time periods.

DISCOVERY TARGETS:
🔍 GEOMETRIC ANOMALIES: Perfect circles, squares, straight lines too regular for nature
🏗️ LANDSCAPE MODIFICATIONS: Raised areas, depressions, cleared patterns, terraces
🛤️ LINEAR FEATURES: Roads, causeways, canals, boundaries, connecting pathways
⭕ CLUSTERED PATTERNS: Grouped features suggesting organized settlements
🌿 VEGETATION ANOMALIES: Different growth patterns indicating buried structures
🏛️ EARTHWORKS: Mounds, platforms, enclosures, defensive works

ANALYSIS APPROACH:
- Question everything that seems "too organized" for nature
- Look for repetition, symmetry, and geometric precision
- Consider multiple scales from small features to large complexes
- Focus on what you actually observe in the imagery

What patterns of human landscape modification do you detect?

OUTPUT_SCHEMA_EXAMPLE: {example}

{json_instruction}"""

    def get_zone_prompt_template(self) -> str:
        """Open discovery zone analysis template"""
        return """CONTEXT:
- Zone ID: {zone_id}
- Center: {zone_center}
- Scale: Zone level (10km × 10km, ~9.8m per pixel)
- Data: optical ({optical}), radar ({radar})

DETAILED PATTERN ANALYSIS:
🎯 GEOMETRIC PRECISION: Circles, rectangles, perfectly straight lines
🏘️ SETTLEMENT INDICATORS: Clustered features, organized layouts
🛡️ DEFENSIVE FEATURES: Enclosures, ramparts, strategic positions
🏗️ CONSTRUCTION EVIDENCE: Raised platforms, excavated areas
🛤️ INFRASTRUCTURE: Pathways, causeways, drainage systems

MEASUREMENT PRECISION: Each pixel = 9.8m. Minimum detectable feature = ~20m.

DISCOVERY APPROACH:
- Map all geometric anomalies regardless of cultural attribution
- Measure dimensions precisely 
- Identify organizational patterns
- Look for evidence of planning and construction

What specific archaeological features do you detect in this zone?

OUTPUT_SCHEMA_EXAMPLE: {example}

{json_instruction}"""

    def get_site_prompt_template(self) -> str:
        """Open discovery site confirmation template"""  
        return """CONTEXT:
- Site ID: {site_id}
- Center: {center}
- Scale: Site confirmation (2km × 2km, ~1.95m per pixel)
- Data: optical ({optical}), radar ({radar})

DETAILED FEATURE MAPPING:
🔍 PRECISE MEASUREMENTS: Platform dimensions, ring diameters, feature heights
🏗️ CONSTRUCTION DETAILS: Building techniques, material evidence
🛡️ DEFENSIVE ANALYSIS: Fortification patterns, strategic design
🛤️ ACCESS ROUTES: Entrances, pathways, connections to other features
📐 GEOMETRIC ANALYSIS: Regularity, symmetry, planning evidence

MEASUREMENT PROTOCOL: Each pixel = 1.95m. Map all features precisely.

CONFIRMATION CRITERIA:
- Clear evidence of human construction
- Geometric regularity beyond natural processes
- Organized layout indicating planning
- Preservation state and modern disturbances

Provide detailed mapping and confirmation of this archaeological site.

OUTPUT_SCHEMA_EXAMPLE: {example}

{json_instruction}"""

    def get_leverage_prompt_template(self) -> str:
        """Open discovery leverage analysis template"""
        return """CONTEXT:
- Discoveries analyzed: {discovery_count} confirmed sites
- Successful patterns: {successful_criteria}
- Pattern characteristics: {pattern_summary}

LEVERAGE STRATEGY:
🎯 PATTERN REPLICATION: Find more sites matching successful discovery patterns
🔍 NETWORK EXPANSION: Follow connections and pathways from known sites  
🚀 VARIATION DISCOVERY: Look for similar but unique pattern variations
📈 SCALING SUCCESS: Apply learned patterns to identify new discovery areas

ADAPTIVE SEARCH: Use confirmed discoveries as templates while remaining open to entirely new patterns.

What additional sites can you discover using these successful patterns?

OUTPUT_SCHEMA_EXAMPLE: {example}

{json_instruction}"""

    def get_regional_prompt(self, region_info: Dict, images: Dict, radar_type: str = "ALOS PALSAR") -> str:
        """Generate open discovery regional prompt"""
        example = (
            '{"analysis_type":"open_discovery_regional",'
            '"region_analyzed":"%s",'
            '"coordinates":%s,'
            '"human_modified_areas":[{"discovery_id":"REG_001","coordinates":[-10.1234,-65.4321],"modification_type":"geometric_earthworks","description":"Circular earthwork with raised center","scale":"large","confidence":0.85,"uniqueness":"unusual"}],'
            '"landscape_patterns":[{"pattern_type":"linear_network","description":"Connected linear features","extent_km":5.2,"confidence":0.7}],'
            '"priority_areas":[{"area_id":"PRIORITY_001","coordinates":[-10.2345,-65.5432],"interest_level":"high","reasoning":"Multiple geometric anomalies clustered together"}],'
            '"discovery_summary":{"total_anomalies_detected":3,"most_significant_discovery":"Large circular earthwork complex","overall_human_impact_assessment":"moderate","recommended_next_steps":"Detailed zone analysis of priority areas"}}'
            % (region_info.get('region_name', 'Unknown Region'), region_info.get('center', [0, 0]))
        )
        
        template = self.get_regional_prompt_template()
        return template.format(
            region_name=region_info.get('region_name', 'Unknown Region'),
            center=region_info.get('center', [0, 0]),
            optical=self.data_sources['optical'],
            radar=self.data_sources['radar'],
            example=example,
            json_instruction=self._json_only_line()
        )

    def get_zone_prompt(self, zone_info: Dict, images: Dict, radar_type: str = "ALOS PALSAR") -> str:
        """Generate open discovery zone prompt"""
        example = (
            '{"analysis_type":"open_discovery_zone",'
            '"zone_id":"%s",'
            '"zone_center":%s,'
            '"sites_detected":[{"site_id":"SITE_001","center_coordinates":[-10.1234,-65.4321],"site_type":"earthwork_complex","diameter_meters":300,"features_detected":["circular_enclosure","central_mound","linear_access"],"measurements":{"outer_diameter_m":300,"central_feature_m":50,"estimated_area_hectares":7},"confidence_score":0.85,"geometric_regularity":0.9}],'
            '"linear_features":[{"feature_id":"LINEAR_001","start_coordinates":[-10.1234,-65.4321],"end_coordinates":[-10.2345,-65.5432],"width_meters":20,"length_meters":800,"description":"Straight pathway connecting features"}],'
            '"zone_summary":{"total_features_detected":2,"geometric_features_count":3,"highest_confidence_discovery":"SITE_001","zone_confidence":0.8,"recommend_site_analysis":true}}'
            % (zone_info.get('zone_id', 'Unknown Zone'), zone_info.get('zone_center', [0, 0]))
        )
        
        template = self.get_zone_prompt_template()
        return template.format(
            zone_id=zone_info.get('zone_id', 'Unknown Zone'),
            zone_center=zone_info.get('zone_center', [0, 0]),
            optical=self.data_sources['optical'],
            radar=self.data_sources['radar'],
            example=example,
            json_instruction=self._json_only_line()
        )

    def get_site_prompt(self, site_info: Dict, images: Dict, radar_type: str = "ALOS PALSAR") -> str:
        """Generate open discovery site prompt"""
        example = (
            '{"analysis_type":"open_discovery_site",'
            '"site_id":"%s",'
            '"coordinates":%s,'
            '"confirmation_status":"confirmed",'
            '"site_features":{"primary_structure":{"type":"circular_earthwork","diameter_m":250,"height_estimate_m":3},"secondary_features":[{"type":"linear_access","width_m":15,"length_m":200}],"geometric_precision":0.92},'
            '"measurements":{"total_area_hectares":5,"primary_feature_diameter_m":250,"secondary_feature_count":2},'
            '"construction_evidence":{"earthwork_volume_estimate":"significant","geometric_regularity":"high","planning_evidence":"clear"},'
            '"site_classification":{"complexity":"moderate","preservation":"good","archaeological_significance":"regional"},'
            '"final_assessment":{"archaeological_confidence":0.88,"recommended_for_submission":true,"discovery_uniqueness":"moderate"}}'
            % (site_info.get('site_id', 'Unknown Site'), site_info.get('center', [0, 0]))
        )
        
        template = self.get_site_prompt_template()
        return template.format(
            site_id=site_info.get('site_id', 'Unknown Site'),
            center=site_info.get('center', [0, 0]),
            optical=self.data_sources['optical'],
            radar=self.data_sources['radar'],
            example=example,
            json_instruction=self._json_only_line()
        )

    def get_leverage_prompt(self, discoveries: List[Dict], search_region: Dict) -> str:
        """Generate open discovery leverage prompt"""
        if not discoveries:
            region_info = {'region_name': 'Amazon Region', 'center': [0, 0]}
            return self.get_regional_prompt(region_info, {})
        
        patterns = self._analyze_discovery_patterns(discoveries)
        
        example = (
            '{"analysis_type":"open_discovery_leverage",'
            '"pattern_analysis":{"successful_patterns":[{"pattern_type":"circular_earthworks","size_range_m":[200,400],"success_rate":0.8}],"spatial_relationships":{"typical_spacing_km":3.2,"clustering_tendency":"moderate"}},'
            '"new_discoveries":[{"discovery_id":"LEV_001","coordinates":[-10.1234,-65.4321],"pattern_match":"circular_earthwork","confidence_based_on_pattern":0.75,"discovery_rationale":"Matches successful geometric pattern"}],'
            '"leverage_success":{"initial_discoveries_analyzed":%d,"pattern_learning_confidence":0.8,"new_discoveries_predicted":2,"search_efficiency_improved":true}}'
            % len(discoveries)
        )
        
        template = self.get_leverage_prompt_template()
        return template.format(
            discovery_count=len(discoveries),
            successful_criteria=patterns['successful_criteria'],
            pattern_summary=patterns['pattern_summary'],
            example=example,
            json_instruction=self._json_only_line()
        )

    def _analyze_discovery_patterns(self, discoveries: List[Dict]) -> Dict:
        """Analyze patterns from discoveries"""
        if not discoveries:
            return {
                'successful_criteria': ['geometric_patterns'],
                'pattern_summary': 'Limited data for pattern analysis'
            }
            
        # Extract common characteristics
        sizes = [d.get('estimated_size_ha', 0) for d in discoveries if d.get('estimated_size_ha', 0) > 0]
        features = []
        for d in discoveries:
            features.extend(d.get('geometric_features', []))
            features.extend(d.get('features_detected', []))
        
        return {
            'successful_criteria': list(set(features))[:3] if features else ['geometric_patterns'],
            'pattern_summary': f"Size range: {min(sizes) if sizes else 0}-{max(sizes) if sizes else 100}ha, Common features: {list(set(features))[:2] if features else ['earthworks']}"
        }

    def get_prompt_metadata(self, prompt_type: str, prompt_content: str) -> Dict:
        """Get metadata for prompt tracking"""
        return {
            'prompt_type': prompt_type,
            'content_length': len(prompt_content),
            'approach': 'open_discovery',
            'data_sources': list(self.data_sources.keys()),
            'competitive_features': [
                'open_ended_discovery',
                'pattern_recognition_focus',
                'no_cultural_bias',
                'ai_driven_insights'
            ],
            'checkpoint2_compliance': True
        }

    def save_prompts_documentation(self, output_dir: str) -> str:
        """Save prompt documentation"""
        import os
        from datetime import datetime
        
        os.makedirs(output_dir, exist_ok=True)
        
        documentation = {
            'open_discovery_system': {
                'version': '4.0_open_discovery',
                'created': datetime.now().isoformat(),
                'description': 'Open-ended AI discovery without cultural templates',
                'advantages': [
                    'No confirmation bias from predefined templates',
                    'AI-driven pattern recognition',
                    'Genuine discovery potential', 
                    'Adaptable to any cultural pattern',
                    'Innovation-focused approach'
                ]
            },
            'data_sources': self.data_sources,
            'system_prompt': self.ARCHAEOLOGICAL_SYSTEM_PROMPT
        }
        
        output_file = os.path.join(output_dir, 'open_discovery_documentation.json')
        with open(output_file, 'w') as f:
            json.dump(documentation, f, indent=2)
        
        return output_file