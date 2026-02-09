import requests
from bs4 import BeautifulSoup

def fetch_html(url):
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"[!] Error fetching URL: {e}")
        return None

def scrape_data(html, tag, class_name=None):
    soup = BeautifulSoup(html, "html.parser")
    if class_name:
        elements = soup.find_all(tag, class_=class_name)
    else:
        elements = soup.find_all(tag)
    results = [el.get_text(strip=True) for el in elements]
    return results

def display_results(results, max_items=20):
    if not results:
        print("No matching elements found.")
        return
    print(f"\nFound {len(results)} items. Showing up to {max_items}:")
    print("-" * 60)
    for i, item in enumerate(results[:max_items], start=1):
        print(f"{i}. {item}")
    print("-" * 60)

def interactive_scraper():
    print("=== Interactive Web Scraper ===")
    print("Example sites to try:")
    print("  - https://news.ycombinator.com/  (titles: tag=a, class=storylink)")
    print("  - https://realpython.github.io/fake-jobs/  (h2.job-title)\n")

    while True:
        url = input("Enter URL (or 'q' to quit): ").strip()
        if url.lower() == 'q':
            print("Goodbye!")
            break

        tag = input("Enter HTML tag to scrape (e.g., a, h1, p): ").strip()
        class_name = input("Enter class name (optional, press Enter to skip): ").strip()
        if class_name == "":
            class_name = None

        html = fetch_html(url)
        if html is None:
            continue

        results = scrape_data(html, tag, class_name)
        display_results(results)

        save_choice = input("Save results to a text file? (y/n): ").strip().lower()
        if save_choice == 'y' and results:
            filename = input("Enter filename (e.g., output.txt): ").strip()
            try:
                with open(filename, "w", encoding="utf-8") as f:
                    for item in results:
                        f.write(item + "\n")
                print(f"Results saved to {filename}")
            except OSError as e:
                print(f"Error saving file: {e}")

        again = input("\nScrape another page? (y/n): ").strip().lower()
        if again != 'y':
            print("Goodbye!")
            break

if __name__ == "__main__":
    interactive_scraper()
