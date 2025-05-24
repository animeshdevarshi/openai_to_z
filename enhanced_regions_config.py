# enhanced_amazon_regions.py
# Comprehensive archaeological regions database based on 2020-2024 literature
# Strategic region selection for OpenAI to Z Challenge

import json
import os

class EnhancedArchaeologicalRegions:
    """
    Comprehensive Amazon archaeological regions based on recent literature
    Organized by priority and archaeological evidence strength
    """
    
    def __init__(self):
        self.regions = self.get_literature_based_regions()
        self.config_file = "enhanced_regions.json"
    
    def get_literature_based_regions(self):
        """
        Complete region database based on 2020-2024 archaeological literature
        Each region includes literature references and strategic priority
        """
        return {
            # TIER 1: HIGH-PRIORITY PROVEN REGIONS
            # These have published archaeological evidence and good data availability
            
            'bolivia_casarabe_main': {
                'name': 'Casarabe Culture Core, Llanos de Mojos, Bolivia',
                'center': [-12.6, -65.3],
                'country': 'Bolivia',
                'priority': 'high',
                'known_sites': True,
                'data_availability': 'excellent',
                'culture': 'Casarabe (500-1400 CE)',
                'site_types': ['Primary centers (100-400 ha)', 'Secondary centers (20-40 ha)', 'Causeway networks'],
                'key_features': 'Cotoca (147 ha), Landívar (315 ha) - monumental architecture',
                'literature_source': 'Prümers et al. 2022 Nature',
                'estimated_sites': '20-50 major sites',
                'notes': 'Most thoroughly documented Amazonian urban system'
            },
            
            'bolivia_casarabe_extended': {
                'name': 'Extended Casarabe Territory, Bolivia',
                'center': [-13.2, -64.8],
                'country': 'Bolivia', 
                'priority': 'high',
                'known_sites': True,
                'data_availability': 'good',
                'culture': 'Casarabe (500-1400 CE)',
                'site_types': ['Satellite settlements', 'Regional centers'],
                'key_features': 'Four-tiered settlement hierarchy',
                'literature_source': 'Prümers et al. 2022 Nature',
                'estimated_sites': '30-70 sites',
                'notes': '4,500 km² culture area with hierarchical organization'
            },

            'ecuador_upano_valley': {
                'name': 'Upano Valley Complex, Ecuador',
                'center': [-2.2, -78.1],
                'country': 'Ecuador',
                'priority': 'high',
                'known_sites': True,
                'data_availability': 'excellent',
                'culture': 'Upano culture (500 BCE - 600 CE)',
                'site_types': ['Garden cities', 'Earthen platforms', 'Road networks'],
                'key_features': '6,000+ earthen platforms, sophisticated urban planning',
                'literature_source': 'Rostain et al. 2024 Science - Major 2024 discovery',
                'estimated_sites': '6,000+ platforms in interconnected network',
                'notes': 'Largest pre-Columbian urban complex in Amazon - 2024 breakthrough'
            },

            'brazil_acre_geoglyphs': {
                'name': 'Acre Geoglyph Region, Brazil',
                'center': [-9.5, -67.8],
                'country': 'Brazil',
                'priority': 'high', 
                'known_sites': True,
                'data_availability': 'good',
                'culture': 'Geoglyph builders (400 BCE - 1400 CE)',
                'site_types': ['Circular geoglyphs', 'Square earthworks', 'Defensive structures'],
                'key_features': '450+ documented geoglyphs, geometric precision',
                'literature_source': 'Multiple studies 2000-2024',
                'estimated_sites': '450+ documented, hundreds more predicted',
                'notes': 'Ceremonial landscape with geometric earthworks'
            },

            'brazil_upper_xingu': {
                'name': 'Upper Xingu Cultural Complex, Brazil',
                'center': [-12.5, -53.0],
                'country': 'Brazil',
                'priority': 'high',
                'known_sites': True,
                'data_availability': 'excellent',
                'culture': 'Xingu culture (800-1600 CE)',
                'site_types': ['Circular villages', 'Fortified settlements', 'Fish weirs'],
                'key_features': 'Defensive moats, central plazas, radial roads',
                'literature_source': 'Heckenberger et al. multiple publications',
                'estimated_sites': '20-40 major settlements',
                'notes': 'Well-preserved circular village system'
            },

            # TIER 2: EMERGING DISCOVERY REGIONS  
            # Recent discoveries with growing evidence
            
            'brazil_santarem_lower_amazon': {
                'name': 'Santarém Region, Lower Amazon, Brazil',
                'center': [-2.4, -54.7],
                'country': 'Brazil',
                'priority': 'medium',
                'known_sites': True,
                'data_availability': 'good',
                'culture': 'Tapajós culture (1000-1600 CE)',
                'site_types': ['Regional centers', 'Upland settlements', 'Water management'],
                'key_features': 'Non-riverine settlements, constructed ponds',
                'literature_source': 'Stenborg et al. 2017 - LiDAR study',
                'estimated_sites': '50-100 settlements on Belterra Plateau',
                'notes': 'LiDAR reveals extensive upland occupation'
            },

            'brazil_acre_mound_villages': {
                'name': 'Acre Mound Villages, Brazil', 
                'center': [-9.8, -67.5],
                'country': 'Brazil',
                'priority': 'medium',
                'known_sites': True,
                'data_availability': 'good',
                'culture': 'Post-Geoglyph culture (1300-1700 CE)',
                'site_types': ['Circular villages', 'Rectangular villages', 'Road networks'],
                'key_features': 'Sun-ray pattern villages, sophisticated road systems',
                'literature_source': 'Iriarte et al. 2020 - helicopter LiDAR',
                'estimated_sites': '25 circular + 11 rectangular villages documented',
                'notes': '2020 discovery using helicopter LiDAR - clock-face layouts'
            },

            'colombia_caqueta_region': {
                'name': 'Caquetá Archaeological Region, Colombia',
                'center': [-1.0, -75.0],
                'country': 'Colombia',
                'priority': 'medium',
                'known_sites': True,
                'data_availability': 'fair',
                'culture': 'Multiple cultures (500-1500 CE)',
                'site_types': ['Earthworks', 'Petroglyphs', 'Settlement mounds'],
                'key_features': 'Rock art sites, earthwork complexes',
                'literature_source': 'Gaspar et al. recent studies',
                'estimated_sites': '10-30 major complexes',
                'notes': 'Colombian Amazon frontier with emerging evidence'
            },

            'peru_ucayali_basin': {
                'name': 'Ucayali Basin Archaeological Zone, Peru',
                'center': [-8.0, -74.5],
                'country': 'Peru',
                'priority': 'medium',
                'known_sites': False,
                'data_availability': 'good', 
                'culture': 'Unknown cultures (500-1500 CE estimated)',
                'site_types': ['Predicted earthworks', 'Settlement mounds'],
                'key_features': 'High predictive model probability',
                'literature_source': 'Levis et al. 2023 Science - predictive modeling',
                'estimated_sites': '100-500 predicted sites',
                'notes': 'Southwestern Amazon - highest predictive probability region'
            },

            # TIER 3: EXPLORATION FRONTIERS
            # High potential based on predictive models but need investigation

            'brazil_rondonia_explore': {
                'name': 'Rondônia Archaeological Frontier, Brazil',
                'center': [-11.5, -62.0],
                'country': 'Brazil',
                'priority': 'medium',
                'known_sites': False,
                'data_availability': 'fair',
                'culture': 'Unknown (predicted)',
                'site_types': ['Predicted earthworks'],
                'key_features': 'Southwestern Amazon prediction zone',
                'literature_source': 'Levis et al. 2023 Science predictive model',
                'estimated_sites': '200-800 predicted',
                'notes': 'High-probability zone for undiscovered earthworks'
            },

            'peru_madre_de_dios': {
                'name': 'Madre de Dios Region, Peru',  
                'center': [-12.0, -70.0],
                'country': 'Peru',
                'priority': 'medium',
                'known_sites': False,
                'data_availability': 'fair',
                'culture': 'Unknown (predicted)',
                'site_types': ['Predicted earthworks', 'Terra preta sites'],
                'key_features': 'Rich soils suggest human occupation',
                'literature_source': 'Multiple predictive studies',
                'estimated_sites': '50-200 predicted',
                'notes': 'Border region with Bolivia - extension of Casarabe territory?'
            },

            'venezuela_amazon_orinoco': {
                'name': 'Venezuelan Amazon-Orinoco Transition, Venezuela',
                'center': [4.0, -67.0],
                'country': 'Venezuela',
                'priority': 'low',
                'known_sites': True,
                'data_availability': 'limited',
                'culture': 'Multiple cultures (500-1500 CE)',
                'site_types': ['Petroglyphs', 'Settlement mounds'],
                'key_features': 'Rock art, landscape modification',
                'literature_source': 'Scattered studies',
                'estimated_sites': '20-50 sites',
                'notes': 'Northern Amazon frontier - limited accessibility'
            },

            'guyana_rupununi_savannas': {
                'name': 'Rupununi Savannas, Guyana',
                'center': [2.5, -59.5], 
                'country': 'Guyana',
                'priority': 'low',
                'known_sites': True,
                'data_availability': 'limited',
                'culture': 'Pre-Columbian cultures',
                'site_types': ['Shell mounds', 'Earthworks'],  
                'key_features': 'Savanna-forest mosaic settlements',
                'literature_source': 'Iriarte, Rostain studies',
                'estimated_sites': '10-30 sites',
                'notes': 'Guiana Shield region - different archaeological context'
            },

            # STRATEGIC ADDITIONS BASED ON 2024 DISCOVERIES

            'honduras_mosquitia_comparison': {
                'name': 'Mosquitia Archaeological Region, Honduras',
                'center': [15.0, -84.5],
                'country': 'Honduras', 
                'priority': 'low',
                'known_sites': True,
                'data_availability': 'good',
                'culture': 'Unknown pre-Columbian culture',
                'site_types': ['Settlement complexes', 'Plaza groups'],
                'key_features': 'LiDAR-discovered cities, carved stone offerings',
                'literature_source': 'Elkins et al. 2016-2019 LiDAR surveys',
                'estimated_sites': '10-20 settlement areas',
                'notes': 'NON-AMAZON comparison site for methodology validation'
            }
        }

    def get_strategic_recommendations(self):
        """
        Strategic recommendations for region selection based on competition goals
        """
        return {
            'competition_optimal': [
                'bolivia_casarabe_main',      # Guaranteed discoveries
                'ecuador_upano_valley',       # 2024 breakthrough site
                'brazil_acre_geoglyphs'       # Proven geometric patterns
            ],
            'discovery_potential': [
                'bolivia_casarabe_extended',  # Expand known system
                'brazil_santarem_lower_amazon', # LiDAR-proven method
                'peru_ucayali_basin'          # High prediction probability
            ],
            'research_frontier': [
                'brazil_acre_mound_villages', # Recent LiDAR discoveries
                'brazil_rondonia_explore',    # Unexplored high-probability
                'colombia_caqueta_region'     # Colombian frontier
            ]
        }

    def save_enhanced_config(self):
        """
        Save the enhanced region configuration
        """
        try:
            with open(self.config_file, 'w') as f:
                json.dump(self.regions, f, indent=2)
            print(f"✅ Enhanced regions saved to {self.config_file}")
            print(f"📊 Total regions: {len(self.regions)}")
            
            # Show summary by priority
            priorities = {}
            for region_id, info in self.regions.items():
                priority = info['priority']
                if priority not in priorities:
                    priorities[priority] = []
                priorities[priority].append(region_id)
            
            for priority, regions in priorities.items():
                print(f"   {priority.upper()}: {len(regions)} regions")
                
        except Exception as e:
            print(f"❌ Error saving config: {e}")

    def show_literature_sources(self):
        """
        Display the academic sources for archaeological evidence
        """
        print("\n📚 LITERATURE SOURCES:")
        print("="*50)
        
        sources = {}
        for region_id, info in self.regions.items():
            source = info['literature_source']
            if source not in sources:
                sources[source] = []
            sources[source].append(f"{region_id}: {info['name']}")
        
        for source, regions in sources.items():
            print(f"\n📖 {source}")
            for region in regions:
                print(f"   • {region}")

    def get_competition_ready_config(self):
        """
        Return configuration optimized for OpenAI to Z Challenge
        Focus on regions with best data availability and discovery potential
        """
        competition_regions = {}
        
        # Priority order for competition
        priority_order = ['high', 'medium', 'low']
        max_per_priority = {'high': 6, 'medium': 4, 'low': 2}
        
        for priority in priority_order:
            count = 0
            for region_id, info in self.regions.items():
                if info['priority'] == priority and count < max_per_priority[priority]:
                    if info['data_availability'] in ['excellent', 'good']:
                        competition_regions[region_id] = info
                        count += 1
        
        return competition_regions


