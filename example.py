#!/usr/bin/env python3
"""
Example/Demo: How to use the ScrapMonster scraper

This script demonstrates how the scraper works with sample data.
To scrape the actual website, run: python scraper.py
"""

from scraper import ScrapMonsterScraper
from bs4 import BeautifulSoup


def demo_with_sample_data():
    """Demonstrate scraper functionality with sample HTML."""
    
    # Sample HTML that simulates ScrapMonster's structure
    sample_html = """
    <html>
    <body>
        <div class="listing-item">
            <h2>Johnson Auto Recycling</h2>
            <span class="location">Phoenix, AZ</span>
            <p class="description">Full-service auto recycling facility</p>
            <div class="address">8200 S 48th St, Phoenix, AZ 85042</div>
        </div>
        <div class="listing-item">
            <h2>Metro Salvage Yard</h2>
            <span class="location">Seattle, WA</span>
            <p class="description">Quality used auto parts</p>
            <div class="address">9500 Aurora Ave N, Seattle, WA 98103</div>
        </div>
    </body>
    </html>
    """
    
    print("=" * 60)
    print("SCRAPER DEMO WITH SAMPLE DATA")
    print("=" * 60)
    
    # Create scraper instance
    scraper = ScrapMonsterScraper("https://example.com")
    
    # Parse sample HTML
    soup = BeautifulSoup(sample_html, 'lxml')
    
    # Extract listings
    scraper.listings = scraper.extract_listings(soup)
    
    # Display results
    print(f"\nExtracted {len(scraper.listings)} listings:\n")
    for i, listing in enumerate(scraper.listings, 1):
        print(f"Listing {i}:")
        print(f"  Company: {listing['Company']}")
        print(f"  Location: {listing['Location']}")
        print(f"  Yard Brief: {listing['YardBrief']}")
        print(f"  Address: {listing['Address']}")
        print()
    
    # Export to Excel
    output_file = 'demo_output.xlsx'
    scraper.export_to_excel(output_file)
    print(f"\n✓ Data exported to {output_file}")
    print("\nTo scrape real data, run: python scraper.py")


if __name__ == "__main__":
    demo_with_sample_data()
