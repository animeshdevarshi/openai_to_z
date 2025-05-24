# simple_region_config.py
# Simple region management for Amazon archaeological sites

import json
import os

class SimpleRegionConfig:
    """
    Simple region configuration manager
    Easy to understand and modify
    """
    
    def __init__(self):
        """Initialize with basic Amazon regions"""
        self.config_file = "simple_regions.json"
        self.regions = self.get_default_regions()
        self.load_config()
    
    def get_default_regions(self):
        """Define 5 basic regions to start with"""
        return {
            'bolivia_main': {
                'name': 'Beni Region, Bolivia',
                'center': [-12.6, -65.3],  # [latitude, longitude]
                'country': 'Bolivia',
                'priority': 'high',
                'known_sites': True,
                'notes': 'Proven archaeological area with documented earthworks'
            },
            'brazil_xingu': {
                'name': 'Upper Xingu Basin, Brazil',
                'center': [-12.5, -53.0],
                'country': 'Brazil', 
                'priority': 'high',
                'known_sites': True,
                'notes': 'Well-documented archaeological region'
            },
            'brazil_acre': {
                'name': 'Acre State, Brazil',
                'center': [-9.5, -67.8],
                'country': 'Brazil',
                'priority': 'medium',
                'known_sites': True,
                'notes': 'Border region with known sites'
            },
            'peru_explore': {
                'name': 'Ucayali Basin, Peru',
                'center': [-8.0, -74.5],
                'country': 'Peru',
                'priority': 'medium', 
                'known_sites': False,
                'notes': 'Exploration area with potential'
            },
            'colombia_test': {
                'name': 'Colombian Amazon',
                'center': [-1.0, -70.0],
                'country': 'Colombia',
                'priority': 'low',
                'known_sites': False,
                'notes': 'Test exploration region'
            }
        }
    
    def load_config(self):
        """Load regions from file if it exists"""
        if os.path.exists(self.config_file):
            try:
                with open(self.config_file, 'r') as f:
                    saved_regions = json.load(f)
                    # Replace default regions with saved regions (don't merge)
                    self.regions = saved_regions
                print(f"✅ Loaded {len(self.regions)} regions from {self.config_file}")
            except Exception as e:
                print(f"⚠️ Could not load config: {e}")
                print("Using default regions")
        else:
            self.save_config()
    
    def save_config(self):
        """Save current regions to file"""
        try:
            with open(self.config_file, 'w') as f:
                json.dump(self.regions, f, indent=2)
            print(f"💾 Saved regions to {self.config_file}")
        except Exception as e:
            print(f"❌ Could not save config: {e}")
    
    def show_regions(self):
        """Display all regions in a simple format"""
        print(f"\n🌍 Available Amazon Regions ({len(self.regions)} total)")
        print("=" * 50)
        
        for region_id, info in self.regions.items():
            priority_emoji = "🔴" if info['priority'] == 'high' else "🟡" if info['priority'] == 'medium' else "🟢"
            sites_emoji = "🏛️" if info['known_sites'] else "🔍"
            
            print(f"{priority_emoji} {sites_emoji} {region_id}")
            print(f"   📍 {info['name']}")
            print(f"   🌍 {info['center'][0]:.2f}, {info['center'][1]:.2f}")
            print(f"   🏴 {info['country']} ({info['priority']} priority)")
            print(f"   📝 {info['notes']}")
            print()
    
    def add_region(self, region_id, name, lat, lng, country, priority='medium', known_sites=False, notes=''):
        """Add a new region (simple version)"""
        new_region = {
            'name': name,
            'center': [lat, lng],
            'country': country,
            'priority': priority,
            'known_sites': known_sites,
            'notes': notes
        }
        
        self.regions[region_id] = new_region
        self.save_config()
        print(f"✅ Added region: {region_id}")
    
    def get_regions_by_priority(self, max_regions=5):
        """Get top priority regions"""
        # Sort by priority (high -> medium -> low)
        priority_order = {'high': 1, 'medium': 2, 'low': 3}
        
        sorted_regions = sorted(
            self.regions.items(),
            key=lambda x: priority_order.get(x[1]['priority'], 3)
        )
        
        # Return top N regions as dictionary
        top_regions = dict(sorted_regions[:max_regions])
        return top_regions
    
    def get_regions_by_country(self, country):
        """Get all regions from a specific country"""
        country_regions = {
            region_id: info for region_id, info in self.regions.items()
            if info['country'].lower() == country.lower()
        }
        return country_regions


# Simple test function
if __name__ == "__main__":
    # Test the region config
    config = SimpleRegionConfig()
    config.show_regions()
    
    # Example: Add a new region
    # config.add_region(
    #     region_id='ecuador_test',
    #     name='Pastaza Province, Ecuador', 
    #     lat=-2.5, lng=-76.5,
    #     country='Ecuador',
    #     priority='low',
    #     known_sites=False,
    #     notes='New exploration area'
    # )
    
    # Example: Get top 3 priority regions
    top_regions = config.get_regions_by_priority(3)
    print(f"🎯 Top 3 priority regions: {list(top_regions.keys())}")