# Test and demonstrate the enhanced region system
if __name__ == "__main__":
    print("🏛️ Enhanced Amazon Archaeological Regions Database")
    print("="*60)
    print("📚 Based on 2020-2024 archaeological literature")
    print("🎯 Optimized for OpenAI to Z Challenge")
    
    # Initialize the enhanced system
    regions_db = EnhancedArchaeologicalRegions()
    
    # Save the configuration
    regions_db.save_enhanced_config()
    
    # Show strategic recommendations
    recommendations = regions_db.get_strategic_recommendations()
    print(f"\n🎯 STRATEGIC RECOMMENDATIONS:")
    print("="*40)
    for category, region_list in recommendations.items():
        print(f"\n{category.upper().replace('_', ' ')}:")
        for region_id in region_list:
            region_info = regions_db.regions[region_id]
            print(f"   • {region_id}: {region_info['name']}")
            print(f"     Culture: {region_info['culture']}")
            print(f"     Evidence: {region_info['literature_source']}")
    
    # Show literature sources
    regions_db.show_literature_sources()
    
    # Get competition-ready configuration
    competition_config = regions_db.get_competition_ready_config()
    print(f"\n🏆 COMPETITION-READY CONFIGURATION:")
    print(f"Selected {len(competition_config)} regions with optimal data/discovery balance")
    
    print(f"\n✅ Enhanced region database ready!")
    print(f"🎯 Use this for maximum competitive advantage")
