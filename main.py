import scraper
import storage
import threading

def worker(link):
    city_links = scraper.get_city_links(link)
    for city_link in city_links:
        data = scraper.extract_city_data(city_link)
        title = list(data.keys())[0]
        print(f"Processed {title}")
        storage.save_to_txt(title, data)

def main():
    links = scraper.get_links_from_home()
    threads = []
    for link in links:
        t = threading.Thread(target=worker, args=(link,))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

if __name__ == '__main__':
    main()
